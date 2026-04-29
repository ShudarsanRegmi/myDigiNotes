## Page Fault



```c
#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <unistd.h>
#include <time.h>

#define SIZE (512 * 1024 * 1024) // 512 MB

long diff_ns(struct timespec a, struct timespec b) {
    return (b.tv_sec - a.tv_sec) * 1e9 + (b.tv_nsec - a.tv_nsec);
}

int main() {
    char *buffer;
    struct timespec start, end;

    // Allocate memory (anonymous mapping)
    buffer = mmap(NULL, SIZE, PROT_READ | PROT_WRITE,
                  MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);

    if (buffer == MAP_FAILED) {
        perror("mmap");
        return 1;
    }

    // Hint kernel: don't keep it in RAM
    madvise(buffer, SIZE, MADV_DONTNEED);

    // First access (cold) → triggers major faults
    clock_gettime(CLOCK_MONOTONIC, &start);
    for (size_t i = 0; i < SIZE; i += 4096) {
        buffer[i] = 1;  // touch each page
    }
    clock_gettime(CLOCK_MONOTONIC, &end);

    printf("Cold access time: %ld ns\n", diff_ns(start, end));

    // Second access (warm) → no major faults
    clock_gettime(CLOCK_MONOTONIC, &start);
    for (size_t i = 0; i < SIZE; i += 4096) {
        buffer[i] += 1;
    }
    clock_gettime(CLOCK_MONOTONIC, &end);

    printf("Warm access time: %ld ns\n", diff_ns(start, end));

    munmap(buffer, SIZE);
    return 0;
}
```

---

<img width="453" height="101" alt="image" src="https://github.com/user-attachments/assets/1ada220c-928e-49b9-8fcd-9444328c2492" />


**Rephrased version of your ask:**
“Walk me through this C program line-by-line so I clearly understand how it triggers page faults and measures their latency.”

---

## :sd → Big picture (what this program *really* does)

This program is a **controlled probe** into virtual memory behavior.
It deliberately creates two scenarios:

1. **Cold access** → forces the OS to bring pages into RAM
2. **Warm access** → reuses already-loaded pages

Then it measures the **temporal disparity** between them.

---

## :sd → Headers (infrastructure layer)

```c
#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <unistd.h>
#include <time.h>
```

* `stdio.h` → printing output
* `sys/mman.h` → memory mapping (`mmap`, `madvise`)
* `time.h` → high-resolution timing

### Vocabulary:

* *Instrumentation*: adding measurement capability to a program

---

## :sd → Memory size definition

```c
#define SIZE (512 * 1024 * 1024)
```

* Allocates **512 MB**
* Large enough to:

  * exceed CPU cache
  * stress RAM
  * expose paging behavior

---

## :sd → Time difference function

```c
long diff_ns(struct timespec a, struct timespec b) {
    return (b.tv_sec - a.tv_sec) * 1000000000L + (b.tv_nsec - a.tv_nsec);
}
```

* Computes elapsed time in **nanoseconds**
* Combines:

  * seconds → converted to ns
  * nanoseconds → added directly

### Vocabulary:

* *Epoch delta*: difference between two time points

---

## :sd → Conversion helper

```c
double ns_to_ms(long ns) {
    return ns / 1e6;
}
```

* Converts ns → ms
* Makes output more **interpretable**

---

## :sd → Memory allocation (critical part)

```c
buffer = mmap(NULL, SIZE, PROT_READ | PROT_WRITE,
              MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
```

### What this does:

* Allocates **virtual memory**, not physical immediately
* `MAP_ANONYMOUS` → not backed by a file
* `MAP_PRIVATE` → changes are not shared

### Important insight:

* This does **lazy allocation**
* No RAM is actually used yet

### Vocabulary:

* *Lazy allocation*: memory is allocated only when accessed

---

## :sd → Error check

```c
if (buffer == MAP_FAILED)
```

* Ensures mapping succeeded
* Prevents undefined behavior

---

## :sd → Forcing “cold” state

```c
madvise(buffer, SIZE, MADV_DONTNEED);
```

### This is the *key trick*

* Tells kernel:

  > “I don’t need these pages right now”

Effect:

* Pages are **evicted / discarded**
* Next access → must reload → **major page faults**

### Vocabulary:

* *Eviction*: removal of data from memory
* *Advisory hint*: kernel may follow this suggestion

---

## :sd → Cold access loop (page fault generator)

```c
for (size_t i = 0; i < SIZE; i += 4096) {
    buffer[i] = 1;
}
```

### Why `i += 4096`?

* 4096 bytes = **1 page (4KB)**
* Each iteration touches:
  → exactly **one page**

### What happens internally:

1. CPU accesses `buffer[i]`
2. Page not in RAM → **page fault**
3. OS loads page
4. Execution resumes

### Result:

* You trigger **one fault per page**

### Vocabulary:

* *Stride access*: stepping through memory in fixed intervals

---

## :sd → Timing the cold access

```c
clock_gettime(CLOCK_MONOTONIC, &start);
...
clock_gettime(CLOCK_MONOTONIC, &end);
```

* Uses **monotonic clock**:

  * immune to system time changes
  * ideal for benchmarking

---

## :sd → Printing cold result

```c
printf("Cold access: %ld ns (%.3f ms)\n", cold_ns, ns_to_ms(cold_ns));
```

* Shows:

  * precise latency (ns)
  * human-readable latency (ms)

---

## :sd → Warm access loop (no major faults)

```c
for (size_t i = 0; i < SIZE; i += 4096) {
    buffer[i] += 1;
}
```

### What changed?

* Pages are already in RAM
* No disk access
* Only:

  * minor faults (maybe)
  * or none

### Result:

* Much faster execution

---

## :sd → Cleanup

```c
munmap(buffer, SIZE);
```

* Releases mapped memory
* Prevents leaks

---

## :sd → What you are *actually observing*

| Phase       | What happens internally | Cost driver    |
| ----------- | ----------------------- | -------------- |
| Cold access | Page fault → disk → RAM | I/O latency    |
| Warm access | Direct RAM access       | Memory latency |

---

## :sd → Hidden OS mechanics (this is the real gold)

During cold loop:

* Page table entry = invalid
* MMU triggers trap → kernel
* Kernel:

  * allocates frame
  * updates page table
  * resumes execution

This is a **context switch into kernel mode** → expensive.

---

## :sd → Why this experiment is powerful

You are isolating:

* **Demand paging**
* **Page fault overhead**
* **Memory locality effects**

in a **minimal, reproducible setup**

---

## :oll → Final intuition

* `mmap` → creates *potential* memory
* first touch → *realizes* memory (page fault)
* second touch → *exploits locality*

You’re literally watching the OS **materialize memory on demand**.

---

If you want to level this up further, we can:

* inspect `/proc/<pid>/pagemap` to see physical mappings
* or modify this to use **huge pages** and observe TLB effects

That’s where this topic becomes deeply systems-level, not just conceptual.


---





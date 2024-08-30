<div align="center">

![Amrita Vishwa Vidyapeetham Logo](https://webfiles.amrita.edu/2024/04/WhQq1FiB-amrita-vishwa-vidyapeetham-university-logo-colored-version.svg)

# Amrita Vishwa Vidyapeetham
## Chennai Campus
337/1A, Vengal Village,  
Thiruvallur Taluk & District – 601 103,  
Tamil Nadu, India

---

### Subject: Operating System Lab

**Submitted By:** Shudarsan Regmi  
**Roll No.:** CH.SC.U4CYS23055

</div>

---
# Question

>Implement a barrier synchronisation method mechanism using semaphores where a group of threads or processes must all reach a certain point in their execution before any of them can proceed . 
This is often used in parallel computing .
Illustrate about synchronisation technique in multi threaded environment and how semaphores can enforce order and coordination.

## Answer
Barrier synchronization is a technique used in parallel computing to ensure that multiple threads or processes reach a certain point in their execution before any of them can proceed. This is essential when you need to coordinate multiple threads or processes that are working in parallel and need to wait for each other to reach a common point before continuing.

### Semaphore-Based Barrier Synchronization

In a multi-threaded environment, semaphores can be used to implement barrier synchronization. Semaphores are synchronization primitives that can be used to manage access to resources or to coordinate actions among threads. 

Here's how you can implement a barrier synchronization mechanism using semaphores:

#### Components of the Barrier Synchronization

1. **Semaphore for Counting**: To keep track of how many threads have reached the barrier.
2. **Semaphore for Waiting**: To make threads wait until all have reached the barrier.

#### Steps to Implement Barrier Synchronization

1. **Initialization**:
   - Create a counting semaphore initialized to 0.
   - Create a binary semaphore (or a mutex) to ensure exclusive access to the critical section where the count is updated.

2. **Barrier Function**:
   - When a thread reaches the barrier, it increments a count of threads that have reached.
   - If the count equals the total number of threads, the barrier is released, allowing all threads to proceed.

Here's a simple implementation in C using POSIX semaphores and threads:

```c
#include <stdio.h>
#include <pthread.h>
#include <semaphore.h>

#define THREAD_COUNT 5

// Global variables for barrier synchronization
sem_t barrier_sem;
sem_t mutex;
int count = 0;

void barrier_init() {
    sem_init(&barrier_sem, 0, 0);  // Initialize the counting semaphore to 0
    sem_init(&mutex, 0, 1);        // Initialize the mutex semaphore to 1 (binary semaphore)
}

void barrier_wait(int total_threads) {
    sem_wait(&mutex);               // Enter critical section
    count++;
    if (count == total_threads) {
        // If this is the last thread to reach the barrier, release all waiting threads
        for (int i = 0; i < total_threads; i++) {
            sem_post(&barrier_sem);
        }
    }
    sem_post(&mutex);               // Exit critical section

    // Wait for the barrier to be released
    sem_wait(&barrier_sem);
}

void* thread_function(void* arg) {
    printf("Thread %d reached the barrier.\n", *(int*)arg);
    barrier_wait(THREAD_COUNT);
    printf("Thread %d passed the barrier.\n", *(int*)arg);
    return NULL;
}

int main() {
    pthread_t threads[THREAD_COUNT];
    int thread_ids[THREAD_COUNT];

    barrier_init();

    // Create threads
    for (int i = 0; i < THREAD_COUNT; i++) {
        thread_ids[i] = i;
        pthread_create(&threads[i], NULL, thread_function, &thread_ids[i]);
    }

    // Join threads
    for (int i = 0; i < THREAD_COUNT; i++) {
        pthread_join(threads[i], NULL);
    }

    sem_destroy(&barrier_sem);
    sem_destroy(&mutex);

    return 0;
}
```

### Explanation of the Code

1. **Initialization**:
   - `sem_init(&barrier_sem, 0, 0);`: Initializes the counting semaphore `barrier_sem` to 0.
   - `sem_init(&mutex, 0, 1);`: Initializes the binary semaphore `mutex` to 1.

2. **Barrier Wait Function**:
   - `sem_wait(&mutex);`: Acquires the mutex to enter the critical section.
   - `count++`: Increments the count of threads that have reached the barrier.
   - `if (count == total_threads)`: Checks if the current thread is the last one to reach the barrier.
     - If true, releases the semaphore `barrier_sem` to unblock all threads.
   - `sem_post(&mutex);`: Releases the mutex after updating the count.
   - `sem_wait(&barrier_sem);`: Each thread waits for the barrier semaphore to be released before continuing.

3. **Thread Function**:
   - Each thread calls `barrier_wait` to synchronize with others.
   - After reaching the barrier and waiting, threads proceed past the barrier.

### Synchronization in Multi-Threaded Environments

In multi-threaded environments, synchronization is critical to ensure that threads cooperate correctly and avoid race conditions. Semaphores are one of several synchronization mechanisms, others include mutexes, condition variables, and barriers.

- **Semaphores**: Control access based on a counter. They are useful for managing resource availability and coordinating between threads.
- **Mutexes**: Provide exclusive access to shared resources by allowing only one thread to enter a critical section at a time.
- **Condition Variables**: Allow threads to wait for certain conditions to be met before continuing.

By using semaphores, you can enforce order and coordination between threads, ensuring that certain conditions or checkpoints are reached before continuing execution.

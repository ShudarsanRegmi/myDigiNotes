Got it. Let me reframe your ask first:

**Your Question (refined):**
“Can you also give me a last-minute revision sheet for Python before a competitive programming contest, just like the C++ one, covering STL-equivalent functions, custom sorting, common snippets, etc.?”

Here’s your **Python CP last-moment kit**:

---

## 🔑 Basics & Fast I/O

```python
import sys
input = sys.stdin.readline  # faster input

# Multiple inputs
n, m = map(int, input().split())
arr = list(map(int, input().split()))

# Output
print(*arr)   # space separated
```

---

## ⚡ Common Tricks

### 1. Sorting

```python
arr.sort()  # ascending
arr.sort(reverse=True)  # descending

# Custom sort
arr.sort(key=lambda x: (x[0], -x[1]))
```

### 2. Heap (priority queue)

```python
import heapq
pq = []
heapq.heappush(pq, 5)
heapq.heappush(pq, 1)
print(heapq.heappop(pq))  # min element
```

### 3. Counter & Frequency

```python
from collections import Counter
cnt = Counter(arr)
print(cnt.most_common(1))  # most frequent
```

### 4. Defaultdict

```python
from collections import defaultdict
g = defaultdict(list)
g[1].append(2)
```

### 5. Deque

```python
from collections import deque
dq = deque([1,2,3])
dq.appendleft(0)
dq.pop()
```

---

## 🛠 Math & Utilities

```python
import math
math.gcd(a, b)
math.lcm(a, b)

# Modular arithmetic
MOD = 10**9+7
res = (a * b) % MOD

# Power with mod
pow(a, b, MOD)  
```

---

## 🎯 Itertools Magic

```python
from itertools import permutations, combinations, accumulate

list(permutations([1,2,3]))    # all perms
list(combinations([1,2,3], 2)) # choose 2
list(accumulate([1,2,3]))      # prefix sums
```

---

## 🔥 Binary Search

```python
import bisect
arr = [1,2,4,4,5]
bisect.bisect_left(arr, 4)  # first >= 4
bisect.bisect_right(arr, 4) # first > 4
```

---

## 🏹 Quick Template

```python
import sys
import math
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations, accumulate
import bisect
import heapq

input = sys.stdin.readline

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    # logic

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()
```

---

# CPP for CP : Transition from Python
---

## **1. Input/Output**
### Python
```python
# Single input
n = int(input())

# Multiple inputs
a, b = map(int, input().split())

# Array input
arr = list(map(int, input().split()))
```

### C++
```cpp
#include <iostream>
#include <vector>
using namespace std;

// Single input
int n;
cin >> n;

// Multiple inputs
int a, b;
cin >> a >> b;

// Array input
int size;
cin >> size;
vector<int> arr(size);
for (int i = 0; i < size; ++i) cin >> arr[i;
```

### Key Differences:
- `cin` in C++ doesn’t handle whitespace automatically like Python's `input()`.
- Use `std::vector` for dynamic arrays.

---

## **2. Looping**
### Python
```python
# Range loop
for i in range(10):
    print(i)

# Iterating over a list
arr = [1, 2, 3]
for elem in arr:
    print(elem)
```

### C++
```cpp
#include <iostream>
#include <vector>
using namespace std;

// Range loop
for (int i = 0; i < 10; ++i) {
    cout << i << endl;
}

// Iterating over a vector
vector<int> arr = {1, 2, 3};
for (int elem : arr) {
    cout << elem << endl;
}
```

### Key Differences:
- C++'s `for` loop is more verbose but very flexible.
- The `for-each` loop in C++ uses `:` syntax.

---

## **3. Sorting**
### Python
```python
arr = [3, 1, 2]
arr.sort()  # Ascending
arr.sort(reverse=True)  # Descending
```

### C++
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> arr = {3, 1, 2};
sort(arr.begin(), arr.end());  // Ascending
sort(arr.rbegin(), arr.rend());  // Descending
```

### Key Differences:
- In C++, use `sort()` with iterators.
- For descending order, use `rbegin()` and `rend()`.

---

## **4. Max/Min and Sum**
### Python
```python
arr = [3, 1, 2]
print(max(arr))  # Max
print(min(arr))  # Min
print(sum(arr))  # Sum
```

### C++
```cpp
#include <iostream>
#include <vector>
#include <numeric> // For accumulate
using namespace std;

vector<int> arr = {3, 1, 2};
cout << *max_element(arr.begin(), arr.end()) << endl; // Max
cout << *min_element(arr.begin(), arr.end()) << endl; // Min
cout << accumulate(arr.begin(), arr.end(), 0) << endl; // Sum
```

### Key Differences:
- Use `max_element` and `min_element` for max/min.
- Use `accumulate` from `<numeric>` for the sum.

---

## **5. Custom Sorting**
### Python
```python
arr = [(1, 2), (2, 1), (3, 3)]
arr.sort(key=lambda x: x[1])  # Sort by second element
```

### C++
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<pair<int, int>> arr = {{1, 2}, {2, 1}, {3, 3}};
sort(arr.begin(), arr.end(), [](pair<int, int> a, pair<int, int> b) {
    return a.second < b.second;  // Sort by second element
});
```

### Key Differences:
- C++ requires a custom comparator (lambda or function).

---

## **6. Set and Map**
### Python
```python
s = {1, 2, 3}  # Set
print(1 in s)  # Check existence

m = {'a': 1, 'b': 2}  # Dictionary (Map)
print(m['a'])  # Access
```

### C++
```cpp
#include <iostream>
#include <set>
#include <map>
using namespace std;

set<int> s = {1, 2, 3};  // Set
cout << (s.count(1) > 0) << endl;  // Check existence

map<char, int> m = {{'a', 1}, {'b', 2}};  // Map
cout << m['a'] << endl;  // Access
```

### Key Differences:
- C++ uses `set` and `map` from the STL.
- Use `.count()` to check for existence in a `set`.

---

## **7. Strings**
### Python
```python
s = "hello"
print(s[::-1])  # Reverse
```

### C++
```cpp
#include <iostream>
#include <algorithm>
using namespace std;

string s = "hello";
reverse(s.begin(), s.end());
cout << s << endl;  // Reverse
```

### Key Differences:
- Strings in C++ are mutable and part of the STL.

---

## **8. Modular Arithmetic**
### Python
```python
MOD = 10**9 + 7
result = (a * b) % MOD
```

### C++
```cpp
const int MOD = 1e9 + 7;
int result = (a * 1LL * b) % MOD;  // Use 1LL to avoid overflow
```

### Key Differences:
- Explicitly handle overflow in C++.

---

## **9. Combinations**
### Python
```python
from itertools import combinations
arr = [1, 2, 3]
for comb in combinations(arr, 2):
    print(comb)
```

### C++
```cpp
#include <iostream>
#include <vector>
#include <bitset>
using namespace std;

vector<int> arr = {1, 2, 3};
int n = arr.size();
for (int mask = 0; mask < (1 << n); ++mask) {
    vector<int> comb;
    for (int i = 0; i < n; ++i) {
        if (mask & (1 << i)) comb.push_back(arr[i]);
    }
    // comb contains a combination
}
```

### Key Differences:
- Use bit manipulation for combinations in C++.

---

## **10. Standard Template Library (STL) Must-Know**
C++ has powerful tools like:
- **Vectors**: Dynamic arrays.
- **Sets and Maps**: Like Python's `set` and `dict`.
- **Priority Queues**: Similar to `heapq` in Python.
- **Algorithms**: `sort`, `lower_bound`, `upper_bound`.

---

## **Tips for CP in C++**
1. Use `#define` for frequently used macros:
   ```cpp
   #define MOD 1000000007
   #define fast_io ios::sync_with_stdio(0); cin.tie(0);
   ```
2. Prefer `vector` over raw arrays for dynamic resizing.
3. Optimize input/output for large data:
   ```cpp
   ios::sync_with_stdio(0);
   cin.tie(0);
   ```
4. Use `auto` to simplify iterator-heavy code.

## 🔑 STL Essentials

### 1. Vectors

```cpp
vector<int> v; 
v.push_back(10); v.pop_back();
sort(v.begin(), v.end()); // ascending
sort(v.rbegin(), v.rend()); // descending
```

### 2. Sets & Maps

```cpp
set<int> s; s.insert(5); s.erase(5); 
if(s.count(5)) { } // check existence

map<int,int> mp; mp[1] = 100;
unordered_map<int,int> ump; // avg O(1)
```

### 3. Priority Queue

```cpp
priority_queue<int> pq; // max-heap
priority_queue<int, vector<int>, greater<int>> pqmin; // min-heap
```

---

## ⚡ Common Algorithms

```cpp
sort(a.begin(), a.end());
reverse(a.begin(), a.end());
auto it = lower_bound(a.begin(), a.end(), x); // >= x
auto it2 = upper_bound(a.begin(), a.end(), x); // > x
```

`next_permutation(a.begin(), a.end());`

`__gcd(a, b)` → gcd
`lcm(a,b) = a / __gcd(a,b) * b;`

---

## 🛠 Custom Comparator Syntax

### 1. For `sort()`

```cpp
bool cmp(pair<int,int>& a, pair<int,int>& b) {
    if(a.first == b.first) return a.second < b.second;
    return a.first > b.first; // descending by first
}
sort(v.begin(), v.end(), cmp);
```

### 2. For `priority_queue`

```cpp
struct Compare {
    bool operator()(int a, int b) {
        return a > b; // min-heap
    }
};
priority_queue<int, vector<int>, Compare> pq;
```

---

## 🎯 Useful Tricks

### 1. Fast IO

```cpp
ios::sync_with_stdio(false);
cin.tie(nullptr);
```

### 2. Fixed Precision

```cpp
cout << fixed << setprecision(10) << ans;
```

### 3. Bit Operations

```cpp
__builtin_popcount(x);   // count 1s
__builtin_clz(x);        // leading zeros
__builtin_ctz(x);        // trailing zeros
```

### 4. Ranges & Loops

```cpp
for(auto &x : v) cout << x << " ";
```

---

## 🏹 Template Snippet

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define all(x) x.begin(), x.end()

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t; cin >> t;
    while(t--) {
        // solve
    }
}
```

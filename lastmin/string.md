# C++ String function revision cheatsheet

---

## 🔹 Initialization

```cpp
string s = "hello";
string t(5, 'a'); // "aaaaa"
```

---

## 🔹 Basic Properties

```cpp
s.size();       // length of string
s.length();     // same as size()
s.empty();      // true if empty
s.clear();      // clears string
```

---

## 🔹 Accessing Characters

```cpp
s[i];           // access (0-indexed)
s.at(i);        // bounds-checked access
s.front();      // first character
s.back();       // last character
```

---

## 🔹 Modifying

```cpp
s.push_back('x');  // append char
s.pop_back();      // remove last char
s += "world";      // concatenate
s.append("abc");   // append
s.insert(2, "zz"); // insert at index 2
s.erase(2, 3);     // erase 3 chars from index 2
s.replace(2, 3, "new"); // replace substring
reverse(s.begin(), s.end()); // reverse
```

---

## 🔹 Substrings

```cpp
s.substr(pos, len); // substring from pos of length len
```

---

## 🔹 Searching

```cpp
s.find("lo");     // index of first "lo" or npos
s.rfind("lo");    // last occurrence
s.find_first_of("aeiou");   // first vowel
s.find_last_of("aeiou");    // last vowel
s.find_first_not_of("aeiou"); // first consonant
```

---

## 🔹 Comparison

```cpp
s == t;       // equality
s.compare(t); // 0 if equal, <0 if s<t, >0 if s>t
```

---

## 🔹 Conversion

```cpp
stoi("123");         // string → int
stoll("123456");     // string → long long
stof("3.14");        // string → float
to_string(123);      // int → string
```

---

## 🔹 Iteration

```cpp
for (char c : s) { ... }
for (int i=0; i<s.size(); i++) { ... }
```

---

## 🔹 Useful Tricks in CP

* `sort(s.begin(), s.end());` → sort characters
* `count(s.begin(), s.end(), 'a');` → frequency of char
* `unique(s.begin(), s.end());` → remove consecutive duplicates (after sorting usually)
* `stringstream ss(s);` → split words from a string

---

## Complexity Analysis

Perfect — let’s add **time complexities** so you know what’s safe in competitive programming vs. what might TLE you.

**Rephrased Question:** *Can you give me the time complexity of commonly used C++ string functions for CP and interviews?*

---

# ⚡ C++ String Functions with Time Complexity

## 🔹 Basics

* `s.size()` / `s.length()` → **O(1)**
* `s.empty()` → **O(1)**
* `s.clear()` → **O(n)** (destroys all chars, sometimes optimized to O(1) in practice)

---

## 🔹 Accessing Characters

* `s[i]`, `s.at(i)` → **O(1)**
* `s.front()`, `s.back()` → **O(1)**

---

## 🔹 Modifying

* `s.push_back(ch)` → **Amortized O(1)**
* `s.pop_back()` → **O(1)**
* `s += "world"` / `s.append(str)` → **O(len(str))**
* `s.insert(pos, str)` → **O(n)** (may shift elements)
* `s.erase(pos, len)` → **O(n)** (shifts leftover chars)
* `s.replace(pos, len, str)` → **O(n)**
* `reverse(s.begin(), s.end())` → **O(n)**

---

## 🔹 Substrings

* `s.substr(pos, len)` → **O(len)** (copies characters)

---

## 🔹 Searching

* `s.find("pattern")` → **O(n \* m)** worst case (n = string size, m = pattern size).

  * For heavy CP, use **KMP** or **Z-algo** for O(n+m).
* `s.rfind()`, `s.find_first_of()`, `s.find_last_of()` → **O(n \* k)** (k = size of search set).

---

## 🔹 Comparison

* `s == t` → **O(min(n, m))**
* `s.compare(t)` → **O(min(n, m))**

---

## 🔹 Conversion

* `stoi`, `stoll`, `stof` → **O(len)**
* `to_string(x)` → **O(len of number)**

---

## 🔹 Iteration

* `for (char c : s)` → **O(n)**

---

## 🔹 STL Tricks

* `sort(s.begin(), s.end())` → **O(n log n)**
* `count(s.begin(), s.end(), 'a')` → **O(n)**
* `unique(s.begin(), s.end())` → **O(n)** (but only removes consecutive duplicates).
* `stringstream` splitting → **O(n)**

---

# 🔑 CP Guidelines

* Avoid repeated `insert` / `erase` in the **middle** of a string → costly (O(n) each).
* Use `push_back` / `pop_back` for efficient growth like a dynamic array.
* Prefer `substr` carefully — it **copies** chars; use iterators/ranges if possible.
* For pattern search → replace `find()` with **KMP/Z/Rabin-Karp** when constraints are big.


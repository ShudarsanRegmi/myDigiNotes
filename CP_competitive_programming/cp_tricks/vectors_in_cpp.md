# Vectors in CPP


### Declaring and Initializing a Vector
```cpp
vector<T> vec_name;
// initializing a vector with default size
vector<T> vec_name(size, value);
vector<T> vec_name = { v1, v2, v3….};
vector<T> vec_name ({ v1, v2, v3….});
vector<data_type> identifier;
vector<int> vec
vector<float> vec;
```

### Accessing Member
```cpp
vec.at(index);
vec[index]
```

### Updating Member
```cpp
vec.at(index) = 5;
vec[index] = 19;
```

### Inserting element
```cpp
v.push_back('z');
v.insert(v.begin() + 1, 'c');
```
### Deleting Elements
```cpp
v.pop_back();
v.erase(find(v.begin(), v.end(), 'f'));
v.erase(v.begin() + 1);
```

#### Finding the length of vector
```cpp
vec.size()
```

#### Removing an element from a specific index 
```cpp
v.erase(v.begin() + 1);
```

#### Sorting a Vector
```cpp
sort(v.begin(), v.end() // in ascending order
sort(vec.begin(), vec.end(), greater<int>());
```
#### Reversing a vector
```cpp
reverse(v.begin(), v.end()
```

### Removing duplicates
```cpp
set<int> mySet(vec.begin(), vec.end()); // remove the duplicate by changing to set
vector<int> myVec(mySet.begin(). mySet.end()); // convert back to the vector
```
### Find maximum and minimum in vector

```cpp
int maxElem = *max_element(vec.begin(), vec.end());
int minElem = *min_element(vec.begin(), vec.end());
```

#### Sum of Elements in a vector
```cpp
int sum = accumulate(vec.begin(), vec.end(), 0);
```

#### Checking for emptiness
```cpp
if(vec.empty()) {
    // vector is empty
}
```

#### Inserting at  a specific position
```cpp
vec.insert(vec.begin() + 2, 10); // insert 10  at index 2
```

#### Erasing an element at specific position
```cpp
vec.erase(vec.begin() + 2);
```

### Resizing a vector
```cpp
vec.resize(10); // larger elements are removed
vec.resize(10, 0);
```

### Check for existence of an element in vector
```cpp
if (find(vec.begin(), vec.end(), 5) != vec.end()) {
  // element exists
}
```

### Filling a vector with a specific value
```cpp
fill(vec.begin(), vec.end(), 5);
```

### Erase a vector in a given range
```cpp
vec.erase(vec.begin() + 2, vec.begin()+5); // erase from index 2 to 4
```

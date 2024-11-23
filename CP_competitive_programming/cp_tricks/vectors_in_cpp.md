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
```

#### Finding the length of vector
```cpp
vec.size()
```


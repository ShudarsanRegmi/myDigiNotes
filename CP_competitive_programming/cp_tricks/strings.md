# Note for Strings in CPP

### Finding the length
```cpp
s.length()
```

### Reversing a string
```cpp
reverse(s.begin(), s.end())
```

### Substring extraction
```cpp
s.substring(l, r-l+1)
```
### Finding the first occurance of a character 
```cpp
s.find('c');
// npos will be returned if not found
```
### String to integer conversion
```cpp
stoi(s);
```
### Counting the frequency of each character
```cpp
unordered_map<char, int> freq;
    
for (char c : s) {
  freq[c]++;
}
```
### Transforming to lowercase 
```cpp
transform(s.begin(), s.end(), s.begin(), ::tolower);
```

### Trnasforming to uppwercase
```cpp
transform(s.begin(), s.end(), s.begin(), ::toupper);
```


### Erase character from a string
```cpp
s.erase(2,1);
```

### 
```cpp

```

### 
```cpp

```



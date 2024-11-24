# HashMaps

### Creating a Frequency map
```cpp
unordered_map<int, int> freqMap;
for ( int  i : arr){
  freqMap[i]++;
}
```

### Check if a key exists in a hashmap
```cpp
if (umap.find(key) != umap.end()) {
  // key exists
}
```

### Count Distinct elements in a range
```cpp

```

### Sort a hashmap by keys
```cpp
vector<pair<int, int>> sortedPairs(umap.begin(), umap.end());
sort(sortedPairs.begin(), sortedPairs.end(), [](auto &a, auto &b) {
  return a.first < b.first;
}
```

### Erase  Key from hashmap
```cpp
umap.erase(key);
```

###
```cpp

```

###
```cpp

```

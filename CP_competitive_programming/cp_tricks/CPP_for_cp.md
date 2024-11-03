# CPP concepts that are useful in competitive programming


## <algorithm> Library

### Sorting 
- sort(vec.begin(), vec.end());
  - Sorting Ascending Order 
- sort(vec.rbegin(), vec.rend());
  - Sorting in Descending order

### Searching
- find(begin, end, element_to_find);
  - Finds for the first occurance of `element_to_find`
  - E.g. ``` auto it = find(numbers.begin(), numbers.end(), 3); ```

- upper_bound(begin, end, value);
  - Finds the first occurance which is greater than the value
  - E.g. ```auto it = upper_bound(numbers.begin(), numbers.end(), 5); ```
  - 

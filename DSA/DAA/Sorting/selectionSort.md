# Selection Sort

### Algorithm

```
loop i : [1,n]
  mi = ar[i]
  loop j : [i+1, n]
    if ar[j] < ar[i]:
      mi = j
  swap(ar[j], ar[mi])

```

```
loop i : [0, n-1]  // Loop from 0 to n-1 for 0-indexed array
  mi = i            // mi is the index of the minimum element
  loop j : [i+1, n-1]
    if ar[j] < ar[mi]:
      mi = j         // Update mi to the index of the smaller element
  swap(ar[i], ar[mi])  // Swap the found minimum with the element at i
```


### Algorithm:
![image](https://github.com/user-attachments/assets/66303e60-58e3-49df-9b08-9fd2af24d83d)


### Code
```cpp
void selectionSort(vector<int> &arr) {
        int si;
        for (int i=0; i< arr.size(); i++) {
            si = i;
            for (int j=i+1; j<arr.size(); j++) {
                if (arr[j] < arr[si]) si = j;
            }
            swap(arr[i], arr[si]);
        }
    }
// Revised on DSA Midsem Exam
// Revised again on dsa endsem lab exam : Wednesday 26 March 2025 06:58:28 PM IST
```

![image](https://github.com/user-attachments/assets/bb363739-2e3b-46a9-9886-c63380c47b04)


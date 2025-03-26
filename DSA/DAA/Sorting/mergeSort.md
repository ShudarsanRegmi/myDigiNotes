# Merge Sort


## C cide
```c
// Merge sort in C++
#include <iostream>
#include <vector>
using namespace std;

// Merge two subarrays L and M into arr
void merge(int arr[], int p, int q, int r) {
  
  // Create L ← A[p..q] and M ← A[q+1..r]
  int n1 = q - p + 1;
  int n2 = r - q;
  
  // Use std::vector to dynamically allocate arrays
  vector<int> L(n1);
  vector<int> M(n2);
  
  for (int i = 0; i < n1; i++)
    L[i] = arr[p + i];
    
  for (int j = 0; j < n2; j++)
    M[j] = arr[q + 1 + j];
    
  // Maintain current index of sub-arrays and main array
  int i = 0, j = 0, k = p;
  
  // Until we reach either end of either L or M, pick larger among
  // elements L and M and place them in the correct position at A[p..r]
  while (i < n1 && j < n2) {
    if (L[i] <= M[j]) {
      arr[k] = L[i];
      i++;
    } else {
      arr[k] = M[j];
      j++;
    }
    k++;
  }
  
  // When we run out of elements in either L or M,
  // pick up the remaining elements and put in A[p..r]
  while (i < n1) {
    arr[k] = L[i];
    i++;
    k++;
  }
  
  while (j < n2) {
    arr[k] = M[j];
    j++;
    k++;
  }
}

// Divide the array into two subarrays, sort them and merge them
void mergeSort(int arr[], int l, int r) {
  if (l < r) {
    // m is the point where the array is divided into two subarrays
    int m = l + (r - l) / 2;
    
    mergeSort(arr, l, m);
    mergeSort(arr, m + 1, r);
    // Merge the sorted subarrays
    merge(arr, l, m, r);
  }
}

// Print the array
void printArray(int arr[], int size) {
  for (int i = 0; i < size; i++)
    cout << arr[i] << " ";
  cout << endl;
}

// Driver program
int main() {
  int arr[] = {6, 5, 12, 10, 9, 1};
  int size = sizeof(arr) / sizeof(arr[0]);
  mergeSort(arr, 0, size - 1);
  cout << "Sorted array: \n";
  printArray(arr, size);
  return 0;
}
```

## C++ Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

void merge(vector<int> &arr, int l, int m, int r) {
    int n1 = m-l+1;
    int n2 = r-m; // 0 1 2 3 4 5

    vector<int> L(n1), R(n2);

    // fill the left and right array
    for (int i=0; i<n1; i++) {
        L[i] = arr[l+i];
    }
    for (int i=0; i<n2; i++) {
        R[i] = arr[m+1+i];
    }

    int i=0, j=0, k=l;
    while (i<n1 && j<n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        }else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    while (i<n1) {
        arr[k] = L[i];
        i++; k++;
    }
    while (j<n2) {
        arr[k] = R[j];
        j++; k++;
    }
}

void mergeSort(vector<int> &arr, int l, int r) {
    if (l<r) {
        int m = l + (r-l)/2;
        mergeSort(arr, l, m);
        mergeSort(arr, m+1, r);
        merge(arr, l, m, r);
    }
}

void printArray(vector<int> &arr) {
    for (int i : arr) {
        cout << i << " ";
    }
    cout << endl;
}

int main() {
    vector<int> arr = {5,4,3,2,1};
    cout << "Input Array is: " << endl;
    printArray(arr);
    mergeSort(arr, 0, arr.size()-1);
    cout << "After Sorting: " << endl;
    printArray(arr);
    return 0;
}
```

## Refactored
```cpp
#include <iostream>
#include <vector>

using namespace std;

void printArray(vector<int> &arr) {
    for (int i : arr) {
        cout << i << " ";
    }
    cout << endl;
}

void merge(vector<int> &arr, int l, int m, int r) {
    int n1 = m-l+1;
    int n2 = r-m;

    vector<int> L(n1), R(n2);

    // copy the value to those vectors
    for (int i=0; i<n1; i++) L[i] = arr[l+i];
    for (int j=0; j<n2; j++) R[j] = arr[m+1+j];

    int i=0,j=0,k=l;
    while(i<n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k++] = L[i++];
        }else{
            arr[k++] = R[j++];
        }
    }
    while(i < n1) arr[k++] = L[i++];
    while(j < n2) arr[k++] = R[j++];
}

void mergeSort(vector<int> &arr, int l, int r) {
    if (l < r) {
        int m = l + (r-l)/2;
        mergeSort(arr, l, m);
        mergeSort(arr, m+1, r);
        merge(arr, l, m, r);
    }
}

int main() {
    vector<int> arr = {1,9,2,7,-11,-15};
    printArray(arr);
    mergeSort(arr, 0, arr.size()-1);
    printArray(arr);
    return 0;
}
```

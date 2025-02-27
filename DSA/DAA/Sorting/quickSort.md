# Quick Sort


```cpp
#include <iostream>
#include <vector>

using namespace std;

int partition(vector<int> &arr, int l, int r) {
    int pivot = arr[r];
    int i = l-1;

    for (int j=l; j<r; j++) {
        if (arr[j] < pivot) {
            i++;
            swap(arr[j], arr[i]);
        }
    }
    swap(arr[i+1], arr[r]);
    return i+1;
}

void quickSort(vector<int> &arr, int l, int r) {
    if (l<r) {
        int pi = partition(arr, l , r);
        quickSort(arr, l, pi-1);
        quickSort(arr, pi+1, r);
    }
}


int main() {
    vector<int> arr = {10, 7, 8, 9, 1, 5};
    int n = arr.size();
    quickSort(arr, 0, n-1);
    for (int i : arr) cout << i << " ";
    cout << endl;
    return 0;
}
// written by following from gfg
```

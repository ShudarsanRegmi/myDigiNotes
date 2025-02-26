# Count Sort

```cpp
#include <iostream>
#include <vector>
using namespace std;

// Function to print the array of pairs
void printArray(vector<int> &arr) {
    for (int i: arr) {
        cout << i << " ";
    }
    cout << endl;
}

vector<int> countSort(vector<int> &arr) {
    // create the count array
    int n = arr.size();
    vector<int> output(n, 0);

    int max = *max_element(arr.begin(), arr.end());

    // create the count array
    vector<int> count(max+1, 0);
    for (int i : arr) count[i]++;

    // store the prefix sum
    for (int i=1; i<=max; i++) count[i] += count[i-1];

    // map it to the output array
    for (int i=n-1; i>=0; i--) {
        int num = arr[i];
        output[--count[num]] = num;
    }
    return output;
}

int main() {
    vector<int> inparr =  { 4, 3, 12, 1, 5, 5, 3, 9 };
    cout << "Input Array " << endl;
    printArray(inparr);
    vector<int> outarr = countSort(inparr);
    cout << "Output Array " << endl;
    printArray(outarr);
    return 0;
}
```

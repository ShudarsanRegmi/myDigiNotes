# Bucket Sort

```cpp
#include <iostream>
#include <vector>
#include <algorithm> // For sort()

using namespace std;

void bucketSort(vector<float> &arr) {
    int n = arr.size();

    vector<vector<float>> buckets(n);

    // fill all the buckets with right element
    for (float i : arr) {
        int idx = i*10;
        if (idx >= n) idx = n-1;
        buckets[idx].push_back(i);
    }

    // sort each bucket
    for (int i=0; i<n; i++) {
        sort(buckets[i].begin(), buckets[i].end());
    }

    // merge teh sorted buckets
    int index=0;
    for (int i=0; i<n; i++) {
        for (float item : buckets[i]) {
            arr[index++] = item;
        }
    }

    // displaying the output
    for (float i : arr) {
        cout << " ";
    }
    cout << endl;
}

int main() {
    vector<float> arr = {0.5, 1.4, 2.3, 3.2, 0.1, 0.7, 0.765};
    
    cout << "Original array: ";
    for (float i : arr) cout << i << " ";
    cout << endl;

    bucketSort(arr);

    cout << "Sorted array: ";
    for (float i : arr) cout << i << " ";
    cout << endl;

    return 0;
}

```

# Heaps code


```cpp
#include <iostream>
#include <vector>

using namespace std;

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

void heapify(vector<int> &hT, int i) {
    int size = hT.size();
    int largest = i;
    int l = 2*i + 1;
    int r = 2*i + 2;
    if (l < size && hT[r] > hT[largest])
        largest = r;
    if (r < size && hT[r] > hT[largest])
        largest = l;

    if (largest != i) {
        swap(&hT[i], &hT[largest]);
        heapify(hT, largest);
    }
}

void insert(vector<int> &hT, int newNum) {
    hT.push_back(newNum);
    int current = hT.size() - 1;

    // Bubble up
    while (current > 0) {
        int parent = (current - 1) / 2;
        if (hT[current] > hT[parent]) {
            swap(&hT[current], &hT[parent]);
            current = parent;
        }else {
            break;
        }
    }
}

void deleteNode(vector<int> &hT, int num) {
    int size = hT.size();
    int i;
    for (i=0; i<size; i++) {
        if (num == hT[i])
            break;
    }
    swap(&hT[i], &hT[size-1]);
    hT.pop_back();

    // Update size after popping
    size = hT.size();

    // Heapify from the current index to adjust the rest of the heap

    if (i < size) {
        heapify(hT, i);
    }
}

void printArray(const vector<int> &hT) {
    for (int num : hT)
        cout << num << " ";
    cout << "\n";
}

int main() {
    vector<int> heapTree;

    insert(heapTree, 3);
    insert(heapTree, 4);
    insert(heapTree, 9);
    insert(heapTree, 5);
    insert(heapTree, 2);

    cout << "Max-Heap Array" << endl;
    printArray(heapTree);

    deleteNode(heapTree, 4);
    cout << "Array After deleitng" << endl;
    printArray(heapTree);

    return 0;


}
```

**If any bug above** <br>
```cpp
#include <iostream>
#include <vector>

using namespace std;

// Heapify function to maintain the max-heap property
void heapify(vector<int> &hT, int i) {
    int size = hT.size();
    int largest = i;
    int l = 2 * i + 1;  // Left child
    int r = 2 * i + 2;  // Right child

    if (l < size && hT[l] > hT[largest])
        largest = l;
    if (r < size && hT[r] > hT[largest])
        largest = r;

    if (largest != i) {
        swap(hT[i], hT[largest]); // Using built-in swap
        heapify(hT, largest);
    }
}

// Insert a new element into the heap
void insert(vector<int> &hT, int newNum) {
    hT.push_back(newNum);
    int current = hT.size() - 1;

    // Bubble up
    while (current > 0) {
        int parent = (current - 1) / 2;
        if (hT[current] > hT[parent]) {
            swap(hT[current], hT[parent]);
            current = parent;
        } else {
            break;
        }
    }
}

// Delete a specific element from the heap
void deleteNode(vector<int> &hT, int num) {
    int size = hT.size();
    int i;

    // Find the index of the element to delete
    for (i = 0; i < size; i++) {
        if (hT[i] == num)
            break;
    }

    if (i == size) {
        cout << "Element not found in heap!\n";
        return;
    }

    // Swap the element with the last element and remove it
    swap(hT[i], hT[size - 1]);
    hT.pop_back();

    // Restore heap property if necessary
    if (i < hT.size()) {
        heapify(hT, i);
    }
}

// Print heap elements
void printHeap(const vector<int> &hT) {
    for (int num : hT)
        cout << num << " ";
    cout << "\n";
}

// Main function
int main() {
    vector<int> heapTree;

    insert(heapTree, 3);
    insert(heapTree, 4);
    insert(heapTree, 9);
    insert(heapTree, 5);
    insert(heapTree, 2);

    cout << "Max-Heap Array: ";
    printHeap(heapTree);

    deleteNode(heapTree, 4);
    cout << "Array After Deleting 4: ";
    printHeap(heapTree);

    return 0;
}
```

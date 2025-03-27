# Priority Queue Implementation


```cpp
#include <iostream>
#include <vector>
#include <algorithm> // For heap operations like push_heap, pop_heap, etc.
using namespace std;

// PriorityQueue class to implement a min-heap
class PriorityQueue {
private:
    vector<int> heap; // Vector to hold the heap elements

public:
    // Insert an element into the priority queue
    void insert(int x) {
        // Insert the element at the end of the heap
        heap.push_back(x);
        // Reorganize the heap to maintain heap property (min-heap)
        push_heap(heap.begin(), heap.end(), greater<int>());
    }

    // Remove the smallest element (root of the heap)
    void remove() {
        if (heap.empty()) {
            cout << "Priority queue is empty!" << endl;
            return;
        }

        // Move the smallest element (root) to the end and then reorganize the heap
        pop_heap(heap.begin(), heap.end(), greater<int>());
        int smallest = heap.back(); // The smallest element to be removed
        heap.pop_back(); // Remove the smallest element from the heap

        // Output the removed element
        cout << "Removed element: " << smallest << endl;
    }

    // Print the contents of the priority queue
    void print() {
        cout << "Priority queue: ";
        for (int x : heap) {
            cout << x << " "; // Print each element in the heap
        }
        cout << endl;
    }
};

int main() {
    PriorityQueue pq;

    // Insert elements into the priority queue
    pq.insert(5);
    pq.insert(3);
    pq.insert(7);
    pq.insert(1);

    // Print the current state of the priority queue
    pq.print(); // Expected output: Priority queue: 1 3 7 5

    // Remove the smallest element
    pq.remove(); // Expected output: Removed element: 1

    // Print the current state of the priority queue
    pq.print(); // Expected output: Priority queue: 3 5 7

    // Insert another element into the priority queue
    pq.insert(4);

    // Print the current state of the priority queue
    pq.print(); // Expected output: Priority queue: 3 4 7 5

    // Remove the smallest element
    pq.remove(); // Expected output: Removed element: 3

    // Print the final state of the priority queue
    pq.print(); // Expected output: Priority queue: 4 5 7

    return 0;
}
```

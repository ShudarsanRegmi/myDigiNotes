# Queue using array

```cpp

#include <iostream>
using namespace std;

#define SIZE 5  // Maximum size of the queue

class Queue {
private:
    int items[SIZE]; // Array to store queue elements
    int front, rear; // Front and rear pointers

public:
    // Constructor to initialize queue
    Queue() {
        front = -1;
        rear = -1;
    }

    // Function to check if the queue is empty
    bool isEmpty() {
        return front == -1;
    }

    // Function to check if the queue is full
    bool isFull() {
        return rear == SIZE - 1;
    }

    // Function to add an element to the queue (enqueue)
    void enqueue(int value) {
        if (isFull()) {
            cout << "Queue is full! Cannot enqueue " << value << endl;
            return;
        }
        if (isEmpty())
            front = 0; // Set front to 0 when inserting the first element

        rear++;
        items[rear] = value;
        cout << "Enqueued: " << value << endl;
    }

    // Function to remove an element from the queue (dequeue)
    void dequeue() {
        if (isEmpty()) {
            cout << "Queue is empty! Cannot dequeue\n";
            return;
        }

        cout << "Dequeued: " << items[front] << endl;

        if (front == rear) {
            // Reset the queue if the last element is dequeued
            front = rear = -1;
        } else {
            front++;
        }
    }

    // Function to display the queue elements
    void display() {
        if (isEmpty()) {
            cout << "Queue is empty!\n";
            return;
        }

        cout << "Queue: ";
        for (int i = front; i <= rear; i++) {
            cout << items[i] << " ";
        }
        cout << endl;
    }
};

// Main function to test queue operations
int main() {
    Queue q;

    q.enqueue(10);
    q.enqueue(20);
    q.enqueue(30);
    q.display();

    q.dequeue();
    q.display();

    q.enqueue(40);
    q.enqueue(50);
    q.enqueue(60);  // This will fail because the queue is full
    q.display();

    return 0;
}
```
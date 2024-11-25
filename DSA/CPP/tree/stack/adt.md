# Stack Abstract Data Type (ADT)

## What is a Stack?

A **stack** is a linear data structure that follows the **Last In, First Out (LIFO)** principle. This means that the most recently added element is the first one to be removed. A stack can be thought of like a stack of plates in a cafeteria: you add plates on top, and when you need one, you take the top one.

### Key Operations on a Stack

- **Push**: Adds an element to the top of the stack.
- **Pop**: Removes and returns the top element from the stack.
- **Peek (or Top)**: Returns the top element of the stack without removing it.
- **isEmpty**: Checks if the stack is empty.
- **Size**: Returns the number of elements currently in the stack.

### Applications of Stacks

1. **Function Call Stack**: In programming languages like Java, C++, etc., the function call stack is used to store information about active subroutines and method calls.
2. **Expression Evaluation**: Stacks are used in evaluating expressions, such as infix, postfix, and prefix expressions.
3. **Backtracking Algorithms**: Stacks are used in backtracking algorithms, such as Depth-First Search (DFS), to keep track of visited nodes or states.
4. **Undo Mechanisms**: Stacks are used to implement undo functionality in applications where users can perform actions and then undo them one by one.
5. **Syntax Parsing**: Stacks are used in syntax parsing algorithms, such as the shunting-yard algorithm, for parsing mathematical expressions and programming languages.

### Implementation of Stacks

Stacks can be implemented in various ways, including:

- **Array-based Implementation**: In this approach, a fixed-size array is used to store the elements of the stack. While simple, this approach has limitations regarding the maximum capacity of the stack.
- **Linked List-based Implementation**: This approach uses a linked list data structure to implement the stack. It allows for dynamic memory allocation and can handle a larger number of elements compared to the array-based implementation.

### Time Complexity of Stack Operations

- **Push**: O(1)
- **Pop**: O(1)
- **Peek**: O(1)
- **isEmpty**: O(1)
- **Size**: O(1)

### Conclusion

Stacks are fundamental data structures used in various fields of computer science and software engineering. Their simplicity and efficiency make them invaluable for solving a wide range of problems. Understanding stacks and their operations is crucial for any programmer or computer science enthusiast.

---

## Implementation Using Array (C++ Code)

```cpp
#include <iostream>

using namespace std;

#define MAX 5
// Implementation using array

int Stack[MAX];
int top = -1; // top points to the last element, not the last empty space.
// This means we have to increment the top pointer to push the element.
// To remove the element, we decrement the top pointer.

bool isFull() {
    return (top >= MAX-1);
}

bool isEmpty() {
    return (top == -1);
}

void push(int item) {
    // Check if the stack is full
    if (isFull()) {
        cout << "Stack Overflow" << endl;
    } else {
        top++;           // Increment the top pointer
        Stack[top] = item; // Add the item at the new top position
    }
}

void pop() {
    // Check if the stack is empty
    if (isEmpty()) {
        cout << "Underflow.. Stack is empty " << endl;
    } else {
        top--;  // Decrement the top pointer
    }
}

int peek() {
    if (isEmpty()) {
        cout << "Stack is empty" << endl;
    } else {
        cout << Stack[top] << endl;
        return Stack[top];
    }
}

int main() {
    push(1); // 0th index
    push(2); // 1st index
    push(3); // 2nd index

    peek();  // Should print 3 (top of the stack)

    pop();    // Removes 3
    peek();   // Should print 2 (top of the stack)

    pop();    // Removes 2
    peek();   // Should print 1 (top of the stack)

    pop();    // Removes 1
    peek();   // Should indicate stack is empty

    pop();    // Underflow condition (stack is empty)

    // Filling the stack again
    push(1);
    push(2);
    push(3);
    push(4);
    push(5);  // Stack is full

    cout << "Filled all room" << endl;
    peek();   // Should print 5 (top of the stack)

    push(6);  // Stack Overflow (since stack is full)

    return 0;
}
```

---

## Stack Implementation Using Linked List

```cpp
#include <iostream>

using namespace std;

#define INT_MIN -12345

class Node {
    public:
        int val;
        Node *next;
        Node(int val) {
            this->val = val;
            this->next = nullptr;
        }
};

class Stack {
    Node *head;

    public:
    
    Stack() {this->head = nullptr;}

    bool isEmpty() {
        return head==nullptr;
    }

    void push(int val) {
        Node *newNode = new Node(val);

        if(!newNode) {
            // memory allocation failed...
            cout << "Stack Overflow" << endl;
        }
        newNode->next = head;
        head = newNode;
    }

    void pop() {
        if(this->isEmpty()) {
            cout << "Stack Underflow" << endl;
        }else{
            Node *temp = head; // this is required to dealocate memory for head
            head = head->next;
            delete temp;
        }
    }
    int peek() {
        if(this->isEmpty()) {
            cout << "Stack is empty";
            return INT_MIN;
        }else{
            return head->val;
        }
    }
};

int main() {
    Stack st;

    // Push elements onto the stack
    st.push(11);
    st.push(22);
    st.push(33);
    st.push(44);

    // Print top element of the stack
    cout << "Top element is " << st.peek() << endl;

    // removing two elemements from the top
    cout << "Removing two elements..." << endl;
    st.pop();
    st.pop();

    // Print top element of the stack
    cout << "Top element is " << st.peek() << endl;
    return 0;
}
```

## Main Points
- we don't need to predefine the size of stack. It is determined at low level..
- It is dynamic


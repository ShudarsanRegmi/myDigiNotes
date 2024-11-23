# Linked List


```cpp
// Linked list implementation in C++

#include <bits/stdc++.h>
#include <iostream>
using namespace std;

// Creating a node
class Node {
   public:
  int value;
  Node* next;
};

int main() {
  Node* head;
  Node* one = NULL;
  Node* two = NULL;
  Node* three = NULL;

  // allocate 3 nodes in the heap
  one = new Node();
  two = new Node();
  three = new Node();

  // Assign value values
  one->value = 1;
  two->value = 2;
  three->value = 3;

  // Connect nodes
  one->next = two;
  two->next = three;
  three->next = NULL;

  // print the linked list value
  head = one;
  while (head != NULL) {
    cout << head->value;
    head = head->next;
  }
}
```
### My Implementation

```cpp
// Design a singly linked list 

#include <iostream>

using namespace std;

typedef struct Node Node;

struct Node {
    int val;
    Node *next;
};


Node* createNode(int val) {
    Node *newNode = (Node *)malloc(sizeof(Node));
    newNode->val = val;
    return newNode;
}

void Traverse(Node *HEAD) {
    Node *temp = HEAD;

    while (temp !=  nullptr) {
        cout << temp->val << '\t';
        temp = temp->next;
    }
}

int main() {
    
    Node *n1 = createNode(1);
    Node *n2 = createNode(2);
    Node *n3 = createNode(3);
    Node *n4 = createNode(4);

    n1->next = n2;
    n2->next = n3;
    n3->next = n4;
    n4->next = nullptr;

    Node *HEAD = n1;

    Traverse(HEAD);

    return 0;
}
```

![image](https://github.com/user-attachments/assets/4b1a03d6-a969-4cc1-a87a-d635df684486)


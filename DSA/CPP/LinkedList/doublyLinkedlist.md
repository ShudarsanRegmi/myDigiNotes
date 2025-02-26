# Doubly Linked List



## Nominal Code


```cpp
#include <iostream>
#include <vector>

using namespace std;

typedef struct Node Node;


struct Node {
    int val;
    Node *next;
    Node *prev;

    Node(int val) : val(val), next(nullptr), prev(nullptr) {};
};


class DoublyLinkedList {
public:
    Node *head;
    DoublyLinkedList() {
        this->head = nullptr;
    }

    void insertAtFront(int val) {
        Node *newNode = new Node(val);
        if (!head) {
            head = newNode;
            return;
        }

        newNode->next = head;
        head->prev = newNode;
        head = newNode;
    }

    void insertAtLast(int val) {
        Node *newNode = new Node(val);
        if (!head) {
            head = newNode;
            return;
        }

        Node *temp = head;
        while (temp->next) temp=temp->next;

        temp->next = newNode;
        newNode->prev = temp;

    }

    void insertAtMiddle(int pos, int val) {
        int i=0;
        Node *newNode = new Node(val);

        if (!head) {
            head = newNode;
            return;
        }
        Node *temp = head;

        for (int i=0; i<pos-2; i++) {
            if (temp) {
                temp = temp->next;
            }else {
                cout << "out of bound" << endl;
                return;
            }
        }

        newNode->next = temp->next;
        temp->next->prev = newNode;
        temp->next = newNode;
        newNode->prev = temp;

    }


    void printLL() {
        cout << "Going to print linked list" << endl;
        Node *temp = head;
        while (temp) {
            cout << temp->val << " ";
            temp = temp->next;
        }
        cout << endl;
    }

};


int main() {
    DoublyLinkedList dbl;
    dbl.insertAtLast(1);
    dbl.insertAtLast(2);
    dbl.insertAtLast(3);
    dbl.insertAtLast(4);
    dbl.insertAtLast(5);

    dbl.insertAtFront(-5);
    dbl.insertAtFront(-6);
    dbl.insertAtFront(-7);

    dbl.insertAtMiddle(3,33);




    dbl.printLL();
    return 0;
}
```


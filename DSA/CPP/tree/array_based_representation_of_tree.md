# Array based representation of a Tree


```cpp
#include <iostream>
#include <vector>

using namespace std;


class BinaryTree {
public:
    vector<char> tree;
    int capacity;

    BinaryTree(int size) {
        capacity = size;
        tree.resize(capacity, '-');
    }

    // void set root
    void setRoot(char key) {
        if (tree[0] != '-') {
            cout << "Tree already has a root";
        }else {
            cout << "Setting up the root" << endl;
            tree[0] = key;
        }
    }

    // void set left
    void setLeft(char key, int p) {
        int l = p*2 + 1;
        if (l >= capacity) {
            cout << "Index out of bound" << endl;
            return;
        }

        if (tree[p] == '-') {
            cout << "Cound not set up child, parent not found" << endl;
        }else {
            tree[l] = key;
        }
    }

    void setRight(int key, int p) {
        int r = p*2 + 2;
        if (r>= capacity) cout << "Index out of bounds" << endl;
        if (tree[p] == '-') cout << "cannot set right child, parent not found";
        else {
            cout << "setting up the right child" << endl;
            tree[r] = key;
        }
    }

    void printTree() {
        for (char c : tree) {
            cout << c << " ";
        }
        cout << endl;
    }
};

int main() {
    BinaryTree bt(10);

    bt.setRoot('A');
    bt.setLeft('B', 0);
    bt.setRight('C', 0);
    bt.setLeft('D', 1);

    bt.printTree();
    return 0;
}
```

## Code : 2

```cpp
#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 100  // Maximum number of nodes

// Binary tree stored in an array
int tree[MAX_SIZE];

// Function to initialize tree with -1 (indicating empty nodes)
void initializeTree() {
    for (int i = 0; i < MAX_SIZE; i++) {
        tree[i] = -1;
    }
}

// Function to insert value into the binary tree
void insert(int value, int index) {
    if (index >= MAX_SIZE) {
        printf("Index out of bounds, cannot insert %d\n", value);
        return;
    }
    if (tree[index] != -1) {
        printf("Position %d already occupied\n", index);
        return;
    }
    tree[index] = value;
}

// Inorder traversal (Left - Root - Right)
void inorderTraversal(int index) {
    if (index >= MAX_SIZE || tree[index] == -1)
        return;

    inorderTraversal(2 * index + 1);  // Left child
    printf("%d ", tree[index]);       // Root
    inorderTraversal(2 * index + 2);  // Right child
}

int main() {
    initializeTree();
    
    // Inserting nodes manually
    insert(10, 0);  // Root
    insert(20, 1);  // Left child of 10
    insert(30, 2);  // Right child of 10
    insert(40, 3);  // Left child of 20
    insert(50, 4);  // Right child of 20
    insert(60, 5);  // Left child of 30
    insert(70, 6);  // Right child of 30

    printf("Inorder Traversal: ");
    inorderTraversal(0);
    printf("\n");

    return 0;
}
```


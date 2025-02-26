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

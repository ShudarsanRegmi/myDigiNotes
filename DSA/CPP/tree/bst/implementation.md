# Binary Search Tree Implementation


```cpp
#include <iostream>
#include <vector>

using namespace std;

// binary search tree

struct Node {
    Node *left=nullptr;
    Node *right=nullptr;
    int val;
    Node(int val, Node *left, Node *right) : val(val), left(left), right(right) {}
    Node(int val) : val(val) {}
};

Node *insert(Node *root, int val) {
    if (!root) return new Node(val);
    if (val < root->val) {
        root->left = insert(root->left, val);
    }else {
        root->right = insert( root->right, val);
    }

    return root;
}

bool search(Node *root, int val) {
    if (!root) {
        cout << "Element not found" << endl;
        return false;
    }
    if (root->val == val) {
        cout << "Element found !!" << endl;
        return true;
    }
    if (val < root->val) {
        search(root->left, val);
    }else {
        search(root->right, val);
    }
}


void inorder(Node *root) {
    if (root) {
        inorder(root->left);
        cout << root->val << " ";
        inorder(root->right);
    }
}

void deletee(Node*& root, int val) {
    if (!root) return;

    if (val < root->val) {
        deletee(root->left, val);
    } else if (val > root->val) {
        deletee(root->right, val);
    } else {
        // Node with only one child or no child
        if (!root->left) {
            Node* temp = root->right;
            delete root;
            root = temp;
        } else if (!root->right) {
            Node* temp = root->left;
            delete root;
            root = temp;
        } else {
            // Node with two children, get the inorder successor (smallest in the right subtree)
            Node* temp = root->right;
            while (temp->left) {
                temp = temp->left;
            }
            root->val = temp->val;
            deletee(root->right, temp->val);
        }
    }
}


int main() {
    // vector<int> values = {1,5,2,3,4,6};
    Node *root = new Node(5);
    insert(root,1);
    insert(root, 10);
    insert(root, 9);
    insert(root, 11);

    search(root, 15);
    search(root,11);


    inorder(root);
    return 0;
}
```

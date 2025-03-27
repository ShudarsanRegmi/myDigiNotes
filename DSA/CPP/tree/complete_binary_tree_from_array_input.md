# Creating a complete binary tree from array input


```cpp
#include <iostream>
#include <queue>
using namespace std;

// Node structure for the binary tree
struct Node {
    int data;
    Node* left;
    Node* right;

    Node(int val) {
        data = val;
        left = right = nullptr;
    }
};

// Class for the Complete Binary Tree
class CompleteBinaryTree {
private:
    Node* root; // Root of the tree

public:
    // Constructor
    CompleteBinaryTree() {
        root = nullptr;
    }

    // Function to insert a node in level order
    void insert(int value) {
        Node* newNode = new Node(value);

        if (!root) {
            root = newNode;
            return;
        }

        queue<Node*> q;
        q.push(root);

        while (!q.empty()) {
            Node* temp = q.front();
            q.pop();

            if (!temp->left) {
                temp->left = newNode;
                return;
            } else {
                q.push(temp->left);
            }

            if (!temp->right) {
                temp->right = newNode;
                return;
            } else {
                q.push(temp->right);
            }
        }
    }

    // Inorder Traversal (Left - Root - Right)
    void inorderTraversal(Node* node) {
        if (!node) return;

        inorderTraversal(node->left);
        cout << node->data << " ";
        inorderTraversal(node->right);
    }

    // Public function to start inorder traversal
    void displayInorder() {
        cout << "Inorder Traversal: ";
        inorderTraversal(root);
        cout << endl;
    }
};

int main() {
    CompleteBinaryTree cbt;
    int n, value;

    cout << "Enter number of elements: ";
    cin >> n;

    cout << "Enter " << n << " elements: ";
    for (int i = 0; i < n; i++) {
        cin >> value;
        cbt.insert(value);
    }

    cbt.displayInorder();

    return 0;
}

```

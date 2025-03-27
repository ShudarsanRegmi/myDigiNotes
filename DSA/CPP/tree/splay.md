# Splay Trees

```cpp
#include <iostream>
using namespace std;

// Node structure for Splay Tree
struct Node {
    int key;
    Node* left;
    Node* right;
    
    Node(int value) : key(value), left(nullptr), right(nullptr) {}
};

// Right rotate (Zig rotation)
Node* rightRotate(Node* x) {
    Node* y = x->left;
    x->left = y->right;
    y->right = x;
    return y;
}

// Left rotate (Zag rotation)
Node* leftRotate(Node* x) {
    Node* y = x->right;
    x->right = y->left;
    y->left = x;
    return y;
}

// Splay operation to move key to root
Node* splay(Node* root, int key) {
    if (!root || root->key == key)
        return root;

    // Key in left subtree
    if (key < root->key) {
        if (!root->left) return root;

        // Zig-Zig (Left Left)
        if (key < root->left->key) {
            root->left->left = splay(root->left->left, key);
            root = rightRotate(root);
        }
        // Zig-Zag (Left Right)
        else if (key > root->left->key) {
            root->left->right = splay(root->left->right, key);
            if (root->left->right)
                root->left = leftRotate(root->left);
        }

        return (root->left) ? rightRotate(root) : root;
    } 
    // Key in right subtree
    else {
        if (!root->right) return root;

        // Zag-Zag (Right Right)
        if (key > root->right->key) {
            root->right->right = splay(root->right->right, key);
            root = leftRotate(root);
        }
        // Zag-Zig (Right Left)
        else if (key < root->right->key) {
            root->right->left = splay(root->right->left, key);
            if (root->right->left)
                root->right = rightRotate(root->right);
        }

        return (root->right) ? leftRotate(root) : root;
    }
}

// Insert into Splay Tree
Node* insert(Node* root, int key) {
    if (!root) return new Node(key);

    root = splay(root, key);

    if (root->key == key)
        return root; // Duplicate keys not allowed

    Node* newNode = new Node(key);

    if (key < root->key) {
        newNode->right = root;
        newNode->left = root->left;
        root->left = nullptr;
    } 
    else {
        newNode->left = root;
        newNode->right = root->right;
        root->right = nullptr;
    }

    return newNode;
}

// Delete a node from the Splay Tree
Node* deleteNode(Node* root, int key) {
    if (!root)
        return nullptr;

    root = splay(root, key);

    if (root->key != key)
        return root;

    Node* temp;
    if (!root->left) {
        temp = root->right;
    } 
    else {
        temp = splay(root->left, key);
        temp->right = root->right;
    }

    delete root;
    return temp;
}

// Search in Splay Tree
Node* search(Node* root, int key) {
    return splay(root, key);
}

// Inorder Traversal (prints sorted order)
void inorder(Node* root) {
    if (root) {
        inorder(root->left);
        cout << root->key << " ";
        inorder(root->right);
    }
}

// Driver Code
int main() {
    Node* root = nullptr;

    // Insert values
    root = insert(root, 10);
    root = insert(root, 20);
    root = insert(root, 30);
    root = insert(root, 40);
    root = insert(root, 50);
    root = insert(root, 25);

    cout << "Inorder traversal of Splay Tree: ";
    inorder(root);
    cout << endl;

    // Search key and splay it to the root
    root = search(root, 30);
    cout << "After searching 30, root: " << root->key << endl;

    // Delete node
    root = deleteNode(root, 40);
    cout << "Inorder traversal after deleting 40: ";
    inorder(root);
    cout << endl;

    return 0;
}

```

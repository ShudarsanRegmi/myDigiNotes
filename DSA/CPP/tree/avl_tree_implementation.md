# AVL Tree implementation

```cpp
#include <iostream>
using namespace std;

// Node structure for AVL Tree
struct Node {
    int key;
    Node* left;
    Node* right;
    int height;
    
    Node(int value) : key(value), left(nullptr), right(nullptr), height(1) {}
};

// Get the height of a node
int getHeight(Node* node) {
    return node ? node->height : 0;
}

// Get the balance factor of a node
int getBalanceFactor(Node* node) {
    return node ? getHeight(node->left) - getHeight(node->right) : 0;
}

// Update height of a node
void updateHeight(Node* node) {
    if (node) {
        node->height = 1 + max(getHeight(node->left), getHeight(node->right));
    }
}

// Right rotation
Node* rightRotate(Node* y) {
    Node* x = y->left;
    Node* T2 = x->right;
    
    // Perform rotation
    x->right = y;
    y->left = T2;

    // Update heights
    updateHeight(y);
    updateHeight(x);

    return x;
}

// Left rotation
Node* leftRotate(Node* x) {
    Node* y = x->right;
    Node* T2 = y->left;

    // Perform rotation
    y->left = x;
    x->right = T2;

    // Update heights
    updateHeight(x);
    updateHeight(y);

    return y;
}

// Insert a node into the AVL Tree
Node* insert(Node* root, int key) {
    if (!root) return new Node(key);

    if (key < root->key)
        root->left = insert(root->left, key);
    else if (key > root->key)
        root->right = insert(root->right, key);
    else
        return root;  // Duplicate keys not allowed

    // Update height
    updateHeight(root);

    // Get balance factor
    int balance = getBalanceFactor(root);

    // Balancing cases
    if (balance > 1 && key < root->left->key)
        return rightRotate(root); // Left Left case

    if (balance < -1 && key > root->right->key)
        return leftRotate(root); // Right Right case

    if (balance > 1 && key > root->left->key) {
        root->left = leftRotate(root->left);
        return rightRotate(root); // Left Right case
    }

    if (balance < -1 && key < root->right->key) {
        root->right = rightRotate(root->right);
        return leftRotate(root); // Right Left case
    }

    return root;
}

// Get the node with minimum value
Node* getMinValueNode(Node* node) {
    Node* current = node;
    while (current->left)
        current = current->left;
    return current;
}

// Delete a node from the AVL Tree
Node* deleteNode(Node* root, int key) {
    if (!root)
        return root;

    if (key < root->key)
        root->left = deleteNode(root->left, key);
    else if (key > root->key)
        root->right = deleteNode(root->right, key);
    else {
        if (!root->left || !root->right) {
            Node* temp = root->left ? root->left : root->right;
            delete root;
            return temp;
        } else {
            Node* temp = getMinValueNode(root->right);
            root->key = temp->key;
            root->right = deleteNode(root->right, temp->key);
        }
    }

    if (!root)
        return root;

    // Update height
    updateHeight(root);

    // Get balance factor
    int balance = getBalanceFactor(root);

    // Balancing cases
    if (balance > 1 && getBalanceFactor(root->left) >= 0)
        return rightRotate(root); // Left Left case

    if (balance > 1 && getBalanceFactor(root->left) < 0) {
        root->left = leftRotate(root->left);
        return rightRotate(root); // Left Right case
    }

    if (balance < -1 && getBalanceFactor(root->right) <= 0)
        return leftRotate(root); // Right Right case

    if (balance < -1 && getBalanceFactor(root->right) > 0) {
        root->right = rightRotate(root->right);
        return leftRotate(root); // Right Left case
    }

    return root;
}

// Inorder traversal (prints in sorted order)
void inorder(Node* root) {
    if (root) {
        inorder(root->left);
        cout << root->key << " ";
        inorder(root->right);
    }
}

// Driver code
int main() {
    Node* root = nullptr;

    // Inserting values
    root = insert(root, 10);
    root = insert(root, 20);
    root = insert(root, 30);
    root = insert(root, 40);
    root = insert(root, 50);
    root = insert(root, 25);

    cout << "Inorder traversal of AVL Tree: ";
    inorder(root);
    cout << endl;

    // Deleting values
    root = deleteNode(root, 50);
    root = deleteNode(root, 40);

    cout << "Inorder traversal after deletion: ";
    inorder(root);
    cout << endl;

    return 0;
}

```

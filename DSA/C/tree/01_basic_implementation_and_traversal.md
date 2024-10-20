# Tree Implementation and Traversal: Inorder , PreOrder, PostOrder Traversal


![{7F296F87-7007-4CE8-9C29-026F7F988509}](https://github.com/user-attachments/assets/7d164452-f342-48d6-9902-9944e0d5eb0e)


```c
#include <stdio.h>
#include <stdlib.h>


typedef struct node {
    int item;
    struct node *left;
    struct node *right;
}Node;

Node *createNode(int item) {
    Node *newNode = (Node *)malloc(sizeof(Node));
    newNode->item = item;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

Node *insertLeft(Node *root, int item) {
    root->left = createNode(item);
    return root->left;
}

Node *insertRight(Node *root, int item) {
    root->right = createNode(item);
    return root->right;
}

void inOrderTraversal(Node *root) {
    if (root == NULL) return;
    inOrderTraversal(root->left);
    printf("%d => ", root->item);
    inOrderTraversal(root->right);
}

void preOrderTraversal(Node *root) {
    if (root == NULL) return;
    printf("%d => ", root->item);
    preOrderTraversal(root->left);
    preOrderTraversal(root->right);
}

void postOrderTraversal(Node *root) {
    if (root == NULL) return;
    postOrderTraversal(root->left);
    postOrderTraversal(root->right);
    printf("%d => ", root->item);
}



int main(void) {
    Node *root = createNode(1);

    Node *n2 = insertLeft(root, 2);
    Node *n3 = insertRight(root, 3);

    Node *n4 = insertLeft(n2, 4);
    Node *n5 = insertRight(n2, 5);

    Node *n6 = insertLeft(n3, 6);
    Node *n7 = insertRight(n3, 7);

    printf("\nInOrder Traversal : \n");
    inOrderTraversal(root);
    printf("\nPreOrder Traversal : \n");
    preOrderTraversal(root);
    printf("\nPostOrder Traversal : \n");
    postOrderTraversal(root);
    return 0;
}
```

[Path](https://www.youtube.com/shorts/Td-XOrU2id8)

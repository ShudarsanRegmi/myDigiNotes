#include <iostream>


typedef struct node Node;

using namespace std;

typedef struct node {
	int data;
	Node* left;
	Node* right;
} Node;


Node* createNode(int data) {
	Node* newNode = (Node*)malloc(sizeof(Node));
	newNode->data = data;
	newNode->left = NULL;
	newNode->right = NULL;
	return newNode;
}

void preOrder(Node* temp) {
	if (temp != NULL) {
		cout << temp->data << " -> ";
		preOrder(temp->left);
		preOrder(temp->right);
	}
}

void inOrder(Node* temp) {
	if (temp != NULL) {
		inOrder(temp->left);
		cout << temp->data << " -> ";
		inOrder(temp->right);
	}
}

void postOrder(Node* temp) {
	if (temp != NULL) {
		postOrder(temp->left);
		postOrder(temp->right);
		cout << temp->data << " -> ";
	}
}


int main() {
	
	Node* rootNode = createNode(0);
	
	Node* n1 = createNode(1);
	Node* n2 = createNode(2);
	Node* n3 = createNode(3);
	Node* n4 = createNode(4);
	Node* n5 = createNode(5);

	rootNode->left = n1;
	rootNode->right = n2;
	n1->left = n3;
	n1->right = n4;
	n3->left = n5;

	preOrder(rootNode);
	cout << endl;
	inOrder(rootNode);
	cout << endl;
	postOrder(rootNode);

	return 0;
}

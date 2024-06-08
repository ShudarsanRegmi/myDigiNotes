#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
	int val;
	struct Node *next;
} Node;



Node *createNode(int val) {
	Node *node = (Node *)malloc(sizeof(Node));
	node->val = val;
	// we'll link at insert function
	return node;
}

Node *insert(Node *node) {
		
}

Node *initialize() {
	Node *head = (Node *)malloc(sizeof(Node));
	head->val = 0;
	head->next = NULL;
	return head;
}

int main() {
	
	return 0;
}

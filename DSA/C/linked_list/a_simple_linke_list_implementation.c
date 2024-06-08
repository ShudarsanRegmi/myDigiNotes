#include <stdio.h>
#include <stdlib.h>


typedef struct node_s {
	int val;
	struct node_s *next;	
} Node;

int main() {
	
	Node *node1 = (Node *)malloc(sizeof(Node));
	Node *node2 = (Node *)malloc(sizeof(Node));
	Node *node3 = (Node *)malloc(sizeof(Node));
	node1->val = 1;
	node1->next = node2;

	node2->val = 2;
	node2->next = node3;

	node3->val = 3;
	node3->next = NULL;


	// simple traverseing
	//
	//
	Node *head = malloc(sizeof(Node));
	head = node1;
	Node tempNode = *head;
	printf("%d\n",tempNode.val);

	do {
		tempNode = *tempNode.next;
		printf("%d\n",tempNode.val);
	} while(tempNode.next != NULL);
	
	
	return 0;
}

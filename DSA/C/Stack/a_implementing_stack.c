#include <stdio.h>
#include <stdlib.h>

typedef struct Stack {
	int size;
	int top;
	int *ptr;
} Stack;


int isFull(Stack *stack) {
	if(stack->size-1 == stack->top)
		return 1;
	return 0;
}

int isEmpty(Stack *stack) {
	if (stack->top == -1)
		return 1;
	return 0;
}

int push(Stack *stack, int elem) {
	if(!isFull(stack)) {
		stack->ptr[stack->top +1] = elem;
		stack->top = stack->top+1;
	}
}

int pop(Stack *stack) {
	if(!isEmpty(stack)) {
		stack->ptr[stack->top] = 0;
		stack->top = stack->top-1;
		return 1;
	}
	return 0;
}
// returns the top element wiithout removing it
int peek(Stack *stack) {
	return stack->ptr[stack->top];
}



int main() {
	Stack *stack = (Stack *)malloc(sizeof(sizeof(Stack)));
	stack->size = 20;
	stack->top = -1;
	stack->ptr = (int *)malloc(sizeof(int)*20);
	
	push(stack,5);
	push(stack,6);
	printf("%d\n",peek(stack));
	pop(stack);
	printf("%d\n",peek(stack));

		
	return 0;
}

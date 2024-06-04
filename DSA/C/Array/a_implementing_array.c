#include <stdio.h>
#include <stdlib.h>


typedef struct suArray {
	int total_length;
	int length;
	int *ptr;
} suArray;

void createArray(suArray *arr, int total_length, int length) {
	arr->total_length = total_length;
	arr->length = length;
	arr->ptr = (int *)malloc(sizeof(int)*total_length);
}

void setValues(suArray *arr) {
	for (int i=0; i<arr->length; i++) {
		printf("\nEnter the value:");
		scanf("%d",(arr->ptr)+i);
	}
}

void displayValues(suArray *arr) {
	for (int i=0; i<arr->length; i++) {
		printf("\n%d",*((arr->ptr)+i));
	}
}

int get(suArray *arr, int index) {
	if (index >= arr->length && index<0) {
		perror("Array out of index");
		exit(0);
	}
	return *((arr->ptr)+index);
}

void set(suArray *arr, int index, int val) {
	// create empty room
	for (int i=arr->length-1;i>=index; i--) {
		arr[i+1] = arr[i];	
	}
	arr->ptr[index] = val; 
}

int push(suArray *arr, int val) {
	arr->ptr[arr->length] = val;
	arr->length= arr->length + 1;
	return val;
}

// Other easy to implement methods will be done in future

int main() {
	// creating the structure
	suArray arr;

	createArray(&arr, 20, 5);
	setValues(&arr);
	displayValues(&arr);
	
	printf("\nGetting index 2\n");
	printf("%d\n",get(&arr,2));

	printf("Setting 123 to index 2\n");
	set(&arr, 2, 123);

	printf("Getting index 2\n");
	printf("%d\n",get(&arr,2));

	printf("PUshing 444\n");
	push(&arr, 444);
	printf("%d\n",get(&arr,5));

	printf("Displaying array\n");
	displayValues(&arr);

	return 0;
}

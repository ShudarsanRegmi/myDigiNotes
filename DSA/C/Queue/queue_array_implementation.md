# Implementation of Queue Using Array in C

#### While Implementing, keep following things in mind
- Empty queue cannot be deQueued and full queue cannot be enQueued
- While enqueue check whether space is there or not
- While enqueue, front = -1 then front++ and reare++ always
- While queue, front++ and check front the condition when front>rear, in this case set both front and rear pointer to -1

```c
#include <stdio.h>

#define SIZE 5


void enQueue(int);
void deQueue();
void display();

int items[SIZE], front = -1, rear = -1;

void enQueue(int value) {
    // check if queue is full
    if (rear == SIZE-1) {
        printf("\nQueue is full\n");
    }else {
        // check if it is the first element
        if (front == -1) {
            front++;
        }
        rear++;
        items[rear] = value;
        printf("\nEnqueued element = %d", value);
    }

}

void deQueue() {
    // check if hte queue is empty
    if (front == -1) {
        printf("\nQueue is empty\n");
    }else {

        printf("Removed element = %d \n", items[front]);
        front++;

        if (front > rear) {
            front = rear = -1;
        }
    }
}


void display() {
    if (rear == -1) {
        printf("\nQueue is Empty!!");
    } else {
        for (int i=front; i <= rear; i++)
            printf("%d <= ", items[i]);
    }
    printf("\n");
}


int main() {
    enQueue(1);
    enQueue(2);
    enQueue(3);
    enQueue(4);
    enQueue(5);
    enQueue(6);


    display();

    deQueue();
    deQueue();
    deQueue();
    deQueue();
    deQueue();


    display();
}





```

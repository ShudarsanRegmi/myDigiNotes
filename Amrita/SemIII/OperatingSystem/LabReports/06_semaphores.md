<div align="center">

![Amrita Vishwa Vidyapeetham Logo](https://webfiles.amrita.edu/2024/04/WhQq1FiB-amrita-vishwa-vidyapeetham-university-logo-colored-version.svg)

# Amrita Vishwa Vidyapeetham
## Chennai Campus
337/1A, Vengal Village,  
Thiruvallur Taluk & District – 601 103,  
Tamil Nadu, India

---

### Subject: Operating System Lab

**Submitted By:** Shudarsan Regmi  
**Roll No.:** CH.SC.U4CYS23055


</div>

## Semaphores 

--

Description: 

Producer consumer problem is a synchronization problem. There is a fixed size buffer where the producer produces items and that is consumed by a consumer process. One solution to the producer- consumer problem uses shared memory. To allow producer and consumer processes to run concurrently, there must be available a buffer of items that can be filled by the producer and emptied by the consumer. This buffer will reside in a region of memory that is shared by the producer and consumer processes. The producer and consumer must be synchronized, so that the consumer does not try to consume an item that has not yet been produced.

## Program

```C
#include <stdio.h>
#include <stdlib.h>

int mutex = 1;
int full = 0;
int empty = 3;
int x = 0;

void producer();
void consumer();

int main() {
	int n;
	int wait(int);
	int signal(int);

	printf("1. Producer \n 2. Consumer \n 3. Exit");
	
	while (1) {
		printf("\nEnter your choice: ");
		scanf("%d",&n);

		switch(n) {
			case 1:
				if ((mutex == 1) && (empty != 0)) {
					producer();
				} else {
					printf("Buffer is full");
				}
				break;

			case 2:
				if ((mutex == 1) && (full != 0)) {
					consumer();
				}else {
					printf("Buffer is empty");
				}
			break;

			case 3:
			exit(0);		
		}
	}
	return 0;
}

int wait(int s) {
	return (--s);
}

int signal(int s) {
	return (++s);
}


void producer() {
	// This will decrease the mutex value to 0, indicating that the producer is producing at this time
	mutex = wait(mutex);
	full = signal(full);
	empty = wait(empty);
	x++;
	printf("Producer produces the item");
	mutex = signal(mutex);
	// This will release the mutex lock(i.e. mutex = 1), indicating that producer has stopped producing :q

}

void consumer() {
	// This will decrease the mutex value to 0, indicating that the consumer is consuming
	mutex = wait(mutex);
	full = wait(full);
	empty = signal(empty);
	printf("Consumer consumes the item %d", x);
	x--;
	mutex = signal(mutex);
	// This will increase the mutex back to 1 indicating that the consumer has stopped consuming
}

```

## Output
![image](https://github.com/user-attachments/assets/69f0e502-0c36-4f9a-a50c-0a5b90ae9432)




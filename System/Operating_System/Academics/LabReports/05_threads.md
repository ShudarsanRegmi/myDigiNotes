# System Calls to create threads in linux

### Prog-1: Illustrate the use of thread

```C
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

void *thread(void *vargp) {
	printf("This function is running in another thread using pthread...\n");
	return NULL;
}

int main() {
	pthread_t thread_id;
	printf("Before thread \n");
	pthread_create(&thread_id, NULL, thread, NULL);
	pthread_join(thread_id, NULL);
	printf("After thread");
	exit(0);
}
```

### Prog-02: Demonstration of Thread Creation, Detachment, and Equality Check in Pthreads

```C
#include <stdio.h>
#include <pthread.h>

// Function to be executed by the thread
void *func(void *arg) {
    // Detach the current thread, making it independent and allowing its resources
    // to be automatically reclaimed upon termination
    pthread_detach(pthread_self());
    printf("Inside the independent thread\n");

    // Exit the thread
    pthread_exit(NULL);
}

// Function to create and manage the thread
void fun() {
    pthread_t ptid;

    // Create a new thread that runs the 'func' function
    pthread_create(&ptid, NULL, &func, NULL);

    // This line may be printed before the thread terminates due to concurrent execution
    printf("This line may be printed before thread terminates\n");

    // Check if the newly created thread is the same as the calling thread
    if (pthread_equal(ptid, pthread_self())) {
        // This block will not be executed because 'ptid' refers to the newly created thread
        // and 'pthread_self()' refers to the calling thread (main thread)
        printf("Threads are equal\n");
    } else {
        // This line will be printed because the created thread and the calling thread are different
        printf("This line will be printed after thread ends\n");

        // Exit the calling thread (main thread) but continue to run other threads
        pthread_exit(NULL);
    }
}

int main() {
    // Call the function that creates and manages the thread
    fun();

    // Return 0 indicating successful completion of main function
    return 0;
}

```
### Input/Output
![image](https://github.com/user-attachments/assets/ed80f83e-cd7e-418b-b4f6-951d7e61512e)



### Input/Output
![image](https://github.com/user-attachments/assets/939dfe37-2450-4a2c-b0a8-7a89a026eb6d)

### Prog-02: Write a Program to add two numbers uisng pthread

```C
#include <stdio.h>
#include <pthread.h>

int global[2];

void *sum_thread(void *arg) {
	int *args_array;
	args_array = arg;
	int n1, n2, sum;
	n1 = args_array[0];
	n2 = args_array[1];

	sum=n1+n2;

	printf("N1 + N2 = %d \n", sum);

	return NULL;

}

int main() {

	printf("First Number: ");
	scanf("%d", &global[0]);

	printf("Second Number: ");
	scanf("%d", &global[1]);

	pthread_t tid_sum;
	pthread_create(&tid_sum, NULL, sum_thread, global);
	pthread_join(tid_sum, NULL);
	return 0;

}

```
## Input/Output:

![image](https://github.com/user-attachments/assets/1d51fe94-b6a6-4e7e-bb1a-8fc6704e6b15)

### Prog-03: Program to illustrate race conditions

>A race condition occurs when multiple threads or processes access and modify shared data concurrently, and the final outcome depends on the unpredictable timing of their execution. This can lead to inconsistent or unintended results because the operations are not synchronized. In the provided code, a race condition exists because `thread1` and `thread2` both read and update the shared variable `shared` without any synchronization mechanism, such as mutex locks, to control their access. This means that the threads can interleave in various ways, leading to different and inconsistent final values of `shared`.

```C
#include <stdio.h>
#include <unistd.h>
#include <pthread.h>

int shared=1;

void *func1() {
	int x;
	x = shared;
	printf("Threads 1 read the value of shared variable as %d \n", x);
	x--;
	printf("Local updation by Thread1: %d \n", x);
	sleep(1);
	shared = x;
	printf("Value of shared variable updated by Thread1 is: %d \n", shared);
}

void *func2() {
	int y;
	y=shared;
	printf("Thread2 reads the value as %d \n", y);
	y++;
	printf("Local updation by Thread2: %d \n", y);
	sleep(1);
	shared=y;
	printf("Value of shared variable updated by Thread2 is: %d\n", shared);
}

int main() {
	pthread_t thread1, thread2;
	pthread_create(&thread1, NULL, func1, NULL);	
	pthread_create(&thread2, NULL, func2, NULL);
	pthread_join(thread1, NULL);
	pthread_join(thread2, NULL);
	
	printf("Final value of shared variable is %d \n", shared);

}

```
## Input/Output
![image](https://github.com/user-attachments/assets/5e8f929f-fea2-4dad-a326-612f92258b88)

**When same Program was run another time, the vaue of shared variable is 0 now. This illustrates the race condition**

![image](https://github.com/user-attachments/assets/23b046f0-c89d-4d68-b122-d6c2755115e4)


# Producer Consumer Problem


**Using C - mutexe and counting semaphores**

```c
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>

#define BUFFER_SIZE 5

int buffer[BUFFER_SIZE];
int in = 0;
int out = 0;

sem_t empty;   // counts empty slots
sem_t full;    // counts filled slots
pthread_mutex_t mutex;  // protects critical section

void* producer(void* arg) {
    int item;
    while (1) {
        item = rand() % 100;

        sem_wait(&empty);          // wait if buffer is full
        pthread_mutex_lock(&mutex); // enter critical section

        buffer[in] = item;
        printf("Produced: %d at index %d\n", item, in);
        in = (in + 1) % BUFFER_SIZE;

        pthread_mutex_unlock(&mutex); // exit critical section
        sem_post(&full);              // increase filled slots

        sleep(1);
    }
}

void* consumer(void* arg) {
    int item;
    while (1) {
        sem_wait(&full);            // wait if buffer is empty
        pthread_mutex_lock(&mutex); // enter critical section

        item = buffer[out];
        printf("Consumed: %d from index %d\n", item, out);
        out = (out + 1) % BUFFER_SIZE;

        pthread_mutex_unlock(&mutex); // exit critical section
        sem_post(&empty);             // increase empty slots

        sleep(2);
    }
}

int main() {
    pthread_t prod_thread, cons_thread;

    sem_init(&empty, 0, BUFFER_SIZE); // initially all slots empty
    sem_init(&full, 0, 0);            // initially no items
    pthread_mutex_init(&mutex, NULL);

    pthread_create(&prod_thread, NULL, producer, NULL);
    pthread_create(&cons_thread, NULL, consumer, NULL);

    pthread_join(prod_thread, NULL);
    pthread_join(cons_thread, NULL);

    pthread_mutex_destroy(&mutex);
    sem_destroy(&empty);
    sem_destroy(&full);

    return 0;
}
```


**Using C++ : Condition Variables**

```cpp
#include <iostream>
#include <thread>
#include <mutex>
#include <condition_variable>
#include <cstdlib>
#include <ctime>

#define BUFFER_SIZE 5

int buffer[BUFFER_SIZE];
int in = 0, out = 0, count = 0;

std::mutex mutex;
std::condition_variable not_full;
std::condition_variable not_empty;

// Producer function
void producer() {
    while (true) {
        int item = rand() % 100; // produce an item

        std::unique_lock<std::mutex> lock(mutex);

        while (count == BUFFER_SIZE) // buffer full
            not_full.wait(lock);

        buffer[in] = item;
        std::cout << "Produced: " << item << " at " << in << std::endl;
        in = (in + 1) % BUFFER_SIZE;
        count++;

        not_empty.notify_one(); // signal buffer has item

        lock.unlock();

        std::this_thread::sleep_for(std::chrono::seconds(1)); // simulate production time
    }
}

// Consumer function
void consumer() {
    while (true) {
        std::unique_lock<std::mutex> lock(mutex);

        while (count == 0) // buffer empty
            not_empty.wait(lock);

        int item = buffer[out];
        std::cout << "Consumed: " << item << " at " << out << std::endl;
        out = (out + 1) % BUFFER_SIZE;
        count--;

        not_full.notify_one(); // signal buffer has space

        lock.unlock();

        std::this_thread::sleep_for(std::chrono::seconds(1)); // simulate consumption time
    }
}

int main() {
    std::srand(std::time(0));
    std::thread prod(producer);
    std::thread cons(consumer);

    prod.join();
    cons.join();

    return 0;
}

```

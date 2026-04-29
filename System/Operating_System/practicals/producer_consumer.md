# Producer Consumer Problem

## Problem Without Synchronization
```cpp
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>

#define BUFFER_SIZE 5

int buffer[BUFFER_SIZE];
int in = 0;
int out = 0;
int count = 0; // number of items in buffer (no protection!)

void* producer(void* arg) {
    int item;
    while (1) {
        item = rand() % 100;

        if (count == BUFFER_SIZE) {
            printf("[Producer] Thinks buffer is full, skipping...\n");
            usleep(100000);
            continue;
        }

        // CRITICAL SECTION (no protection!)
        buffer[in] = item;
        printf("[Producer] Produced %d at %d\n", item, in);

        in = (in + 1) % BUFFER_SIZE;
        count++;  // race condition here

        usleep(rand() % 200000);
    }
}

void* consumer(void* arg) {
    int item;
    while (1) {
        if (count == 0) {
            printf("[Consumer] Thinks buffer is empty, skipping...\n");
            usleep(150000);
            continue;
        }

        // CRITICAL SECTION (no protection!)
        item = buffer[out];
        printf("[Consumer] Consumed %d from %d\n", item, out);

        out = (out + 1) % BUFFER_SIZE;
        count--;  // race condition here

        usleep(rand() % 250000);
    }
}

int main() {
    pthread_t p1, p2, c1, c2;

    pthread_create(&p1, NULL, producer, NULL);
    pthread_create(&p2, NULL, producer, NULL);
    pthread_create(&c1, NULL, consumer, NULL);
    pthread_create(&c2, NULL, consumer, NULL);

    pthread_join(p1, NULL);
    pthread_join(p2, NULL);
    pthread_join(c1, NULL);
    pthread_join(c2, NULL);

    return 0;
}
```

<img width="581" height="527" alt="image" src="https://github.com/user-attachments/assets/8efcdd65-1658-4e1f-8e2b-9911a723ce41" />


## Using C - mutexes and counting semaphores

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

## Output

<img width="791" height="500" alt="image" src="https://github.com/user-attachments/assets/0a777305-9668-49fc-99ca-76042b8bc826" />


## More Verbose Version of Above

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

sem_t empty;
sem_t full;
pthread_mutex_t mutex;

void* producer(void* arg) {
    int item;
    while (1) {
        item = rand() % 100;

        // Try non-blocking first
        if (sem_trywait(&empty) != 0) {
            printf("[Producer] Buffer full → waiting...\n");
            sem_wait(&empty);  // now block
        } else {
            printf("[Producer] Found empty slot → proceeding\n");
        }

        pthread_mutex_lock(&mutex);
        printf("[Producer] Entered critical section\n");

        buffer[in] = item;
        printf("[Producer] Produced %d at index %d\n", item, in);
        in = (in + 1) % BUFFER_SIZE;

        printf("[Producer] Leaving critical section\n");
        pthread_mutex_unlock(&mutex);

        sem_post(&full);
        printf("[Producer] Signaled full (item available)\n\n");

        sleep(1);
    }
}

void* consumer(void* arg) {
    int item;
    while (1) {

        if (sem_trywait(&full) != 0) {
            printf("[Consumer] Buffer empty → waiting...\n");
            sem_wait(&full);
        } else {
            printf("[Consumer] Found item → proceeding\n");
        }

        pthread_mutex_lock(&mutex);
        printf("[Consumer] Entered critical section\n");

        item = buffer[out];
        printf("[Consumer] Consumed %d from index %d\n", item, out);
        out = (out + 1) % BUFFER_SIZE;

        printf("[Consumer] Leaving critical section\n");
        pthread_mutex_unlock(&mutex);

        sem_post(&empty);
        printf("[Consumer] Signaled empty (slot free)\n\n");

        sleep(2);
    }
}

int main() {
    pthread_t prod_thread, cons_thread;

    sem_init(&empty, 0, BUFFER_SIZE);
    sem_init(&full, 0, 0);
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

<img width="800" height="635" alt="image" src="https://github.com/user-attachments/assets/59ccca29-cb97-452b-9c36-4d4fd7242b6f" />

```
(base) aparichit@SUSHANKYA:~/rough/os$ ./out
[Producer] Found empty slot → proceeding
[Producer] Entered critical section
[Consumer] Buffer empty → waiting...
[Producer] Produced 83 at index 0
[Producer] Leaving critical section
[Producer] Signaled full (item available)

[Consumer] Entered critical section
[Consumer] Consumed 83 from index 0
[Consumer] Leaving critical section
[Consumer] Signaled empty (slot free)

[Producer] Found empty slot → proceeding
[Producer] Entered critical section
[Producer] Produced 86 at index 1
[Producer] Leaving critical section
[Producer] Signaled full (item available)

[Consumer] Found item → proceeding
[Consumer] Entered critical section
[Consumer] Consumed 86 from index 1
[Consumer] Leaving critical section
[Consumer] Signaled empty (slot free)

[Producer] Found empty slot → proceeding
[Producer] Entered critical section
[Producer] Produced 77 at index 2
[Producer] Leaving critical section
[Producer] Signaled full (item available)

[Producer] Found empty slot → proceeding
[Producer] Entered critical section
[Producer] Produced 15 at index 3
[Producer] Leaving critical section
[Producer] Signaled full (item available)

[Consumer] Found item → proceeding
[Consumer] Entered critical section
[Consumer] Consumed 77 from index 2
[Consumer] Leaving critical section
[Consumer] Signaled empty (slot free)

[Producer] Found empty slot → proceeding
[Producer] Entered critical section
[Producer] Produced 93 at index 4
[Producer] Leaving critical section
[Producer] Signaled full (item available)

[Producer] Found empty slot → proceeding
[Producer] Entered critical section
[Producer] Produced 35 at index 0
[Producer] Leaving critical section
[Producer] Signaled full (item available)

[Consumer] Found item → proceeding
[Consumer] Entered critical section
[Consumer] Consumed 15 from index 3
[Consumer] Leaving critical section
[Consumer] Signaled empty (slot free)

[Producer] Found empty slot → proceeding
[Producer] Entered critical section
[Producer] Produced 86 at index 1
[Producer] Leaving critical section
[Producer] Signaled full (item available)

[Producer] Found empty slot → proceeding
[Producer] Entered critical section
[Producer] Produced 92 at index 2
[Producer] Leaving critical section
[Producer] Signaled full (item available)


```
## Multiple Producers and Multiple Consumers

```c
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>

#define BUFFER_SIZE 5
#define PRODUCERS 3
#define CONSUMERS 3

int buffer[BUFFER_SIZE];
int in = 0, out = 0;

sem_t empty, full;
pthread_mutex_t mutex;

void* producer(void* arg) {
    int id = *(int*)arg;
    int item;

    while (1) {
        item = rand() % 100;

        sem_wait(&empty);
        pthread_mutex_lock(&mutex);

        buffer[in] = item;
        printf("[Producer %d] Produced %d at index %d\n", id, item, in);
        in = (in + 1) % BUFFER_SIZE;

        pthread_mutex_unlock(&mutex);
        sem_post(&full);

        usleep(rand() % 300000);
    }
}

void* consumer(void* arg) {
    int id = *(int*)arg;
    int item;

    while (1) {
        sem_wait(&full);
        pthread_mutex_lock(&mutex);

        item = buffer[out];
        printf("[Consumer %d] Consumed %d from index %d\n", id, item, out);
        out = (out + 1) % BUFFER_SIZE;

        pthread_mutex_unlock(&mutex);
        sem_post(&empty);

        usleep(rand() % 400000);
    }
}

int main() {
    pthread_t prod[PRODUCERS], cons[CONSUMERS];
    int p_ids[PRODUCERS], c_ids[CONSUMERS];

    sem_init(&empty, 0, BUFFER_SIZE);
    sem_init(&full, 0, 0);
    pthread_mutex_init(&mutex, NULL);

    for (int i = 0; i < PRODUCERS; i++) {
        p_ids[i] = i + 1;
        pthread_create(&prod[i], NULL, producer, &p_ids[i]);
    }

    for (int i = 0; i < CONSUMERS; i++) {
        c_ids[i] = i + 1;
        pthread_create(&cons[i], NULL, consumer, &c_ids[i]);
    }

    for (int i = 0; i < PRODUCERS; i++)
        pthread_join(prod[i], NULL);

    for (int i = 0; i < CONSUMERS; i++)
        pthread_join(cons[i], NULL);

    pthread_mutex_destroy(&mutex);
    sem_destroy(&empty);
    sem_destroy(&full);

    return 0;
}
```
**Output**

<img width="551" height="514" alt="image" src="https://github.com/user-attachments/assets/66bf7258-efe4-4c1a-b0d5-6a5d264edf49" />

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

```C

#include <pthread.h>
#include <stdio.h>

int counter = 0;            // Shared resource
pthread_mutex_t lock;       // Mutex

void *increment_counter(void *arg) {
    pthread_mutex_lock(&lock);  // Lock the mutex before modifying the shared resource
    counter++;
    printf("Counter: %d\n", counter);
    pthread_mutex_unlock(&lock);  // Unlock the mutex after modification
    pthread_exit(NULL);
}

int main() {
    pthread_t threads[3];

    // Initialize the mutex
    pthread_mutex_init(&lock, NULL);
    
    // Create threads
    for (int i = 0; i < 3; i++) {
        pthread_create(&threads[i], NULL, increment_counter, NULL);
    }

    // Wait for threads to finish
    for (int i = 0; i < 3; i++) {
        pthread_join(threads[i], NULL);
    }

    // Destroy the mutex
    pthread_mutex_destroy(&lock);
    
    return 0;
}

```

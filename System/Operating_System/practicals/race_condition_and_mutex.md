
## Race Condition

```c
#include <stdio.h>
#include <pthread.h>

int counter = 0;   // Shared variable

void* increment(void* arg) {
    for (int i = 0; i < 1000000; i++) {
        counter++;          // Not atomic!
    }
    return NULL;
}

int main() {
    pthread_t t1, t2;

    pthread_create(&t1, NULL, increment, NULL);
    pthread_create(&t2, NULL, increment, NULL);

    pthread_join(t1, NULL);
    pthread_join(t2, NULL);

    printf("Counter = %d\n", counter);

    return 0;
}
```
## Output

<img width="610" height="354" alt="image" src="https://github.com/user-attachments/assets/3d663c45-b18d-46eb-8d1e-93231771077e" />

<img width="613" height="378" alt="image" src="https://github.com/user-attachments/assets/3be6fcbb-737f-4d12-9401-030dbe6a0228" />


## Race Condition Solution With mutex

```c
#include <stdio.h>
#include <pthread.h>

int counter = 0;
pthread_mutex_t lock = PTHREAD_MUTEX_INITIALIZER;

void* increment(void* arg) {
    for (int i = 0; i < 1000000; i++) {
        pthread_mutex_lock(&lock);

        counter++;

        pthread_mutex_unlock(&lock);
    }
    return NULL;
}

int main() {
    pthread_t t1, t2;

    pthread_create(&t1, NULL, increment, NULL);
    pthread_create(&t2, NULL, increment, NULL);

    pthread_join(t1, NULL);
    pthread_join(t2, NULL);

    printf("Counter = %d\n", counter);

    pthread_mutex_destroy(&lock);
    return 0;
}
```


## Output

<img width="702" height="244" alt="image" src="https://github.com/user-attachments/assets/9071117f-93e3-4952-bfaf-a88474cb5bf7" />





The **Dining Philosophers Problem** is a classic synchronization problem that illustrates the challenges of allocating shared resources among multiple processes or threads. It involves a group of philosophers who are sitting around a table, and each philosopher needs two utensils (forks) to eat. The challenge is to design a protocol that ensures no deadlock and no starvation while allowing all philosophers to eat.

### **Problem Description**

1. **Philosophers**: Each philosopher thinks and occasionally needs to eat.
2. **Forks**: Each philosopher needs two forks to eat, one on their left and one on their right.
3. **Resource Sharing**: Forks are shared between adjacent philosophers.

### **Challenges**

- **Deadlock**: A situation where all philosophers hold one fork and wait for the other fork, causing none of them to eat.
- **Starvation**: A situation where a philosopher might never get both forks to eat if the forks are continuously taken by others.

### **Solution Using Semaphores**

Semaphores can be used to manage access to the shared forks and ensure that philosophers can eat without causing deadlock or starvation. Here’s how to solve the problem using semaphores:

#### **1. Semaphore Initialization**

- Use a semaphore for each fork to manage access.
- Use additional semaphores to manage mutual exclusion for picking up and putting down forks.

#### **2. Pseudocode Solution**

```c
#include <semaphore.h>
#include <pthread.h>
#include <stdio.h>

#define NUM_PHILOSOPHERS 5

sem_t forks[NUM_PHILOSOPHERS];  // Semaphores for each fork
sem_t mutex;  // Mutex for controlling access to forks

void* philosopher(void* id) {
    int philosopher_id = (int)id;

    while (true) {
        // Thinking
        printf("Philosopher %d is thinking\n", philosopher_id);

        // Trying to pick up forks
        sem_wait(&mutex);  // Enter critical section

        sem_wait(&forks[philosopher_id]);         // Pick up left fork
        sem_wait(&forks[(philosopher_id + 1) % NUM_PHILOSOPHERS]); // Pick up right fork

        sem_post(&mutex);  // Leave critical section

        // Eating
        printf("Philosopher %d is eating\n", philosopher_id);

        // Putting down forks
        sem_post(&forks[philosopher_id]);         // Put down left fork
        sem_post(&forks[(philosopher_id + 1) % NUM_PHILOSOPHERS]); // Put down right fork

        // Resting
    }

    return NULL;
}

int main() {
    pthread_t threads[NUM_PHILOSOPHERS];
    int ids[NUM_PHILOSOPHERS];

    // Initialize semaphores
    sem_init(&mutex, 0, 1);  // Binary semaphore for mutual exclusion
    for (int i = 0; i < NUM_PHILOSOPHERS; i++) {
        sem_init(&forks[i], 0, 1);  // Binary semaphores for each fork
        ids[i] = i;
    }

    // Create philosopher threads
    for (int i = 0; i < NUM_PHILOSOPHERS; i++) {
        pthread_create(&threads[i], NULL, philosopher, (void*)ids[i]);
    }

    // Wait for philosopher threads to finish (they won't in this infinite loop example)
    for (int i = 0; i < NUM_PHILOSOPHERS; i++) {
        pthread_join(threads[i], NULL);
    }

    // Cleanup semaphores
    for (int i = 0; i < NUM_PHILOSOPHERS; i++) {
        sem_destroy(&forks[i]);
    }
    sem_destroy(&mutex);

    return 0;
}
```

### **Explanation**

1. **Initialization**:
   - Each fork is initialized with a semaphore value of 1 (indicating it is available).
   - A mutex semaphore is initialized to control access to the forks array and prevent race conditions.

2. **Philosopher Function**:
   - **Thinking**: The philosopher thinks (no semaphore operation needed here).
   - **Pick Up Forks**:
     - The philosopher first acquires the mutex to enter the critical section.
     - Then, the philosopher picks up the left and right forks using `sem_wait` operations.
     - The mutex is released after picking up the forks.
   - **Eating**: The philosopher eats (with both forks held).
   - **Put Down Forks**:
     - The philosopher releases the forks using `sem_post`.
     - The mutex is used to control access while putting down the forks.

3. **Deadlock Prevention**:
   - By using a mutex to protect the fork acquisition and release, we prevent the situation where all philosophers hold one fork and wait indefinitely for the other.

4. **Starvation Prevention**:
   - Although the above solution prevents deadlock, it doesn't inherently prevent starvation. To address starvation, additional mechanisms (e.g., an "ordering" of fork acquisition or an algorithm ensuring that no philosopher is perpetually blocked) might be needed.

This solution is a basic example and demonstrates the use of semaphores to manage concurrent access to shared resources, ensuring that the philosophers can alternate between thinking and eating without causing deadlock.


--- 

### Problem Illustration in Simple

![image](https://github.com/user-attachments/assets/96118e9f-8ce9-4f2b-a34b-c5bdf150a0c9)


# Simple C like Pseudo Code
Certainly! Here’s a C-like pseudo code for solving the Dining Philosophers Problem using semaphores. This version is concise and focuses on core concepts:

### **Initialization**

```c
int num_philosophers = 5;
semaphore forks[num_philosophers];  // Forks (semaphores)
semaphore mutex;  // Mutex for critical section

// Initialize semaphores
for (int i = 0; i < num_philosophers; i++) {
    forks[i] = 1;  // Each fork is available
}
mutex = 1;  // Mutex for mutual exclusion
```

### **Philosopher Function**

```c
void philosopher(int id) {
    while (true) {
        // Think
        // ...

        // Pick up forks
        wait(mutex);  // Enter critical section
        wait(forks[id]);           // Pick up left fork
        wait(forks[(id + 1) % num_philosophers]);  // Pick up right fork
        signal(mutex);  // Exit critical section

        // Eat
        // ...

        // Put down forks
        signal(forks[id]);           // Put down left fork
        signal(forks[(id + 1) % num_philosophers]);  // Put down right fork
    }
}
```

### **Main Function**

```c
int main() {
    for (int i = 0; i < num_philosophers; i++) {
        create_thread(philosopher, i);  // Create philosopher thread
    }

    // Wait for threads to complete (in practice, they run indefinitely)
    wait_for_threads();  
    return 0;
}
```

### **Function Definitions**

```c
void wait(semaphore s) {
    // Decrement semaphore value
    // If value < 0, block until semaphore is available
}

void signal(semaphore s) {
    // Increment semaphore value
    // Wake up a blocked thread if any
}

void create_thread(void (*func)(int), int arg) {
    // Create a new thread and run func(arg)
}

void wait_for_threads() {
    // Wait for all threads to complete (if needed)
}
```

### **Explanation**

- **Initialization**:
  - `forks[]`: Semaphores for each fork, initialized to 1 (available).
  - `mutex`: Semaphore for mutual exclusion, initialized to 1.

- **Philosopher Function**:
  - **Think**: Philosophers think without synchronization.
  - **Pick Up Forks**: Use `wait(mutex)` to enter the critical section. Use `wait(forks[id])` and `wait(forks[(id + 1) % num_philosophers])` to pick up the forks.
  - **Eat**: Philosophers eat while holding both forks.
  - **Put Down Forks**: Use `signal(forks[id])` and `signal(forks[(id + 1) % num_philosophers])` to put down the forks.

- **Main Function**:
  - Creates threads for each philosopher and starts them.

This C-like pseudo code provides a clear structure for solving the Dining Philosophers Problem using semaphores to manage concurrent access to shared resources.



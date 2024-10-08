

# A Simple Program to Visualize Recursion Depths 

```c
#include <stdio.h>

// Recursive function to count down from a number
void countdown(int n, int depth) {
    // Print the current recursion depth and value of n
    printf("[Depth %d] Current n = %d\n", depth, n);

    // Base case: Stop recursion when n reaches 0
    if (n == 0) {
        printf("[Depth %d] Base case reached: n = %d\n", depth, n);
        return;
    }

    // Recursive case: Call countdown with n-1, increasing depth
    countdown(n - 1, depth + 1);

    // Print when returning from recursion (unwinding)
    printf("[Depth %d] Returning from recursion, n = %d\n", depth, n);
}

int main() {
    int start = 5; // Start countdown from 5
    printf("Starting countdown from %d...\n", start);

    // Start the recursion with depth 0
    countdown(start, 0);

    return 0;
}


```

**Big Doubt in above program:**

![image](https://github.com/user-attachments/assets/c9a5fe4e-22a7-4a0a-a701-69d79c40f77d)


>Why the last stack frame is not getting destoroyed immediately, when the function hits the return statement. Why still in depth 5? why the depth = 5 statemnt gets printed?
>Note: for now, I'm leaving, but I still have nuances left in these concepts

# Recursion Concepts More In-depths insights


```c
#include <stdio.h>

// Recursive function to compute factorial with detailed tracking of recursion concepts
int factorial(int n, int depth) {
    // Print current depth and value of n
    printf("[Depth %d] Entering factorial with n = %d\n", depth, n);

    // Base case: If n is 0 or 1, return 1 (Factorial of 0 or 1 is 1)
    if (n <= 1) {
        printf("[Depth %d] Base case reached: factorial(%d) = 1\n", depth, n);
        printf("[Depth %d] Exiting factorial with n = %d (Returning 1)\n", depth, n);
        return 1;
    }

    // Recursive case: factorial(n) = n * factorial(n-1)
    printf("[Depth %d] Recursing with n = %d -> factorial(%d - 1)\n", depth, n, n);
    int result = n * factorial(n - 1, depth + 1); // Recursive call, increasing depth

    // Print the return of the recursive call and the result of current computation
    printf("[Depth %d] Returning from factorial(%d - 1) -> %d\n", depth, n, result);
    printf("[Depth %d] Exiting factorial with n = %d (Returning %d)\n", depth, n, result);

    return result;
}

// Main function to initiate the recursive function and track the recursion process
int main() {
    int num = 5;

    // Start the recursion with an initial depth of 0
    printf("Calculating factorial of %d with recursion...\n", num);
    int result = factorial(num, 0);

    // Print the final result
    printf("\nFactorial of %d is: %d\n", num, result);
    return 0;
}

```


## Sum of Numbers Recursion Examples

```c
#include <stdio.h>

// Recursive function to calculate the sum of numbers from n to 1
int sumUpTo(int n, int depth) {
    // Print the current recursion depth and value of n
    printf("[Depth %d] Entering sumUpTo with n = %d\n", depth, n);

    // Base case: If n is 0, return 0
    if (n == 0) {
        printf("[Depth %d] Base case reached: n = %d, returning 0\n", depth, n);
        return 0;
    }

    // Recursive case: n + sum of (n-1), increase depth
    int sum = n + sumUpTo(n - 1, depth + 1);

    // Print the value of sum as recursion unwinds
    printf("[Depth %d] Returning sum = %d for n = %d\n", depth, sum, n);

    return sum;
}

int main() {
    int num = 5;
    printf("Calculating sum of numbers from %d to 1...\n", num);

    // Start the recursion with depth 0
    int result = sumUpTo(num, 0);

    // Print the final result
    printf("\nSum of numbers from %d to 1 is: %d\n", num, result);
    return 0;
}

```

## Some Other Helpful Materials

- [Visualizing Recursion](https://medium.com/swlh/visualizing-recursion-6a81d50d6c41)
- []()

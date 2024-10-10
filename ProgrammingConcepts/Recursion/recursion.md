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

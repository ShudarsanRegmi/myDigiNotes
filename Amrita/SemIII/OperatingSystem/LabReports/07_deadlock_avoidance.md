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

## Deadlock Avoidance Algorithm

```c
#include <stdio.h>

int main() {
    int n = 5, m = 3, i, j, k;
    
    // Allocation matrix
    int alloc[5][3] = {
        {0, 1, 0},
        {2, 0, 0},
        {3, 0, 2},
        {2, 1, 1},
        {0, 0, 2}
    };

    // Maximum matrix
    int max[5][3] = {
        {7, 5, 3},
        {3, 2, 2},
        {9, 0, 2},
        {2, 2, 2},
        {4, 3, 3}
    };

    // Available resources
    int avail[3] = {3, 3, 2};
    
    int f[n], ans[n], ind = 0;
    
    // Initialize finished processes array
    for (k = 0; k < n; k++) {
        f[k] = 0;
    }
    
    // Calculate need matrix
    int need[n][m];
    for (i = 0; i < n; i++) {
        for (j = 0; j < m; j++) {
            need[i][j] = max[i][j] - alloc[i][j];
        }
    }
    
    int y = 0;
    
    // Find the safe sequence
    for (k = 0; k < n; k++) {
        int progressMade = 0;
        for (i = 0; i < n; i++) {
            if (f[i] == 0) {
                int flag = 0;
                for (j = 0; j < m; j++) {
                    if (need[i][j] > avail[j]) {
                        flag = 1;
                        break;
                    }
                }
                if (flag == 0) {
                    ans[ind++] = i;
                    for (y = 0; y < m; y++) {
                        avail[y] += alloc[i][y];
                    }
                    f[i] = 1;
                    progressMade = 1;
                }
            }
        }
        // If no progress was made in this iteration, the system is not safe
        if (!progressMade) {
            printf("The following system is not safe\n");
            return 0;
        }
    }
    
    // Print the safe sequence
    printf("Following is the SAFE Sequence:\n");
    for (i = 0; i < n - 1; i++) {
        printf("P%d -> ", ans[i]);
    }
    printf("P%d\n", ans[n - 1]);
    
    return 0;
}

```

### commented code

```C
#include <stdio.h>

int main() {
    // n = number of processes, m = number of resource types
    int n = 5, m = 3, i, j, k;
    
    // Allocation matrix: How much each process has currently allocated of each resource type
    int alloc[5][3] = {
        {0, 1, 0}, // P0
        {2, 0, 0}, // P1
        {3, 0, 2}, // P2
        {2, 1, 1}, // P3
        {0, 0, 2}  // P4
    };

    // Maximum matrix: The maximum demand of each process for each resource type
    int max[5][3] = {
        {7, 5, 3}, // P0
        {3, 2, 2}, // P1
        {9, 0, 2}, // P2
        {2, 2, 2}, // P3
        {4, 3, 3}  // P4
    };

    // Available resources: Initially available instances of each resource type
    int avail[3] = {3, 3, 2}; // Resources R1, R2, R3
    
    // f[] keeps track of finished processes (0 = unfinished, 1 = finished)
    int f[n], ans[n], ind = 0; // 'ans[]' will store the safe sequence, 'ind' tracks index
    
    // Initialize finished processes array to 0 (no process has finished initially)
    for (k = 0; k < n; k++) {
        f[k] = 0;
    }
    
    // Calculate the need matrix:
    // Need[i][j] = max[i][j] - alloc[i][j], which shows the remaining resource requirement for each process
    int need[n][m];
    for (i = 0; i < n; i++) {
        for (j = 0; j < m; j++) {
            need[i][j] = max[i][j] - alloc[i][j];
        }
    }
    
    int y = 0; // Used for updating available resources after a process finishes
    
    // Iterate through processes to find the safe sequence
    for (k = 0; k < n; k++) {
        int progressMade = 0; // This will track if we make any progress in this iteration
        
        // Loop through each process to check if it can be executed (i.e., finished)
        for (i = 0; i < n; i++) {
            if (f[i] == 0) { // If process 'i' is not finished yet
                int flag = 0; // Flag to check if the process can be safely executed
                
                // Check if the need of this process can be satisfied with the available resources
                for (j = 0; j < m; j++) {
                    if (need[i][j] > avail[j]) { // If any needed resource is greater than what's available
                        flag = 1; // Set flag indicating this process can't be executed yet
                        break;    // Exit this loop as we can't satisfy this process
                    }
                }
                
                // If the process can be safely executed (flag == 0)
                if (flag == 0) {
                    ans[ind++] = i; // Add this process to the safe sequence
                    for (y = 0; y < m; y++) {
                        avail[y] += alloc[i][y]; // Release resources after finishing this process
                    }
                    f[i] = 1;   // Mark this process as finished
                    progressMade = 1; // Record that we made progress in this iteration
                }
            }
        }
        
        // If no progress was made, then a deadlock could occur, and the system is not safe
        if (!progressMade) {
            printf("The following system is not safe\n");
            return 0; // Exit the program, indicating the system is in an unsafe state
        }
    }
    
    // If we reach this point, the system is safe, and we can print the safe sequence
    printf("Following is the SAFE Sequence:\n");
    for (i = 0; i < n - 1; i++) {
        printf("P%d -> ", ans[i]); // Print each process in the safe sequence
    }
    printf("P%d\n", ans[n - 1]); // Print the last process in the safe sequence
    
    return 0;
}

```

### Output
```
sudoerson@Aparichit:~/oslab$ gcc -o out deadlock.c
sudoerson@Aparichit:~/oslab$ ./out
The following system is not safe
```

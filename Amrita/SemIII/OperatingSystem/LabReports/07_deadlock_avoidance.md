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


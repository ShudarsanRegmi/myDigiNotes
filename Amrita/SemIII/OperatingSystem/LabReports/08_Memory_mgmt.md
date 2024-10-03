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

---

# Memory Management

>Write an algorithm to execute first fit algorithm

```c
#include <stdio.h>

void main() {
    int bsize[10], psize[10], bno, pno, flags[10], allocation[10], i, j; 
    for(i = 0; i < 10; i++) {
        flags[i] = 0;
        allocation[i] = -1;
    }
    printf("\n\t\t\tMemory Management - First Fit\n"); 
    printf("Enter no. of blocks: ");
    scanf("%d", &bno);
    printf("\nEnter size of each block: "); 
    for(i = 0; i < bno; i++)
        scanf("%d", &bsize[i]); 

    printf("\nEnter no. of processes: ");
    scanf("%d", &pno);
    printf("\nEnter size of each process: "); 
    for(i = 0; i < pno; i++)
        scanf("%d", &psize[i]); 

    for(i = 0; i < pno; i++) 
        for(j = 0; j < bno; j++)
            if(flags[j] == 0 && bsize[j] >= psize[i]) {
                allocation[j] = i; 
                flags[j] = 1; 
                break;
            }
    
    printf("\nBlock no.\tsize\t\tprocess no.\t\tsize"); 
    for(i = 0; i < bno; i++) {
        printf("\n%d\t\t%d\t\t", i + 1, bsize[i]); 
        if(flags[i] == 1)
            printf("%d\t\t\t%d", allocation[i] + 1, psize[allocation[i]]);
        else
            printf("Not allocated");
    }
}

```

### Output
```
sudoerson@Aparichit:~/oslab$ gcc -o out mem_mgmt.c
sudoerson@Aparichit:~/oslab$ ./out

                        Memory Management - First Fit
Enter no. of blocks: 3

Enter size of each block: 20 10 30

Enter no. of processes: 3

Enter size of each process: 9 15 19

Block no.       size            process no.             size
1               20              1                       9
2               10              Not allocated
3               30              2                       15
```

>Write an algorithm to execute the best fit algorithm

```c
#include <stdio.h>

void main() {
    int fragment[20], b[20], p[20], i, j, nb, np, temp, lowest = 9999; 
    static int barray[20], parray[20];
    
    printf("\n\t\t\t Memory Management - Best Fit\n"); 
    printf("\nEnter the number of blocks:"); 
    scanf("%d", &nb);
    printf("Enter the number of processes:"); 
    scanf("%d", &np);
    
    printf("\nEnter the size of the blocks:-\n"); 
    for(i = 1; i <= nb; i++) {
        printf("Block no.%d:", i);
        scanf("%d", &b[i]);
    }
    
    printf("\nEnter the size of the processes :-\n"); 
    for(i = 1; i <= np; i++) {
        printf("Process no.%d:", i);
        scanf("%d", &p[i]);
    }
    
    for(i = 1; i <= np; i++) {
        lowest = 9999;  // Reset lowest for each process
        for(j = 1; j <= nb; j++) {
            if(barray[j] != 1) {
                temp = b[j] - p[i]; 
                if(temp >= 0 && lowest > temp) {
                    parray[i] = j; 
                    lowest = temp;
                }
            }
        }
        fragment[i] = lowest; 
        barray[parray[i]] = 1; 
    }

    printf("\nProcess_no\tProcess_size\tBlock_no\tBlock_size\tFragment"); 
    for(i = 1; i <= np && parray[i] != 0; i++) {
        printf("\n%d\t\t%d\t\t%d\t\t%d\t\t%d", i, p[i], parray[i], b[parray[i]], fragment[i]);
    }
}
```

### Output
```c
                         Memory Management - Best Fit

Enter the number of blocks:3
Enter the number of processes:3

Enter the size of the blocks:-
Block no.1:200
Block no.2:100
Block no.3:250

Enter the size of the processes :-
Process no.1:89
Process no.2:199
Process no.3:201

Process_no      Process_size    Block_no        Block_size      Fragment
1               89              2               100             11
2               199             1               200             1
3               201             3               250             49
```

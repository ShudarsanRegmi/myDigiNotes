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

# Paging Memory Management

>To write a program to simulate paging technique of memory management

### Paging Technique for Memory Management

```c
#include <stdio.h>
#define MAX 50

int main() {
    int page[MAX], i, n, f, ps, off, pno; 
    int choice = 0;

    printf("\nEnter the number of pages in memory: "); 
    scanf("%d", &n);
    printf("\nEnter page size: "); 
    scanf("%d", &ps); 
    printf("\nEnter number of frames: "); 
    scanf("%d", &f); 

    for (i = 0; i < n; i++)
        page[i] = -1;

    printf("\nEnter the page table\n");
    printf("(Enter frame number as -1 if that page is not present in any frame)\n\n"); 
    printf("\npageno\tframeno\n-------\t ");
    
    for (i = 0; i < n; i++) { 
        printf("\n\n%d\t\t", i); 
        scanf("%d", &page[i]);
    }

    do {
        printf("\n\nEnter the logical address (i.e., page number & offset): "); 
        scanf("%d%d", &pno, &off);

        if (page[pno] == -1) {
            printf("\n\nThe required page is not available in any of the frames."); 
        } else {
            printf("\n\nPhysical address (i.e., frame number & offset): %d, %d", page[pno], off); 
        }

        printf("\nDo you want to continue (1/0)?: ");
        scanf("%d", &choice);
    } while (choice == 1); 

    return 0;
}

```

### Output

```
Enter the number of pages in memory: 4

Enter page size: 2

Enter number of frames: 4

Enter the page table
(Enter frame number as -1 if that page is not present in any frame)


pageno  frameno
-------

0               3


1               4


2               1


3               2


Enter the logical address (i.e., page number & offset): 0 4


Physical address (i.e., frame number & offset): 3, 4
Do you want to continue (1/0)?: 0
```


<div align="center">

![Amrita Vishwa Vidyapeetham Logo](https://webfiles.amrita.edu/2024/04/WhQq1FiB-amrita-vishwa-vidyapeetham-university-logo-colored-version.svg)

# Amrita Vishwa Vidyapeetham
## Chennai Campus
337/1A, Vengal Village,  
Thiruvallur Taluk & District – 601 103,  
Tamil Nadu, India

---

### Subject: Operating System Lab
### Assignment: 2

**Submitted By:** Shudarsan Regmi  
**Roll No.:** CH.SC.U4CYS23055

</div>

---

### Task - 1: Write a program to simulate address translation in a segmented memory system. Given a logical address (segment number and offset), segment table, and segment sizes, output the corresponding physical address or indicate an invalid address

```c
#include <stdio.h>

// Structure to store segment table entries
struct Segment {
    int base;
    int size;
};

// Function to simulate segmented address translation
void translateSegmentedAddress(int segmentNumber, int offset, struct Segment segmentTable[], int totalSegments) {
    // Check if the segment number is valid
    if (segmentNumber >= totalSegments || segmentNumber < 0) {
        printf("Invalid segment number!\n");
        return;
    }
    
    // Get the base and size of the segment
    struct Segment segment = segmentTable[segmentNumber];
    
    // Check if the offset is valid
    if (offset >= segment.size || offset < 0) {
        printf("Invalid offset for the segment!\n");
    } else {
        // Compute physical address
        int physicalAddress = segment.base + offset;
        printf("Physical Address: %d\n", physicalAddress);
    }
}

int main() {
    // Define segment table (base and size for each segment)
    struct Segment segmentTable[] = {
        {100, 500},   // Segment 0: base=100, size=500
        {600, 300},   // Segment 1: base=600, size=300
        {1000, 400}   // Segment 2: base=1000, size=400
    };
    
    int totalSegments = sizeof(segmentTable) / sizeof(segmentTable[0]);
    
    // Input logical address (segment number, offset)
    int segmentNumber, offset;
    printf("Enter Segment Number: ");
    scanf("%d", &segmentNumber);
    printf("Enter Offset: ");
    scanf("%d", &offset);
    
    // Call the function to translate the address
    translateSegmentedAddress(segmentNumber, offset, segmentTable, totalSegments);
    
    return 0;
}

```

## Output

```
Enter Segment Number: 1
Enter Offset: 150
Physical Address: 750
```


### Task - 2: Write a program to simulate address translation in a paged memory system. Given a virtual address, page size, and page table, output the corresponding physical address or indicate a page fault.

```c
#include <stdio.h>

#define PAGE_FAULT -1

// Function to simulate paged address translation
void translatePagedAddress(int virtualAddress, int pageSize, int pageTable[], int totalPages) {
    // Calculate page number and offset
    int pageNumber = virtualAddress / pageSize;
    int offset = virtualAddress % pageSize;
    
    // Check if the page number is valid
    if (pageNumber >= totalPages || pageNumber < 0) {
        printf("Invalid page number!\n");
        return;
    }
    
    // Get the physical frame number from the page table
    int frameNumber = pageTable[pageNumber];
    
    if (frameNumber == PAGE_FAULT) {
        printf("Page fault!\n");
    } else {
        // Compute physical address
        int physicalAddress = frameNumber * pageSize + offset;
        printf("Physical Address: %d\n", physicalAddress);
    }
}

int main() {
    // Define page table (frame numbers for each page)
    int pageTable[] = {
        3,  // Page 0 is mapped to frame 3
        5,  // Page 1 is mapped to frame 5
        PAGE_FAULT, // Page 2 is not mapped (page fault)
        7   // Page 3 is mapped to frame 7
    };
    
    int totalPages = sizeof(pageTable) / sizeof(pageTable[0]);
    int pageSize = 1024;  // Define the page size (e.g., 1 KB)
    
    // Input virtual address
    int virtualAddress;
    printf("Enter Virtual Address: ");
    scanf("%d", &virtualAddress);
    
    // Call the function to translate the address
    translatePagedAddress(virtualAddress, pageSize, pageTable, totalPages);
    
    return 0;
}

```

## Output

```
Enter Virtual Address: 3076
Physical Address: 7172
```

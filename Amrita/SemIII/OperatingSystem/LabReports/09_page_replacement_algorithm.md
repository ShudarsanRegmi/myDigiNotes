


# Plage Replacement Algorithm

### First In First Out

>To write a program to execute First in First out Page Replacement Algorithm
```c
#include <stdio.h>

int main() {
    int incomingStream[] = {4, 1, 2, 4, 5};
    int frames = 3; // Assuming a frame size of 3 for this example
    int temp[frames];
    int pageFaults = 0;
    int s, n, m;

    // Initialize temp array
    for (n = 0; n < frames; n++) {
        temp[n] = -1;
    }

    for (m = 0; m < sizeof(incomingStream) / sizeof(incomingStream[0]); m++) {
        s = 0;
        for (n = 0; n < frames; n++) {
            if (incomingStream[m] == temp[n]) {
                s++;
                pageFaults--;
            }
        }
        pageFaults++;
        if ((pageFaults <= frames) && (s == 0)) {
            temp[m] = incomingStream[m];
        } else if (s == 0) {
            temp[(pageFaults - 1) % frames] = incomingStream[m];
        }
        printf("\n");
        printf("%d\t\t\t", incomingStream[m]);
        for (n = 0; n < frames; n++) {
            if (temp[n] != -1)
                printf(" %d\t\t\t", temp[n]); 
            else
                printf(" - \t\t\t");
        }
    }
    printf("\nTotal Page Faults:\t%d\n", pageFaults); 
    return 0;
}

```

### Output

```
sudoerson@Aparichit:~/oslab/page_repl$ ./out

4                        4                       -                       -
1                        4                       1                       -
2                        4                       1                       2
4                        4                       1                       2
5                        5                       1                       2
Total Page Faults:      4
```

### Least Recently Used

```c
#include <stdio.h>
#include <limits.h>

void printFrame(int queue[], int occupied) {
    for (int i = 0; i < occupied; i++) {
        printf("%d\t\t", queue[i]);
    }
    printf("\n");
}

int checkHit(int page, int queue[], int occupied) {
    for (int i = 0; i < occupied; i++) {
        if (queue[i] == page) {
            return 1; // Hit
        }
    }
    return 0; // Miss
}

int main() {
    int incomingStream[] = {1, 2, 3, 2, 1, 5, 2, 1, 6, 2, 5, 6, 3, 1, 3}; 
    int n = sizeof(incomingStream) / sizeof(incomingStream[0]);
    int frames = 3; 
    int queue[frames]; 
    int distance[n];
    int occupied = 0; 
    int pagefault = 0;

    printf("Page\t Frame1 \t Frame2 \t Frame3\n"); 

    for (int i = 0; i < n; i++) {
        printf("%d: \t\t", incomingStream[i]); 
        if (checkHit(incomingStream[i], queue, occupied)) {
            printFrame(queue, occupied);
        } else if (occupied < frames) { 
            queue[occupied] = incomingStream[i]; 
            pagefault++;
            occupied++;
            printFrame(queue, occupied);
        } else {
            int max = INT_MIN; 
            int index;
            for (int j = 0; j < frames; j++) {
                distance[j] = 0;
                // Traverse in reverse direction to find
                // at what distance frame item occurred last 
                for (int k = i - 1; k >= 0; k--) {
                    distance[j]++;
                    if (queue[j] == incomingStream[k]) {
                        break;
                    }
                }
                if (distance[j] > max) { 
                    max = distance[j]; 
                    index = j;
                }
            }
            queue[index] = incomingStream[i]; 
            printFrame(queue, occupied); 
            pagefault++;
        }
        printf("\n");
    }
    printf("Page Faults: %d\n", pagefault);
    return 0;
}

```

### Output
```
Page     Frame1          Frame2          Frame3
1:              1

2:              1               2

3:              1               2               3

2:              1               2               3

1:              1               2               3

5:              1               2               5

2:              1               2               5

1:              1               2               5

6:              1               2               6

2:              1               2               6

5:              5               2               6

6:              5               2               6

3:              5               3               6

1:              1               3               6

3:              1               3               6

Page Faults: 8
```

### Optimal Page replacement algorithm

>Write an algorithm for optimal page replacement

```c
#include <stdio.h>

int search(int key, int frame_items[], int frame_occupied) {
    for (int i = 0; i < frame_occupied; i++) 
        if (frame_items[i] == key)
            return 1;
    return 0;
}

void printOuterStructure(int max_frames) { 
    printf("Stream ");
    for (int i = 0; i < max_frames; i++) 
        printf("Frame%d ", i + 1);
}

void printCurrFrames(int item, int frame_items[], int frame_occupied, int max_frames) { 
    printf("\n%d \t\t", item);
    for (int i = 0; i < max_frames; i++) { 
        if (i < frame_occupied)
            printf("%d \t\t", frame_items[i]); 
        else
            printf("- \t\t");
    }
}

int predict(int ref_str[], int frame_items[], int refStrLen, int index, int frame_occupied) {
    int result = -1, farthest = index;
    for (int i = 0; i < frame_occupied; i++) { 
        int j;
        for (j = index; j < refStrLen; j++) {
            if (frame_items[i] == ref_str[j]) {
                if (j > farthest) { 
                    farthest = j; 
                    result = i;
                }
                break;
            }
        }
        if (j == refStrLen) 
            return i;
    }
    return (result == -1) ? 0 : result;
}

void optimalPage(int ref_str[], int refStrLen, int frame_items[], int max_frames) {
    int frame_occupied = 0; 
    printOuterStructure(max_frames); 
    int hits = 0;
    
    for (int i = 0; i < refStrLen; i++) {
        if (search(ref_str[i], frame_items, frame_occupied)) { 
            hits++;
            printCurrFrames(ref_str[i], frame_items, frame_occupied, max_frames);
            continue;
        }
        if (frame_occupied < max_frames) { 
            frame_items[frame_occupied] = ref_str[i]; 
            frame_occupied++;
            printCurrFrames(ref_str[i], frame_items, frame_occupied, max_frames);
        } else {
            int pos = predict(ref_str, frame_items, refStrLen, i + 1, frame_occupied);
            frame_items[pos] = ref_str[i];
            printCurrFrames(ref_str[i], frame_items, frame_occupied, max_frames);
        }
    }
    
    printf("\n\nHits: %d\n", hits); 
    printf("Misses: %d\n", refStrLen - hits);
}

int main() {
    // int ref_str[] = {9, 0, 5, 1, 0, 3, 0, 4, 1, 3, 0, 3, 1, 3};
    int ref_str[] = {7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1};
    int refStrLen = sizeof(ref_str) / sizeof(ref_str[0]);
    int max_frames = 3;
    int frame_items[max_frames];
    optimalPage(ref_str, refStrLen, frame_items, max_frames); 
    return 0;
}

```

### Output

```
sudoerson@Aparichit:~/oslab/page_repl$ ./out
Stream Frame1 Frame2 Frame3
7               7               -               -
0               7               0               -
1               7               0               1
2               2               0               1
0               2               0               1
3               2               0               3
0               2               0               3
4               2               4               3
2               2               4               3
3               2               4               3
0               2               0               3
3               2               0               3
2               2               0               3
1               2               0               1
2               2               0               1
0               2               0               1
1               2               0               1
7               7               0               1
0               7               0               1
1               7               0               1

Hits: 11
Misses: 9
```

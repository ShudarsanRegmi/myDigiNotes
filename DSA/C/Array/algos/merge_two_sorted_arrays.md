# Merging two sorted arrays


## Using Merge of merge sort

#### The one which I crafted

```c
#include <stdio.h>

void printArr(int arr[], size_t size);

int main() {
    int x[] = {1,3,6,7,10,11};
    int y[] = {2,4,5,9};

    int l1 = sizeof(x) / sizeof(int);
    int l2 = sizeof(y) / sizeof(int);

    int merged[l1+l2] = {};

    int cx = 0, cy= 0, l=0;

    while (l < l1+l2) {

        // we've to check if one of the array is exhausted
        if (cx == l1) {
            // merge all and break out of this loop
            while (l < l1+l2) {
                merged[l] = y[cy];
                l++;
                cy++;
            }
            break;
        }
        // if the other loop is exhausted we've to check that condition too
        if (cy == l2) {
            while (l < l1+l2) {
                merged[l] = x[cx];
                cx++;
                l++;
            }
            break;
        }

        if (x[cx] < y[cy]) {
            merged[l] = x[cx];
            cx++;
        }else {
            merged[l] = y[cy];
            cy++;
        }
        l++;
    }
    printArr(merged, l1+l2);
    return 0;
}

void printArr(int arr[], size_t size) {
    for (int i = 0; i < size; i++) {
        printf("%d \t", arr[i]);
    }
}

```

#### Refactored

```c
#include <stdio.h>

void printArr(int arr[], size_t size);

int main() {
    int x[] = {1, 3, 7, 9, 11, 14};
    int y[] = {2, 4, 5, 9};

    int l1 = sizeof(x) / sizeof(int);
    int l2 = sizeof(y) / sizeof(int);

    int merged[l1 + l2];
    int cx = 0, cy = 0, l = 0;

    while (l < l1 + l2) {
        // If x is exhausted, merge the rest of y
        if (cx == l1) {
            while (cy < l2) {
                merged[l++] = y[cy++];
            }
            break;
        }

        // If y is exhausted, merge the rest of x
        if (cy == l2) {
            while (cx < l1) {
                merged[l++] = x[cx++];
            }
            break;
        }

        // Merge the smaller element or handle the case when both are equal
        if (x[cx] < y[cy]) {
            merged[l++] = x[cx++];
        } else {
            merged[l++] = y[cy++];
        }
    }

    printArr(merged, l1 + l2);
    return 0;
}

void printArr(int arr[], size_t size) {
    for (int i = 0; i < size; i++) {
        printf("%d\t", arr[i]);
    }
    printf("\n");
}

```

#### Improved by ChatGPT

```c
#include <stdio.h>

void printArr(int arr[], size_t size);

int main() {
    int x[] = {1, 3, 6, 7, 10, 11};
    int y[] = {2, 4, 5, 9};

    int l1 = sizeof(x) / sizeof(int);
    int l2 = sizeof(y) / sizeof(int);

    int merged[l1 + l2];

    int cx = 0, cy = 0, l = 0;

    while (cx < l1 && cy < l2) {
        if (x[cx] < y[cy]) {
            merged[l++] = x[cx++];
        } else {
            merged[l++] = y[cy++];
        }
    }

    // Merge remaining elements (if any)
    while (cx < l1) {
        merged[l++] = x[cx++];
    }

    while (cy < l2) {
        merged[l++] = y[cy++];
    }

    printArr(merged, l1 + l2);
    return 0;
}

void printArr(int arr[], size_t size) {
    for (int i = 0; i < size; i++) {
        printf("%d \t", arr[i]);
    }
}

```

### GFG
```c
#include <stdio.h>

// Merge ar1[0..n1-1] and ar2[0..n2-1] into ar3
void mergeArrays(int* ar1, int n1, int* ar2, int n2, int* ar3) {
    int i = 0, j = 0, k = 0;

    while (i < n1 && j < n2) {
      
        // Pick smaller of the two current elements and move ahead in the array of the picked element
        if (ar1[i] < ar2[j])
            ar3[k++] = ar1[i++];
        else
            ar3[k++] = ar2[j++];
    }

    // if there are remaining elements of the first array, move them
    while (i < n1)
        ar3[k++] = ar1[i++];

    // Else if there are remaining elements of the second array, move them
    while (j < n2)
        ar3[k++] = ar2[j++];
}

// Driver code
int main() {
    int ar1[] = {1, 3, 5, 7};
    int ar2[] = {2, 4, 6, 8};
    int n1 = sizeof(ar1) / sizeof(ar1[0]);
    int n2 = sizeof(ar2) / sizeof(ar2[0]);
    int ar3[n1 + n2];

    mergeArrays(ar1, n1, ar2, n2, ar3);

    for (int i = 0; i < n1 + n2; i++)
        printf("%d ", ar3[i]);

    return 0;
}

```

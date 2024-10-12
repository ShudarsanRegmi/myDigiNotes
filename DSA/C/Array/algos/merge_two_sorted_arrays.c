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

# Radix Sort

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

// Function to get the maximum element in the array
int getMax(const std::vector<int>& arr) {
    return *max_element(arr.begin(), arr.end());
}

// Radix sort using std::sort
void radixSort(std::vector<int>& arr) {
    int maxNum = getMax(arr);

    // Sort by each digit, using std::sort instead of counting sort
    for (int exp = 1; maxNum / exp > 0; exp *= 10) {
        std::sort(arr.begin(), arr.end(), [exp](int a, int b) {
            return (a / exp) % 10 < (b / exp) % 10;
        });
    }
}

// Utility function to print an array
void printArray(const std::vector<int>& arr) {
    for (int num : arr) 
        std::cout << num << " ";
    std::cout << std::endl;
}

// Driver code
int main() {
    std::vector<int> arr = {170, 45, 75, 90, 802, 24, 2, 66};
    std::cout << "Original array: ";
    printArray(arr);

    radixSort(arr);

    std::cout << "Sorted array: ";
    printArray(arr);

    return 0;
}

```

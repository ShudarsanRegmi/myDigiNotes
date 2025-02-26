# Insertion Sort

```algorithm
// corrected in midsem dsa
loop i : [0, n-1]
  loop j : [i, 0) ;  j--
    if arr[j-1] < arr[j]:
      break
    swap arr[j-1], arr[j]
```

```algorithm
loop i : [1, n]
  loop j : [i, 0]
  while ar[j-1 > ar[j]:
      swap (ar[j-1], ar[j])
```



```cpp
 void insertionSort(vector<int>& arr) {
        for (int i=0; i<arr.size(); i++) {
            int j=i;
            // insert the current element in the right position
            while(j>0 && arr[j] < arr[j-1]) { // chatgpt: < wlil give stability <= will not mentioning that <= will case unnecessary swaps for equal elements.. 
                swap(arr[j], arr[j-1]);
                j--;
            }
        }
    }
```

## Code to prove which of the logic gives stability
```cpp
#include <iostream>
#include <vector>
using namespace std;

// Function to print the array of pairs
void printArray(const vector<pair<int, char>>& arr, string msg) {
    cout << msg << ": ";
    for (auto& p : arr) {
        cout << "(" << p.first << "," << p.second << ") ";
    }
    cout << endl;
}

// Stable Insertion Sort (using < for comparison)
void stableInsertionSort(vector<pair<int, char>>& arr) {
    int n = arr.size();
    for (int i = 1; i < n; i++) {
        pair<int, char> key = arr[i];
        int j = i - 1;

        // Move elements that are greater than key one position ahead
        while (j >= 0 && arr[j].first > key.first) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key; // Insert at the correct position
    }
}

// Unstable Insertion Sort (using <= for comparison)
void unstableInsertionSort(vector<pair<int, char>>& arr) {
    int n = arr.size();
    for (int i = 1; i < n; i++) {
        pair<int, char> key = arr[i];
        int j = i - 1;

        // This may swap equal elements, making it unstable
        while (j >= 0 && arr[j].first >= key.first) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key; // Insert at the correct position
    }
}

int main() {
    // Input with duplicate keys
    vector<pair<int, char>> arr1 = {{1, 'a'}, {2, 'b'}, {1, 'c'}};
    vector<pair<int, char>> arr2 = arr1; // Copy for the unstable sort

    // Sorting
    stableInsertionSort(arr1);
    unstableInsertionSort(arr2);

    // Print results
    printArray(arr1, "Stable Insertion Sort Result");
    printArray(arr2, "Unstable Insertion Sort Result");

    return 0;
}
```


```cpp
#include <iostream>

using namespace std;

int main() {
	int ar[5] = { 2,8,5,3,4 };
	int temp;
	for (int i = 0; i < 5; i++) {
		for (int j = i; j > 0; j--) {
			if (ar[j - 1] < ar[j]) {
				break;
			}
			temp = ar[j - 1];
			ar[j - 1] = ar[j];
			ar[j] = temp;

		}
	}

	for (int i : ar) {
		cout << i << "\t";
	}
	return 0;
}

```

## Complexity Analysis
![image](https://github.com/user-attachments/assets/6ea848d7-b2bc-46a0-88cc-a3b3d0259e20)

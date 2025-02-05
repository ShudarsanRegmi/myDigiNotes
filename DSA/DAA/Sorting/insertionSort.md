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

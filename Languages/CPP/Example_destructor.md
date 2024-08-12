### **Example Program Demonstrating a Good Use of Destructors**

A destructor in C++ is a special member function that is executed automatically when an object goes out of scope or is explicitly deleted. It is typically used to release resources that the object may have acquired during its lifetime, such as memory, file handles, or network connections.

Let's create an example where we manage dynamic memory allocation using a destructor. The program will define a `DynamicArray` class that allocates memory for an array of integers. The destructor will ensure that the memory is properly released when the object is destroyed.

#### **Program: `DynamicArray` Class with Destructor**

```cpp
#include <iostream>
using namespace std;

class DynamicArray {
private:
    int* arr;  // Pointer to dynamically allocated array
    int size;

public:
    // Constructor to allocate memory and initialize the array
    DynamicArray(int s) : size(s) {
        cout << "Constructor: Allocating memory for array of size " << size << endl;
        arr = new int[size];  // Dynamically allocate memory for the array

        // Initialize the array with some values
        for (int i = 0; i < size; ++i) {
            arr[i] = i + 1;
        }
    }

    // Destructor to free the allocated memory
    ~DynamicArray() {
        cout << "Destructor: Releasing memory allocated for the array" << endl;
        delete[] arr;  // Free the dynamically allocated memory
    }

    // Method to display the array
    void display() const {
        for (int i = 0; i < size; ++i) {
            cout << arr[i] << " ";
        }
        cout << endl;
    }
};

int main() {
    {
        cout << "Creating a DynamicArray object inside a block." << endl;
        DynamicArray arr(5);  // Create an object with an array of size 5
        arr.display();        // Display the array elements
    } // The object goes out of scope here, and the destructor is called

    cout << "Exiting the program." << endl;
    return 0;
}
```

### **Explanation**

1. **Dynamic Memory Allocation**:
   - The `DynamicArray` constructor dynamically allocates memory for an integer array using the `new[]` operator.
   - The array is initialized with values from `1` to `size`.

2. **Destructor**:
   - The destructor (`~DynamicArray()`) is defined to free the dynamically allocated memory using the `delete[]` operator.
   - The destructor is automatically invoked when the `DynamicArray` object goes out of scope (e.g., at the end of the block in the `main()` function).

3. **Resource Management**:
   - The use of a destructor ensures that the memory allocated for the array is properly released when the object is destroyed, preventing memory leaks.

### **Output**

```
Creating a DynamicArray object inside a block.
Constructor: Allocating memory for array of size 5
1 2 3 4 5 
Destructor: Releasing memory allocated for the array
Exiting the program.
```

### **Key Points**

- **Automatic Resource Management**: Destructors are crucial for managing resources such as dynamic memory, ensuring that resources are released when an object is destroyed.
- **No Memory Leaks**: By freeing allocated memory in the destructor, we prevent memory leaks that could otherwise occur if the memory was not properly managed.
- **RAII Principle**: This example follows the RAII (Resource Acquisition Is Initialization) principle, where resource management is tied to the lifetime of objects.

This program demonstrates the effective use of destructors in managing resources and ensuring that they are properly released when they are no longer needed.

--- 

## Short Example

### **Short Example: Destructor in C++**

Here's a concise example to demonstrate the use of a destructor:

```cpp
#include <iostream>
using namespace std;

class MyClass {
private:
    int* ptr;

public:
    // Constructor: Allocates memory
    MyClass(int size) {
        ptr = new int[size];
        cout << "Memory allocated for array of size " << size << endl;
    }

    // Destructor: Frees the allocated memory
    ~MyClass() {
        delete[] ptr;
        cout << "Memory deallocated" << endl;
    }
};

int main() {
    MyClass obj(5);  // Creating an object
    return 0;  // Destructor is called automatically here
}
```

### **Key Points for Exams**:
- **Constructor**: Allocates memory dynamically using `new`.
- **Destructor**: Automatically called when the object goes out of scope, freeing the memory with `delete[]`.
- **Output**:
  ```
  Memory allocated for array of size 5
  Memory deallocated
  ```

This example is straightforward and demonstrates the essential concept of a destructor in C++.

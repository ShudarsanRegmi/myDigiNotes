# Creating Dynamic Libraries




### **Creating and Using a Dynamic Library in C**

The process of creating and utilizing a **dynamic library (shared library)** in C involves several steps. The development takes place in a **Linux** environment, where the shared object file (`.so`) is compiled and linked with a program.

#### **1. Development of the Library**
A dynamic library typically consists of reusable functions that can be shared across multiple programs. In this case, a **mathematical library** was developed.

![image](https://github.com/user-attachments/assets/47637a92-c80d-4f3b-8dc4-94ef38484e9d)

##### **1.1. Implementation of the Library (`mymath.c`)**
A source file named `mymath.c` was created to define mathematical functions. The functions included in the library perform basic arithmetic operations such as addition, subtraction, multiplication, and division. The implementation is as follows:

```c
#include <stdio.h>

int add(int a, int b) {
    return a + b;
}

int subtract(int a, int b) {
    return a - b;
}

int multiply(int a, int b) {
    return a * b;
}

double divide(int a, int b) {
    if (b == 0) {
        printf("Error: Division by zero!\n");
        return 0.0;
    }
    return (double)a / b;
}
```

##### **1.2. Declaration of Function Prototypes (`mymath.h`)**
A header file (`mymath.h`) was created to declare the function prototypes. This header file allows other programs to access the functions contained within the library.

```c
#ifndef MYMATH_H
#define MYMATH_H

int add(int a, int b);
int subtract(int a, int b);
int multiply(int a, int b);
double divide(int a, int b);

#endif
```

---

#### **2. Compilation of the Shared Library**
To generate the shared object file, the source code was compiled using **GCC**. The following commands were used:

```sh
gcc -fPIC -c mymath.c -o mymath.o
gcc -shared -o libmymath.so mymath.o
```

![image](https://github.com/user-attachments/assets/bd85618e-abba-4468-a8be-6472d9965fd1)


- The `-fPIC` flag was used to generate **position-independent code**, which is necessary for shared libraries.
- The `-c` flag compiled the source file into an object file without linking.
- The `-shared` flag was used to create a **shared object file (`.so`)**.

As a result of this process, a file named **`libmymath.so`** was successfully generated.

---

#### **3. Utilization of the Shared Library**
To verify the functionality of the newly created library, a **C program (`main.c`)** was written.

##### **3.1. Implementation of the Main Program (`main.c`)**
A program was created to utilize the functions from `libmymath.so`. The corresponding implementation is shown below:

```c
#include <stdio.h>
#include "mymath.h"

int main() {
    int a = 10, b = 5;

    printf("Addition: %d\n", add(a, b));
    printf("Subtraction: %d\n", subtract(a, b));
    printf("Multiplication: %d\n", multiply(a, b));
    printf("Division: %.2f\n", divide(a, b));

    return 0;
}
```

##### **3.2. Compilation of the Main Program**
The main program was compiled with the following command:

```sh
gcc -o main main.c -L. -lmymath
```
![image](https://github.com/user-attachments/assets/d08cca6a-4bc7-404e-b8c6-711828610c13)


- The `-L.` option specified the current directory as the location of the library.
- The `-lmymath` option linked the program against `libmymath.so`.

---

#### **4. Execution and Library Path Configuration**
During execution, an error was encountered due to the **shared library not being found** by the system. The following message was displayed:

```
error while loading shared libraries: libmymath.so: cannot open shared object file: No such file or directory
```

To resolve this issue, the **LD_LIBRARY_PATH** environment variable was modified temporarily:

```sh
export LD_LIBRARY_PATH=.:$LD_LIBRARY_PATH
./main
```

![image](https://github.com/user-attachments/assets/421a6542-58fa-49f7-8164-a03b9cefb639)


Alternatively, to make the library accessible system-wide, it was moved to `/usr/local/lib` and registered with the system:

```sh
sudo cp libmymath.so /usr/local/lib
sudo ldconfig
```


Following this step, the program was executed without requiring additional environment variables.

---

#### **5. Output Verification**
After successful execution, the following output was produced:

```
Addition: 15
Subtraction: 5
Multiplication: 50
Division: 2.00
```

![image](https://github.com/user-attachments/assets/aded1708-59bf-458d-b58c-cab6de8825e9)


The expected results were observed, confirming the successful creation and integration of the **dynamic library** in C.

---

### **Conclusion**
A **shared library** (`.so` file) was successfully developed, compiled, and integrated into a program. The necessary steps included defining functions, generating the library, linking it with a program, and ensuring proper execution by configuring the shared library path. The approach demonstrated the modular nature of dynamic libraries, allowing multiple programs to use the same functions without requiring static linking.

Would an exploration of **runtime dynamic linking (`dlopen`)** be beneficial for further understanding?

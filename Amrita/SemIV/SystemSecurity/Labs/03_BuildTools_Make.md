# Makefile
---

## Theory
When working on a C project with multiple source files, manually compiling each file can be inefficient. The `make` tool helps automate this process by only recompiling files that have changed, using timestamps.

### **How Does `make` Track Changes?**
- `make` checks **timestamps** of files.
- If a `.c` file has been **modified after** its corresponding `.o` file was last compiled, `make` recompiles only that file.
- This helps in **incremental compilation**, making the build process faster.

---

## **Project Directory Structure**
```
project/
│── Makefile
│── main.c
│── calculator.c
│── calculator.h
```

---

![image](https://github.com/user-attachments/assets/08507596-cd45-4756-9fac-23a5ab784658)


## **Makefile**
```make
# Compiler
CC = gcc

# Compiler flags
CFLAGS = -g -Wall -Wextra -std=c11

# Target executable
TARGET = calculator

# Source and object files
SRC = main.c calculator.c
OBJ = $(SRC:.c=.o)

# Default rule (build the executable)
$(TARGET) : $(OBJ)
	$(CC) $(CFLAGS) -o $(TARGET) $(OBJ)

# Rule to compile C files into object files
%.o : %.c
	$(CC) $(CFLAGS) -c $< -o $@

# Clean rule to remove generated files
clean:
	rm -f $(TARGET) $(OBJ)
```

---

## **Source Code**
### `main.c`
```c
#include <stdio.h>
#include "calculator.h"

int main() {
    int a = 5, b = 3;
    printf("Sum: %d\n", add(a, b));
    printf("Difference: %d\n", subtract(a, b));
    return 0;
}
```

### `calculator.c`
```c
#include "calculator.h"

int add(int a, int b) {
    return a + b;
}

int subtract(int a, int b) {
    return a - b;
}
```

### `calculator.h`
```c
#ifndef CALCULATOR_H
#define CALCULATOR_H

int add(int a, int b);
int subtract(int a, int b);

#endif // CALCULATOR_H
```

![image](https://github.com/user-attachments/assets/73b61512-3332-440a-9fdb-d1b568a6ae50)

---

## **Building the Project**
1. Open a terminal and navigate to the project directory:
   ```bash
   cd project
   ```
2. Run `make`:
   ```bash
   make
   ```
   - This will compile `main.c` and `calculator.c`, producing the `calculator` executable.

3. Execute the program:
   ```bash
   ./calculator
   ```
   - Expected output:
     ```
     Sum: 8
     Difference: 2
     ```

4. To clean up the compiled files:
   ```bash
   make clean
   ```

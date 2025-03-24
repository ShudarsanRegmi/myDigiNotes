# Creating Static Libraries in C

![image](https://github.com/user-attachments/assets/03ff3b7b-29c4-495b-b62e-16849cdfc128)


## What is a Static Library?

A static library is a collection of object files (.o) bundled together in a single archive (.a) that can be linked into executables. Unlike dynamic libraries (.so or .dll), static libraries are copied into the final binary, making them self-contained.


```
finance_project/
│── include/
│   ├── finance.h
│── src/
│   ├── finance.c
│── lib/
│── main.c
│── Makefile
```

### Codes

![image](https://github.com/user-attachments/assets/4aad0593-aa1a-430a-9022-1501960bc639)

![image](https://github.com/user-attachments/assets/025fc450-84da-4298-94d8-2ae8ae2cbaa0)


**main.c**
```c
#include <stdio.h>
#include "finance.h"


int main() {
    double p = 1000.0, r = 5.0;
    int t = 3;

    printf("Simple Interest: %2.f \n", simple_interest(p, t, r));
    printf("Compound Interest: %2.f \n", compound_interest(p, t, r));

    return 0;
}
```
**finance.h**
```c
#ifndef FINANCE_H
#define FINANCE_H

double simple_interest(double principal, int time, double rate);
double compound_interest(double principal, int time, double rate);

#endif
```
**finance.c**
```c
#include "finance.h"
#include <math.h>

double simple_interest(double principal, int time, double rate) {
    return principal * time * rate;
}

double compound_interest(double principal, int time, double rate) {
    return principal * pow(1 + rate, time) - principal;
}

```
```Makefile
# Compiler
CC = gcc

# Directories
SRC_DIR = src
INCLUDE_DIR = include
LIB_DIR = lib

# Source and Object Files
SRC_FILES = $(SRC_DIR)/finance.c
OBJ_FILES = $(SRC_DIR)/finance.o

# Static Library Name
LIB_NAME = libfinance.a

# Executable Name
TARGET = finance_app

# Compiler and Linker Flags
CFLAGS = -I$(INCLUDE_DIR)
LDFLAGS = -L$(LIB_DIR) -lfinance -lm 

# Default target
all: $(TARGET)

# Build the Static Library
$(LIB_DIR)/$(LIB_NAME): $(OBJ_FILES)
	ar rcs $@ $^

# Compile Object Files
$(SRC_DIR)/finance.o: $(SRC_DIR)/finance.c $(INCLUDE_DIR)/finance.h
	$(CC) -c $< -o $@ $(CFLAGS)

# Build the Executable
$(TARGET): main.c $(LIB_DIR)/$(LIB_NAME)
	$(CC) main.c -o $(TARGET) $(CFLAGS) $(LDFLAGS)

# Force re-linking every time
# .PHONY: all clean

# Clean up generated files
clean:
	rm -f $(SRC_DIR)/*.o $(LIB_DIR)/*.a $(TARGET)

```

### Compiling the library
```bash
gcc -c src/finance.c -o src/finance.o -Iinclude
```

### Creating .a archive from object files
```bash
ar rcs lib/libfinance.a src/finance.o # use this
ar rcs lib/finance.a src/finance.o # this had created problem, i.e. giving non-standard name to the library file
```
**Checking what object files does the archive contains**
```bash
ar -t lib/libfinance.a
```

### Final compilation command
```bash
gcc main.c -Llib -l:finance.a -lm -Iinclude -o finance_app # if the library name is non standard
gcc main.c -Llib -lfinance -lm -Iinclude -o finance_app # if follows standard naming of static file like. libfinance, libcalculator, etc.
```
>Static libraries in Unix-like systems follow the lib<name>.a convention because the linker (ld) automatically searches for files prefixed with lib when using -l<name>, and omitting this prefix requires explicitly specifying the filename with -l:<name>.a.

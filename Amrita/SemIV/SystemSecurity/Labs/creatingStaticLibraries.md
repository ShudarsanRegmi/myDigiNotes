# Creating Static Libraries in C

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

### Compiling the library
```bash
gcc -c src/finance.c -o src/finance.o -Iinclude
```

### Creating .a archive from object files
```bash
ar rcs lib/finance.a src/finance.o
```
**Checking what object files does the archive contains**
```bash
ar -t lib/libfinance.a
```

### Final compilation command
```bash
gcc main.c -Llib -l:finance.a -lm -Iinclude -o finance_app
```


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

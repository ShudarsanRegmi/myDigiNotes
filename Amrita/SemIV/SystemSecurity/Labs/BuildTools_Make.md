# Make Tools


## How Does make Keep Track of Changed Files?
>make determines which files need to be recompiled based on timestamps. It checks the modification time of each source file and its corresponding object file. If a source file has been updated after its object file was last compiled, make recompiles only that file.


### The Problem
```bash
gcc -c file1.c -o file1.o
gcc -c file2.c -o file2.o
gcc file1.o file2.o -o my_program
```

### Syntax:
```make
target: dependencies
    command
```
- The first target is the default target executed when you run make.

#### File Structure
```
project/
│── Makefile
│── main.c
│── helper.c
│── helper.h

```


```make
CC = gcc

CFLAGS = -g -Wall -Wextra -std=c11

# Target executable
TARGET = calculator
SRC = main.c calculator.c

OBJ = $(SRC:.c=.o)

#Rule to build the executable
$(TARGET) : $(OBJ)
	$(CC) $(CFLAGS) -o $(TARGET) $(OBJ)

# Rule to compile C files into object files
%.o : %.c
	$(CC) $(CFLAGS) -c $< -o $@

# Clean rule
clean:
	rm -f $(TARGET) $(OBJ)
```




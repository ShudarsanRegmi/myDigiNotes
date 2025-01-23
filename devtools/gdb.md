# GDB Guide

### Compile by keeping the debuggnig flag
```
g++ -o out input.cpp -g # for cpp
gcc -o out input.c -g # for C
```

### Changing the Layout
```
layout next
lay n
```
### Setting the breakpoints
```
break main
break <line_no>
```
### Listing All the breakpoints
```
info breakpoints
```


### Clearing the breakpoing
```
clear <line_number>
```

### Start the program
```
run
run arg1 arg2
```

### Go to the next line (Step Over)
```
next
n
```

### Step into a function
```
step
s
```

### Step out of the current function
```
finish
```
### Continue to the next breakpoint
```
continue
c
```

### Show Local variables in the current scope
```
info locals
```
### Display the code around the current line
```cpp
list
l
```

---

## Printing the Variables

### Printing variables
```
print <variable>
p <variable>
p arr
```
### Setting up watch point
```
watch <variable>
```

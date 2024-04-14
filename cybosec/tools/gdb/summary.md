# Using GNU GDB(Debugger)

## Compiling with gcc while keeping symbols for easy debugging

```
gcc -g -o out input.c
```

## Changing the layouts

```
layout next
or
lay n
```

## Refreshing the window
```
ctrl + l 
or
refresh
```


## Starting a program
```
run
or
r
```

## Killing a running program
```
kill
```

## Breakpoints

### Setting up Breakpoint
```
break line/func
Eg. break main
```

### Finding Breakpoints
```
info breakpoints
```

### Deleting a breakpoint
```
delete <breakpoint>
```

### Clearing all breakpoints
```
clear
```

### Disabling a breakpoint
```
disable <breakpoint>
```

### Enabling a disabled breakpoint
```
enable <breakpoint>
```



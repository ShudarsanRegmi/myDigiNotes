# Creating Dynamic Linked Libraries(Shared Objects) in Linux



## Codes

![image](https://github.com/user-attachments/assets/a518eb02-b91f-4299-ae67-43d8c9dd12cc)


**mathlib.h**
```c
#ifndef MATHLIB_H
#define MATHLIB_H


int add  (int a, int b);
int sub(int a, int b);


#endif
```

**mathlib.c**
```c
#include "mathlib.h"

int add (int a, int b) {
    return a+b;
}

int sub(int a, int b) {
    return a-b;
}

```

**main.c**

```c
#include <stdio.h>
#include <dlfcn.h>

int main() {
    void *handle = dlopen("./mathlib.so", RTLD_LAZY);
    if(!handle) {
        printf("!Error loading the library.. %s \n", dlerror());
        return 1;
    }

    // Load function pointers
    int (*add)(int, int) = dlsym(handle, "add");
    int (*sub)(int, int) = dlsym(handle, "sub");

    if(!add || !sub) {
        printf("Error handling functions... %s \n", dlerror());
        dlclose(handle);
        return 1;
    }

    // Using those functions
    printf("5 + 3 = %d \n", add(5,3));
    printf("5 - 3 = %d \n", sub(5,3));

    // close the library
    dlclose(handle);

    return 0;
}
```

### Creating the shared object
```bash
gcc -fPIC -shared -o mathlib.so mathlib.c
```

### Linking the shared object
```bash
 gcc -o main main.c -ldl
```





```c
#include <stdio.h>
#include <string.h>

int main()
{
    char buffer[5];
    
    strcpy(buffer, "Hell");
    
    
    char buf2[10];
    strcpy(buf2, "abcdefg");
    
    printf("%s", buffer);
    return 0;
}
```

**output**


<img width="724" height="414" alt="image" src="https://github.com/user-attachments/assets/23955888-32f6-4563-b0c6-c4c16c42b23e" />

```c
#include <stdio.h>
#include <string.h>

int main()
{
    char buffer[5];
    
    strcpy(buffer, "Helll");
    
    
    char buf2[10];
    strcpy(buf2, "abcdefg");
    
    printf("%s", buffer);
    return 0;
}
```


**Output**

<img width="800" height="583" alt="image" src="https://github.com/user-attachments/assets/370cb05e-41b5-495b-bbb9-5a05218abb35" />

> This program shows the seriousness of overwritign the null pointer.


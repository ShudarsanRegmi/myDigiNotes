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

## Sprintf

**sprintf basic usage**

```
#include <stdio.h>
#include <string.h>

int main()
{
    char buffer[5];
    
    strncpy(buffer, "Hell", 5);

    
    char buf2[10];
    strcpy(buf2, "abcdefg");
    
    printf("%s", buffer);
    return 0;
}
```
**Output**
<img width="1042" height="430" alt="image" src="https://github.com/user-attachments/assets/6a950c58-3596-4f72-97b3-d70fa2eeaba9" />

> Output is safe

**Copying source to destination without leaving room for null char in dest**

```
#include <stdio.h>
#include <string.h>

int main()
{
    char buffer[5];
    
    strncpy(buffer, "Hello", 5);

    
    char buf2[10];
    strcpy(buf2, "abcdefg");
    
    printf("%s", buffer);
    return 0;
}
```

<img width="994" height="443" alt="image" src="https://github.com/user-attachments/assets/80ffe704-69eb-48ef-bebc-a9a5561c6c8c" />

**Null terminator coped by strncpy but it was overridden by second strcpy**

```c
#include <stdio.h>
#include <string.h>

int main()
{
    char buffer[5];
    
    strncpy(buffer, "Hello", 6);

    
    char buf2[10];
    strcpy(buf2, "abcdefg");
    
    printf("%s", buffer);
    return 0;
}
```

<img width="1115" height="602" alt="image" src="https://github.com/user-attachments/assets/5d618160-7b0b-4e2e-8c40-aa44fc482609" />

> the warning for bufferoverflow is obvious as we're writing 6 bytes(including null) in the 5 bytes buffer


**Perfectly fitting all chars with no care for null termination**

```c
#include <stdio.h>
#include <string.h>

int main()
{
    char buffer[5];
    
    strncpy(buffer, "Hello", 5);

    
    char buf2[10];
    strcpy(buf2, "abcdefg");
    
    printf("%s", buffer);
    return 0;
}
```

**Output**
<img width="1105" height="446" alt="image" src="https://github.com/user-attachments/assets/15e4d77f-a617-42ea-89ca-3f1b2e9f2a33" />

> This is the standard problem discussed in textbook. 


**Mitigation**
```c
#include <stdio.h>
#include <string.h>

int main()
{
    char buffer[5];
    
    strncpy(buffer, "Helllajljaljllo", 5);
    buffer[4] = '\0';

    
    char buf2[10];
    strcpy(buf2, "abcdefg");
    
    printf("%s", buffer);
    return 0;
}


```

> Null terminate the last index.


> 

**Output**
<img width="1091" height="475" alt="image" src="https://github.com/user-attachments/assets/e87968ea-7977-4542-89f0-689d013a36a6" />





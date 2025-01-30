# Generate a wordlist and then brute force the password when the seed from random generator is known

```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    char characters[] = "abcdefghijklmnoqprstuvwyzxABCDEFGHIJKLMNOQPRSTUYWVZX0123456789";
    FILE *fptr = fopen("wordlist.txt", "w");
    long long t = 1548441000;
    for(int i = 0; i <= 86400; i++) {
        t += 1;
        srand(t);
        char password[16];
        for(int i = 0; i < 15; i++) {
            password[i] = characters[rand()%62];
        }
        password[15] = '\n';
        fwrite(password, sizeof(char), 16, fptr);
    }
    fclose(fptr);
    return 0;
}
```

**Brute forcing code**
```
zip2john encrypted.zip > hash
john --wordlist=wordlist.txt hash
```

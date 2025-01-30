# Random Generator gives exactly same output given the same seed

```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void generate_password(int length, const char *charset, int seed) {
    srand(seed);  // Set the seed value
    int charset_size = 0;
    while (charset[charset_size] != '\0') {
        charset_size++;
    }

    printf("Generated Password: ");
    for (int i = 0; i < length; i++) {
        printf("%c", charset[rand() % charset_size]);
    }
    printf("\n");
}

int main() {
    const char *charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*";
    int password_length = 12;
    
    // Example: Seed with a fixed timestamp (26th Jan 2019, IST = 1548467400)
    int seed = 1548467400;

    printf("Using seed: %d\n", seed);
    generate_password(password_length, charset, seed);

    // Re-run with the same seed to check if output is identical
    printf("Re-generating with same seed:\n");
    generate_password(password_length, charset, seed);
    
    printf("Re-generating with same seed:\n");
    generate_password(password_length, charset, seed);
    
    printf("Re-generating with same seed:\n");
    generate_password(password_length, charset, seed);
    
    printf("Re-generating with same seed:\n");
    generate_password(password_length, charset, seed);

    return 0;
}

```

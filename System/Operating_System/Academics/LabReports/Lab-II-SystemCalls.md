# System Calls - Lab-II

- CH.SC.U4CYS23055
- Shudarsan Regmi

## 1. To write program to get PID in UNIX
```C
#include <stdio.h>
#include <unistd.h>

int main() {
	printf("PID of this process is = %d\n",getpid());
	return 0;
}
```
### Code and Output
![image](https://github.com/user-attachments/assets/3167d556-d6a5-4e04-b455-d34321838b55)

## 2. To write a program to execute fork system call

1. The `fork()` system call is used to create a new process by duplicating the calling process, resulting in a parent-child process pair that execute concurrently.
2. After `fork()`, both the parent and the child processes continue executing from the point where `fork()` was called, with `fork()` returning 0 to the child process and the child's PID to the parent process.
3. Proper handling of the return value of `fork()` allows differentiation between parent and child processes, enabling distinct actions for each.

```C
#include <stdio.h>
#include <unistd.h>

int main() {
	printf("PID of this process is = %d\n",getpid());
	printf("Executing fork system call...\n");
	fork();
	// The lines below will be executed by both parent and child
	printf("Child PID is = %d\n", getpid());
	return 0;
}
```
### Output
![image](https://github.com/user-attachments/assets/27548249-d246-4a0c-98b4-f10e3fb55980)

**Didn't Understand**
## 3. Write a program to print number of times a message is printed using fork system call and apply OR Command
```C

```
#include <stdio.h>
#include <unistd.h>

int main() {
	if ( fork() || fork() ) {
		printf("%d True\n", getpid());
	}else {
		printf("%d False\n", getpid());
	}
}



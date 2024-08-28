<div align="center">

![Amrita Vishwa Vidyapeetham Logo](https://webfiles.amrita.edu/2024/04/WhQq1FiB-amrita-vishwa-vidyapeetham-university-logo-colored-version.svg)

# Amrita Vishwa Vidyapeetham
## Chennai Campus
337/1A, Vengal Village,  
Thiruvallur Taluk & District – 601 103,  
Tamil Nadu, India

---

### Subject: Operating System

**Submitted By:** Shudarsan Regmi  
**Roll No.:** CH.SC.U4CYS23055

</div>

---

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
#include <stdio.h>
#include <unistd.h>

int main() {
	if ( fork() || fork() ) {
		printf("%d True\n", getpid());
	}else {
		printf("%d False\n", getpid());
	}
}
```
### Code and Output
![image](https://github.com/user-attachments/assets/92bbe517-b4f5-4a46-b50b-0416c2fadc86)

## 4. 05. To write a program to calculate number of times a message is printed using fork() system and apply AND command .
05. To write a program to calculate number of times a message is printed using fork() system and apply AND command .

```C

#include <stdio.h>
#include <unistd.h>

int main() {
	if ( fork() && fork() ) {
		printf("%d True\n", getpid());
	}else {
		printf("%d False\n", getpid());
	}
}
```

### Code and Output
![image](https://github.com/user-attachments/assets/5c8ee6b9-51c7-47d0-b920-7f6a1a305fa6)

## 5. execv system call 
```C
#include <stdio.h>
#include <unistd.h>

int main(int argc, char *argv[])
{
printf("PID of this main program = %d\n", getpid());
char *args[] = {"Hello","C","Programming",NULL};
execv("./anotherProg",args);
printf("Back to 9.c");
return 0;
}
```

![image](https://github.com/user-attachments/assets/1a8e9bc9-fe34-4e50-8f96-2143899513d0)

## 6. 
```C
#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main()
{
if(fork() == 0)
printf("hello from child\n");
else
{
printf("hello from parent\n");
wait(NULL);
printf("child has terminated\n");
}
printf("Hi\n");
return 0;
}
```
### Output
![image](https://github.com/user-attachments/assets/fb8cf79c-5c3e-46c5-a4aa-bc9d94ce83d9)

### 7. Sleep system call
```C
#include <stdio.h>
#include <unistd.h>

int main()
{
fork();
if(fork() == 0)
{
sleep(5);
printf("This will finish after the parent\n");
}
else
printf("This will finish below the child\n");
return 0;
}

```
![image](https://github.com/user-attachments/assets/0f3cad73-eb3e-49d0-aaf0-bab274d6f8c9)

### 8. 




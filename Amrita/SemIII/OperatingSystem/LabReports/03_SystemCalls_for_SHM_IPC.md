<div align="center">

![Amrita Vishwa Vidyapeetham Logo](https://webfiles.amrita.edu/2024/04/WhQq1FiB-amrita-vishwa-vidyapeetham-university-logo-colored-version.svg)

# Amrita Vishwa Vidyapeetham
## Chennai Campus
337/1A, Vengal Village,  
Thiruvallur Taluk & District – 601 103,  
Tamil Nadu, India

---

### Subject: Operating System Lab

**Submitted By:** Shudarsan Regmi  
**Roll No.:** CH.SC.U4CYS23055


</div>

# System Calls for SHM and IPC in Unix/Linux Systems

## Write a program to Shared Memory

```C
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/shm.h>
#include <string.h>

int main() {
	int i;
	void *shared_memory;
	char buff[100];
	int shmid;
	shmid = shmget((key_t)2345, 1024, 0666 | IPC_CREAT);
	shared_memory = shmat(shmid, NULL, 0);
	printf("Enter some data to write to shared memory\n");
	read(0, buff, 100);
	strcpy(shared_memory, buff);
	printf("You wrote: %s \n", (char *)shared_memory);
	return 0;
}
```

## Explanation:
```
int shmget(key_t key, size_t size, int shmflg);

DESCRIPTION
       shmget()  returns the identifier of the System V shared memory segment associated with the value of the argument key.  It may be used ei‐
       ther to obtain the identifier of a previously created shared memory segment (when shmflg is zero and key does not have the value IPC_PRI‐
       VATE), or to create a new set.

       A  new shared memory segment, with size equal to the value of size rounded up to a multiple of PAGE_SIZE, is created if key has the value
       IPC_PRIVATE or key isn't IPC_PRIVATE, no shared memory segment corresponding to key exists, and IPC_CREAT is specified in shmflg.

       If shmflg specifies both IPC_CREAT and IPC_EXCL and a shared memory segment already exists for key, then shmget() fails with errno set to
       EEXIST.  (This is analogous to the effect of the combination O_CREAT | O_EXCL for open(2).)

void *shmat(int shmid, const void *shmaddr, int shmflg);

       shmat()  attaches  the System V shared memory segment identified by shmid to the address space of the calling process.  The attaching ad‐
       dress is specified by shmaddr with one of the following criteria:

       • If shmaddr is NULL, the system chooses a suitable (unused) page-aligned address to attach the segment.

       • If shmaddr isn't NULL and SHM_RND is specified in shmflg, the attach occurs at the address equal to shmaddr rounded down to the nearest
         multiple of SHMLBA.

       • Otherwise, shmaddr must be a page-aligned address at which the attach occurs.



```

 - If shmaddr is NULL, the system chooses a suitable (unused) page-aligned address to attach the segment.
### Input / Output
![image](https://github.com/user-attachments/assets/7b4dc4c9-cf95-484b-aad4-b03b4fb0dc28)


## To write a code to use Internet Process Communication (IPC)

```C
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <sys/types.h>
#include <sys/msg.h>

#define MAX_TEXT 512

struct my_msg {
	long int msg_type;
	char some_text[MAX_TEXT];
};

int main() {
	int running=1;
	int msgid;
	struct my_msg some_data;
	char buffer[50];

	msgid = msgget((key_t)14534, 0666 | IPC_CREAT);

	if (msgid == -1) {
		printf("Error in creating queue");
	}

	while (running ) {
		printf("Enter some text: \n");
		fgets(buffer, 50, stdin);

		some_data.msg_type = 1;
		strcpy(some_data.some_text, buffer);

		if (msgsnd(msgid, (void *)&some_data, MAX_TEXT, 0) == -1) {
			printf("Msg not sent \n");
		}

		if (strncmp(buffer, "end", 3) == 0 ) {
			running = 0;
		}
	}
}

```
### Input/Output
![image](https://github.com/user-attachments/assets/0f659f52-e52a-4ce7-95bd-7f59bc5111b6)

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

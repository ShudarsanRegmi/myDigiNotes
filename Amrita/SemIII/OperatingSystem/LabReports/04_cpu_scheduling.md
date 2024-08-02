# CPU Scheduling Algorithms

## Round Robbin Algorithm

```C
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX 100
int queue[MAX];
int front = -1;
int rear = -1;
struct process {
char name[4];
int id; // Process id
int at; // Arrival time
int bt; // Burst time
int rt; // Remaining time
int ct; // Completion time
int ta; // Turn Around time
int wt; // Waiting time
18struct process* next;
} *P = NULL;
struct Gantt
{
int id;
int start;
int stop;
struct Gantt *next;
}*head = NULL;
int dequeue()
{
int data;
if(front == -1 || front == rear + 1)
{
printf("Queue underflow\n");
exit(1);
}
data = queue[front];
front++;
return data;
}
void enqueue(int data)
{
if(rear == MAX-1)
{
printf("Queue overflow\n");
exit(1);
}
if(front == -1)
front = 0;
rear++;
queue[rear] = data;
}
void update(int stop,int id)
{
struct process *ptr = P;
while(ptr != NULL)
19{
if(ptr->id == id)
{
ptr->ct = stop;
}
ptr = ptr->next;
}
}
void addGantt(int id, int start, int stop)
{
struct Gantt *newNode = (struct Gantt*)malloc(sizeof(struct
Gantt));
struct Gantt *ptr = head;
newNode->id = id;
newNode->start = start;
newNode->stop = stop;
newNode->next = NULL;
if(head == NULL)
head = newNode;
else
{
while(ptr->next != NULL)
{
ptr=ptr->next;
}
ptr->next = newNode;
}
update(stop,id);
}
struct process* swap(struct process* ptr1, struct process* ptr2) {
if (ptr1 && ptr2) {
struct process* tmp = ptr2->next;
ptr2->next = ptr1;
ptr1->next = tmp;
return ptr2;
}
return NULL;
}
void bubbleSort(int count) {
20struct process** head = &P;
struct process** h;
int i, j, swapped;
for (i = 0; i < count - 1; i++) {
h = head;
swapped = 0;
for (j = 0; j < count - i - 1; j++) {
struct process* p1 = *h;
struct process* p2 = p1->next;
if (p1->at > p2->at) {
/* update the link after swapping */
*h = swap(p1, p2);
swapped = 1;
}
h = &(*h)->next;
}
/* break if the loop ended without any swap */
if (swapped == 0)
break;
}
}
void addProcess(char* name, int at, int bt,int id) {
struct process* newNode = (struct process*)malloc(sizeof(struct
process));
strcpy(newNode->name, name);
newNode->at = at;
newNode->bt = bt;
newNode->rt = bt;
newNode->id = id;
newNode->ct = 0;
newNode->ta = 0;
newNode->wt = 0;
newNode->next = NULL;
21if (P == NULL)
P = newNode;
else {
struct process* temp = P;
while (temp->next != NULL) {
temp = temp->next;
}
temp->next = newNode;
}
}
void printGantt()
{
struct Gantt *temp = head;
printf("%d",temp->id);
temp = temp->next;
while(temp != NULL)
{
printf(" -> %d",temp->id);
temp = temp->next;
}
}
void main()
{
int n, i, tt = 0, quantum, at, bt;
char name[4];
printf("Enter the no. of processes : ");
scanf("%d", &n);
int AT[n], BT[n], RT[n], id[n];
for (i = 0; i < n; i++)
{
printf("Enter the name of the process : ");
scanf("%s", name);
printf("Enter the Arrival time : ");
scanf("%d", &at);
printf("Enter the Burst time : ");
scanf("%d", &bt);
tt += bt;
addProcess(name, at, bt,i);
AT[i] = at;
BT[i] = bt;
22RT[i] = bt;
id[i] = i;
}
printf("Enter the time quantum : ");
scanf("%d", &quantum);
bubbleSort(n);
i = 0;
int temp_id,start = AT[0],stop = 0;
enqueue(id[0]);
while(i<tt)
{
temp_id = dequeue();
if(RT[temp_id] >= quantum)
{
stop = stop + quantum;
i = i + quantum;
RT[temp_id] = RT[temp_id] - quantum;
}
else if(RT[temp_id] < quantum)
{
stop = stop + RT[temp_id];
i = i + RT[temp_id];
RT[temp_id] = 0;
}
addGantt(temp_id,start,stop);
int j,k;
for(j=start+1;j<=stop;j++)
{
for(k=1;k<n;k++)
{
if(AT[k] == j)
{
enqueue(id[k]);
}
}
}
start = stop;
if(RT[temp_id] != 0)
enqueue(id[temp_id]);
23}
double sumwt = 0.0, sumta = 0.0, sumct = 0.0;
printGantt();
struct process *ptr = P;
printf("\nProcess name\tCT\tTA\tWT\n");
while(ptr != NULL)
{
ptr->ta = ptr->ct - ptr->at;
ptr->wt = ptr->ta - ptr->bt;
sumct += ptr->ct;
sumta += ptr->ta;
sumwt += ptr->wt;
printf("%s
\t%d \t%d \t%d\n",ptr->name,ptr->ct,ptr-
>ta,ptr->wt);
ptr = ptr->next;
}
printf("\nAverage Completion time: %.2f\n", (double)sumct / n);
printf("Average Turn Around Time: %.2f\n", (double)sumta / n);
printf("Average Waiting time: %.2f\n", (double)sumwt / n);
}#include<stdio.h>
struct process
{
int WT,AT,BT,TAT;
};
struct process a[10];
int main()
{
int n,temp[10];
int count=0,t=0,short_P;
float total_WT=0, total_TAT=0,Avg_WT,Avg_TAT;
printf("Enter the number of the process\n");
scanf("%d",&n);
printf("Enter the arrival time and burst time of the
process\n");
for(int i=0;i<n;i++)
{
printf("Enter the arrival time of process[%d]",(i+1));
scanf("%d",&a[i].AT);
printf("Enter the burst time of process[%d]",i+1);
scanf("%d",&a[i].BT);
temp[i]=a[i].BT;
}
a[9].BT=10000;
for(t=0;count!=n;t++)
{
short_P=9;
for(int i=0;i<n;i++)
{
if(a[i].BT<a[short_P].BT && (a[i].AT<=t && a[i].BT>0))
{
short_P=i;
}
}
a[short_P].BT=a[short_P].BT-1;
// if any process is completed if(a[short_P].BT==0)
{
// one process complete count++;
a[short_P].WT=t+1-a[short_P].AT-temp[short_P];
a[short_P].TAT=t+1-a[short_P].AT;
// total calculation total_WT=total_WT+a[short_P].WT;
total_TAT=total_TAT+a[short_P].TAT;
}
}
Avg_WT = total_WT/n;
Avg_TAT = total_TAT/n;
// printing of the answer
printf("\nProcess Waiting Time Turn Around Time \n");
for(int i=0;i<n;i++)
{
printf("%d\t\t%d\t\t%d\n",i+1,a[i].WT,a[i].TAT);
}
printf("Avg waiting time of the process is %f\n",Avg_WT);
printf("Avg turn around time of the process %f\n",Avg_TAT);
}
```
### Input/Output

## Shortest Job First (SJF) - Preemptive

```C
#include<stdio.h>
struct process
{
int WT,AT,BT,TAT;
};
struct process a[10];
int main()
{
int n,temp[10];
int count=0,t=0,short_P;
float total_WT=0, total_TAT=0,Avg_WT,Avg_TAT;
printf("Enter the number of the process\n");
scanf("%d",&n);
printf("Enter the arrival time and burst time of the
process\n");
for(int i=0;i<n;i++)
25{
printf("Enter the arrival time of process[%d]",(i+1));
scanf("%d",&a[i].AT);
printf("Enter the burst time of process[%d]",i+1);
scanf("%d",&a[i].BT);
temp[i]=a[i].BT;
}
a[9].BT=10000;
for(t=0;count!=n;t++)
{
short_P=9;
for(int i=0;i<n;i++)
{
if(a[i].BT<a[short_P].BT && (a[i].AT<=t && a[i].BT>0))
{
short_P=i;
}
}
a[short_P].BT=a[short_P].BT-1;
// if any process is completed if(a[short_P].BT==0)
{
// one process complete count++;
a[short_P].WT=t+1-a[short_P].AT-temp[short_P];
a[short_P].TAT=t+1-a[short_P].AT;
// total calculation total_WT=total_WT+a[short_P].WT;
total_TAT=total_TAT+a[short_P].TAT;
}
}
Avg_WT = total_WT/n;
Avg_TAT = total_TAT/n;
// printing of the answer
printf("\nProcess Waiting Time Turn Around Time \n");
for(int i=0;i<n;i++)
{
printf("%d\t\t%d\t\t%d\n",i+1,a[i].WT,a[i].TAT);
}
printf("Avg waiting time of the process is %f\n",Avg_WT);
printf("Avg turn around time of the process %f\n",Avg_TAT);
}
```

## Shortest Job First - Non-Preemptive

```C
#include<stdio.h>
int main()
{
int bt[20],p[20],wt[20],tat[20],i,j,n,total=0,pos,temp;
float avg_wt,avg_tat;
printf("Enter number of process:");
scanf("%d",&n); printf("\nEnter Burst Time:\n");
for(i=0;i<n;i++)
{
printf("p%d:",i+1);
scanf("%d",&bt[i]); p[i]=i+1;
}
for(i=0;i<n;i++)
{
pos=i;
for(j=i+1;j<n;j++)
{
if(bt[j]<bt[pos])
pos=j;
}
temp=bt[i]; bt[i]=bt[pos]; bt[pos]=temp; temp=p[i];
p[i]=p[pos]; p[pos]=temp;
}
wt[0]=0;
for(i=1;i<n;i++)
{
wt[i]=0;
for(j=0;j<i;j++)
wt[i]+=bt[j];
total+=wt[i];
}
avg_wt=(float)total/n; total=0;
printf("\nProcess\t Burst Time \tWaiting Time\tTurnaround
Time");
for(i=0;i<n;i++)
{
tat[i]=bt[i]+wt[i]; total+=tat[i];
printf("\np%d\t\t
%d\t\t
%d\t\t\t%d",p[i],bt[i],wt[i],tat[i]);
}
avg_tat=(float)total/n;
printf("\n\nAverage Waiting Time=%f",avg_wt);
printf("\nAverage Turnaround Time=%f\n",avg_tat);
}
```

### Input/Output

## First Come First Serve (FCFS)

```C
#include<stdio.h>
29int main()
{
int n,bt[20],wt[20],tat[20],avwt=0,avtat=0,i,j;
printf("Enter total number of processes(maximum 20):");
scanf("%d",&n);
printf("Enter Process Burst Time\n");
for(i=0;i<n;i++)
{
printf("P[%d]:",i+1);
scanf("%d",&bt[i]);
}
wt[0]=0;
for(i=1;i<n;i++)
{
wt[i]=0;
for(j=0;j<i;j++)
wt[i]+=bt[j];
}
printf("\nProces\tBurst Time\tWaiting Time\tTurnaround Time");
for(i=0;i<n;i++)
{
tat[i]=bt[i]+wt[i]; avwt+=wt[i]; avtat+=tat[i];
printf("\nP[%d]\t\t%d\t\t%d\t\t%d",i+1,bt[i],wt[i],tat[i]);
}
avwt/=i;
avtat/=i;
printf("\nnAverage Waiting Time:%d",avwt);
printf("\nAverage Turnaround Time:%d",avtat);
return 0;
}
```

### Input/Output

## Priority Schedulign Algorihm

```C
#include<stdio.h>
struct priority_scheduling
{
char process_name; int burst_time;
int waiting_time;
int turn_around_time; int priority;
};
int main()
{
int number_of_process; int total = 0;
struct priority_scheduling temp_process;
int ASCII_number = 65;
int position;
float average_waiting_time;
float average_turnaround_time;
printf("Enter the total number of Processes: ");
scanf("%d", & number_of_process);
struct priority_scheduling process[number_of_process];
printf("\nPlease Enter the Burst Time and Priority of each
process:\n");
for (int i = 0; i < number_of_process; i++)
{
process[i].process_name = (char) ASCII_number;
printf("\nEnter the details of the process %c \n",
process[i].process_name);
printf("Enter the burst time: ");
scanf("%d", & process[i].burst_time);
printf("Enter the priority: ");
scanf("%d", & process[i].priority); ASCII_number++;
}
for (int i = 0; i < number_of_process; i++)
{
position = I;
for (int j = i + 1; j < number_of_process; j++)
{
if (process[j].priority > process[position].priority)
position = j;
}
temp_process = process[i]; process[i] = process[position];
process[position] = temp_process;
}
process[0].waiting_time = 0;
for (int i = 1; i < number_of_process; i++)
{
process[i].waiting_time = 0;
for (int j = 0; j < i; j++)
{
process[i].waiting_time += process[j].burst_time;
}
total += process[i].waiting_time;
}
average_waiting_time = (float) total / (float)
number_of_process;
total = 0;
printf("\n\nProcess_name \t Burst Time \t Waiting Time \t
Turnaround Time\n"); printf(" \n");
for (int i = 0; i < number_of_process; i++)
{
process[i].turn_around_time = process[i].burst_time +
process[i].waiting_time;
total += process[i].turn_around_time;
printf("\t %c \t\t %d \t\t %d \t\t %d",
process[i].process_name, process[i].burst_time,
process[i].waiting_time, process[i].turn_around_time);
printf("\n \n");
}
average_turnaround_time = (float) total / (float)
number_of_process;
printf("\n\n Average Waiting Time : %f", average_waiting_time);
printf("\n Average Turnaround Time: %f\n",
average_turnaround_time);
return 0;
}
```
### Input/Output



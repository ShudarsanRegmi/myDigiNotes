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

# CPU Scheduling Algorithms

## Task-1: Round Robbin Algorithm

```c

#include<stdio.h>
#define max 20 // maximum size for array
main()
{
    int i,burstTime[max],remainTime[max],remainProcess,arrivalTime[max],totalExecutionTime=0,timeQuantum,flag=0,n;
    float totalWaitingTime=0;
    printf("Enter the Number of Process(max 20) : ");
    scanf("%d",&n); // n is the number of Process
    remainProcess=n;

    printf("Enter Arrival Time\n");
    for(i=0;i<n;i++){
        printf("For P[%d]: ",i+1);
        scanf("%d",&arrivalTime[i]);
    }

    printf("\nEnter Burst Time\n");
    for(i=0;i<n;i++){
        printf("For P[%d]: ",i+1);
        scanf("%d",&burstTime[i]);
        remainTime[i]=burstTime[i]; // initially assume remain time for any process is equal to it's burst time !
    }

    printf("\nEnter Time Quantum :");
    scanf("%d",&timeQuantum);

    printf("\n");
    for(i=0;remainProcess!=0;){
        /**
            * this below condition check the remain time for any process is less than or equal with the time quantum
            * or not and also check the remain time is greater than 0 or not. if both condition are true that means
            * the process can execute fully at one time.
        */
        if(remainTime[i]<=timeQuantum && remainTime[i]>0){
            totalExecutionTime+=remainTime[i];
            remainTime[i]=0;
            flag=1;
        }

        else if(remainTime[i]>0){
            remainTime[i]-=timeQuantum;
            totalExecutionTime+=timeQuantum;
        }

        if(flag==1 && remainTime[i]==0){
            printf("P[%d] | waiting Time : %d\n",i+1,totalExecutionTime-arrivalTime[i]-burstTime[i]);
            totalWaitingTime+=totalExecutionTime-arrivalTime[i]-burstTime[i];
            flag=0;
            remainProcess--;
        }

        if(i==n-1)
            i=0;
        else if(arrivalTime[i+1]<=totalExecutionTime){
            i++;
        }
        else
            i=0;
    }

    totalWaitingTime=(float)totalWaitingTime/n;
    printf("\nThe Average Waiting Time : %.2f \n",totalWaitingTime);

}

```

## Output

```
C:\Users\Shudarsan\CLionProjects\DSA\cmake-build-debug\DSA.exe
Enter the no. of processes :3
Enter the quantum
2
Enter the process numbers
1
2
3
Enter the Arrival time of processes
0
0
0
Enter the Burst time of processes
6
8
10
Process number Arrival time Burst time  Start time                      Final time      Wait Time       TurnAround Time

1               0               6       0 6 12                                14                8               14
2               0               8       2 8 14 18                             20                12              20
3               0               10      4 10 16 20 22                          24               14              24
The average wait time is : 11.333333
The average TurnAround time is : 19.333334

```

## Task - 2: Shortest Job First(SJF)

```c
#include <stdio.h>

struct process {
    int WT, AT, BT, TAT;
};

struct process a[10];

int main() {
    int n, temp[10];
    int count = 0, t = 0, short_P;
    float total_WT = 0, total_TAT = 0, Avg_WT, Avg_TAT;

    printf("Enter the number of processes: ");
    scanf("%d", &n);

    printf("Enter the arrival time and burst time of the processes:\n");
    for (int i = 0; i < n; i++) {
        printf("Enter the arrival time of process p[%d]: ", (i + 1));
        scanf("%d", &a[i].AT);

        printf("Enter the burst time of process p[%d]: ", (i + 1));
        scanf("%d", &a[i].BT);

        temp[i] = a[i].BT;
    }

    a[9].BT = 10000;  // Initialize a very high burst time for comparison

    for (t = 0; count != n; t++) {
        short_P = 9;

        for (int i = 0; i < n; i++) {
            if (a[i].BT < a[short_P].BT && (a[i].AT <= t && a[i].BT > 0)) {
                short_P = i;
            }
        }

        a[short_P].BT -= 1;

        // If any process is completed
        if (a[short_P].BT == 0) {
            count++;
            a[short_P].WT = t + 1 - a[short_P].AT - temp[short_P];
            a[short_P].TAT = t + 1 - a[short_P].AT;

            total_WT += a[short_P].WT;
            total_TAT += a[short_P].TAT;
        }
    }

    Avg_WT = total_WT / n;
    Avg_TAT = total_TAT / n;

    // Printing the results
    printf("\nProcess\t\tWaiting Time\tTurn Around Time\n");
    for (int i = 0; i < n; i++) {
        printf("%d\t\t%d\t\t%d\n", i + 1, a[i].WT, a[i].TAT);
    }

    printf("Average waiting time of the processes: %.2f\n", Avg_WT);
    printf("Average turn around time of the processes: %.2f\n", Avg_TAT);

    return 0;
}

```

## Output

```
C:\Users\Shudarsan\CLionProjects\DSA\cmake-build-debug\DSA.exe
Enter the number of processes:3
Enter the arrival time and burst time of the processes:
Enter the arrival time of process p[1]: 0
Enter the burst time of process p[1]: 16
Enter the arrival time of process p[2]: 2
Enter the burst time of process p[2]: 18
Enter the arrival time of process p[3]: 5
Enter the burst time of process p[3]: 10

Process         Waiting Time    Turn Around Time
1               10              26
2               24              42
3               0               10
Average waiting time of the processes: 11.33
Average turn around time of the processes: 26.00
```

## Task-3: Doing Shorteste Job First(SJF) - (Non-Preemptive)

```c
#include <stdio.h>

int main() {
    int bt[20], p[20], wt[20], tat[20], i, j, n, total = 0, pos, temp;
    float avg_wt, avg_tat;

    printf("Enter number of processes: ");
    scanf("%d", &n);

    printf("\nEnter Burst Time:\n");
    for (i = 0; i < n; i++) {
        printf("p%d: ", i + 1);
        scanf("%d", &bt[i]);
        p[i] = i + 1;  // Process number
    }

    // Sorting burst time in ascending order using selection sort
    for (i = 0; i < n; i++) {
        pos = i;
        for (j = i + 1; j < n; j++) {
            if (bt[j] < bt[pos]) {
                pos = j;
            }
        }

        temp = bt[i];
        bt[i] = bt[pos];
        bt[pos] = temp;

        temp = p[i];
        p[i] = p[pos];
        p[pos] = temp;
    }

    wt[0] = 0;  // Waiting time for first process is 0

    // Calculating waiting time
    for (i = 1; i < n; i++) {
        wt[i] = 0;
        for (j = 0; j < i; j++) {
            wt[i] += bt[j];
        }
        total += wt[i];
    }

    avg_wt = (float)total / n;
    total = 0;

    printf("\nProcess\t Burst Time \tWaiting Time\tTurnaround Time");
    for (i = 0; i < n; i++) {
        tat[i] = bt[i] + wt[i];  // Calculating turnaround time
        total += tat[i];
        printf("\np%d\t\t%d\t\t %d\t\t\t%d", p[i], bt[i], wt[i], tat[i]);
    }

    avg_tat = (float)total / n;

    printf("\n\nAverage Waiting Time = %f", avg_wt);
    printf("\nAverage Turnaround Time = %f\n", avg_tat);

    return 0;
}

```

## Output

```
C:\Users\Shudarsan\CLionProjects\DSA\cmake-build-debug\DSA.exe
Enter number of processes:3

Enter Burst Time:
p1: 16
p2: 18
p3: 10

Process  Burst Time     Waiting Time    Turnaround Time
p3              10               0                      10
p1              16               10                     26
p2              18               26                     44

Average Waiting Time = 12.000000
Average Turnaround Time = 26.666666
```

## Task - 4: Shortest Job First (Preemptive)

```c
#include <stdio.h>

int main()
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

## Output

```
C:\Users\Shudarsan\CLionProjects\DSA\cmake-build-debug\DSA.exe
Enter total number of processes(maximum 20):3
Enter Process Burst Time
P[1]:12
P[2]:18
P[3]:6

Proces  Burst Time      Waiting Time    Turnaround Time
P[1]            12              0               12
P[2]            18              12              30
P[3]            6               30              36
nAverage Waiting Time:14
Average Turnaround Time:26
```


# Task - 4: Priority Scheduling Algorithm

```cpp
#include <stdio.h>

struct priority_scheduling {
    char process_name;
    int burst_time;
    int waiting_time;
    int turn_around_time;
    int priority;
};

int main() {
    int number_of_process;
    int total = 0;
    struct priority_scheduling temp_process;
    int ASCII_number = 65; // ASCII value for 'A'
    int position;
    float average_waiting_time;
    float average_turnaround_time;

    printf("Enter the total number of processes: ");
    scanf("%d", &number_of_process);

    struct priority_scheduling process[number_of_process];

    printf("\nPlease enter the burst time and priority of each process:\n");
    for (int i = 0; i < number_of_process; i++) {
        process[i].process_name = (char) ASCII_number;
        printf("\nEnter the details of process %c\n", process[i].process_name);
        printf("Enter the burst time: ");
        scanf("%d", &process[i].burst_time);
        printf("Enter the priority: ");
        scanf("%d", &process[i].priority);
        ASCII_number++;
    }

    // Sorting processes by priority (higher number = higher priority)
    for (int i = 0; i < number_of_process; i++) {
        position = i;
        for (int j = i + 1; j < number_of_process; j++) {
            if (process[j].priority > process[position].priority) {
                position = j;
            }
        }

        // Swapping the process with the highest priority
        temp_process = process[i];
        process[i] = process[position];
        process[position] = temp_process;
    }

    // Calculating waiting time for each process
    process[0].waiting_time = 0; // Waiting time for the first process is 0
    for (int i = 1; i < number_of_process; i++) {
        process[i].waiting_time = 0;
        for (int j = 0; j < i; j++) {
            process[i].waiting_time += process[j].burst_time;
        }
        total += process[i].waiting_time;
    }

    average_waiting_time = (float)total / (float)number_of_process;
    total = 0;

    printf("\n\nProcess Name\tBurst Time\tWaiting Time\tTurnaround Time\n");
    printf("------------------------------------------------------------\n");
    for (int i = 0; i < number_of_process; i++) {
        process[i].turn_around_time = process[i].burst_time + process[i].waiting_time;
        total += process[i].turn_around_time;
        printf("%c\t\t%d\t\t%d\t\t%d\n",
                process[i].process_name,
                process[i].burst_time,
                process[i].waiting_time,
                process[i].turn_around_time);
    }

    average_turnaround_time = (float)total / (float)number_of_process;

    printf("\n\nAverage Waiting Time: %f", average_waiting_time);
    printf("\nAverage Turnaround Time: %f\n", average_turnaround_time);

    return 0;
}


```

## Output

```
Enter the total number of processes:3

Please enter the burst time and priority of each process:

Enter the details of process A
Enter the burst time:3
 Enter the priority:3

Enter the details of process B
Enter the burst time:14
 Enter the priority:1

Enter the details of process C
Enter the burst time:2
 Enter the priority:2


Process Name    Burst Time      Waiting Time    Turnaround Time
------------------------------------------------------------
A               3               0               3
C               2               3               5
B               14              5               19


Average Waiting Time: 2.666667
Average Turnaround Time: 9.000000
```


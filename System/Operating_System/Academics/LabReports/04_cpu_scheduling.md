# CPU Scheduling Algorithms

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

# Output
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


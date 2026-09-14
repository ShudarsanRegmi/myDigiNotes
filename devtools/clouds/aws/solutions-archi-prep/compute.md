<img width="1024" height="1536" alt="image" src="https://github.com/user-attachments/assets/ca842cad-7e50-4172-bd98-ffe9bc119c5b" />


# Part II: Compute

For Compute, build this hierarchy in your head:

```text
Compute
│
├── EC2                 → Virtual machines
│   └── Auto Scaling    → Automatically adjust EC2 capacity
│
├── Elastic Load Balancing
│   ├── ALB             → HTTP/HTTPS, Layer 7
│   ├── NLB             → TCP/UDP, Layer 4
│   └── GWLB            → Network/security appliances
│
├── Lambda              → Serverless functions
│
├── Containers
│   ├── ECS             → AWS container orchestration
│   ├── Fargate         → Serverless container compute
│   └── EKS             → Managed Kubernetes
│
└── Elastic Beanstalk   → Managed application platform
```

---

# 1. EC2

## What is it?

**Amazon EC2 = virtual servers in AWS.**

You choose:

* CPU
* Memory
* Storage
* Networking
* Operating system
* Instance type
* Pricing model

Think:

> **"I need control over a server." → EC2**

---

## EC2 Instance Types

Don't memorize every instance family. Understand the categories.

| Type                  | Optimized for                   |
| --------------------- | ------------------------------- |
| General purpose       | Balanced CPU + memory           |
| Compute optimized     | High CPU                        |
| Memory optimized      | Large memory                    |
| Storage optimized     | High local storage I/O          |
| Accelerated computing | GPU / ML / specialized hardware |

### Exam keywords

**CPU-heavy workload** → Compute optimized

**Large in-memory database** → Memory optimized

**High sequential/random local storage I/O** → Storage optimized

**GPU / ML / graphics** → Accelerated computing

---

# 2. AMI

**AMI = Amazon Machine Image**

Contains the information required to launch an EC2 instance.

Think:

> **AMI = blueprint/image for an EC2 server**

Can contain:

* OS
* Applications
* Configuration
* Software

### Exam pattern

If you need:

> "Launch many identical EC2 instances with the same configuration"

Think:

**AMI + Launch Template + Auto Scaling**

---

# 3. EC2 Instance Store

Temporary, physically attached storage.

### Important

* Very fast
* Ephemeral
* Data is lost when instance is stopped/terminated depending on lifecycle
* Not suitable for persistent data

Use for:

* Cache
* Temporary files
* Scratch data

Don't use it for:

> Critical persistent database data

---

# 4. EBS with EC2

**EBS = persistent block storage.**

Compared with Instance Store:

|                  | EBS             | Instance Store            |
| ---------------- | --------------- | ------------------------- |
| Persistent       | Yes             | No                        |
| Network-attached | Yes             | Physically attached       |
| Snapshot         | Yes             | No                        |
| Use              | Persistent data | Temporary/high-speed data |

### Exam shortcut

**Persistent EC2 storage → EBS**

**Temporary local storage → Instance Store**

---

# 5. EC2 User Data

Allows scripts to run when an instance launches.

Useful for:

* Installing packages
* Configuring applications
* Starting services
* Bootstrapping servers

Example concept:

```text
Launch EC2
   ↓
User Data
   ↓
Install/configure application
   ↓
Start application
```

---

# 6. EC2 Metadata

Provides information about the running instance.

Examples:

* Instance ID
* Private IP
* IAM role credentials
* Availability Zone
* Instance type

Accessed from the instance through the metadata service.

### Exam keyword

> "Application needs to retrieve instance information"

→ **Instance Metadata Service**

---

# 7. Security Groups

For EC2:

> **Security Group = stateful virtual firewall**

Remember:

* Allow rules
* No explicit deny
* Stateful
* Attached to ENI

Very common architecture:

```text
Internet
   ↓
ALB SG
   ↓
EC2 SG
   ↓
Database SG
```

Each layer only accepts traffic from the layer before it.

---

# 8. EC2 Pricing Models

### On-Demand

* Pay as you go
* No commitment
* Most flexible
* Usually most expensive for sustained workloads

Use when:

> Workload is unpredictable or short-term.

---

### Reserved Instances

Commit to instance configuration for a period.

Good for:

> Predictable, steady-state EC2 workloads.

---

### Savings Plans

Commit to a certain amount of compute spending.

More flexible than traditional Reserved Instances.

Think:

> **Long-term predictable compute usage + flexibility → Savings Plans**

---

### Spot Instances

Uses spare AWS capacity.

Can be interrupted.

Very cheap.

Good for:

* Batch jobs
* Data processing
* Fault-tolerant workloads
* Stateless workers

Bad for:

> Workloads that cannot tolerate interruption.

### Exam trigger

**"Lowest cost + can tolerate interruption" → Spot**

---

# 9. Dedicated Hosts vs Dedicated Instances

### Dedicated Host

Physical server dedicated to your use.

Useful for:

* Licensing requirements
* Compliance
* Specific server-placement requirements

### Dedicated Instance

Instance runs on hardware dedicated to your AWS account, but you don't get the same host-level control.

Exam questions usually emphasize:

> **Existing software license tied to physical sockets/cores**

→ **Dedicated Host**

---

# 10. Placement Groups

Three important types.

### Cluster

Instances physically close together.

Goal:

> **Very high network performance + low latency**

Think:

**HPC**

---

### Spread

Instances placed on distinct underlying hardware.

Goal:

> **Reduce correlated hardware failure**

Good for:

* Critical instances
* Small number of instances

---

### Partition

Instances distributed across logical partitions.

Useful for:

* Large distributed systems
* Hadoop
* Cassandra
* Kafka

### Memorize

```text
Cluster   → Performance
Spread    → Failure isolation
Partition → Distributed workloads
```

---

# 11. EC2 Auto Scaling

Auto Scaling means:

> Automatically maintain the appropriate number of EC2 instances.

Important parameters:

* Minimum capacity
* Desired capacity
* Maximum capacity

Example:

```text
Min = 2
Desired = 4
Max = 10
```

Normally:

```text
Traffic increases
      ↓
Instances increase
```

```text
Traffic decreases
      ↓
Instances decrease
```

---

# 12. Auto Scaling Policies

### Target Tracking

Maintain a target metric.

Example:

> Keep average CPU around 50%.

Usually the easiest answer when the question says:

> "Automatically maintain a target utilization."

---

### Step Scaling

Scale based on alarm thresholds.

Example:

```text
CPU > 70% → +2 instances
CPU > 85% → +4 instances
```

---

### Scheduled Scaling

Known traffic patterns.

Example:

> Every weekday at 9 AM, increase capacity.

---

### Predictive Scaling

Uses historical patterns to forecast future demand.

---

# 13. Auto Scaling Health Checks

Auto Scaling can detect unhealthy instances and replace them.

Typical architecture:

```text
ALB
 ↓
Target Group
 ↓
Auto Scaling Group
 ↓
EC2
```

If EC2 becomes unhealthy:

```text
Unhealthy EC2
      ↓
ASG terminates/replaces it
      ↓
Healthy EC2
```

This is **self-healing architecture**.

---

# 14. Elastic Load Balancing

ELB distributes traffic across targets.

Main ones you need:

```text
ALB → Layer 7
NLB → Layer 4
GWLB → Network appliances
```

---

# 15. Application Load Balancer

**ALB = Layer 7 load balancer**

Best for:

* HTTP
* HTTPS
* Web applications
* REST APIs
* Microservices

Supports intelligent routing.

### Path-based routing

```text
example.com/images/*
       ↓
Image service
```

```text
example.com/api/*
       ↓
API service
```

### Host-based routing

```text
api.example.com
       ↓
API servers
```

```text
www.example.com
       ↓
Web servers
```

### Exam trigger

> "Route requests based on URL path/hostname"

→ **ALB**

---

# 16. Network Load Balancer

**NLB = Layer 4**

Supports:

* TCP
* UDP
* TLS

Characteristics:

* Very high performance
* Very low latency
* Static IP addresses
* Good for non-HTTP workloads

### Exam trigger

> "TCP/UDP"

> "Static IP"

> "Ultra-high-performance network traffic"

→ **NLB**

---

# 17. Gateway Load Balancer

**GWLB = load balancing for network/security appliances.**

Think:

```text
Traffic
   ↓
GWLB
   ↓
Firewall / IDS / IPS / inspection appliance
```

Exam keyword:

> "Deploy third-party virtual network appliances"

→ **GWLB**

---

# 18. ALB vs NLB

| Requirement         | Answer |
| ------------------- | ------ |
| HTTP/HTTPS          | ALB    |
| URL path routing    | ALB    |
| Host-based routing  | ALB    |
| Microservices       | ALB    |
| TCP                 | NLB    |
| UDP                 | NLB    |
| Static IP           | NLB    |
| Extreme performance | NLB    |
| Security appliance  | GWLB   |

---

# 19. Lambda

**AWS Lambda = serverless, event-driven compute.**

You provide:

* Code
* Runtime
* Memory
* Timeout
* IAM execution role

AWS handles:

* Servers
* OS
* Infrastructure
* Scaling

Think:

> **"Run code without managing servers." → Lambda**

---

# 20. Lambda Invocation

Two broad patterns.

### Synchronous

Caller waits for response.

```text
Client
 ↓
API Gateway
 ↓
Lambda
 ↓
Response
```

Common for:

* APIs
* Web requests

---

### Asynchronous

Event is submitted and Lambda processes it later.

Common sources:

* S3
* EventBridge
* SNS

Think:

> **"Event happens, Lambda reacts."**

---

# 21. Lambda + SQS

Very important architecture.

```text
Producer
   ↓
SQS
   ↓
Lambda
   ↓
Processing
```

Why?

* Decoupling
* Buffering
* Retry
* Handling traffic spikes
* Lambda automatically polls SQS

### Exam pattern

> "Application experiences bursts of traffic and processing can happen asynchronously."

→ **SQS + Lambda**

---

# 22. Lambda Concurrency

Concurrency = number of Lambda executions running simultaneously.

### Reserved concurrency

Reserves capacity for a function.

Can also act as a limit.

Useful to:

> Prevent one function from consuming all account concurrency.

### Provisioned concurrency

Keeps execution environments initialized.

Purpose:

> **Reduce cold-start latency**

### Memorize

**Reserved → capacity limit/protection**

**Provisioned → reduce cold starts**

---

# 23. Lambda Cold Start

When Lambda needs to initialize a new execution environment, there can be additional latency.

Important for:

* Latency-sensitive APIs
* Large runtimes
* Frequently scaled workloads

Solution:

> **Provisioned Concurrency**

---

# 24. Lambda Limits

Know conceptually:

* Maximum execution duration is limited
* Memory is configurable
* Stateless execution model
* Temporary filesystem available
* Not suitable for long-running processes

### Exam trigger

> "Long-running workload"

Don't immediately choose Lambda.

Consider:

**EC2 / ECS / Fargate**

depending on the workload.

---

# 25. Containers

Three names:

```text
ECS       → Container orchestration
Fargate   → Serverless container compute
EKS       → Managed Kubernetes
```

---

# 26. ECS

**ECS = AWS container orchestration service.**

Important concepts:

```text
Cluster
  ↓
Service
  ↓
Task
```

### Task Definition

Blueprint describing:

* Container image
* CPU
* Memory
* Networking
* Environment
* IAM roles
* Ports

### Task

Running instance of a task definition.

### Service

Maintains desired number of tasks.

---

# 27. ECS EC2 vs Fargate

### ECS on EC2

You manage:

* EC2 instances
* Instance scaling
* Underlying infrastructure

AWS manages:

* ECS control plane

### ECS Fargate

AWS manages:

* Servers
* Infrastructure
* Capacity

You manage:

* Containers
* Task definitions
* Application

### Shortcut

> **Want containers without managing servers → Fargate**

---

# 28. EKS

**EKS = managed Kubernetes.**

Choose it when:

* Organization already uses Kubernetes
* Need Kubernetes ecosystem
* Kubernetes portability is important

Don't choose EKS merely because:

> "We need containers."

For a straightforward AWS container workload, **ECS/Fargate** may be simpler.

---

# 29. Elastic Beanstalk

Beanstalk is:

> **Managed application deployment platform.**

You provide application code.

AWS handles much of:

* EC2
* Load balancing
* Auto Scaling
* Deployment environment

Useful when:

> Developers want to deploy an application without manually designing all infrastructure.

### Important

Beanstalk is **not serverless**.

Underneath, it can use EC2, load balancers, Auto Scaling, etc.

---

# 30. Compute Decision Tree

This is probably the **most valuable part to memorize**.

### "I need a virtual machine."

→ **EC2**

### "I need virtual machines but automatically scale them."

→ **EC2 + Auto Scaling**

### "I need HTTP/HTTPS intelligent routing."

→ **ALB**

### "I need TCP/UDP or static IP."

→ **NLB**

### "I need to run code without managing servers."

→ **Lambda**

### "I need containers without managing servers."

→ **Fargate**

### "I need AWS-native container orchestration."

→ **ECS**

### "I specifically need Kubernetes."

→ **EKS**

### "I need easy application deployment without managing infrastructure manually."

→ **Elastic Beanstalk**

### "I need a network/security appliance architecture."

→ **GWLB**

---

# 31. High-Yield Architecture Patterns

### Traditional scalable web application

```text
                    Internet
                       ↓
                      ALB
                       ↓
              Auto Scaling Group
                 ↙    ↓    ↘
               EC2  EC2  EC2
                       ↓
                      RDS
```

**Key ideas:**

* ALB distributes traffic
* ASG provides horizontal scaling
* Multi-AZ provides availability
* RDS provides managed database

---

### Serverless API

```text
Client
  ↓
API Gateway
  ↓
Lambda
  ↓
DynamoDB
```

Think:

> **Fully serverless application**

---

### Event-driven processing

```text
S3
 ↓
EventBridge / SNS
 ↓
Lambda
 ↓
Processing
```

---

### Buffered workload

```text
Application
     ↓
    SQS
     ↓
Workers
```

If worker capacity is variable:

```text
SQS
 ↓
Lambda
```

or:

```text
SQS
 ↓
EC2 Auto Scaling
```

---

# 32. Compute Exam Traps

Memorize these.

1. **EC2 = control over virtual servers**
2. **Lambda = serverless functions**
3. **Fargate = serverless container compute**
4. **ECS ≠ Fargate**

   * ECS is orchestration
   * Fargate is compute engine
5. **EKS = Kubernetes**
6. **ALB = Layer 7**
7. **NLB = Layer 4**
8. **GWLB = network/security appliances**
9. **Target tracking = maintain target metric**
10. **Scheduled scaling = predictable traffic**
11. **Spot = cheap but interruptible**
12. **Savings Plans = committed compute spending with flexibility**
13. **Reserved Instances = predictable EC2 usage**
14. **Provisioned Lambda concurrency = reduce cold starts**
15. **Reserved Lambda concurrency = limit/reserve concurrency**
16. **Instance Store = ephemeral**
17. **EBS = persistent block storage**
18. **AMI = instance blueprint**
19. **User Data = bootstrapping script**
20. **Placement Group Cluster = performance**
21. **Placement Group Spread = failure isolation**
22. **Placement Group Partition = distributed systems**
23. **ASG can replace unhealthy instances**
24. **ALB supports path/host-based routing**
25. **NLB supports static IP addresses**

---

# The 60-second Compute Memory Map

```text
                    COMPUTE
                       |
        +--------------+--------------+
        |              |              |
       EC2           Lambda        Containers
        |              |              |
    Auto Scaling       |        +-----+-----+
        |              |        |           |
       ALB          API/Event   ECS         EKS
        |              |        |
       EC2          DynamoDB   Fargate
        |
    Pricing
    ├─ On-Demand
    ├─ Reserved
    ├─ Savings Plans
    └─ Spot

LOAD BALANCING
├─ ALB → HTTP/HTTPS → Layer 7
├─ NLB → TCP/UDP → Layer 4 → Static IP
└─ GWLB → Security/network appliances

EC2 STORAGE
├─ EBS → Persistent
└─ Instance Store → Ephemeral

PLACEMENT GROUPS
├─ Cluster   → Performance
├─ Spread    → Failure isolation
└─ Partition → Distributed systems

LAMBDA
├─ Reserved concurrency → Limit/protect
└─ Provisioned concurrency → Reduce cold starts
```

**For your last-day prep, the highest priority here is:**
**EC2 + ASG + ALB/NLB + Lambda + ECS/Fargate + Spot/Savings Plans + placement groups + Lambda concurrency.**

Next logical section is **Storage: S3, EBS, EFS, FSx, Storage Gateway, and Snow Family**, with the same high-yield treatment.

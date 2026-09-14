<img width="1223" height="1286" alt="image" src="https://github.com/user-attachments/assets/7894fcef-3e2e-4bcc-809a-b4d8a9ffed84" />



# Part VI: Cost Optimization

For SAA, cost questions are rarely about memorizing prices. They are about recognizing:

> **“What is the cheapest architecture that still satisfies the requirements?”**

The core mental model:

```text
                    COST OPTIMIZATION
                           |
       +-------------------+-------------------+
       |                   |                   |
   Compute              Storage             Network
       |                   |                   |
 Spot / RI / SP       S3 classes         Data transfer
 Auto Scaling         Lifecycle           NAT / Endpoints
 Right-sizing         Glacier             CloudFront
       |
   Serverless
```

---

# 1. The Four Core Cost Principles

### 1. Right-size

Don't use a larger resource than necessary.

Example:

```text
Current: m7i.4xlarge
Actual workload: low CPU/memory
             ↓
       Smaller instance
             ↓
          Lower cost
```

Exam keyword:

> **"Over-provisioned" → Right-size**

---

### 2. Elasticity

Scale resources according to demand.

```text
Traffic ↑ → Capacity ↑
Traffic ↓ → Capacity ↓
```

Use:

* EC2 Auto Scaling
* Lambda
* Fargate
* DynamoDB On-Demand
* S3

### Exam idea

> Don't pay for capacity you aren't using.

---

### 3. Choose the correct pricing model

```text
Unpredictable / short-term → On-Demand
Predictable EC2             → Reserved Instances
Predictable compute spend   → Savings Plans
Interruptible workload      → Spot
```

---

### 4. Choose the right storage class

Frequently accessed:

→ **S3 Standard**

Infrequent:

→ **S3 Standard-IA**

Unknown/changing access:

→ **S3 Intelligent-Tiering**

Long-term archive:

→ **S3 Glacier**

---

# 2. On-Demand

### Characteristics

* No long-term commitment
* Pay for usage
* Maximum flexibility
* Generally more expensive than committed pricing

Use when:

* Workload is unpredictable
* Short-term
* Cannot commit to usage

### Exam trigger

> "Short-term workload with unpredictable demand."

→ **On-Demand**

---

# 3. Reserved Instances

Best for:

> **Predictable, steady-state EC2 workloads**

You commit to a term in exchange for discounted pricing.

Examples:

* Production database
* Always-running application server
* Stable backend workload

### Exam trigger

> "EC2 runs continuously for several years."

→ **Reserved Instances**

---

# 4. Savings Plans

Commit to a certain amount of **compute usage/spend**.

More flexible than traditional Reserved Instances.

Can apply to:

* EC2
* Lambda
* Fargate

### Shortcut

> **Predictable compute + flexibility → Savings Plans**

---

# 5. Spot Instances

Uses spare AWS capacity.

Huge cost savings are possible, but:

> **AWS can interrupt the instance.**

Best for:

* Batch processing
* Big data processing
* Distributed workloads
* Stateless workers
* Fault-tolerant workloads

Bad for:

* Critical workloads that cannot tolerate interruption
* Long-running stateful workloads without interruption handling

### Exam trigger

> "Lowest cost and workload can tolerate interruption."

→ **Spot**

---

# 6. Pricing Model Cheat Sheet

| Requirement                                | Choose            |
| ------------------------------------------ | ----------------- |
| Short/unpredictable                        | On-Demand         |
| Long-term predictable EC2                  | Reserved Instance |
| Long-term compute commitment + flexibility | Savings Plan      |
| Cheapest + interruptible                   | Spot              |

---

# 7. Auto Scaling = Cost Optimization

Auto Scaling isn't only about availability.

It also reduces cost.

Example:

```text
Daytime
10 EC2
   ↓
Night
2 EC2
```

Instead of:

```text
24 hours
10 EC2
```

### Exam trigger

> "Workload varies significantly throughout the day."

→ **Auto Scaling**

---

# 8. Serverless = Pay for Usage

Lambda:

> Pay based on execution rather than continuously running a server.

Compare:

```text
EC2
→ Pay while instance is running

Lambda
→ Pay for function execution
```

For highly intermittent workloads:

> Lambda can be more cost-efficient.

### Exam trap

Don't blindly choose Lambda for every workload.

If the workload is:

* Long-running
* Constantly running
* Requires specialized OS/server control

EC2/containers may be more appropriate.

---

# 9. S3 Cost Optimization

S3 provides multiple storage classes.

Think:

```text
Frequent
   ↓
S3 Standard

Unknown access
   ↓
Intelligent-Tiering

Infrequent
   ↓
Standard-IA

Archive
   ↓
Glacier
```

---

# 10. S3 Lifecycle

Automatically transition objects.

Example:

```text
Day 0
S3 Standard
   ↓
Day 30
Standard-IA
   ↓
Day 90
Glacier
   ↓
Day 365
Delete
```

Exam question:

> "Automatically move old objects to cheaper storage."

→ **Lifecycle Policy**

---

# 11. Intelligent-Tiering

Best when:

> **Access patterns are unknown or change over time.**

AWS automatically moves objects between access tiers.

### Exam distinction

**Known infrequent access**

→ Standard-IA

**Unknown/changing access**

→ Intelligent-Tiering

---

# 12. Glacier

Use for:

> **Archival data that doesn't need frequent access.**

The Glacier family gives different retrieval characteristics.

Think:

```text
Need instant archive access
→ Glacier Instant Retrieval

Minutes/hours acceptable
→ Glacier Flexible Retrieval

Very long-term archive
→ Glacier Deep Archive
```

### Exam keyword

> "Compliance archive retained for years."

→ **Glacier Deep Archive**

---

# 13. Delete Unnecessary Data

A surprisingly common cost-optimization principle.

Use:

* S3 Lifecycle expiration
* DynamoDB TTL
* Log retention policies
* Snapshot lifecycle
* Automated cleanup

Example:

```text
Temporary logs
     ↓
Retention policy
     ↓
Automatic deletion
     ↓
Lower storage cost
```

---

# 14. EBS Cost Optimization

Avoid unnecessarily expensive volumes.

Think:

```text
General workload
→ gp3

Extreme IOPS requirement
→ io2
```

Don't use io2 simply because:

> "It's faster."

Use it when the workload **actually requires high IOPS**.

Also consider:

* Delete unused EBS volumes
* Delete unnecessary snapshots
* Right-size volumes
* Use appropriate volume type

---

# 15. EC2 Right-Sizing

Monitor actual utilization.

If:

```text
CPU: 10%
Memory: 20%
```

but you're running a huge instance:

→ **Over-provisioned**

Potential solution:

> Smaller instance type.

Use monitoring data such as CloudWatch metrics and recommendations from Compute Optimizer.

---

# 16. NAT Gateway Cost Trap

This appears in architecture questions.

Architecture:

```text
Private EC2
    ↓
NAT Gateway
    ↓
S3
```

If the only purpose is accessing S3:

> Consider **S3 Gateway Endpoint** instead.

Architecture:

```text
Private EC2
    ↓
S3 Gateway Endpoint
    ↓
S3
```

This can avoid unnecessary NAT processing charges and keeps traffic private.

### Exam trigger

> "Reduce NAT Gateway costs for S3 traffic."

→ **S3 Gateway Endpoint**

---

# 17. CloudFront and Cost

CloudFront can reduce:

* Origin load
* Repeated data transfer from origin
* Latency

Architecture:

```text
Users
  ↓
CloudFront
  ↓
Origin
```

If many users request the same content:

```text
Without CDN:
1000 requests → Origin

With CDN:
1000 requests
     ↓
CloudFront cache
     ↓
Origin receives fewer requests
```

---

# 18. Data Transfer Costs

A major architectural consideration.

Be aware of:

* Internet data transfer
* Inter-AZ transfer
* Inter-Region transfer
* NAT Gateway processing
* Cross-Region replication

### Exam thinking

If two components communicate heavily:

> Consider where they're deployed.

For example, excessive cross-AZ traffic can introduce additional costs.

Don't sacrifice required availability merely to save small amounts of data-transfer cost, though.

---

# 19. Cost Explorer

**Cost Explorer = analyze spending.**

Useful for:

* Viewing AWS costs
* Identifying spending trends
* Filtering usage
* Finding cost drivers

Think:

> **"Where is my AWS money going?"**

→ **Cost Explorer**

---

# 20. AWS Budgets

**Budgets = set spending/usage thresholds and receive alerts.**

Example:

```text
Monthly budget = $500
       ↓
80% reached
       ↓
Alert
```

### Exam trigger

> "Notify the team when spending exceeds a threshold."

→ **AWS Budgets**

---

# 21. Cost and Usage Report

**CUR = detailed AWS cost and usage data.**

Useful when:

> You need granular billing/usage analysis.

Think:

**Cost Explorer → interactive analysis**

**Cost & Usage Report → detailed billing dataset**

---

# 22. Consolidated Billing

AWS Organizations can consolidate billing across accounts.

Benefits:

* Centralized billing
* Combined usage
* Potential volume pricing benefits
* Central cost management

Architecture:

```text
Management Account
       |
 +-----+-----+-----+
 ↓           ↓     ↓
Account A  Account B  Account C
       |
 Consolidated Billing
```

---

# 23. Cost Allocation Tags

Tags can help attribute costs.

Example:

```text
Environment = Production
Department  = Finance
Project     = X
```

Then analyze spending by those dimensions.

### Exam trigger

> "Need to determine costs by department/project."

→ **Cost allocation tags**

---

# 24. Trusted Advisor

Can provide cost optimization recommendations.

Examples:

* Idle resources
* Underutilized resources
* Potential savings

Think:

> **"AWS, tell me where I can save money."**

→ **Trusted Advisor**

---

# 25. Famous Cost-Optimization Architecture Patterns

## Pattern 1: Variable EC2 workload

```text
CloudWatch
    ↓
Auto Scaling
    ↓
EC2
```

**Cost principle:** only run the capacity you need.

---

## Pattern 2: Interruptible batch processing

```text
SQS
 ↓
EC2 Auto Scaling
 ↓
Spot Instances
 ↓
Workers
```

Excellent combination for:

> Large, distributed, fault-tolerant batch workloads.

---

## Pattern 3: S3 lifecycle

```text
New Data
   ↓
S3 Standard
   ↓
Lifecycle
   ↓
IA
   ↓
Glacier
   ↓
Delete
```

---

## Pattern 4: Private EC2 + S3

```text
EC2
 ↓
S3 Gateway Endpoint
 ↓
S3
```

Instead of:

```text
EC2
 ↓
NAT Gateway
 ↓
S3
```

when S3 is the required destination.

---

## Pattern 5: Global content delivery

```text
Users
  ↓
CloudFront
  ↓
S3 / ALB
```

Caching reduces origin traffic and improves performance.

---

# 26. Cost Optimization Decision Tree

```text id="u0vuxg"
Need to reduce cost?
       |
       +── EC2?
       |     |
       |     +── Predictable → RI / Savings Plan
       |     +── Interruptible → Spot
       |     +── Variable → Auto Scaling
       |     +── Oversized → Right-size
       |
       +── S3?
       |     |
       |     +── Unknown access → Intelligent-Tiering
       |     +── Infrequent → IA
       |     +── Archive → Glacier
       |     +── Old objects → Lifecycle
       |
       +── Network?
       |     |
       |     +── S3 from private subnet → Gateway Endpoint
       |     +── Repeated global content → CloudFront
       |     +── Excessive cross-AZ traffic → Reconsider architecture
       |
       +── Spending visibility?
             |
             +── Analyze → Cost Explorer
             +── Threshold alerts → Budgets
             +── Detailed billing → CUR
```

---

# 27. The Most Important Cost Comparisons

### Reserved vs Savings Plans

**Reserved Instance**

→ More tied to specific EC2 configuration/usage characteristics.

**Savings Plan**

→ Commitment to compute spend, generally more flexible.

---

### Spot vs On-Demand

**Spot**

→ Cheap + interruptible

**On-Demand**

→ Flexible + no interruption due to Spot reclamation

---

### S3 Standard vs Intelligent-Tiering

**Standard**

→ Frequently accessed

**Intelligent-Tiering**

→ Unknown/changing access

---

### Cost Explorer vs Budgets

**Cost Explorer**

→ **Analyze**

**Budgets**

→ **Alert**

---

### CloudWatch vs Cost Explorer

**CloudWatch**

→ Monitor operational metrics

**Cost Explorer**

→ Analyze AWS spending

---

# 28. Exam Traps

1. **Spot = interruptible**
2. **On-Demand = flexibility**
3. **Reserved = predictable EC2 usage**
4. **Savings Plans = committed compute spend + flexibility**
5. **Auto Scaling can reduce cost, not just improve availability**
6. **Right-sizing = eliminate over-provisioning**
7. **Intelligent-Tiering = unknown/changing access**
8. **Standard-IA = known infrequent access**
9. **Glacier = archival**
10. **Lifecycle = automate storage transitions/deletion**
11. **S3 Gateway Endpoint can avoid NAT for S3 access**
12. **CloudFront = caching + reduced origin load**
13. **Cost Explorer = analyze costs**
14. **Budgets = spending alerts**
15. **CUR = detailed cost/usage data**
16. **Cost allocation tags = attribute spending**
17. **Trusted Advisor = recommendations**
18. Don't choose the cheapest service if it violates the workload requirement.
19. Don't choose Spot for workloads that cannot tolerate interruption.
20. Don't choose expensive high-performance storage without an actual performance requirement.

---

# 29. 30-Second Cost Map

```text
                    COST
                     |
       +-------------+-------------+
       |             |             |
     COMPUTE       STORAGE       NETWORK
       |             |             |
   Right-size      S3 Class      Endpoints
   Auto Scale      Lifecycle     CloudFront
   Spot            Glacier       Reduce transfer
   RI              Delete old
   Savings Plan

       MANAGEMENT
           |
    +------+------+------+
    |      |      |      |
 Cost   Budgets  CUR   Trusted
Explorer                 Advisor
    |       |      |       |
 Analyze  Alert  Detail  Recommend
```

### The 8 lines I'd memorize before the exam

> **Predictable compute → Reserved / Savings Plan**

> **Interruptible compute → Spot**

> **Variable demand → Auto Scaling**

> **Over-provisioned → Right-size**

> **Unknown S3 access → Intelligent-Tiering**

> **Long-term archive → Glacier**

> **Analyze spending → Cost Explorer**

> **Set spending threshold/alert → AWS Budgets**

And one particularly useful architecture pattern:

> **Private EC2 → S3 Gateway Endpoint → S3**, instead of routing S3 traffic through a NAT Gateway when the goal is cost-efficient private S3 access.

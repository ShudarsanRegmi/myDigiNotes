<img width="1223" height="1286" alt="image" src="https://github.com/user-attachments/assets/274bd1c1-a24e-4ad2-8f3e-ef08324921a1" />


# Part VII: Disaster Recovery & Business Continuity

This is a **very high-value SAA topic** because AWS exam questions frequently give you a business requirement such as:

> "The application must recover within 15 minutes with minimal data loss."

Then you need to translate that into:

**RTO/RPO → DR strategy → AWS architecture**

The core mental model:

```text
                    DISASTER RECOVERY
                           |
              +------------+------------+
              |                         |
             RTO                       RPO
              |                         |
       How fast to recover?       How much data loss?
              |                         |
              +------------+------------+
                           |
                    DR Strategies
                           |
        +------------------+------------------+
        |                  |                  |
 Backup & Restore     Pilot Light        Warm Standby
        |                  |                  |
    Cheapest          Faster             Faster
    Slowest           recovery           recovery
                           |
                    Multi-Site Active/Active
                           |
                     Fastest / Costliest
```

---

# 1. Business Continuity vs Disaster Recovery

### Business Continuity

Broad concept:

> **How does the business continue operating during disruption?**

Includes:

* Disaster recovery
* Backups
* Redundancy
* Failover
* Operational procedures

### Disaster Recovery

More specifically:

> **How do we restore IT systems after a disaster?**

For SAA, the important concepts are **RTO, RPO, HA, backup, replication, and failover**.

---

# 2. RTO

**RTO = Recovery Time Objective**

Question:

> **"How long can the application be unavailable?"**

Example:

```text
Disaster
   ↓
Application down
   ↓
Recovery
   ↓
15 minutes
```

RTO = **15 minutes**

### Remember

> **RTO = Time to recover**

Lower RTO:

→ Faster recovery
→ Usually higher cost

---

# 3. RPO

**RPO = Recovery Point Objective**

Question:

> **"How much data can we afford to lose?"**

Example:

Last backup:

```text
10:00
```

Disaster:

```text
10:30
```

If you can tolerate losing up to 30 minutes of data:

**RPO = 30 minutes**

### Remember

> **RPO = Data loss tolerance**

Lower RPO:

→ Less data loss
→ Usually requires more frequent replication/backup

---

# 4. RTO vs RPO

This distinction is **must memorize**.

|                  | RTO                    | RPO                        |
| ---------------- | ---------------------- | -------------------------- |
| Question         | How quickly recover?   | How much data can we lose? |
| Measures         | Downtime               | Data loss                  |
| Lower is         | Faster recovery        | Less data loss             |
| Typical solution | Standby infrastructure | Frequent replication       |

### Mental shortcut

> **T in RTO → Time**

> **P in RPO → Point in time**

---

# 5. DR Strategy 1: Backup and Restore

Cheapest and simplest.

Architecture:

```text
Production
    ↓
Backups
    ↓
S3 / Backup storage
    ↓
DISASTER
    ↓
Restore infrastructure
    ↓
Application
```

During normal operation:

> Minimal infrastructure running in DR environment.

During disaster:

> Restore everything from backups.

### Advantages

* Lowest cost
* Simple
* Good for non-critical workloads

### Disadvantages

* Highest recovery time
* Potentially larger data loss

### Exam trigger

> "Lowest-cost DR strategy"

→ **Backup and Restore**

---

# 6. DR Strategy 2: Pilot Light

Core idea:

> **Keep only the critical core components running in DR.**

Example:

```text
Primary Region
EC2 + Application
      ↓
Database replication
      ↓
DR Region
Database
```

Application servers aren't fully running.

When disaster occurs:

```text
Database
   ↓
Launch EC2
   ↓
Deploy application
   ↓
Route traffic
```

### Compared with Backup/Restore

Pilot Light:

* Some infrastructure already exists
* Faster recovery
* More expensive than backup/restore

### Exam trigger

> "Keep the database/data synchronized, but launch application servers only during disaster."

→ **Pilot Light**

---

# 7. DR Strategy 3: Warm Standby

Here, a smaller but **fully functional environment** is continuously running in the DR Region.

```text
Primary Region
Large production
      ↓
      ↓ replication
      ↓
DR Region
Smaller running environment
```

During disaster:

```text
Warm standby
      ↓
Scale up
      ↓
Handle production traffic
```

### Characteristics

* Faster recovery than pilot light
* More expensive
* Application is already running
* Capacity is usually smaller than production

### Exam trigger

> "A scaled-down but fully functional environment is always running."

→ **Warm Standby**

---

# 8. DR Strategy 4: Multi-Site Active/Active

Both Regions actively serve production traffic.

```text
              Route 53
              /       \
             ↓         ↓
        Region A     Region B
        Production   Production
             ↕         ↕
             Database
```

If Region A fails:

```text
Region B
   ↓
100% traffic
```

### Characteristics

* Fastest recovery
* Minimal downtime
* Potentially minimal data loss
* Highest cost
* Complex architecture

### Exam trigger

> "Near-zero downtime"

> "Both Regions actively serve traffic"

→ **Active/Active**

---

# 9. DR Strategy Comparison

Memorize this table:

| Strategy                 | Cost | Recovery Speed |
| ------------------------ | ---: | -------------: |
| Backup & Restore         |    $ |        Slowest |
| Pilot Light              |   $$ |         Faster |
| Warm Standby             |  $$$ |           Fast |
| Multi-Site Active/Active | $$$$ |        Fastest |

Think:

```text
Backup
   ↓
Pilot Light
   ↓
Warm Standby
   ↓
Active/Active

Cost ↑
Recovery time ↓
```

---

# 10. Famous DR Architecture

## Backup & Restore

```text
Production
    ↓
AWS Backup / S3
    ↓
Cross-Region backup
    ↓
Disaster
    ↓
Restore
```

Best when:

> RTO/RPO requirements are relaxed.

---

# 11. Cross-Region S3 Replication

For important S3 data:

```text
Region A
S3 Bucket
    ↓
Cross-Region Replication
    ↓
Region B
S3 Bucket
```

Useful for:

* Disaster recovery
* Regional redundancy
* Compliance
* Geographic distribution

### Exam trigger

> "Maintain copies of objects in another Region."

→ **S3 Cross-Region Replication**

---

# 12. RDS Cross-Region Read Replica

For relational databases:

```text
Region A
RDS Primary
      ↓
Cross-Region Read Replica
      ↓
Region B
```

Useful for:

* Disaster recovery
* Cross-Region read workloads
* Reducing recovery time

During disaster:

> Promote the replica.

### Important

Don't confuse:

**RDS Multi-AZ**

→ Same-Region HA

with:

**Cross-Region Read Replica**

→ Cross-Region DR/read scaling

---

# 13. Aurora Global Database

Excellent for global DR.

```text
Region A
Aurora Primary
      ↓
Region B
Aurora Secondary
      ↓
Region C
Aurora Secondary
```

Useful for:

* Global applications
* Low-latency reads
* Cross-Region disaster recovery
* Faster regional failover

### Exam trigger

> "Need a globally distributed relational database with low-latency reads and DR."

→ **Aurora Global Database**

---

# 14. DynamoDB Global Tables

Multi-Region, multi-active DynamoDB.

```text
Region A ←→ Region B
    ↕           ↕
Region C ←→ Region D
```

Applications can read/write locally.

Useful for:

* Global applications
* Low latency
* Multi-Region resilience
* Active/active architectures

### Compare

**Aurora Global Database**

→ Relational

**DynamoDB Global Tables**

→ NoSQL

---

# 15. Route 53 Failover Routing

Classic DR architecture:

```text
                Route 53
                   |
             Health Check
              /        \
             ↓          ↓
         Primary     Secondary
         Region A     Region B
```

If primary fails:

```text
Route 53
    ↓
Secondary Region
```

### Exam trigger

> "Automatically redirect users to a backup endpoint if primary becomes unhealthy."

→ **Route 53 Failover Routing**

---

# 16. Elastic Disaster Recovery

**AWS Elastic Disaster Recovery (DRS)** provides continuous replication of workloads to AWS.

Think:

> **Replicate servers continuously → recover them quickly in AWS.**

Useful for:

* On-premises → AWS DR
* Physical servers
* Virtual machines
* Cloud workloads

It is particularly useful when you need DR without completely redesigning the application.

---

# 17. AWS Backup

Centralized backup service.

Can manage backups for supported AWS resources.

Think:

> **"I need centralized backup policies across AWS services."**

Useful for:

* Centralized backup
* Backup policies
* Cross-Region/account backup strategies
* Compliance

### Exam trigger

> "Create centralized automated backups across multiple AWS services."

→ **AWS Backup**

---

# 18. Backup vs Replication

Important conceptual distinction.

### Backup

```text
Data
 ↓
Backup copy
```

Usually:

* Point-in-time recovery
* Cheaper
* Slower recovery

### Replication

```text
Primary
   ↓
Continuous/near-continuous copy
   ↓
Secondary
```

Usually:

* Faster recovery
* Lower RPO
* Higher cost/complexity

### Exam clue

> "Need very low RPO"

Think:

**Replication**, not occasional backups.

---

# 19. High Availability vs Disaster Recovery

Don't confuse them.

### High Availability

Protects against:

> **Component/AZ failures**

Example:

```text
ALB
 ↓
EC2 AZ-A
EC2 AZ-B
```

### Disaster Recovery

Protects against:

> **Major failures, including Region-level disasters**

Example:

```text
Region A
   ↓
Region B
```

### Shortcut

> **AZ failure → Multi-AZ**

> **Region failure → Multi-Region DR**

---

# 20. Famous HA + DR Architecture

A strong SAA architecture might look like:

```text
                    Route 53
                   /        \
                  ↓          ↓
             Region A      Region B
               ALB           ALB
                ↓             ↓
             EC2 ASG       EC2 ASG
                ↓             ↓
              RDS          Replica
                ↓             ↓
                +-------------+
```

For even stronger global architectures:

```text
                 Route 53
                /         \
               ↓           ↓
          Region A       Region B
             ALB            ALB
              ↓              ↓
            EC2            EC2
              ↕              ↕
          Global DB / replicated data
```

---

# 21. DR Decision Tree

```text id="t0i2x3"
Need disaster recovery?
         |
         +── Lowest cost / slow recovery okay?
         |       ↓
         |   Backup & Restore
         |
         +── Critical data always replicated?
         |       ↓
         |   Pilot Light
         |
         +── Need faster recovery?
         |       ↓
         |   Warm Standby
         |
         +── Near-zero downtime?
                 ↓
          Active / Active
```

---

# 22. Requirement → Architecture

| Requirement                      | Think                     |
| -------------------------------- | ------------------------- |
| Lowest DR cost                   | Backup & Restore          |
| Long RTO acceptable              | Backup & Restore          |
| Keep critical DB synchronized    | Pilot Light               |
| Small environment always running | Warm Standby              |
| Near-zero downtime               | Active/Active             |
| Very low RPO                     | Continuous replication    |
| S3 cross-Region DR               | CRR                       |
| RDS cross-Region DR              | Cross-Region Read Replica |
| Global relational DB             | Aurora Global Database    |
| Global NoSQL DB                  | DynamoDB Global Tables    |
| Automatic DNS failover           | Route 53 Failover         |
| Centralized backups              | AWS Backup                |
| Server replication for DR        | Elastic Disaster Recovery |

---

# 23. Exam Traps

These are **high priority**:

1. **RTO = maximum acceptable downtime**
2. **RPO = maximum acceptable data loss**
3. Lower RTO → generally more expensive
4. Lower RPO → generally more frequent/continuous replication
5. **Backup & Restore = cheapest, slowest**
6. **Pilot Light = critical core always running**
7. **Warm Standby = scaled-down but functional environment**
8. **Active/Active = both environments actively serving traffic**
9. **Multi-AZ = HA**
10. **Multi-Region = DR/global resilience**
11. **RDS Multi-AZ ≠ Read Replica**
12. **RDS Multi-AZ = failover/HA**
13. **Read Replica = read scaling / DR depending on placement**
14. **Cross-Region replication = DR**
15. **S3 CRR = cross-Region object replication**
16. **Aurora Global Database = global relational**
17. **DynamoDB Global Tables = global NoSQL**
18. **Route 53 Failover = DNS-level traffic switching**
19. **AWS Backup = centralized backup management**
20. **DRS = continuous server replication/recovery**
21. Backups alone generally don't provide very low RPO.
22. Don't choose active/active simply because it is "best." SAA questions usually ask for the **least expensive solution that satisfies the requirement**.

---

# 24. The SAA Cost vs Recovery Graph

This is a useful mental picture:

```text
Recovery speed
     ↑
     |
     |                    Active/Active
     |                  /
     |             Warm Standby
     |           /
     |       Pilot Light
     |     /
     | Backup & Restore
     |
     +--------------------------------→ Cost
```

The exam frequently gives you a constraint such as:

> "The company wants the lowest-cost solution while an RTO of several hours is acceptable."

Don't overengineer it.

→ **Backup & Restore**

But:

> "The company requires recovery within minutes."

→ Think **Pilot Light / Warm Standby**

And:

> "The application must remain available with almost no interruption."

→ **Active/Active**

---

# 25. The 30-Second DR Memory Map

```text
                       DR
                        |
                +-------+-------+
                |               |
               RTO             RPO
                |               |
             Recovery          Data
               Time            Loss
                |               |
        +-------+-------+       |
        |       |       |       |
      Backup  Pilot   Warm   Replication
      Restore Light  Standby
        |               |
      Cheap            Fast
      Slow             |
                       +------+
                          |
                    Active/Active
                    Fastest / costly


DATABASE DR
├─ RDS Multi-AZ
│    → Same-Region HA
│
├─ RDS Cross-Region Replica
│    → Cross-Region DR
│
├─ Aurora Global DB
│    → Global relational
│
└─ DynamoDB Global Tables
     → Global NoSQL


OTHER DR
├─ S3 CRR
│    → Cross-Region objects
├─ AWS Backup
│    → Centralized backups
├─ Route 53 Failover
│    → DNS failover
└─ DRS
     → Continuous server replication
```

## If you remember only 10 things

> **RTO = how fast?**

> **RPO = how much data can we lose?**

> **Backup/Restore = cheapest**

> **Pilot Light = core infrastructure running**

> **Warm Standby = scaled-down working environment**

> **Active/Active = both sites serving traffic**

> **Multi-AZ = HA**

> **Multi-Region = DR**

> **Replication = lower RPO**

> **Choose the cheapest strategy that satisfies the stated RTO/RPO.**

That last principle is particularly important: **SAA is not testing whether you can design the most sophisticated architecture. It is testing whether you can design the most appropriate architecture for the stated business requirements.**

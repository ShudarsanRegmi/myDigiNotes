<img width="1223" height="1286" alt="image" src="https://github.com/user-attachments/assets/127bce33-a80c-454a-b6ad-e4d86f0bf84e" />



# Part IV: Databases

For SAA, database questions are heavily about **choosing the right database model**, then understanding **availability, scaling, consistency, caching, and replication**.

The core mental map:

```text
Relational / SQL
    ↓
RDS / Aurora

NoSQL / Key-value
    ↓
DynamoDB

Cache
    ↓
ElastiCache

Specialized
    ├── Neptune       → Graph
    ├── DocumentDB    → Document
    ├── Timestream    → Time-series
    ├── Keyspaces     → Cassandra
    └── MemoryDB      → Redis-compatible durable DB
```

---

# 1. Amazon RDS

## What is it?

**RDS = managed relational database service.**

Supports common relational engines such as:

* MySQL
* PostgreSQL
* MariaDB
* Oracle
* SQL Server

Think:

> **"I need SQL/relational database but don't want to manage the database server myself." → RDS**

AWS handles much of:

* Provisioning
* Patching
* Backups
* Maintenance
* Infrastructure

You still manage:

* Database configuration
* Schema
* Queries
* Users/permissions inside the DB
* Application-side optimization

---

# 2. RDS Multi-AZ

**Multi-AZ = high availability / failover**

Architecture:

```text
             RDS
              |
       +------+------+
       |             |
   AZ-A Primary   AZ-B Standby
```

The standby is maintained through **synchronous replication**.

If primary fails:

```text
Primary fails
     ↓
Automatic failover
     ↓
Standby becomes primary
```

### Important

**Multi-AZ is primarily for availability, not read scaling.**

You generally don't send application read traffic to the standby.

### Exam trigger

> "Database must automatically fail over if an AZ/database instance fails."

→ **RDS Multi-AZ**

---

# 3. RDS Read Replicas

Read replicas are for:

> **Read scaling**

Architecture:

```text
                 RDS Primary
                /           \
               ↓             ↓
          Read Replica   Read Replica
```

Useful when:

* Application is read-heavy
* Need additional read capacity
* Reporting/analytics queries should not affect primary

### Important

Read replicas are **not the same as Multi-AZ**.

| Requirement                | Answer       |
| -------------------------- | ------------ |
| High availability/failover | Multi-AZ     |
| Scale reads                | Read Replica |

---

# 4. RDS Backups

### Automated backups

* Point-in-time recovery
* Retention period
* Used for operational recovery

### Manual snapshots

* User initiated
* Persist until deleted
* Can be copied
* Useful for migration/backup

### Exam distinction

> **Point-in-time recovery → Automated backups**

> **Long-term/manual backup → Snapshot**

---

# 5. RDS Encryption

RDS supports encryption at rest using **AWS KMS**.

Encryption can cover:

* Database storage
* Automated backups
* Read replicas
* Snapshots

### Important exam trap

If an existing unencrypted RDS database must become encrypted, you generally **cannot simply toggle encryption on**.

Typical approach:

```text
Unencrypted RDS
      ↓
Snapshot
      ↓
Copy snapshot with encryption
      ↓
Restore encrypted DB
      ↓
Switch application
```

Remember this pattern.

---

# 6. Amazon Aurora

**Aurora = AWS cloud-optimized relational database.**

Compatible with:

* MySQL
* PostgreSQL

### Key architectural idea

Aurora separates:

```text
Compute
   +
Distributed storage
```

Aurora storage automatically replicates data across multiple AZs.

### Think:

> **"Need a high-performance, highly available AWS relational database." → Aurora**

---

# 7. Aurora Replicas

Aurora supports multiple read replicas.

Architecture:

```text
             Aurora Writer
              /    |    \
             ↓     ↓     ↓
          Reader Reader Reader
```

Useful for:

* Read scaling
* High availability
* Failover

### Aurora failover

If writer fails:

> Aurora can promote a replica to writer.

---

# 8. Aurora Serverless

Provides database capacity that automatically adjusts based on workload.

Think:

> **Variable/unpredictable database workload + don't want to provision capacity manually.**

Useful for:

* Intermittent workloads
* Variable demand
* Applications where database traffic changes significantly

---

# 9. Aurora Global Database

Designed for:

> **Cross-Region database architectures**

Architecture:

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
* Disaster recovery
* Cross-Region read workloads
* Low-latency global reads

### Exam keyword

> "Need relational database across multiple AWS Regions with fast replication."

→ **Aurora Global Database**

---

# 10. RDS vs Aurora

|                     | RDS              | Aurora                      |
| ------------------- | ---------------- | --------------------------- |
| Relational          | Yes              | Yes                         |
| Managed             | Yes              | Yes                         |
| Engines             | Multiple         | MySQL/PostgreSQL compatible |
| AWS optimized       | Standard         | Highly cloud-optimized      |
| Distributed storage | Engine-dependent | Yes                         |
| Global Database     | No               | Yes                         |
| High-performance HA | Good             | Excellent                   |

### Shortcut

> **Standard managed SQL → RDS**

> **High-performance AWS-native SQL → Aurora**

---

# 11. DynamoDB

**DynamoDB = managed NoSQL database.**

Think:

> **Key-value/document database with massive scalability.**

Characteristics:

* Serverless
* Highly scalable
* Low latency
* Managed
* No traditional server management

Great for:

* Web applications
* Gaming
* IoT
* User profiles
* Shopping carts
* High-scale applications

---

# 12. DynamoDB Data Model

```text
Table
 ├── Item
 │    ├── Attribute
 │    ├── Attribute
 │    └── Attribute
 └── Item
```

Similar conceptually to:

```text
Table → rows
Item → record
Attribute → field
```

But DynamoDB is **not relational SQL**.

---

# 13. Partition Key

Extremely important.

DynamoDB distributes data based on the **partition key**.

Example:

```text
UserID
```

If users are:

```text
User001
User002
User003
...
```

DynamoDB distributes those items across partitions.

### Bad partition key

A key with very low cardinality.

Example:

```text
Country = India
```

If most requests hit the same key:

> **Hot partition**

### Good partition key

High-cardinality, evenly distributed values.

Think:

> **Good partition key = evenly distributes workload**

---

# 14. Composite Primary Key

Can consist of:

```text
Partition Key + Sort Key
```

Example:

```text
UserID      = 123
OrderID     = 456
```

This allows multiple items with the same partition key but different sort keys.

---

# 15. Query vs Scan

### Query

Finds items based on key conditions.

```text
Partition Key = 123
```

Efficient.

### Scan

Examines the entire table/index.

Usually expensive.

### Exam trigger

> "Improve DynamoDB read efficiency."

→ Design access patterns around **Query**, not Scan.

---

# 16. GSI

**Global Secondary Index**

Allows querying using a different key structure.

Example:

Original:

```text
PK = UserID
```

GSI:

```text
PK = Email
```

Useful when:

> Application needs an additional query pattern.

### Important

GSI can have a different partition key and sort key from the base table.

---

# 17. LSI

**Local Secondary Index**

* Same partition key as base table
* Different sort key
* Must be created when the table is created
* Limited to the table's partition-key structure

### Shortcut

**GSI → different partition key possible**

**LSI → same partition key**

---

# 18. DynamoDB Capacity Modes

### Provisioned

You specify:

* Read capacity
* Write capacity

Good for:

> Predictable workloads.

Can use Auto Scaling.

### On-Demand

Automatically handles capacity.

Good for:

> Unpredictable/spiky workloads.

### Shortcut

**Predictable → Provisioned**

**Unpredictable → On-Demand**

---

# 19. DynamoDB Consistency

### Eventually Consistent Reads

May briefly return older data.

* Lower latency/cost
* Default behavior

### Strongly Consistent Reads

Returns the latest data after successful write.

Use when:

> Application needs the most up-to-date value.

### Shortcut

> **Latest data immediately → Strongly consistent read**

---

# 20. DynamoDB Global Tables

Provides:

> **Multi-Region, multi-active DynamoDB.**

Architecture:

```text
Region A ←→ Region B
    ↕           ↕
Region C ←→ Region D
```

Useful for:

* Global applications
* Low-latency regional access
* Multi-Region resilience
* Active-active architecture

### Exam keyword

> "Users globally need local low-latency database access."

→ **DynamoDB Global Tables**

---

# 21. DynamoDB Streams

Captures changes to DynamoDB items.

Example:

```text
DynamoDB
   ↓
DynamoDB Streams
   ↓
Lambda
   ↓
Process change
```

Useful for:

* Event-driven architectures
* Auditing
* Replication
* Triggering downstream processes

---

# 22. DynamoDB TTL

**Time To Live**

Automatically expires/deletes items after their configured expiration time.

Useful for:

* Temporary data
* Sessions
* Caches
* Expiring records

### Exam trigger

> "Automatically remove old/expired DynamoDB items."

→ **TTL**

---

# 23. DynamoDB Transactions

Allows multiple operations to be executed atomically.

Think:

> **Need ACID-like transactional behavior across multiple DynamoDB items.**

---

# 24. DAX

**DAX = DynamoDB Accelerator**

Managed in-memory cache for DynamoDB.

Architecture:

```text
Application
     ↓
    DAX
     ↓
DynamoDB
```

Useful for:

> Extremely low-latency, read-heavy DynamoDB workloads.

### Shortcut

**DynamoDB cache → DAX**

---

# 25. ElastiCache

Managed in-memory caching.

Main engines you need to recognize:

* Valkey/Redis OSS compatible offerings
* Memcached

Think:

> **Reduce database load + extremely fast reads**

Architecture:

```text
Application
     ↓
ElastiCache
     ↓ cache miss
Database
```

---

# 26. Redis vs Memcached

For SAA, remember the conceptual distinction.

### Redis/Valkey

More feature-rich.

Supports things such as:

* Persistence
* Replication
* High availability
* Complex data structures

### Memcached

Simpler distributed cache.

Think:

> Simple, horizontally scalable cache.

### Shortcut

> **Need advanced caching/HA/features → Redis/Valkey**

> **Simple cache → Memcached**

---

# 27. ElastiCache Use Cases

Excellent for:

* Frequently accessed data
* Session storage
* Database caching
* Reducing DB load

Example:

```text
User
 ↓
Application
 ↓
ElastiCache
 ↓ cache miss
RDS
```

### Exam keyword

> "Database is overloaded because the same data is repeatedly read."

→ **ElastiCache**

---

# 28. Neptune

**Amazon Neptune = graph database.**

Think:

> **Relationships between entities are the core of the application.**

Examples:

* Social networks
* Recommendation engines
* Knowledge graphs
* Fraud relationship analysis

### Exam trigger

> "Need to efficiently model and query complex relationships."

→ **Neptune**

---

# 29. DocumentDB

MongoDB-compatible managed document database.

Think:

> **Document-oriented application requiring MongoDB compatibility.**

---

# 30. Timestream

Time-series database.

Think:

> **Data indexed by time**

Examples:

* IoT sensor data
* Metrics
* Operational telemetry

---

# 31. Keyspaces

Managed Apache Cassandra-compatible database.

Think:

> **Cassandra workloads without managing Cassandra infrastructure.**

---

# 32. MemoryDB

Durable, Redis-compatible in-memory database.

Important distinction:

**ElastiCache**

→ primarily caching

**MemoryDB**

→ database with in-memory performance and durability

---

# 33. Database Decision Tree

```text id="q4l6w3"
Need a database?
       |
       +── Relational / SQL?
       |       |
       |       +── Standard managed SQL → RDS
       |       |
       |       +── High-performance AWS SQL → Aurora
       |       |
       |       +── Global relational → Aurora Global Database
       |
       +── NoSQL?
       |       |
       |       → DynamoDB
       |
       +── Need caching?
       |       |
       |       → ElastiCache
       |       |
       |       +── DynamoDB-specific → DAX
       |
       +── Graph relationships?
       |       → Neptune
       |
       +── Document / MongoDB?
       |       → DocumentDB
       |
       +── Time-series?
       |       → Timestream
       |
       +── Cassandra?
       |       → Keyspaces
       |
       +── Durable in-memory database?
               → MemoryDB
```

---

# 34. Famous Database Architecture Patterns

## Pattern 1: Highly Available RDS

```text
              Application
                   ↓
            RDS Multi-AZ
             /         \
          AZ-A         AZ-B
        Primary       Standby
```

**Purpose: HA/failover**

Not read scaling.

---

## Pattern 2: Read-Heavy RDS

```text
                 Application
                /     |     \
               ↓      ↓      ↓
          Read Replica Replica Replica
                \      |      /
                    RDS
                  Primary
```

**Purpose: read scaling**

---

## Pattern 3: Caching RDS

```text
Application
    ↓
ElastiCache
    ↓ cache miss
   RDS
```

**Purpose: reduce DB reads + latency**

---

## Pattern 4: Serverless Web Application

```text
API Gateway
     ↓
  Lambda
     ↓
DynamoDB
```

**Purpose: fully managed/serverless architecture**

---

## Pattern 5: DynamoDB Event-Driven

```text
DynamoDB
    ↓
Streams
    ↓
 Lambda
    ↓
Other service
```

**Purpose: react to database changes**

---

## Pattern 6: Global DynamoDB

```text
Users
 ↓
Nearest Region
 ↓
DynamoDB Global Tables
 ↕
Other Regions
```

**Purpose: global low latency + multi-Region resilience**

---

## Pattern 7: Global Aurora

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

**Purpose: global relational database + DR + regional reads**

---

# 35. Critical Comparisons

### Multi-AZ vs Read Replica

```text
Multi-AZ
→ Availability
→ Automatic failover

Read Replica
→ Read scaling
→ Offload read traffic
```

This is one of the **most important database distinctions in SAA**.

---

### RDS vs DynamoDB

| Requirement                        | Think      |
| ---------------------------------- | ---------- |
| SQL                                | RDS/Aurora |
| Relational relationships           | RDS/Aurora |
| Complex SQL queries                | RDS/Aurora |
| Massive NoSQL scale                | DynamoDB   |
| Serverless NoSQL                   | DynamoDB   |
| Millisecond-scale key-value access | DynamoDB   |

---

### RDS vs Aurora

**RDS**

→ Managed relational engines

**Aurora**

→ AWS-optimized MySQL/PostgreSQL-compatible relational database

---

### ElastiCache vs DAX

**ElastiCache**

→ Cache for applications/databases generally

**DAX**

→ Specifically accelerates DynamoDB

---

### ElastiCache vs MemoryDB

**ElastiCache**

→ Cache

**MemoryDB**

→ Durable primary database

---

# 36. Database Exam Traps

Memorize these:

1. **RDS Multi-AZ = HA/failover**
2. **RDS Read Replica = read scaling**
3. Multi-AZ standby isn't primarily for serving reads.
4. **Aurora = MySQL/PostgreSQL compatible**
5. **Aurora Global Database = cross-Region relational**
6. **DynamoDB = NoSQL**
7. **DynamoDB partition key determines data distribution**
8. Poor partition-key distribution → **hot partition**
9. **Query is preferable to Scan**
10. **GSI can use a different partition key**
11. **LSI uses the same partition key**
12. LSI must be created when the table is created.
13. **Provisioned = predictable workload**
14. **On-Demand = unpredictable workload**
15. **Strong consistency = latest data**
16. **Global Tables = multi-Region DynamoDB**
17. **DynamoDB Streams = react to item changes**
18. **TTL = automatically expire items**
19. **DAX = DynamoDB cache**
20. **ElastiCache = general application/database cache**
21. **Neptune = graph**
22. **DocumentDB = document/MongoDB compatible**
23. **Timestream = time-series**
24. **Keyspaces = Cassandra**
25. **MemoryDB = durable in-memory database**

---

# 37. The 30-Second Database Map

```text id="i4xwq7"
                       DATABASE
                           |
          +----------------+----------------+
          |                                 |
       RELATIONAL                         NoSQL
          |                                 |
     +----+----+                       DynamoDB
     |         |                          |
    RDS      Aurora                  +----+----+
     |         |                     |         |
  Multi-AZ   Global              Global Tbl   DAX
  → HA       Database
  Read Rep
  → Reads

              CACHING
                 |
            ElastiCache
             /        \
        Redis/Valkey  Memcached

           SPECIALIZED
           ├─ Neptune    → Graph
           ├─ DocumentDB → Document
           ├─ Timestream → Time-series
           ├─ Keyspaces  → Cassandra
           └─ MemoryDB   → Durable in-memory
```

### The five things I would absolutely memorize before the exam

**1. Multi-AZ ≠ Read Replica**

**2. RDS/Aurora = relational, DynamoDB = NoSQL**

**3. GSI vs LSI**

**4. ElastiCache vs DAX**

**5. Partition-key design determines DynamoDB scalability**

These five distinctions have disproportionately high value in SAA scenario questions.

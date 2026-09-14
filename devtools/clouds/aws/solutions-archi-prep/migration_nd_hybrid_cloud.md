<img width="1223" height="1286" alt="image" src="https://github.com/user-attachments/assets/c32bab53-5b31-4c3f-912f-994087f166a2" />


# Part VIII: Migration & Hybrid Architecture

This section is mainly about recognizing **where the workload/data currently lives** and **how it should move or connect to AWS**.

The core mental model:

```text
                         MIGRATION
                            |
             +--------------+--------------+
             |                             |
        Application                     Data
             |                             |
     Application Migration           DMS / DataSync
          Service
             |
       6 R's strategy
```

And for hybrid:

```text
                    AWS
                     |
        +------------+------------+
        |                         |
       VPN                  Direct Connect
        |                         |
     Internet              Dedicated link
        |                         |
                 On-Premises
```

---

# 1. The 6 R's of Migration

This is **high-yield**.

| Strategy       | Meaning                      | Think            |
| -------------- | ---------------------------- | ---------------- |
| **Rehost**     | Move as-is                   | Lift and shift   |
| **Replatform** | Minor optimization           | Move + optimize  |
| **Repurchase** | Replace with another product | Buy/SaaS         |
| **Refactor**   | Redesign application         | Cloud-native     |
| **Retain**     | Keep where it is             | Don't migrate    |
| **Retire**     | Remove it                    | No longer needed |

### Rehost

```text
On-Prem EC2-like VM
       ↓
      EC2
```

Minimal changes.

> **"Move quickly with minimal modification." → Rehost**

---

### Replatform

Move to AWS with some optimization.

Example:

```text
Self-managed MySQL
       ↓
      RDS
```

Application architecture largely remains the same.

> **"Move to managed service with minimal changes." → Replatform**

---

### Refactor

Redesign the application for cloud-native architecture.

Example:

```text
Monolith
   ↓
Lambda + API Gateway
   ↓
DynamoDB
```

More effort, but potentially greater cloud benefits.

> **"Need to transform the application to exploit cloud capabilities." → Refactor**

---

### Repurchase

Replace existing software with another product/SaaS.

Example concept:

```text
Existing CRM
    ↓
SaaS CRM
```

---

### Retain

Don't migrate yet.

Reasons:

* Not worth migrating
* Compliance
* Dependencies
* Recent investment

---

### Retire

Application is no longer needed.

> **Don't migrate something that doesn't need to exist.**

---

# 2. AWS Application Migration Service

**AWS Application Migration Service (MGN)** is used to migrate servers/workloads to AWS.

Think:

> **"I have physical/virtual/cloud servers and want to move them to AWS with minimal changes."**

It performs continuous replication of source servers and helps launch them in AWS.

### Exam trigger

> "Migrate an existing server workload to AWS with minimal application changes."

→ **AWS Application Migration Service**

---

# 3. Database Migration Service

**AWS DMS = Database Migration Service**

Used to migrate databases.

Think:

```text
Source Database
      ↓
     DMS
      ↓
Target Database
```

Can migrate between different database environments.

Example:

```text
On-Prem MySQL
      ↓
     DMS
      ↓
Amazon Aurora
```

### Important

DMS can support **ongoing replication**, helping minimize downtime during migration.

---

# 4. AWS Schema Conversion Tool

**AWS SCT = Schema Conversion Tool**

Useful when migrating between **different database engines**.

Example:

```text
Oracle
  ↓
SCT
  ↓
PostgreSQL
```

It helps convert:

* Database schema
* SQL code
* Database objects

### DMS vs SCT

This is important:

**SCT**

→ Converts schema/code

**DMS**

→ Moves/replicates the actual data

Often:

```text
SCT → convert schema
DMS → migrate data
```

---

# 5. AWS DataSync

**DataSync = automated online data transfer.**

Used to transfer data between:

* On-premises
* S3
* EFS
* FSx
* Other supported storage

Think:

> **"I have a network connection and need to move lots of files/data efficiently."**

### DataSync vs Snow Family

**DataSync**

→ Network available

**Snow**

→ Network transfer impractical

---

# 6. AWS Transfer Family

Provides managed file-transfer protocols to AWS storage.

Supports protocols such as:

* SFTP
* FTPS
* FTP

Typical architecture:

```text
External Partner
       ↓
Transfer Family
       ↓
S3
```

### Exam trigger

> "Existing partners send files using SFTP, and the company wants to store them in S3."

→ **AWS Transfer Family**

---

# 7. Migration Hub

**AWS Migration Hub** provides a centralized place to track migration progress across workloads.

Think:

> **"I have many migrations and want one place to monitor them."**

It is more about **tracking/orchestration visibility** than actually moving the workload itself.

---

# 8. Hybrid Architecture

Hybrid means:

> **On-premises infrastructure + AWS working together.**

Example:

```text
              AWS
               |
          Connectivity
          /           \
        VPN      Direct Connect
          \           /
            On-Prem
```

Common reasons:

* Gradual migration
* Existing infrastructure
* Regulatory requirements
* Latency-sensitive systems
* Data center dependencies

---

# 9. Site-to-Site VPN

Connects:

**On-premises ↔ AWS**

through the Internet.

```text
On-Prem
   ↓
Customer Gateway
   ↓
Internet
   ↓
VGW / Transit Gateway
   ↓
VPC
```

### Characteristics

* Encrypted
* Uses Internet
* Quick to deploy
* Lower cost
* Good for backup connectivity

### Exam trigger

> "Need secure connectivity to AWS quickly."

→ **Site-to-Site VPN**

---

# 10. Direct Connect

Provides a **dedicated network connection** between your network and AWS.

```text
On-Prem
   ↓
Direct Connect
   ↓
AWS
```

### Use when

* Consistent performance
* High bandwidth
* Large data transfers
* Long-term hybrid architecture
* Need private connectivity

### Critical

**Direct Connect is not encrypted by default.**

You can combine Direct Connect with VPN when encryption is required.

---

# 11. VPN vs Direct Connect

|             | VPN          | Direct Connect    |
| ----------- | ------------ | ----------------- |
| Path        | Internet     | Dedicated         |
| Encryption  | Yes          | Not by default    |
| Setup       | Fast         | Longer            |
| Cost        | Lower        | Higher            |
| Performance | Variable     | Consistent        |
| Best for    | Quick hybrid | Enterprise hybrid |

### Memory

> **Quick + encrypted → VPN**

> **Dedicated + consistent → Direct Connect**

---

# 12. Virtual Private Gateway

**VGW = VPN/DX gateway for a VPC.**

Think:

```text
On-Prem
   ↓
VPN
   ↓
VGW
   ↓
VPC
```

For more complex multi-VPC architectures, **Transit Gateway** is often used instead.

---

# 13. Direct Connect Gateway

Allows Direct Connect connectivity to multiple VPCs/Regions through appropriate AWS networking architecture.

Think:

> **One Direct Connect environment → multiple VPCs**

---

# 14. Transit Gateway in Hybrid Architecture

Very important architecture pattern:

```text
                  Transit Gateway
                 /       |       \
                /        |        \
             VPC A     VPC B     VPC C
                |
             VPN / DX
                |
             On-Prem
```

Useful when:

* Many VPCs
* Centralized connectivity
* Hybrid network
* Centralized routing

### Exam trigger

> "Connect multiple VPCs and on-premises networks using a central hub."

→ **Transit Gateway**

---

# 15. AWS Outposts

**AWS Outposts = AWS infrastructure deployed in your own data center/location.**

Think:

> **AWS services on-premises**

Useful when workloads need:

* Very low latency to on-prem systems
* Local data processing
* Specific data residency requirements
* Hybrid consistency

Architecture:

```text
Your Data Center
      |
   Outposts
      |
 AWS services
```

---

# 16. AWS Local Zones

Places AWS infrastructure closer to large population centers.

Useful for:

> **Very low-latency applications that need AWS compute/storage closer to users.**

Think:

```text
AWS Region
    |
Local Zone
    |
Nearby users
```

### Exam trigger

> "Need single-digit millisecond latency to users in a specific metropolitan area."

→ Consider **Local Zones**

---

# 17. AWS Wavelength

Designed to bring AWS infrastructure closer to **5G networks**.

Think:

> **5G + ultra-low latency**

Useful for:

* Telecom applications
* Connected vehicles
* AR/VR
* Real-time mobile applications

### Shortcut

```text
On-prem AWS → Outposts
City/metro low latency → Local Zones
5G edge → Wavelength
```

---

# 18. Migration Decision Tree

```text id="l6zq6w"
What are you migrating?
          |
     +----+----+
     |         |
 Application  Database
     |         |
    MGN       DMS
     |         |
     |      Different DB engine?
     |         |
     |        Yes
     |         ↓
     |        SCT
     |
 Data / Files
     |
 +---+----------------+
 |                    |
Online              Offline
 |                    |
DataSync          Snow Family
```

---

# 19. Famous Migration Architecture Patterns

## Pattern 1: Lift and Shift

```text
On-Prem Server
      ↓
Application Migration Service
      ↓
EC2
```

**Goal:** migrate quickly with minimal modification.

→ **Rehost**

---

## Pattern 2: Database Migration

```text
On-Prem DB
    ↓
   DMS
    ↓
RDS / Aurora
```

If database engines differ:

```text
Source DB
   ↓
SCT → Schema conversion
   ↓
DMS → Data migration
   ↓
Target DB
```

---

## Pattern 3: Hybrid During Migration

```text
              AWS
               |
          VPN / DX
               |
           On-Prem
```

The application can gradually move components to AWS while maintaining connectivity with remaining on-prem systems.

---

## Pattern 4: Centralized Multi-VPC Hybrid

```text
                     VPC A
                       |
                     VPC B
                       |
                Transit Gateway
                   /       \
                  /         \
                VPC C      VPN / DX
                              |
                           On-Prem
```

Excellent for enterprise environments.

---

## Pattern 5: SFTP to S3

```text
External Partner
       ↓
Transfer Family
       ↓
      S3
       ↓
 Lambda / Processing
```

Classic serverless file-ingestion architecture.

---

# 20. DataSync vs Snowball vs DMS

This distinction is useful:

| Requirement                | Service                       |
| -------------------------- | ----------------------------- |
| Database migration         | DMS                           |
| Database schema conversion | SCT                           |
| Online file/data transfer  | DataSync                      |
| Huge offline data transfer | Snow Family                   |
| SFTP/FTP into AWS          | Transfer Family               |
| Server migration           | Application Migration Service |

---

# 21. Migration Strategy Decision

Question says:

> **"Move application as quickly as possible with minimal changes."**

→ **Rehost**

> **"Move to AWS managed database with minimal changes."**

→ **Replatform**

> **"Redesign application to use serverless/cloud-native services."**

→ **Refactor**

> **"Replace existing software with SaaS."**

→ **Repurchase**

> **"Application isn't worth migrating."**

→ **Retire**

> **"Keep application on-premises for now."**

→ **Retain**

---

# 22. Hybrid Connectivity Decision

```text id="a2h3d7"
Need AWS ↔ On-Prem connectivity?
             |
        +----+----+
        |         |
      Quick     Dedicated
        |         |
       VPN       DX
        |
    Encrypted
    Internet


Many VPCs?
      ↓
Transit Gateway


AWS infrastructure
inside your facility?
      ↓
Outposts


Low latency in metro area?
      ↓
Local Zones


5G edge?
      ↓
Wavelength
```

---

# 23. Exam Traps

Memorize these:

1. **Rehost = lift and shift**
2. **Replatform = move + minor optimization**
3. **Refactor = redesign**
4. **Repurchase = replace with another product/SaaS**
5. **Retain = keep**
6. **Retire = remove**
7. **MGN = server/application migration**
8. **DMS = database migration**
9. **SCT = database schema/code conversion**
10. **DataSync = online data transfer**
11. **Snow Family = offline/physical data transfer**
12. **Transfer Family = SFTP/FTP → AWS storage**
13. **Migration Hub = track migrations**
14. **VPN = encrypted over Internet**
15. **Direct Connect = dedicated, not encrypted by default**
16. **Transit Gateway = centralized multi-VPC/hybrid connectivity**
17. **Outposts = AWS infrastructure on-premises**
18. **Local Zones = AWS closer to metro users**
19. **Wavelength = AWS at 5G edge**
20. **DMS can provide ongoing replication to minimize migration downtime.**
21. **SCT + DMS** is a common heterogeneous database migration combination.

---

# 24. The 30-Second Memory Map

```text id="j0l7q4"
                     MIGRATION
                         |
         +---------------+---------------+
         |               |               |
     APPLICATION       DATABASE         DATA
         |               |               |
        MGN             DMS           DataSync
         |               |
     6 R's          Different engine?
                        |
                       SCT


                    HYBRID
                       |
              On-Prem ↔ AWS
                       |
               +-------+-------+
               |               |
              VPN             DX
               |               |
          Internet         Dedicated
          Encrypted       Not encrypted
                         by default

                 MANY VPCs
                     |
               Transit Gateway

                 AWS ON-PREM
                     |
                  Outposts

               LOW LATENCY
              /             \
        Local Zones       Wavelength
        Metro users          5G
```

## If you have 2 minutes before the exam

Memorize these pairs:

> **Rehost → Lift & shift**

> **Replatform → Minor optimization**

> **Refactor → Redesign**

> **MGN → Servers**

> **DMS → Databases**

> **SCT → Schema conversion**

> **DataSync → Online data**

> **Snow → Offline huge data**

> **Transfer Family → SFTP/FTP**

> **VPN → Quick + encrypted**

> **Direct Connect → Dedicated + consistent**

> **Transit Gateway → Many VPCs**

> **Outposts → AWS on-prem**

> **Local Zones → Metro low latency**

> **Wavelength → 5G edge**

The most important architectural principle here is **don't confuse migration with connectivity**. **DMS/DataSync/MGN move workloads or data; VPN/DX/TGW provide the network path that lets hybrid environments communicate.**

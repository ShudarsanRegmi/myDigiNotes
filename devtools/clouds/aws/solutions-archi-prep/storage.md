<img width="1223" height="1286" alt="image" src="https://github.com/user-attachments/assets/e64f0663-25af-4b63-bf0c-da568a150226" />



# Part III: Storage

For SAA, think of storage as a **fundamental architectural choice**:

```text
Object      → S3
Block       → EBS
Shared file → EFS / FSx
Hybrid      → Storage Gateway
Offline     → Snow Family
```

The exam usually tests **which storage model fits the requirement**, rather than obscure configuration details.

---

# 1. Amazon S3

## What is it?

**S3 = highly durable object storage.**

You store:

```text
Bucket
 └── Object
      ├── Data
      ├── Metadata
      └── Key
```

### Key facts

* Object storage
* Virtually unlimited scalability
* Region-based
* Extremely high durability
* Access controlled through IAM/bucket policies/etc.
* Not a traditional filesystem
* Objects are identified by **keys**

### Think:

> **Images, videos, backups, logs, documents, static files, data lakes → S3**

---

# 2. S3 Storage Classes

You don't need to memorize every pricing detail. Understand the **access pattern**.

| Storage class              | Think                                        |
| -------------------------- | -------------------------------------------- |
| S3 Standard                | Frequently accessed                          |
| Intelligent-Tiering        | Unknown/changing access pattern              |
| Standard-IA                | Infrequently accessed, but needs fast access |
| One Zone-IA                | Infrequent + can tolerate single-AZ risk     |
| Glacier Instant Retrieval  | Archive + milliseconds access                |
| Glacier Flexible Retrieval | Archive + retrieval delay acceptable         |
| Glacier Deep Archive       | Very long-term archive, lowest storage cost  |

### Critical distinction

**Intelligent-Tiering**

> "I don't know how frequently these objects will be accessed."

**Standard-IA**

> "I know they're infrequently accessed."

---

# 3. S3 Lifecycle Policies

Automatically transition/delete objects based on age.

Example:

```text
Day 0
 ↓
S3 Standard
 ↓
Day 30
 ↓
Standard-IA
 ↓
Day 90
 ↓
Glacier
 ↓
Day 365
 ↓
Delete
```

### Exam trigger

> "Automatically move old objects to cheaper storage."

→ **S3 Lifecycle Policy**

---

# 4. S3 Versioning

Keeps multiple versions of an object.

Useful for:

* Accidental deletion
* Accidental overwrite
* Recovery from unwanted changes

Example:

```text
file.txt
 ├── v1
 ├── v2
 └── v3
```

### Important

Versioning does **not** replace backups completely.

It protects against accidental modification/deletion, but you still need appropriate backup/replication strategy for broader disaster scenarios.

---

# 5. S3 Object Lock

Prevents objects from being deleted or overwritten for a defined retention period.

Used for:

* Compliance
* Regulatory requirements
* WORM storage

**WORM = Write Once, Read Many**

### Exam trigger

> "Data must not be deleted/modified during a mandatory retention period."

→ **S3 Object Lock**

---

# 6. S3 Replication

### Cross-Region Replication

```text
S3 Bucket A
    ↓
S3 Bucket B
Different Region
```

Useful for:

* Disaster recovery
* Compliance
* Geographic redundancy
* Lower-latency access in another Region

### Same-Region Replication

Replicates objects to another bucket in the same Region.

### Important

S3 replication generally requires **versioning enabled** on the relevant buckets.

---

# 7. S3 Encryption

Know the names:

### SSE-S3

AWS manages encryption keys.

### SSE-KMS

Uses AWS KMS.

Useful when you need:

* More control over keys
* Key policies
* Auditing through KMS

### SSE-C

Customer provides the encryption key with the request.

### Client-side encryption

Application encrypts data **before uploading to S3**.

### Shortcut

> **Need AWS-managed encryption → SSE-S3**

> **Need KMS control/auditing → SSE-KMS**

---

# 8. S3 Bucket Policy

Resource-based policy attached to a bucket.

Can control:

* Who can access bucket
* What actions are allowed
* Which resources
* Conditions such as source VPC endpoint, IP, etc.

### Common exam architecture

> Allow only a specific application/account to access an S3 bucket.

→ **Bucket policy + IAM**

---

# 9. S3 Block Public Access

Very important.

If the requirement says:

> "Ensure the S3 bucket cannot accidentally become publicly accessible."

Think:

**S3 Block Public Access**

This is a broad safeguard against public access configurations.

---

# 10. S3 Presigned URLs

Allows temporary access to a private object.

Example:

```text
Private S3 Object
       ↑
Presigned URL
       ↑
Temporary User
```

Useful when:

> A user needs temporary access to upload/download an object without making the bucket public.

---

# 11. S3 Multipart Upload

Breaks a large object into multiple parts and uploads them independently.

Useful for:

* Large files
* Faster uploads
* Parallel uploads
* Recovering failed parts without restarting entire upload

### Exam trigger

> "Upload very large files efficiently."

→ **Multipart Upload**

---

# 12. S3 Transfer Acceleration

Uses AWS edge locations to accelerate uploads/downloads to S3 over long distances.

Think:

> **Far-away users → faster S3 transfer**

Don't confuse with CloudFront.

**CloudFront → content delivery**

**S3 Transfer Acceleration → accelerate transfers to/from S3**

---

# 13. S3 Static Website Hosting

S3 can host static content:

* HTML
* CSS
* JavaScript
* Images

Typical architecture:

```text
User
 ↓
CloudFront
 ↓
S3
```

For modern/private architectures, CloudFront + **Origin Access Control** is commonly preferred.

---

# 14. S3 Event Notifications

S3 can trigger event-driven workflows when objects change.

Example:

```text
S3 Upload
    ↓
Event
    ↓
Lambda
    ↓
Process Image
```

Can integrate with:

* Lambda
* SNS
* SQS
* EventBridge

---

# 15. EBS

**EBS = Elastic Block Store**

Think:

> **Virtual hard disk attached to EC2**

```text
EC2
 ↓
EBS Volume
```

### Characteristics

* Block storage
* Persistent
* Designed for EC2
* Can create snapshots
* Supports encryption
* Volume generally tied to an AZ

---

# 16. EBS Volume Types

For the exam, focus on these:

### gp3

General-purpose SSD.

Good default choice.

> Balanced price/performance.

### io2

Provisioned IOPS SSD.

For:

> High-performance, mission-critical workloads requiring high IOPS.

### st1

Throughput-optimized HDD.

For:

> Large sequential workloads.

### sc1

Cold HDD.

For:

> Infrequently accessed large sequential workloads.

### Mental map

```text
General → gp3
High IOPS → io2
High throughput → st1
Lowest-cost cold HDD → sc1
```

---

# 17. EBS Snapshots

Point-in-time backup of EBS volumes.

Useful for:

* Backup
* Disaster recovery
* Creating new volumes
* Copying data across Regions

### Important

Snapshots are stored in **Amazon S3-managed infrastructure**, but you don't directly manage the underlying S3 bucket.

### Exam pattern

> "Need to back up an EBS volume."

→ **EBS Snapshot**

---

# 18. EBS vs Instance Store

|                               | EBS                                              | Instance Store       |
| ----------------------------- | ------------------------------------------------ | -------------------- |
| Type                          | Block                                            | Local block          |
| Persistent                    | **Yes**                                          | **No**               |
| Snapshot                      | Yes                                              | No                   |
| Best for                      | Persistent data                                  | Temporary data/cache |
| Survives instance termination | Depending on delete-on-termination configuration | No                   |

### Shortcut

> **Persistent → EBS**

> **Ephemeral/high-speed local → Instance Store**

---

# 19. EFS

**EFS = managed elastic file system.**

Think:

> **Shared Linux file system.**

```text
EC2-A ─┐
EC2-B ─┼── EFS
EC2-C ─┘
```

Multiple instances can access the same filesystem.

### Characteristics

* File storage
* NFS
* Linux workloads
* Automatically scales
* Multi-AZ
* Shared across multiple EC2 instances

### Exam trigger

> "Multiple EC2 instances need shared file storage."

→ **EFS**

---

# 20. EFS vs EBS

|             | EBS                                   | EFS               |
| ----------- | ------------------------------------- | ----------------- |
| Storage     | Block                                 | File              |
| Shared      | Usually not simultaneously across AZs | Yes               |
| Scaling     | Provision/manage capacity             | Elastic           |
| Typical use | Single EC2 / databases                | Shared filesystem |
| Multi-AZ    | No, volume is AZ-specific             | Yes               |

### Shortcut

**One EC2 → persistent disk → EBS**

**Many EC2 → shared filesystem → EFS**

---

# 21. EFS Storage Classes

High-level knowledge:

* Standard
* Infrequent Access
* Archive

EFS lifecycle management can automatically move files to cheaper classes based on access patterns.

Exam trigger:

> "Automatically move infrequently accessed files to lower-cost storage."

→ **EFS lifecycle management**

---

# 22. FSx

FSx provides managed specialized filesystems.

Remember the four:

```text
FSx for Windows File Server
FSx for Lustre
FSx for NetApp ONTAP
FSx for OpenZFS
```

---

# 23. FSx for Windows File Server

Think:

> **Windows + SMB + Microsoft environment**

Useful for:

* Windows applications
* SMB
* Active Directory integration
* Windows file shares

### Exam trigger

> "Existing Windows application requires a shared SMB filesystem."

→ **FSx for Windows File Server**

---

# 24. FSx for Lustre

Think:

> **High-performance computing**

Good for:

* HPC
* Machine learning
* Big data
* High-performance workloads

Can integrate with S3.

Common pattern:

```text
S3
 ↓
FSx for Lustre
 ↓
HPC / ML workload
```

---

# 25. FSx for NetApp ONTAP

Think:

> **Enterprise storage features + NetApp compatibility**

Useful when existing workloads require NetApp capabilities/protocols.

---

# 26. FSx for OpenZFS

Think:

> **High-performance Linux/Unix workloads using OpenZFS**

Less frequently the primary answer, but recognize it.

---

# 27. Storage Gateway

Storage Gateway connects **on-premises environments with AWS storage**.

Main types:

```text
Storage Gateway
├── File Gateway
├── Volume Gateway
└── Tape Gateway
```

---

# 28. File Gateway

Provides file access from on-premises to S3.

Think:

> **On-premises file shares backed by S3**

Useful for:

* SMB/NFS
* Hybrid storage
* Moving files into S3

---

# 29. Volume Gateway

Provides block storage volumes for on-premises applications while storing data in AWS.

Two conceptual modes:

* Cached volumes
* Stored volumes

Exam-level idea:

> **On-premises block storage + AWS-backed storage**

---

# 30. Tape Gateway

Virtual tape infrastructure backed by AWS.

Think:

> **Replace physical tape infrastructure with AWS**

Useful for:

* Existing backup systems
* Virtual tape libraries
* Long-term backup/archive

---

# 31. Snow Family

Physical devices for moving data when network transfer is impractical.

```text
On-Prem
   ↓
Snow Device
   ↓
AWS
```

### Snowcone

Smallest.

### Snowball Edge

Larger data transfer and edge computing capability.

### Snowmobile

Massive-scale data migration using a physical truck/container.

### Exam trigger

> "Hundreds of TB/PB and network transfer would take too long."

→ **Snow Family**

---

# 32. Data Transfer Service: DataSync

Don't confuse this with Snow Family.

**AWS DataSync = online data transfer service.**

Used to move data between:

* On-premises ↔ AWS
* AWS storage services

Think:

> **Network is available and you want automated high-speed transfer.**

### Shortcut

**Network transfer feasible → DataSync**

**Network transfer impractical → Snow Family**

---

# 33. Famous Storage Architecture Patterns

## Pattern 1: Static Website

```text
Users
  ↓
CloudFront
  ↓
S3
```

Benefits:

* Serverless
* Highly scalable
* CDN caching
* Low operational overhead

---

## Pattern 2: Private S3 Content

```text
Users
  ↓
CloudFront
  ↓
OAC
  ↓
Private S3
```

**Don't make S3 public merely to serve CloudFront.**

---

## Pattern 3: EC2 Persistent Storage

```text
EC2
 ↓
EBS
```

Use when the application needs a persistent block device.

---

## Pattern 4: Shared Application Storage

```text
EC2 ─┐
EC2 ─┼── EFS
EC2 ─┘
```

Use when multiple instances need the same files.

---

## Pattern 5: HPC + S3

```text
          S3
           ↓
     FSx for Lustre
           ↓
       HPC / ML
```

Think:

> **S3 data + high-performance filesystem**

---

## Pattern 6: Hybrid File Storage

```text
On-Premises
     ↓
File Gateway
     ↓
     S3
```

---

## Pattern 7: Huge Data Migration

```text
On-Prem
   ↓
Snowball
   ↓
AWS
```

Use when network transfer would be prohibitively slow.

---

# 34. Storage Decision Tree

```text
Need storage?
     |
     +── Object? ─────────→ S3
     |
     +── Block? ──────────→ EBS
     |
     +── Shared file?
     |       |
     |       +── Linux/NFS → EFS
     |       |
     |       +── Windows/SMB → FSx Windows
     |       |
     |       +── HPC → FSx Lustre
     |       |
     |       +── NetApp → FSx ONTAP
     |       |
     |       +── OpenZFS → FSx OpenZFS
     |
     +── Hybrid?
     |       |
     |       +── File → File Gateway
     |       +── Block → Volume Gateway
     |       +── Tape → Tape Gateway
     |
     +── Huge offline migration?
             |
             → Snow Family
```

---

# 35. Storage Exam Traps

Memorize these.

1. **S3 = object storage**
2. **EBS = block storage**
3. **EFS = shared file storage**
4. **S3 is not a traditional filesystem**
5. **EBS volume is AZ-specific**
6. **EFS can be accessed across multiple AZs**
7. **S3 Standard = frequent access**
8. **Intelligent-Tiering = unpredictable/changing access**
9. **Standard-IA = known infrequent access + fast retrieval**
10. **One Zone-IA = cheaper + single-AZ risk**
11. **Glacier = archival storage**
12. **Lifecycle = automatically transition/delete objects**
13. **Versioning = recover from accidental overwrite/delete**
14. **Object Lock = WORM/compliance retention**
15. **Presigned URL = temporary private object access**
16. **Multipart upload = large object upload**
17. **Transfer Acceleration = faster long-distance S3 transfer**
18. **SSE-KMS = KMS-controlled encryption**
19. **EBS snapshot = EBS backup**
20. **Instance Store = ephemeral**
21. **gp3 = general-purpose SSD**
22. **io2 = high IOPS**
23. **st1 = throughput-oriented HDD**
24. **sc1 = cold/infrequent HDD**
25. **EFS = multiple instances sharing files**
26. **FSx Windows = Windows/SMB**
27. **FSx Lustre = HPC**
28. **File Gateway = on-prem file → S3**
29. **Volume Gateway = on-prem block storage**
30. **Tape Gateway = virtual tape**
31. **DataSync = online data transfer**
32. **Snow Family = offline/physical data transfer**

---

# 36. The 30-Second Storage Map

```text
                         STORAGE
                            |
          +-----------------+-----------------+
          |                 |                 |
        OBJECT            BLOCK             FILE
          |                 |                 |
         S3                EBS          +-----+------+
          |                              |            |
    Storage Classes                    EFS          FSx
    Versioning                          |        /    |    \
    Lifecycle                         Linux   Windows Lustre ONTAP...
    Replication                        NFS      SMB     HPC
    Object Lock
    Encryption
    Presigned URL

              HYBRID
                 |
          Storage Gateway
          /      |       \
       File    Volume    Tape

          MASSIVE MIGRATION
                 |
            Snow Family

          ONLINE TRANSFER
                 |
              DataSync
```

### The single most important distinction

> **S3 = object**
> **EBS = block**
> **EFS/FSx = file**

If you get that classification right, a surprisingly large portion of SAA storage questions becomes much easier.

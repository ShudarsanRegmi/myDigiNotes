# AWS SAA Final-Day Master Revision: Table of Contents

## 1. Compute

### 1.1 Amazon EC2

* What EC2 is
* Instance types and when to use them
* AMIs
* Instance lifecycle
* User data
* Instance metadata
* EBS vs instance store
* Security groups
* Key pairs
* Elastic IP
* Placement groups

  * Cluster
  * Spread
  * Partition
* Dedicated Hosts vs Dedicated Instances
* On-Demand vs Reserved vs Savings Plans vs Spot
* Burstable instances
* CPU credits
* Auto Scaling
* EC2 pricing concepts
* Shared responsibility
* Common exam traps

### 1.2 EC2 Auto Scaling

* Launch templates
* Desired/min/max capacity
* Scaling policies
* Target tracking
* Step scaling
* Scheduled scaling
* Dynamic scaling
* Health checks
* Instance replacement
* Multi-AZ Auto Scaling
* Scaling vs load balancing

### 1.3 Elastic Load Balancing

* ALB
* NLB
* GWLB
* CLB legacy awareness
* Layer 7 vs Layer 4
* Path-based routing
* Host-based routing
* Listener rules
* Target groups
* Health checks
* Cross-zone load balancing
* TLS termination
* Sticky sessions
* When to choose ALB vs NLB

### 1.4 AWS Lambda

* Serverless compute
* Invocation models
* Event-driven architecture
* Synchronous vs asynchronous invocation
* Concurrency
* Reserved vs provisioned concurrency
* Cold starts
* Lambda layers
* Environment variables
* Versions and aliases
* Execution role
* Timeout/memory
* Lambda + API Gateway
* Lambda + S3
* Lambda + EventBridge
* Lambda + SQS
* Lambda + DynamoDB
* Lambda limitations
* Common traps

### 1.5 Containers

* Amazon ECS
* ECS cluster
* Task definition
* Task
* Service
* ECS launch types
* EC2 vs Fargate
* ECS networking
* ECS Auto Scaling
* Amazon EKS
* EKS basic exam knowledge
* ECS vs EKS
* Fargate vs EC2

### 1.6 Other Compute

* AWS Batch
* Elastic Beanstalk
* Lightsail
* VMware Cloud on AWS
* Compute decision patterns

---

# 2. Storage

### 2.1 Amazon S3

* Object storage
* Buckets and objects
* Storage classes
* Standard
* Intelligent-Tiering
* Standard-IA
* One Zone-IA
* Glacier Instant Retrieval
* Glacier Flexible Retrieval
* Glacier Deep Archive
* Lifecycle policies
* Versioning
* Object Lock
* Replication
* Cross-Region Replication
* Same-Region Replication
* Encryption
* SSE-S3
* SSE-KMS
* SSE-C
* Bucket policies
* ACL awareness
* Block Public Access
* Presigned URLs
* Multipart upload
* Transfer Acceleration
* S3 event notifications
* S3 static website hosting
* S3 consistency
* S3 performance
* Common exam traps

### 2.2 Amazon EBS

* Block storage
* Volume types
* gp3
* gp2
* io2
* st1
* sc1
* Magnetic awareness
* IOPS vs throughput
* Snapshots
* Encryption
* Availability characteristics
* EBS vs instance store
* EBS resizing

### 2.3 Amazon EFS

* File storage
* NFS
* Multi-AZ
* Elastic scaling
* Performance modes
* Throughput modes
* EFS vs EBS
* EFS vs S3

### 2.4 Amazon FSx

* FSx for Windows File Server
* FSx for Lustre
* FSx for NetApp ONTAP
* FSx for OpenZFS
* When each makes sense

### 2.5 Storage Gateway

* File Gateway
* Volume Gateway
* Tape Gateway
* Hybrid cloud storage
* On-premises integration

### 2.6 Snow Family

* Snowcone
* Snowball
* Snowmobile
* Offline data migration
* Edge computing

---

# 3. Databases

### 3.1 Amazon RDS

* Managed relational database
* Supported engines
* Multi-AZ
* Read replicas
* Automated backups
* Manual snapshots
* Point-in-time recovery
* Encryption
* Maintenance
* Failover
* Scaling
* Storage
* RDS vs EC2 database

### 3.2 Amazon Aurora

* Aurora architecture
* Aurora storage
* Multi-AZ
* Read replicas
* Aurora Serverless
* Global Database
* Aurora vs standard RDS

### 3.3 DynamoDB

* NoSQL
* Tables/items/attributes
* Partition key
* Composite key
* Query vs Scan
* GSI
* LSI
* Provisioned vs on-demand capacity
* Read/write capacity
* Eventually consistent vs strongly consistent reads
* DynamoDB Streams
* TTL
* Global Tables
* Transactions
* DAX
* Hot partitions
* Common exam patterns

### 3.4 ElastiCache

* Redis/Valkey concepts
* Memcached
* Caching
* Session storage
* Read-heavy workloads
* Redis vs Memcached
* Cluster mode
* Multi-AZ
* ElastiCache vs DynamoDB DAX

### 3.5 Other Databases

* Neptune
* DocumentDB
* Keyspaces
* Timestream
* MemoryDB
* Database selection patterns

---

# 4. Networking

This is **extremely high priority** for SAA.

### 4.1 VPC Fundamentals

* VPC
* CIDR
* Subnets
* Public vs private subnet
* Route tables
* Main route table
* Internet Gateway
* NAT Gateway
* NAT instance awareness
* Network interfaces
* Availability Zones

### 4.2 Routing

* Local routes
* Default routes
* Longest prefix matching
* Public IP routing
* Private subnet routing
* NAT routing
* Route propagation

### 4.3 Security

* Security Groups
* Network ACLs
* Stateful vs stateless
* Inbound/outbound rules
* Ephemeral ports
* SG vs NACL

### 4.4 VPC Connectivity

* VPC Peering
* Transit Gateway
* AWS PrivateLink
* VPC endpoints
* Gateway endpoints
* Interface endpoints
* Site-to-Site VPN
* Direct Connect
* Direct Connect Gateway
* Client VPN
* Transit Gateway vs VPC Peering

### 4.5 DNS

* Route 53
* Hosted zones
* Public vs private hosted zones
* Record types
* Alias
* CNAME
* Routing policies

  * Simple
  * Weighted
  * Latency
  * Failover
  * Geolocation
  * Geoproximity
  * Multi-value answer
* Health checks

### 4.6 CloudFront

* CDN
* Edge locations
* Origins
* Behaviors
* Cache policies
* TTL
* Cache invalidation
* Origin Access Control
* HTTPS
* CloudFront + S3
* CloudFront + ALB
* Regional edge caches

### 4.7 Global Accelerator

* Static Anycast IP
* Global application acceleration
* TCP/UDP
* Health checks
* Global Accelerator vs CloudFront

---

# 5. Security and Identity

### 5.1 IAM

* Users
* Groups
* Roles
* Policies
* Managed vs inline policies
* Identity-based policies
* Resource-based policies
* Explicit deny
* Policy evaluation
* Least privilege
* IAM roles
* Temporary credentials
* Cross-account access
* IAM policy conditions
* Federation
* IAM Identity Center

### 5.2 AWS Organizations

* Organizations
* Accounts
* Organizational Units
* Service Control Policies
* Consolidated billing
* SCP vs IAM policy

### 5.3 KMS

* Customer managed keys
* AWS managed keys
* Envelope encryption
* Key policies
* Grants
* Automatic rotation
* KMS vs Secrets Manager
* KMS vs CloudHSM

### 5.4 Secrets and Certificates

* Secrets Manager
* Systems Manager Parameter Store
* ACM
* Certificate management
* Secrets Manager vs Parameter Store

### 5.5 Network Security

* AWS WAF
* AWS Shield
* Shield Standard vs Advanced
* AWS Firewall Manager
* Network Firewall
* DDoS protection
* WAF vs Network Firewall

### 5.6 Monitoring Security

* GuardDuty
* Inspector
* Macie
* Security Hub
* Detective
* Trusted Advisor security checks

---

# 6. Messaging and Application Integration

### 6.1 SQS

* Queue
* Standard queue
* FIFO queue
* Visibility timeout
* Long polling
* Dead-letter queue
* Message retention
* Delay queues
* Duplicate messages
* At-least-once delivery
* Exactly-once processing concepts
* Scaling consumers

### 6.2 SNS

* Pub/Sub
* Topics
* Subscribers
* Fan-out
* Filtering
* SQS + SNS architecture
* SNS vs SQS

### 6.3 EventBridge

* Event-driven architecture
* Event buses
* Rules
* Event patterns
* Targets
* Scheduled events
* SaaS integrations
* EventBridge vs SNS
* EventBridge vs SQS

### 6.4 Step Functions

* Workflow orchestration
* State machines
* Standard vs Express
* Retry
* Catch
* Parallel
* Choice
* Wait

---

# 7. Monitoring, Logging and Management

### 7.1 CloudWatch

* Metrics
* Logs
* Alarms
* Dashboards
* Events/EventBridge distinction
* Logs Insights
* Agent
* Custom metrics
* Metric filters

### 7.2 CloudTrail

* API activity
* Management events
* Data events
* Audit trail
* Organization trails
* CloudTrail vs CloudWatch

### 7.3 AWS Config

* Resource configuration
* Compliance
* Configuration history
* Rules
* Remediation
* Config vs CloudTrail

### 7.4 Systems Manager

* Parameter Store
* Session Manager
* Patch Manager
* Run Command
* Automation
* Fleet Manager

### 7.5 Other Management

* Trusted Advisor
* Service Health Dashboard
* AWS Health
* Compute Optimizer

---

# 8. Application Deployment

### 8.1 Elastic Beanstalk

* Managed application deployment
* Environment
* Platform
* Scaling
* Load balancing
* Deployment strategies

### 8.2 Code Services

* CodeCommit awareness
* CodeBuild
* CodeDeploy
* CodePipeline
* CodeArtifact
* CI/CD concepts

### 8.3 Deployment Strategies

* Rolling
* Rolling with additional batch
* Immutable
* Blue/green
* Canary
* All-at-once

---

# 9. Serverless Architecture

This deserves its own revision because questions often combine services.

* Lambda
* API Gateway
* DynamoDB
* S3
* CloudFront
* EventBridge
* SQS
* SNS
* Step Functions
* Cognito
* Serverless reference architectures
* API Gateway REST vs HTTP API
* API Gateway throttling
* Lambda authorizers
* Cognito authentication
* Caching
* Event-driven architecture

---

# 10. Analytics and Data Processing

Only **exam-level recognition** is needed.

* Athena
* Redshift
* EMR
* Glue
* Kinesis

  * Data Streams
  * Firehose
  * Analytics awareness
* OpenSearch
* Lake Formation
* QuickSight
* Data lake architecture
* Athena vs Redshift
* Kinesis vs SQS
* Glue vs EMR

---

# 11. Migration and Hybrid Architecture

### Migration

* Migration Hub
* Application Migration Service
* Database Migration Service
* Schema Conversion Tool
* DataSync
* Transfer Family

### Hybrid

* Direct Connect
* VPN
* Storage Gateway
* Outposts
* Local Zones
* Wavelength

### Migration Strategies

* Rehost
* Replatform
* Refactor
* Repurchase
* Retire
* Retain

---

# 12. Disaster Recovery and Business Continuity

**Very high exam value.**

* Backup and restore
* Pilot light
* Warm standby
* Multi-site active/active
* RTO
* RPO
* Cost vs recovery speed
* Cross-Region replication
* S3 replication
* RDS replication
* Aurora Global Database
* DynamoDB Global Tables
* Route 53 failover
* AWS Backup
* Elastic Disaster Recovery

---

# 13. High Availability and Resilience

This section is less about individual services and more about **architecture questions**.

* Single AZ vs Multi-AZ
* Multi-Region
* Stateless architecture
* Stateful architecture
* Horizontal vs vertical scaling
* Fault tolerance
* Automatic failover
* Health checks
* Self-healing
* Decoupling
* Redundancy
* Retry
* Backoff
* Idempotency
* Queue-based architecture
* Distributed systems basics

---

# 14. Cost Optimization

**Extremely common in SAA questions.**

* Cost Explorer
* AWS Budgets
* Cost and Usage Report
* Savings Plans
* Reserved Instances
* Spot Instances
* On-Demand
* S3 storage classes
* Lifecycle policies
* Data transfer costs
* NAT Gateway costs
* VPC endpoint cost considerations
* Right-sizing
* Auto Scaling
* Serverless cost model
* Reserved capacity
* Consolidated billing
* Cost allocation tags

---

# 15. Architecture Patterns and Exam Decision Trees

This is where we convert everything into **“If the question says X, think Y.”**

### Compute

> EC2 vs Lambda vs ECS vs Fargate vs Beanstalk

### Storage

> S3 vs EBS vs EFS vs FSx

### Database

> RDS vs Aurora vs DynamoDB vs ElastiCache

### Networking

> NAT Gateway vs Internet Gateway vs VPC Endpoint vs PrivateLink

### Connectivity

> VPC Peering vs Transit Gateway vs VPN vs Direct Connect

### Messaging

> SQS vs SNS vs EventBridge vs Kinesis

### CDN / Global

> CloudFront vs Global Accelerator vs Route 53

### Security

> WAF vs Shield vs Network Firewall vs Security Group vs NACL

### Identity

> IAM role vs IAM user vs resource policy vs SCP

### Monitoring

> CloudWatch vs CloudTrail vs Config

### Disaster Recovery

> Backup/restore vs pilot light vs warm standby vs active/active

---

# 16. SAA Exam Traps and “Keyword → Service” Recognition

Finally, we'll maintain a compact mental dictionary like:

| If the question says...            | Think...                                                |
| ---------------------------------- | ------------------------------------------------------- |
| Object storage                     | S3                                                      |
| Shared file system across AZs      | EFS                                                     |
| Windows file system                | FSx for Windows                                         |
| High-performance HPC filesystem    | FSx for Lustre                                          |
| Block storage                      | EBS                                                     |
| Temporary high-speed local storage | Instance Store                                          |
| Serverless compute                 | Lambda                                                  |
| Container without managing servers | Fargate                                                 |
| Layer 7 load balancing             | ALB                                                     |
| Layer 4 / static IP                | NLB                                                     |
| Pub/sub fan-out                    | SNS                                                     |
| Decouple applications              | SQS                                                     |
| Event-driven routing               | EventBridge                                             |
| Managed relational DB              | RDS                                                     |
| Serverless NoSQL                   | DynamoDB                                                |
| Database caching                   | ElastiCache                                             |
| Global DNS routing                 | Route 53                                                |
| CDN                                | CloudFront                                              |
| DDoS                               | Shield                                                  |
| Web application filtering          | WAF                                                     |
| API audit trail                    | CloudTrail                                              |
| Resource compliance                | Config                                                  |
| Metrics/alarms                     | CloudWatch                                              |
| Secrets                            | Secrets Manager                                         |
| Encryption keys                    | KMS                                                     |
| Hybrid dedicated connection        | Direct Connect                                          |
| Private AWS service access         | VPC Endpoint                                            |
| Cross-VPC connectivity at scale    | Transit Gateway                                         |
| Cheapest interruptible compute     | Spot                                                    |
| Predictable compute usage          | Savings Plans / Reserved                                |
| Disaster recovery                  | AWS Backup / DRS / replication depending on requirement |

---

## The order I'd recommend for today

Don't study these in random order. Use this sequence:

**1. Networking**
**2. EC2 + Auto Scaling + ELB**
**3. S3 + EBS + EFS**
**4. RDS + Aurora + DynamoDB**
**5. IAM + KMS + security services**
**6. Lambda + API Gateway + serverless**
**7. SQS + SNS + EventBridge**
**8. Route 53 + CloudFront + Global Accelerator**
**9. DR + HA + resilience**
**10. Monitoring + management**
**11. Cost optimization**
**12. Containers + remaining services**
**13. Final architecture decision trees + exam traps**

For **each section**, I'll keep the format deliberately terse:

> **Service → What it is → When to use → Key features → Important limits/behaviors → Comparisons → Architecture patterns → Exam traps → Keywords**

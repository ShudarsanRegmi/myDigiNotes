<img width="1223" height="1286" alt="image" src="https://github.com/user-attachments/assets/cac5c9a1-f692-476a-8f6b-abfac7dd8c62" />



# Part V: Monitoring, Logging & Management

This section is comparatively smaller, but **CloudWatch vs CloudTrail vs Config** is a classic SAA distinction. The key is understanding **what is being observed**.

Mental model:

```text
What is happening?
        |
   +----+----------------+----------------+
   |                     |                |
Metrics / Logs         API activity    Configuration
   |                     |                |
CloudWatch            CloudTrail        Config
   |
Alarms / Dashboards
```

---

# 1. Amazon CloudWatch

## What is it?

**CloudWatch = monitoring and observability service.**

It collects and monitors:

* Metrics
* Logs
* Events
* Application/system performance

Think:

> **"How is my application/infrastructure performing?" → CloudWatch**

---

## CloudWatch Metrics

Numerical measurements over time.

Examples:

* EC2 CPU utilization
* Network traffic
* Lambda invocations
* Lambda errors
* RDS connections
* Application latency

Example:

```text
CPU = 85%
        ↓
CloudWatch Alarm
        ↓
Auto Scaling
        ↓
Launch EC2
```

### Exam trigger

> "Scale when CPU utilization exceeds 70%."

→ **CloudWatch metric + alarm + Auto Scaling**

---

# 2. CloudWatch Alarms

An alarm watches a metric and changes state based on a threshold.

Example:

```text
CPU > 80%
   ↓
CloudWatch Alarm
   ↓
SNS / Auto Scaling / other action
```

Common uses:

* Trigger Auto Scaling
* Send SNS notification
* Monitor application health
* Detect abnormal behavior

### Important

CloudWatch doesn't merely **store metrics**. It can actively trigger actions through alarms.

---

# 3. CloudWatch Logs

Collects logs from:

* EC2
* Lambda
* Applications
* Containers
* AWS services

Useful for:

* Troubleshooting
* Error analysis
* Application debugging
* Centralized logging

### Log Groups / Log Streams

Think:

```text
Log Group
   ├── Stream 1
   ├── Stream 2
   └── Stream 3
```

A log group commonly represents an application/service, while streams separate sources or instances.

---

# 4. CloudWatch Logs Insights

Allows querying and analyzing CloudWatch logs.

Exam trigger:

> "Search/analyze application logs to identify errors."

→ **CloudWatch Logs Insights**

---

# 5. CloudWatch Dashboards

Provides visual monitoring of:

* Metrics
* Graphs
* Alarms
* Resource health

Think:

> **"Give operations team a single monitoring view." → CloudWatch Dashboard**

---

# 6. CloudWatch Custom Metrics

AWS provides many default metrics, but applications can publish their own.

Example:

```text
Application
   ↓
Custom Metric
   ↓
CloudWatch
   ↓
Alarm
```

Examples:

* Number of orders
* Queue processing time
* Application-specific errors
* Active users

---

# 7. CloudWatch Agent

Used to collect additional information from EC2, such as:

* Memory utilization
* Disk usage
* Logs

### Exam trap

EC2's standard CloudWatch metrics don't automatically give you every OS-level metric.

If you need things like:

> **Memory utilization**

think:

**CloudWatch Agent**

---

# 8. CloudTrail

**CloudTrail = API activity/auditing.**

It answers:

> **"Who did what, when, and from where?"**

Example:

```text
User
 ↓
Delete S3 Bucket
 ↓
CloudTrail
 ↓
Audit record
```

Records AWS API activity such as:

* IAM changes
* EC2 actions
* S3 API activity
* Security configuration changes
* Console/API/CLI activity

---

# 9. CloudTrail Events

Two broad categories worth knowing:

### Management Events

Control-plane operations.

Examples:

* Create EC2 instance
* Create IAM user
* Modify security group
* Create VPC

### Data Events

Data-plane operations.

Examples:

* S3 object-level operations
* Lambda function invocation

### Exam trap

Don't assume every data access is automatically logged in the same way as management activity. For certain high-volume data events, you explicitly configure CloudTrail logging.

---

# 10. CloudTrail Organization Trail

AWS Organizations can use a centralized CloudTrail trail across accounts.

Useful for:

> **Centralized auditing across an AWS organization.**

Exam keyword:

> "Audit API activity across all AWS accounts."

→ **Organization CloudTrail trail**

---

# 11. CloudTrail vs CloudWatch

This distinction is **must memorize**.

| Question                      | Service        |
| ----------------------------- | -------------- |
| How is the system performing? | **CloudWatch** |
| CPU utilization?              | CloudWatch     |
| Application logs?             | CloudWatch     |
| Trigger scaling?              | CloudWatch     |
| Who deleted the resource?     | **CloudTrail** |
| Who changed IAM?              | CloudTrail     |
| What API call happened?       | CloudTrail     |
| Audit AWS activity?           | CloudTrail     |

### Mental shortcut

> **CloudWatch = Watch the system**

> **CloudTrail = Track the API trail**

---

# 12. AWS Config

**AWS Config = resource configuration and compliance.**

It answers:

> **"What is the configuration/state of my AWS resources, and does it comply with my rules?"**

Examples:

* Is an S3 bucket public?
* Does an EC2 instance have a particular configuration?
* Is encryption enabled?
* Does a security group violate policy?

---

# 13. Config Rules

Rules evaluate resource configurations.

Example:

```text
Security Group
      ↓
Config Rule
      ↓
"Port 22 open to 0.0.0.0/0?"
      ↓
NON-COMPLIANT
```

Useful for:

* Compliance
* Governance
* Security posture
* Automated configuration checking

---

# 14. AWS Config vs CloudTrail

Another **extremely important distinction**.

### CloudTrail

> **What API activity happened?**

Example:

> "Who changed the security group?"

→ CloudTrail

### Config

> **What is the resource configuration?**

Example:

> "Is this security group currently allowing SSH from the Internet?"

→ Config

---

# 15. AWS Config Remediation

Config can be combined with remediation actions.

Example:

```text
Config Rule
    ↓
Non-compliant
    ↓
Remediation
    ↓
Fix configuration
```

Useful for:

> Automatically correcting configuration violations.

---

# 16. Systems Manager

**AWS Systems Manager = operational management of AWS infrastructure.**

Think:

> **"I need to manage my fleet of servers centrally."**

Major capabilities:

* Session Manager
* Parameter Store
* Run Command
* Patch Manager
* Automation
* Fleet Manager

---

# 17. Systems Manager Session Manager

Allows you to connect to EC2 instances without traditional SSH/RDP access.

Architecture:

```text
Administrator
      ↓
Session Manager
      ↓
EC2
```

Advantages:

* No need to expose SSH port 22
* No need to manage SSH keys
* Centralized access control
* Can log sessions

### Exam trigger

> "Administrators need secure shell access to private EC2 instances without opening port 22."

→ **Systems Manager Session Manager**

This is a **very common SAA scenario**.

---

# 18. Systems Manager Parameter Store

Stores configuration values and parameters.

Examples:

```text
DB_HOST
API_ENDPOINT
ENVIRONMENT
```

Can also store encrypted sensitive values using KMS.

### Parameter Store vs Secrets Manager

**Parameter Store**

→ Configuration + parameters

**Secrets Manager**

→ Secrets + credential lifecycle/rotation

For database passwords requiring automated rotation:

→ **Secrets Manager**

---

# 19. Systems Manager Run Command

Execute commands across managed instances without logging into each one manually.

Example:

```text
100 EC2 instances
       ↓
Run Command
       ↓
"Install security update"
```

Useful for:

* Fleet administration
* Running scripts
* Operational tasks

---

# 20. Systems Manager Patch Manager

Automates patching of managed instances.

Think:

> **"Patch a fleet of servers according to policy."**

→ Patch Manager

---

# 21. Systems Manager Automation

Automates common AWS operational tasks.

Can perform multi-step workflows such as:

```text
Detect issue
   ↓
Stop instance
   ↓
Modify configuration
   ↓
Restart
```

---

# 22. Trusted Advisor

Provides recommendations related to:

* Cost optimization
* Performance
* Security
* Fault tolerance
* Service limits

Think:

> **"How can I improve my AWS environment?"**

→ **Trusted Advisor**

---

# 23. AWS Health

Provides information about:

* AWS service events
* Account-specific issues
* Scheduled maintenance
* Service disruptions

Think:

> **"Is AWS itself having an issue affecting my resources?"**

→ **AWS Health**

---

# 24. Service Health Dashboard

Provides broad public information about AWS service availability.

Difference at high level:

**Service Health Dashboard**

→ General AWS service status

**AWS Health Dashboard**

→ Personalized/account-specific events + broader health information

---

# 25. Compute Optimizer

Provides recommendations for resource sizing.

Examples:

* EC2 instance types
* EBS volumes
* Lambda configurations

Think:

> **"Is this resource over-provisioned or under-provisioned?"**

→ **Compute Optimizer**

---

# 26. Famous Monitoring Architecture Patterns

## Pattern 1: Automatic scaling

```text
EC2
 ↓
CloudWatch Metric
 ↓
CloudWatch Alarm
 ↓
Auto Scaling
 ↓
More/Fewer EC2
```

**Performance → scaling**

---

## Pattern 2: Centralized application logs

```text
EC2 / Lambda / App
       ↓
CloudWatch Logs
       ↓
Logs Insights
       ↓
Troubleshooting
```

---

## Pattern 3: API auditing

```text
AWS Account
     ↓
CloudTrail
     ↓
S3 / CloudWatch Logs
     ↓
Security / Audit
```

---

## Pattern 4: Configuration compliance

```text
AWS Resources
      ↓
AWS Config
      ↓
Config Rules
      ↓
Compliant / Non-compliant
      ↓
Remediation
```

---

## Pattern 5: Private EC2 administration

```text
Administrator
      ↓
Session Manager
      ↓
Private EC2
```

No public SSH exposure required.

---

# 27. The Big Three

This is the part you **must know cold**:

```text
                    MONITORING
                         |
             +-----------+-----------+
             |           |           |
          CloudWatch  CloudTrail    Config
             |           |           |
         Performance    API        Configuration
          & Logs       Activity     & Compliance
             |           |           |
          "How?"      "Who?"       "What?"
```

### Example question:

**"CPU utilization is consistently above 80%."**

→ CloudWatch

**"Who modified the security group?"**

→ CloudTrail

**"Which security groups currently violate our policy?"**

→ Config

---

# 28. Service Decision Table

| Requirement                       | Service                  |
| --------------------------------- | ------------------------ |
| Metrics                           | CloudWatch               |
| Logs                              | CloudWatch Logs          |
| Alarms                            | CloudWatch               |
| Dashboards                        | CloudWatch               |
| Analyze logs                      | CloudWatch Logs Insights |
| Custom application metrics        | CloudWatch               |
| OS memory/disk metrics            | CloudWatch Agent         |
| API auditing                      | CloudTrail               |
| "Who did what?"                   | CloudTrail               |
| Organization-wide API audit       | CloudTrail               |
| Resource configuration            | AWS Config               |
| Compliance rules                  | AWS Config               |
| Configuration remediation         | AWS Config               |
| Secure EC2 shell access           | Session Manager          |
| Run command across fleet          | Systems Manager          |
| Patch fleet                       | Patch Manager            |
| Configuration parameters          | Parameter Store          |
| Secret management/rotation        | Secrets Manager          |
| AWS best-practice recommendations | Trusted Advisor          |
| AWS/account health events         | AWS Health               |
| Resource right-sizing             | Compute Optimizer        |

---

# 29. Exam Traps

1. **CloudWatch ≠ CloudTrail**
2. CloudWatch → **performance/metrics/logs**
3. CloudTrail → **API activity/audit**
4. Config → **resource configuration/compliance**
5. **"Who changed it?" → CloudTrail**
6. **"What is its current configuration?" → Config**
7. **"How is it performing?" → CloudWatch**
8. CloudWatch Alarm can trigger Auto Scaling.
9. CloudWatch Agent can collect memory/disk metrics.
10. Session Manager can access private EC2 without exposing SSH.
11. Parameter Store → configuration parameters.
12. Secrets Manager → secrets and credential rotation.
13. Run Command → execute commands across instances.
14. Patch Manager → patch fleet.
15. Trusted Advisor → optimization recommendations.
16. AWS Health → account/service health events.
17. Compute Optimizer → right-sizing recommendations.

---

# 30. 30-Second Memory Map

```text id="1i9o3q"
                 OPERATIONS
                     |
       +-------------+-------------+
       |             |             |
   CloudWatch     CloudTrail     Config
       |             |             |
   Performance      Audit       Compliance
   Metrics          API         Configuration
   Logs             Activity
   Alarms
       |
   Auto Scaling

              SYSTEMS MANAGER
                     |
       +-------------+-------------+
       |             |             |
   Session       Run Command    Patch Manager
   Manager
       |
   Private EC2
   without SSH

              OTHER
       ├─ Parameter Store → Config
       ├─ Secrets Manager → Secrets
       ├─ Trusted Advisor → Recommendations
       ├─ AWS Health → AWS issues
       └─ Compute Optimizer → Right-sizing
```

### If you have only 2 minutes before the exam

Memorize this:

> **CloudWatch = What is happening/performance?**

> **CloudTrail = Who did what?**

> **Config = What is configured, and is it compliant?**

> **Systems Manager = Manage the fleet**

> **Session Manager = Securely access private EC2**

> **Parameter Store = Configuration**

> **Secrets Manager = Secrets + rotation**

> **Trusted Advisor = Recommendations**

That distinction alone covers a substantial portion of the monitoring/management questions you'll encounter.

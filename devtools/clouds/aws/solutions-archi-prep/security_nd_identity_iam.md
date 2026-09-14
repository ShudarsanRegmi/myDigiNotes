<img width="1223" height="1286" alt="image" src="https://github.com/user-attachments/assets/1a9eb553-5107-45ec-93f0-66bab3722810" />


## #5 Security & Identity

For SAA, don't try to memorize every security service. The exam mostly tests **which security control/service fits a particular requirement**.

### Mental model

> **Identity → Permissions → Encryption → Network protection → Threat detection → Governance**

---

# 1. IAM — Identity & Access Management

IAM answers:

> **Who can access what, and what can they do?**

### IAM Users

Represents a person/application identity with long-term credentials.

### IAM Groups

Collection of users.

```text
Users → Group → Permissions
```

Groups **cannot contain other groups**.

### IAM Roles ⭐⭐⭐

Roles provide **temporary credentials**.

Common cases:

```text
EC2 ──assume role──> IAM Role ──> S3
Lambda ──assume role──> IAM Role ──> DynamoDB
Account A ──assume role──> Account B
```

**Exam rule:**

> EC2/Lambda/application needs AWS access → **IAM Role**, not hard-coded access keys.

---

# 2. IAM Policies ⭐⭐⭐

JSON documents defining permissions.

```text
Principal → Action → Resource
```

Example concept:

```text
Allow
s3:GetObject
bucket/object
```

### Identity-based policy

Attached to:

* User
* Group
* Role

### Resource-based policy

Attached to the resource:

* S3 bucket policy
* SQS queue policy
* SNS topic policy
* KMS key policy

### Explicit Deny ⭐⭐⭐

The most important IAM evaluation rule:

> **Explicit Deny overrides Allow.**

```text
Explicit Deny
      ↓
    DENIED
```

Also remember:

> By default, everything is denied unless an applicable policy allows it.

---

# 3. IAM Policy Conditions

Conditions allow more precise access.

Examples:

* Source IP
* VPC endpoint
* MFA
* AWS account
* Tags
* Encryption requirements

Very common exam pattern:

> "Allow S3 access only through a specific VPC endpoint"

→ **S3 bucket policy + condition**

---

# 4. IAM Best Practices ⭐⭐⭐

Know these extremely well:

* **Least privilege**
* Use **roles** instead of long-term credentials
* Enable MFA for privileged users
* Avoid root user for normal operations
* Rotate credentials when credentials must exist
* Use temporary credentials wherever possible
* Use IAM Access Analyzer to identify unintended access

### Root user

Root has complete account access.

Use it only for tasks requiring root credentials.

---

# 5. IAM Identity Center

Used for **centralized workforce access** to multiple AWS accounts.

```text
Employee
   ↓
IAM Identity Center
   ↓
AWS Account A
AWS Account B
AWS Account C
```

Useful with:

* AWS Organizations
* Multiple AWS accounts
* SSO
* Corporate identity providers

### IAM vs IAM Identity Center

| Requirement                  | Use                 |
| ---------------------------- | ------------------- |
| AWS permissions for workload | IAM Role            |
| Individual AWS identity      | IAM                 |
| Employee SSO across accounts | IAM Identity Center |

---

# 6. AWS Organizations + SCP ⭐⭐⭐

Organizations manages multiple AWS accounts.

```text
Organization
 ├── Security Account
 ├── Production
 ├── Development
 └── Testing
```

### Service Control Policy (SCP)

SCP defines the **maximum permissions** available to accounts/OUs.

Important:

> **SCP does NOT grant permissions.**

Think:

```text
SCP
 ↓
Maximum allowed permissions

IAM Policy
 ↓
Actual permissions
```

Both must permit the action.

### Classic exam trap

> "Prevent all accounts from using a particular AWS service."

→ **SCP**

Not IAM policy individually in every account.

---

# 7. KMS — Key Management Service ⭐⭐⭐

KMS manages encryption keys.

Used for:

* S3
* EBS
* RDS
* EFS
* Secrets Manager
* many other AWS services

Mental model:

```text
Data
 ↓
Encryption
 ↓
KMS key
```

### AWS managed vs Customer managed keys

**AWS managed key**

* Managed by AWS
* Less control

**Customer managed KMS key**

* You control policies/configuration
* More control over key lifecycle

---

# 8. Envelope Encryption ⭐⭐

You don't generally encrypt huge datasets directly with KMS.

Instead:

```text
KMS
 ↓
Data Key
 ↓
Encrypt large data
```

The data key encrypts the actual data, while KMS protects the data key.

This is called **envelope encryption**.

---

# 9. Secrets Manager vs Parameter Store ⭐⭐⭐

Very common comparison.

### Secrets Manager

For:

* DB passwords
* API keys
* credentials
* secret rotation

Important feature:

> **Automatic secret rotation**

### Systems Manager Parameter Store

For:

* configuration
* parameters
* environment values
* simple secrets

Can integrate with KMS for encryption.

| Requirement                      | Answer              |
| -------------------------------- | ------------------- |
| DB password + automatic rotation | **Secrets Manager** |
| Application configuration        | **Parameter Store** |
| Temporary AWS credentials        | **IAM Role**        |

---

# 10. S3 Security ⭐⭐⭐

Know these:

### Block Public Access

Prevents accidental public exposure.

### Bucket Policy

Resource-based access control.

### IAM Policy

Identity-based access control.

### S3 Object Ownership

Useful when controlling ownership of uploaded objects.

### Encryption

Common choices:

```text
SSE-S3
SSE-KMS
SSE-C
Client-side encryption
```

If the requirement says:

> "Need control/audit of encryption keys"

→ **SSE-KMS**

---

# 11. AWS WAF ⭐⭐⭐

**Web Application Firewall**

Protects web applications against Layer 7 attacks.

Common protections:

* SQL injection
* XSS
* malicious HTTP requests
* IP blocking
* rate limiting
* geographic restrictions

Can associate with:

* CloudFront
* Application Load Balancer
* API Gateway

Mental model:

```text
Internet
   ↓
 WAF
   ↓
 ALB / CloudFront / API Gateway
   ↓
 Application
```

### WAF ≠ Security Group

Security Group:

> Network-level stateful firewall

WAF:

> HTTP/HTTPS application-layer protection

---

# 12. AWS Shield ⭐⭐

DDoS protection.

### Shield Standard

Automatically provides basic DDoS protection.

### Shield Advanced

Enhanced DDoS protection for critical applications.

Provides additional visibility/protection and DDoS response capabilities.

### Exam distinction

```text
SQL Injection / XSS
        ↓
       WAF

DDoS
        ↓
      Shield
```

They can be used together.

---

# 13. AWS Network Firewall

Managed **network firewall** for VPC traffic.

Useful for:

* centralized traffic inspection
* stateful/stateless filtering
* deep network traffic controls
* controlling traffic between networks

Think:

```text
VPC
 ↓
AWS Network Firewall
 ↓
Internet / other networks
```

Don't confuse it with WAF:

|             | Network Firewall  | WAF           |
| ----------- | ----------------- | ------------- |
| Layer       | Network           | Application   |
| Main target | VPC traffic       | HTTP/HTTPS    |
| Example     | Network filtering | SQL injection |

---

# 14. GuardDuty ⭐⭐⭐

Threat detection service.

Analyzes sources such as:

* CloudTrail
* VPC Flow Logs
* DNS logs
* S3 activity
* runtime signals

Detects suspicious activity.

Examples:

> Compromised credentials, unusual API activity, malicious IP communication.

Mental model:

```text
AWS activity
     ↓
 GuardDuty
     ↓
 Threat finding
```

**GuardDuty = threat detection**

Not a firewall.

---

# 15. Amazon Inspector ⭐⭐⭐

Automated vulnerability management.

Looks for vulnerabilities in things such as:

* EC2
* container images
* Lambda

Example:

> "Find vulnerable packages on my EC2 instances."

→ **Inspector**

---

# 16. Amazon Macie ⭐⭐

Discovers and protects **sensitive data in S3**.

Especially:

* PII
* credentials
* sensitive information

Example:

> "Identify S3 buckets containing personally identifiable information."

→ **Macie**

Easy memory:

> **Macie = sensitive data**

---

# 17. AWS Security Hub ⭐⭐

Central security findings/dashboard.

```text
GuardDuty ─────┐
Inspector ─────┤
Macie ─────────┼──> Security Hub
Config ────────┘
```

Think:

> **Security Hub = centralized view of security findings**

It doesn't replace GuardDuty/Inspector/Macie.

---

# 18. Amazon Detective

Used to **investigate security findings**.

A useful distinction:

```text
GuardDuty
"Something suspicious happened."

Detective
"Let's investigate what happened."
```

---

# 19. AWS Config

You already saw Config in Monitoring.

Security perspective:

> **Is my infrastructure configured according to security/compliance rules?**

Examples:

* S3 bucket publicly accessible?
* Security group allows `0.0.0.0/0` on SSH?
* EBS volumes encrypted?
* Required tags present?

```text
Resource
 ↓
AWS Config
 ↓
Configuration/compliance
```

### Config vs GuardDuty

| Requirement                    | Service       |
| ------------------------------ | ------------- |
| Detect malicious activity      | **GuardDuty** |
| Check configuration compliance | **Config**    |
| Investigate security incident  | **Detective** |

---

# 20. Cognito ⭐⭐

Cognito is primarily for **application users**, not AWS administrators.

```text
Mobile/Web App
      ↓
   Cognito
      ↓
User authentication
```

### User Pools

Authentication:

* Sign-up
* Sign-in
* Password management
* MFA
* Federation

### Identity Pools

Provide users with **temporary AWS credentials** to access AWS resources.

```text
Application user
      ↓
Cognito Identity Pool
      ↓
Temporary AWS credentials
      ↓
S3 / DynamoDB / etc.
```

### Exam distinction

> "Users need to sign in to my web/mobile application."

→ **Cognito User Pool**

> "Authenticated users need temporary AWS credentials."

→ **Cognito Identity Pool**

---

# 21. Shared Responsibility Model ⭐⭐⭐

This is fundamental.

AWS is responsible for:

> **Security OF the cloud**

You are responsible for:

> **Security IN the cloud**

Example:

### EC2

AWS:

* physical datacenter
* physical hardware
* underlying infrastructure

You:

* OS patching
* security groups
* IAM
* application
* data

### S3

AWS manages infrastructure.

You manage:

* bucket policies
* access
* encryption configuration
* data

---

# 22. Security Service Cheat Sheet

| Requirement                          | Service                 |
| ------------------------------------ | ----------------------- |
| AWS identities/permissions           | **IAM**                 |
| Temporary AWS credentials            | **IAM Role**            |
| SSO across AWS accounts              | **IAM Identity Center** |
| Restrict maximum account permissions | **SCP**                 |
| Encryption keys                      | **KMS**                 |
| Secrets + automatic rotation         | **Secrets Manager**     |
| Configuration parameters             | **Parameter Store**     |
| Web application firewall             | **WAF**                 |
| DDoS protection                      | **Shield**              |
| VPC network firewall                 | **Network Firewall**    |
| Threat detection                     | **GuardDuty**           |
| Vulnerability scanning               | **Inspector**           |
| Sensitive data in S3                 | **Macie**               |
| Central security findings            | **Security Hub**        |
| Investigate security incidents       | **Detective**           |
| Configuration compliance             | **Config**              |
| Application user authentication      | **Cognito**             |

---

# 23. Famous Exam Architecture Patterns

### Pattern 1: Secure Web Application

```text
Internet
   ↓
CloudFront
   ↓
 WAF
   ↓
 ALB
   ↓
Private EC2
   ↓
Private RDS
```

---

### Pattern 2: Private EC2 → AWS Services

```text
Private EC2
    ↓
VPC Endpoint
    ↓
S3 / DynamoDB
```

Avoid unnecessary Internet/NAT traversal when a suitable endpoint exists.

---

### Pattern 3: Multi-account Security

```text
AWS Organizations
       ↓
      SCP
       ↓
Multiple AWS Accounts
       ↓
Security services
       ↓
Security Hub
```

---

### Pattern 4: Application User Authentication

```text
Web/Mobile App
      ↓
Cognito User Pool
      ↓
Authentication
      ↓
Application
```

If the user also needs direct AWS-resource access:

```text
Cognito Identity Pool
       ↓
Temporary IAM credentials
       ↓
S3 / DynamoDB
```

---

# 24. The Exam Traps You MUST Know

### Trap 1

**"EC2 needs access to S3."**

❌ Access key stored on EC2
✅ **IAM Role**

---

### Trap 2

**"Prevent an entire AWS account from using a service."**

→ **SCP**

Remember:

> SCP restricts; it doesn't grant.

---

### Trap 3

**"Protect web application from SQL injection."**

→ **WAF**

Not Security Group.

---

### Trap 4

**"Detect compromised credentials/unusual AWS activity."**

→ **GuardDuty**

---

### Trap 5

**"Find vulnerable software packages."**

→ **Inspector**

---

### Trap 6

**"Find sensitive/PII data in S3."**

→ **Macie**

---

### Trap 7

**"Encrypt data and control encryption keys."**

→ **KMS**

---

### Trap 8

**"Store database password and automatically rotate it."**

→ **Secrets Manager**

---

### Trap 9

**"Check whether security groups/resources violate compliance rules."**

→ **AWS Config**

---

### Trap 10

**"Employee needs access to multiple AWS accounts."**

→ **IAM Identity Center**

---

# Highest Priority for Your Last-Day Revision

If time is tight, learn these **cold**:

1. **IAM Users vs Groups vs Roles**
2. **IAM policy evaluation + Explicit Deny**
3. **IAM Role vs access keys**
4. **SCP**
5. **KMS**
6. **Secrets Manager vs Parameter Store**
7. **WAF vs Shield vs Network Firewall**
8. **GuardDuty vs Inspector vs Macie**
9. **Security Hub vs Detective**
10. **Config**
11. **Cognito User Pools vs Identity Pools**
12. **Shared Responsibility Model**

### One-line memory map

> **IAM = access | KMS = encryption | Secrets Manager = secrets | WAF = web attacks | Shield = DDoS | Network Firewall = VPC traffic | GuardDuty = threats | Inspector = vulnerabilities | Macie = S3 sensitive data | Config = compliance | Security Hub = findings | Detective = investigation | Cognito = app users | SCP = account guardrail**

This is the **SAA-level security depth** I'd prioritize. Don't spend your remaining preparation time memorizing implementation details of every security service.

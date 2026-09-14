<img width="1024" height="1536" alt="image" src="https://github.com/user-attachments/assets/7e6b73f6-812f-4f48-9342-901f34ffbab5" />



# Part I: Networking and VPC

For the final-day revision, don't try to memorize networking as isolated definitions. Build one mental model:

**VPC → Subnets → Route tables → Gateways/endpoints → Security → Connectivity → DNS → Global networking**

---

# 1. Amazon VPC

### What it is

* **VPC = logically isolated virtual network in AWS**
* You define:

  * IP address range
  * Subnets
  * Route tables
  * Gateways
  * Network security

### Key points

* VPC is **Region-scoped**
* Subnets are **AZ-scoped**
* A VPC can span multiple AZs
* Each subnet belongs to exactly **one AZ**
* VPC CIDR must be specified
* VPC has a default **local route** allowing communication within the VPC

### Exam keywords

> isolated network, CIDR, private network, AWS resources, IP range

---

# 2. CIDR

Example:

`10.0.0.0/16`

* `/16` = first 16 bits identify the network
* Remaining 16 bits identify addresses within the network
* `/16` gives **65,536 IPv4 addresses**
* `/24` gives **256 addresses**

Important:

* AWS reserves **5 IP addresses in every subnet**
* Therefore a `/24` subnet has **251 usable IPv4 addresses**

### Exam trap

Don't calculate usable subnet addresses as simply `2^n` for AWS subnets.

---

# 3. Subnets

Two major conceptual types:

### Public subnet

A subnet whose route table has a route to an **Internet Gateway**.

Example:

`0.0.0.0/0 → Internet Gateway`

### Private subnet

No direct route to an Internet Gateway.

Usually:

`0.0.0.0/0 → NAT Gateway`

### Isolated subnet

No route to external networks.

Useful for:

* Databases
* Highly restricted internal resources

### Critical distinction

**A subnet is not inherently public or private.**

Its routing configuration determines that.

---

# 4. Route Tables

Route tables determine:

> **Where network traffic should go.**

Example:

| Destination   | Target           |
| ------------- | ---------------- |
| `10.0.0.0/16` | local            |
| `0.0.0.0/0`   | Internet Gateway |

### Important concepts

* Every subnet is associated with a route table.
* A subnet can only have **one route table association at a time**.
* A route table can be associated with multiple subnets.
* VPC automatically has a **local route**.
* More specific routes take precedence.

### Longest prefix match

If you have:

`10.0.0.0/16 → TGW`

and

`10.0.1.0/24 → VPC Peering`

Traffic destined for:

`10.0.1.50`

uses the `/24` route.

**More specific route wins.**

---

# 5. Internet Gateway

### What it does

Allows communication between a VPC and the **public Internet**.

Architecture:

```text
EC2
 ↓
Public Subnet
 ↓
Route Table
 ↓
Internet Gateway
 ↓
Internet
```

### Important

An Internet Gateway:

* Is horizontally scalable
* Is highly available
* Does not require bandwidth provisioning
* Supports IPv4 and IPv6
* Performs NAT for instances using public IPv4 addresses

### Exam trap

Attaching an Internet Gateway to a VPC **does NOT automatically make instances public**.

You need:

1. Route to Internet Gateway
2. Public IPv4 address / appropriate public addressing
3. Security group allows traffic
4. NACL allows traffic

---

# 6. NAT Gateway

This one is **very important**.

### Purpose

Allows resources in a **private subnet to initiate outbound connections to the Internet**.

Example:

```text
Private EC2
    ↓
Private Route Table
    ↓
NAT Gateway
    ↓
Internet Gateway
    ↓
Internet
```

### Key point

NAT Gateway is primarily:

> **Private → Internet**

It does **not** allow unsolicited Internet → private instance connections.

### NAT Gateway requirements

* Created in a subnet
* For public Internet access, normally placed in a **public subnet**
* Requires an Elastic IP for IPv4 Internet access

### High availability

For production:

> **One NAT Gateway per AZ**

Why?

If AZ-A's NAT Gateway fails, private resources in AZ-A shouldn't depend on AZ-B's NAT Gateway.

### Exam trap

A NAT Gateway does **not** replace an Internet Gateway.

You generally need:

**Private subnet → NAT Gateway → Internet Gateway → Internet**

---

# 7. NAT Gateway vs Internet Gateway

|                     | Internet Gateway                                     | NAT Gateway                             |
| ------------------- | ---------------------------------------------------- | --------------------------------------- |
| Main purpose        | Internet connectivity                                | Outbound Internet for private resources |
| Public subnet       | Yes                                                  | Usually deployed here                   |
| Private subnet      | Can be route target for public resources             | Yes, as outbound target                 |
| Internet → instance | Possible with appropriate public addressing/security | No                                      |
| Requires EIP        | No                                                   | Yes for public IPv4 NAT                 |
| Managed by AWS      | Yes                                                  | Yes                                     |

### Mental shortcut

**IGW = Internet access for public resources**

**NAT = Internet access for private resources**

---

# 8. Security Groups

Security Groups are **virtual firewalls attached to network interfaces/instances**.

### Characteristics

* **Stateful**
* Allow rules only
* No explicit deny
* Inbound rules
* Outbound rules
* Can reference other security groups

### Stateful means

If inbound traffic is allowed:

```text
Client → EC2
```

the response traffic is automatically allowed.

You don't need a separate outbound rule specifically permitting that response, assuming the SG configuration otherwise permits the flow.

### Security Group references

Very important architecture pattern:

```text
ALB SG
   ↓
EC2 SG
```

EC2 SG can allow:

`Inbound TCP 443 from ALB-SG`

Instead of allowing:

`0.0.0.0/0`

This is more secure and follows **least privilege**.

---

# 9. Network ACL

NACL = subnet-level network firewall.

### Characteristics

* **Stateless**
* Supports Allow and Deny
* Inbound rules
* Outbound rules
* Rules evaluated in **number order**
* First matching rule wins
* Applies to subnet

### Stateful vs Stateless

**Security Group:**

```text
Request allowed
      ↓
Response automatically allowed
```

**NACL:**

```text
Request allowed
      ↓
Response must separately be allowed
```

### Exam trap

If you see:

> "Need to explicitly deny a particular IP address"

Think:

**NACL**

because Security Groups don't support explicit deny rules.

---

# 10. Security Group vs NACL

| Feature         | Security Group          | NACL                           |
| --------------- | ----------------------- | ------------------------------ |
| Level           | ENI/instance            | Subnet                         |
| Stateful        | Yes                     | No                             |
| Allow           | Yes                     | Yes                            |
| Deny            | No                      | Yes                            |
| Rule evaluation | All applicable rules    | Lowest numbered matching rule  |
| Common use      | Instance-level firewall | Subnet-level network filtering |

### Exam shortcut

**SG = instance firewall**

**NACL = subnet firewall**

---

# 11. Elastic IP

An Elastic IP is a **static public IPv4 address**.

Useful when an application needs:

> A persistent public IPv4 address.

Example:

* NAT Gateway
* Certain EC2 architectures

### Important

Elastic IP is associated with your AWS account until released.

Avoid unnecessary EIPs because AWS charges for public IPv4 addresses.

---

# 12. VPC Endpoints

This is a **very high-value exam topic**.

Purpose:

> Access AWS services privately without sending traffic through the public Internet.

Two major types to remember:

### Gateway Endpoint

Used for:

* **S3**
* **DynamoDB**

Characteristics:

* Route-table based
* No ENI
* No additional endpoint hourly charge

Mental model:

```text
Private EC2
    ↓
Route Table
    ↓
Gateway Endpoint
    ↓
S3 / DynamoDB
```

### Interface Endpoint

Uses:

* **PrivateLink**
* Elastic Network Interface
* Private IP address

Used for many AWS services such as:

* Secrets Manager
* CloudWatch
* Systems Manager
* KMS
* SNS
* SQS
* etc.

### Mental shortcut

**S3/DynamoDB → Gateway Endpoint**

**Most other AWS services → Interface Endpoint**

---

# 13. AWS PrivateLink

PrivateLink allows private connectivity to services without exposing traffic to the public Internet.

Common architecture:

```text
Consumer VPC
     ↓
Interface Endpoint
     ↓
PrivateLink
     ↓
Service Provider
```

Useful for:

* Accessing AWS services privately
* Accessing third-party services
* Sharing services across VPCs
* Service provider/consumer architectures

### Exam keyword

> "Private access to a service without VPC peering"

Think:

**PrivateLink / Interface Endpoint**

---

# 14. VPC Peering

Connects:

**VPC A ↔ VPC B**

Traffic uses private IP addresses.

### Important

* Can connect VPCs across AWS accounts
* Can connect VPCs across Regions
* **Non-transitive**

Example:

```text
A ↔ B ↔ C
```

A cannot automatically communicate with C.

You need:

```text
A ↔ C
```

### Exam trap

If the question says:

> "VPC A is peered with VPC B, and VPC B is peered with VPC C. How can A communicate with C?"

Answer:

**Create another peering connection or use Transit Gateway.**

---

# 15. Transit Gateway

Think of Transit Gateway as:

> **A central network hub for connecting many VPCs and networks.**

Instead of:

```text
A ↔ B
A ↔ C
A ↔ D
B ↔ C
B ↔ D
C ↔ D
```

you can have:

```text
       A
       |
B ─ Transit Gateway ─ C
       |
       D
```

### Useful for

* Many VPCs
* Centralized networking
* Hybrid connectivity
* Connecting VPCs and VPNs
* Large-scale network architecture

### Exam shortcut

**Few VPCs → Peering**

**Many VPCs → Transit Gateway**

---

# 16. VPC Peering vs Transit Gateway

|                     | VPC Peering        | Transit Gateway |
| ------------------- | ------------------ | --------------- |
| Architecture        | Point-to-point     | Hub-and-spoke   |
| Transitive          | No                 | Yes             |
| Many VPCs           | Becomes cumbersome | Designed for it |
| Centralized routing | Limited            | Yes             |
| Cross-account       | Yes                | Yes             |

---

# 17. VPN

### Site-to-Site VPN

Connects:

**On-premises network ↔ AWS VPC**

over an encrypted connection through the Internet.

Typical architecture:

```text
On-Premises
    |
Customer Gateway
    |
Internet
    |
Virtual Private Gateway / Transit Gateway
    |
AWS VPC
```

### Key characteristics

* Encrypted
* Relatively quick to deploy
* Uses Internet
* Generally cheaper than Direct Connect
* Internet-dependent

---

# 18. Direct Connect

Provides a **dedicated network connection** between on-premises infrastructure and AWS.

### Useful when

* Need consistent network performance
* Large data transfer
* Hybrid architecture
* Need private dedicated connectivity
* Want to avoid traversing the public Internet

### Important

Direct Connect:

> **is not encrypted by default.**

If encryption is required, additional mechanisms such as VPN can be used.

### Exam shortcut

**Fast to establish + encrypted over Internet → VPN**

**Dedicated/private + consistent performance → Direct Connect**

---

# 19. Direct Connect vs VPN

|                         | VPN                       | Direct Connect                 |
| ----------------------- | ------------------------- | ------------------------------ |
| Connection              | Internet                  | Dedicated connection           |
| Encryption              | Yes                       | Not by default                 |
| Setup                   | Faster                    | Longer                         |
| Cost                    | Lower                     | Higher                         |
| Performance consistency | Lower                     | Higher                         |
| Use case                | Quick hybrid connectivity | Enterprise hybrid connectivity |

---

# 20. Route 53

AWS's **DNS service**.

Main capabilities:

* Domain registration
* DNS resolution
* Health checks
* Routing policies

### Important routing policies

#### Simple

Basic DNS routing.

#### Weighted

Send traffic according to weights.

Example:

```text
80% → Server A
20% → Server B
```

Useful for:

* Testing
* Gradual migration

#### Latency-based

Routes users to the Region with the **lowest latency**.

#### Failover

Primary/secondary architecture.

```text
Primary
  ↓ failure
Secondary
```

#### Geolocation

Route based on user's geographic location.

#### Geoproximity

Route based on geographic location of resources/users, with traffic flow controls.

#### Multi-value answer

Returns multiple healthy IPs.

---

# 21. Route 53 Alias vs CNAME

### Alias

AWS-specific DNS feature.

Can point to AWS resources such as:

* ALB
* CloudFront
* S3 website endpoint
* API Gateway

### CNAME

Maps one hostname to another hostname.

Important limitation:

> CNAME cannot be used at the zone apex/root domain.

For example:

`example.com`

Alias can be used.

CNAME generally cannot.

### Exam shortcut

**AWS resource → Alias**

---

# 22. CloudFront

AWS CDN.

Purpose:

> Deliver content from locations closer to users.

### Architecture

```text
User
 ↓
CloudFront Edge Location
 ↓
Origin
 ↓
S3 / ALB / EC2 / etc.
```

### Important concepts

* Distribution
* Origin
* Cache behavior
* TTL
* Edge locations
* Cache
* Origin Access Control
* HTTPS
* Cache invalidation

### Common use cases

* Static websites
* Images/videos
* APIs
* Global content delivery
* Reducing latency
* Reducing origin load

---

# 23. CloudFront + S3

Very common exam architecture:

```text
User
 ↓
CloudFront
 ↓
S3
```

For private S3 content:

> Use **Origin Access Control (OAC)**.

Don't make the S3 bucket publicly accessible just to serve CloudFront content.

---

# 24. Global Accelerator

Provides global application acceleration using AWS's global network.

Uses:

* Static Anycast IP addresses
* TCP/UDP
* Regional application endpoints
* Health checks
* Automatic traffic routing

### CloudFront vs Global Accelerator

**CloudFront**

> Content delivery + caching

**Global Accelerator**

> Network-level acceleration for applications

### Shortcut

If the question emphasizes:

> "Cache static content closer to users"

→ **CloudFront**

If it emphasizes:

> "Improve global performance of TCP/UDP application"

→ **Global Accelerator**

---

# 25. VPC Flow Logs

Records information about network traffic flowing through:

* VPC
* Subnet
* Network interface

Useful for:

* Troubleshooting connectivity
* Security analysis
* Investigating rejected traffic

### Important distinction

Flow Logs don't capture packet contents.

They capture **metadata about network traffic**.

---

# 26. IPv6

AWS VPC supports IPv6.

Important concept:

> IPv6 addresses are globally routable.

For IPv6 private-subnet-like outbound-only Internet access, AWS provides:

**Egress-only Internet Gateway**

### Compare

**Internet Gateway**

→ IPv4/IPv6 Internet connectivity

**Egress-only Internet Gateway**

→ IPv6 outbound-only connectivity

---

# 27. High-Value Architecture Patterns

### Pattern 1: Public web + private application + private database

```text
                 Internet
                    |
                CloudFront
                    |
                   ALB
                    |
          Public / edge subnet
                    |
              Private EC2
                    |
              Private DB
```

Security:

```text
Internet → ALB SG
ALB SG → EC2 SG
EC2 SG → DB SG
```

Never:

```text
Internet → DB
```

---

### Pattern 2: Private EC2 needs Internet

```text
Private EC2
    ↓
Route Table
    ↓
NAT Gateway
    ↓
Internet Gateway
    ↓
Internet
```

---

### Pattern 3: Private EC2 needs S3

Prefer:

```text
Private EC2
    ↓
S3 Gateway Endpoint
    ↓
S3
```

rather than:

```text
Private EC2
    ↓
NAT Gateway
    ↓
Internet
    ↓
S3
```

This can improve security and avoid NAT data-processing costs.

---

### Pattern 4: Many VPCs

```text
VPC A ─┐
VPC B ─┤
VPC C ─┼── Transit Gateway
VPC D ─┤
On-Prem ┘
```

---

# 28. The Exam Decision Table

| Requirement                       | Think              |
| --------------------------------- | ------------------ |
| Create isolated AWS network       | VPC                |
| Divide VPC network                | Subnets            |
| Decide traffic destination        | Route table        |
| Public Internet access            | Internet Gateway   |
| Private subnet outbound Internet  | NAT Gateway        |
| Instance-level firewall           | Security Group     |
| Subnet-level firewall             | NACL               |
| Private S3 access                 | Gateway Endpoint   |
| Private AWS service access        | Interface Endpoint |
| Private service publishing        | PrivateLink        |
| Connect two VPCs                  | VPC Peering        |
| Connect many VPCs                 | Transit Gateway    |
| Quick encrypted hybrid connection | Site-to-Site VPN   |
| Dedicated hybrid connection       | Direct Connect     |
| DNS                               | Route 53           |
| CDN/caching                       | CloudFront         |
| Global TCP/UDP acceleration       | Global Accelerator |
| IPv6 outbound-only Internet       | Egress-only IGW    |
| Network traffic troubleshooting   | VPC Flow Logs      |

---

# 29. Must-Memorize Exam Traps

These are worth consciously memorizing:

1. **VPC = Region, Subnet = AZ**
2. **Public subnet = route to Internet Gateway**
3. Internet Gateway alone doesn't make an instance public.
4. **NAT Gateway enables outbound connectivity from private resources.**
5. NAT Gateway does not permit unsolicited inbound connections.
6. NAT Gateway should generally be deployed per AZ for high availability.
7. **Security Groups are stateful.**
8. **NACLs are stateless.**
9. Security Groups support **allow**, not explicit deny.
10. NACLs support **allow + deny**.
11. **VPC Peering is non-transitive.**
12. **Transit Gateway is designed for many VPCs.**
13. **S3/DynamoDB → Gateway Endpoint.**
14. Most other AWS service private access → **Interface Endpoint**.
15. Direct Connect is **not encrypted by default**.
16. **CloudFront = CDN/cache.**
17. **Global Accelerator = network acceleration.**
18. Route 53 **latency routing ≠ geolocation routing**.
19. Route 53 **failover routing** is for primary/secondary architectures.
20. **Alias can point to AWS resources and works at the zone apex.**

---

## The mental model to retain

If you remember only this before the exam:

```text
                    AWS REGION
                        |
                      VPC
                        |
              +---------+---------+
              |                   |
         Public Subnet       Private Subnet
              |                   |
         Route Table          Route Table
              |                   |
             ALB              EC2 / App
              |                   |
            EC2                  DB
              |
       Internet Gateway

Private outbound:
EC2 → NAT Gateway → Internet Gateway → Internet

Private AWS service:
EC2 → VPC Endpoint → AWS Service

Many VPCs:
VPC → Transit Gateway ← VPC

Hybrid:
On-Prem → VPN / Direct Connect → AWS
```

**Part I priority:** If you're short on time, spend most of your mental effort on **VPC/subnets/routes, NAT vs IGW, SG vs NACL, endpoints, peering vs Transit Gateway, VPN vs Direct Connect, and Route 53 routing policies**. These distinctions repeatedly show up in architecture questions.

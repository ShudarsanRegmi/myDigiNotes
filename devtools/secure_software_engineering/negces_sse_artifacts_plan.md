### Rephrased question

> I have almost completed my NEGCES Lab Slot Booking and Resource Management project, although new requirements may be introduced later. At this stage, I want to use the project as a case study to learn the complete software engineering lifecycle by creating the artifacts produced at each phase.
>
> Can you give me a structured, phase-by-phase plan of the software engineering artifacts I should create for this project? For each phase, include the applicable documents/artifacts and explain their purpose. Since my specialization is Cybersecurity, I also want to incorporate relevant security engineering activities wherever applicable.
>
> My CDP course outcomes are:
>
> * **CO1:** Develop secure system models depending on user requirements.
> * **CO2:** Build analysis models and apply threat modeling for analysing system vulnerabilities.
> * **CO3:** Understand software security economics and practices in containerized development.
> * **CO4:** Develop security testing of software and understand basics of security governance, risk and compliance.

Yes. This is actually a very good way to turn your already-built project into a **complete software engineering case study**. You don't need to rebuild the system. Instead, you'll reverse-engineer and document the engineering process, then add a few artifacts for the newer requirements.

I would structure your work as a **Software Engineering + Secure SDLC portfolio**.

# 1. Overall roadmap

For your NEGCES project, I recommend following this lifecycle:

```text
1. Project Initiation
        ↓
2. Requirements Engineering
        ↓
3. Feasibility & Planning
        ↓
4. System Modeling / Analysis
        ↓
5. Architecture & Design
        ↓
6. Security Engineering
        ↓
7. Database & Detailed Design
        ↓
8. Implementation / Development
        ↓
9. Testing
        ↓
10. Security Testing
        ↓
11. Deployment / Containerization
        ↓
12. Operations & Monitoring
        ↓
13. Maintenance / Change Management
        ↓
14. Governance, Risk & Compliance
        ↓
15. Project Retrospective
```

You don't necessarily need one huge document per phase. Some phases naturally produce multiple artifacts, while others can be represented by a single concise document.

---

# 2. Phase 1: Project Initiation

This establishes **why the system exists and what problem it solves**.

### Artifacts

| Artifact                  | Purpose                                                    |
| ------------------------- | ---------------------------------------------------------- |
| Project Charter           | Defines project purpose, scope, stakeholders, objectives   |
| Problem Statement         | Clearly describes the existing problem                     |
| Vision & Scope Document   | Defines what the system will and won't do                  |
| Stakeholder Register      | Identifies students, faculty, lab admins, superadmin, etc. |
| Assumptions & Constraints | Documents limitations such as campus infrastructure        |
| Initial Risk Register     | Identifies major project risks                             |

For your project:

```text
Problem:
Manual / fragmented lab resource booking and monitoring.

Goal:
Provide centralized lab booking, approval, attendance,
resource monitoring and administrative management.
```

### Security angle

At this stage, introduce:

**Security objectives**

For example:

```text
Confidentiality
    ↓
Protect student identity, credentials, telemetry

Integrity
    ↓
Prevent unauthorized modification of bookings/telemetry

Availability
    ↓
Booking system and monitoring service should remain available

Authenticity
    ↓
Only legitimate users and agents can interact with backend
```

This begins satisfying **CO1**.

---

# 3. Phase 2: Requirements Engineering

This is one of the most important phases for your CDP.

## Artifact 1: Software Requirements Specification

Create a proper **SRS**.

Structure it approximately like:

```text
1. Introduction
2. Overall Description
3. Stakeholders
4. Functional Requirements
5. Non-functional Requirements
6. External Interface Requirements
7. System Constraints
8. Assumptions
9. Dependencies
10. Acceptance Criteria
```

### Functional requirements

For example:

```text
FR-01 User Registration/Login
FR-02 Book Lab Slot
FR-03 Cancel Booking
FR-04 Approve/Reject Booking
FR-05 Cooldown Enforcement
FR-06 Attendance Recording
FR-07 Telemetry Ingestion
FR-08 View Resource Utilization
FR-09 Admin Management
FR-10 Email Notification
```

### Non-functional requirements

This is where you can make the project much more professional.

```text
NFR-01 Security
NFR-02 Availability
NFR-03 Performance
NFR-04 Scalability
NFR-05 Maintainability
NFR-06 Usability
NFR-07 Reliability
NFR-08 Auditability
```

---

## Artifact 2: Requirements Traceability Matrix

Create:

```text
Requirement → Design → Implementation → Test Case
```

Example:

| Requirement     | Design            | Implementation      | Test       |
| --------------- | ----------------- | ------------------- | ---------- |
| FR-05 Cooldown  | Booking Service   | cooldown.js         | TC-BOOK-05 |
| FR-07 Telemetry | Telemetry API     | telemetryController | TC-TEL-03  |
| FR-08 Analytics | Analytics Service | dashboard.jsx       | TC-ANA-02  |

This becomes extremely useful later.

---

## Artifact 3: Use Case Specification

For every major use case:

```text
Use Case:
Book Lab Slot

Actor:
Student

Precondition:
User is authenticated

Main Flow:
1. Student selects lab
2. Selects date/time
3. System checks conflicts
4. System checks cooldown
5. Request is created
6. Admin approves
7. Confirmation is sent

Alternative Flow:
Slot already booked
Cooldown active
Invalid request
Unauthorized user
```

---

## Artifact 4: Requirements Change Log

Since you specifically said:

> new requirements may come in the future

create a **Change Request / Change Log**.

Example:

| ID     | Change                | Reason                 | Impact | Status      |
| ------ | --------------------- | ---------------------- | ------ | ----------- |
| CR-001 | Add attendance        | Faculty request        | Medium | Implemented |
| CR-002 | Add process telemetry | Monitoring requirement | High   | Implemented |
| CR-003 | TPM authentication    | Security requirement   | High   | Proposed    |

This teaches you **requirements evolution**, which is very important in real software engineering.

---

# 4. Phase 3: Feasibility & Planning

Create a:

## Feasibility Study

Analyze:

```text
Technical feasibility
Economic feasibility
Operational feasibility
Schedule feasibility
Security feasibility
```

For example:

### Technical

Can MERN + InfluxDB + Go + Podman support the requirements?

### Economic

Compare:

```text
Self-hosted
vs
Cloud deployment
```

### Operational

Can lab administrators actually operate the platform?

### Security

Can the architecture securely authenticate:

```text
Student
Admin
Superadmin
Telemetry Agent
```

---

## Project Management Plan

Include:

```text
Work Breakdown Structure
Milestones
Timeline
Resource allocation
Risk management
```

You can create a **WBS** such as:

```text
NEGCES
│
├── Authentication
├── Booking
├── Administration
├── Attendance
├── Telemetry
├── Analytics
├── Security
├── Deployment
└── Testing
```

---

# 5. Phase 4: System Analysis and Modeling

This directly maps to **CO1 + CO2**.

You should produce several models.

## 1. Use Case Diagram

Actors:

```text
Student
Faculty
Lab Admin
Superadmin
Telemetry Agent
System Administrator
```

---

## 2. Activity Diagrams

Create activity diagrams for important workflows:

```text
Booking
Approval
Cancellation
Attendance
Telemetry ingestion
Admin privilege assignment
```

---

## 3. Sequence Diagrams

These are particularly valuable.

For example:

```text
Student
   │
   │ Book Slot
   ↓
Frontend
   │
   ↓
Backend API
   │
   ├── Authentication Service
   │
   ├── Booking Service
   │
   ├── Database
   │
   └── Notification Service
```

Do this for at least:

* Login
* Booking
* Admin approval
* Telemetry submission
* Admin privilege modification

---

## 4. Data Flow Diagram

Create:

```text
Context Diagram
      ↓
Level 0 DFD
      ↓
Level 1 DFD
```

This is particularly useful for security analysis because you can identify where sensitive information crosses trust boundaries.

---

## 5. Domain Model / Class Diagram

Classes might include:

```text
User
Student
Admin
Booking
Lab
Machine
Attendance
Telemetry
Notification
CooldownPolicy
AuditLog
```

---

# 6. Phase 5: Architecture Design

Now transition from **what the system does** to **how the system is structured**.

## Software Architecture Document

Your architecture could be represented as:

```text
                    ┌──────────────┐
                    │    Client    │
                    │ React / GUI  │
                    └──────┬───────┘
                           │
                           ↓
                    ┌──────────────┐
                    │ API Gateway  │
                    └──────┬───────┘
                           │
             ┌─────────────┼─────────────┐
             ↓             ↓             ↓
        Auth Service   Booking       Telemetry
                         Service       Service
             │             │             │
             ↓             ↓             ↓
          MongoDB       MongoDB       InfluxDB
                                         ↑
                                         │
                                    Go Agent
```

Then document:

* Architectural style
* Component responsibilities
* Communication protocols
* Deployment architecture
* Data storage architecture
* Authentication architecture
* External dependencies

---

## Architecture Decision Records

This is something I strongly recommend because you're trying to **learn software engineering practices**, not merely produce academic diagrams.

Create **ADRs**.

Examples:

```text
ADR-001: Why MERN?
ADR-002: Why MongoDB?
ADR-003: Why InfluxDB for telemetry?
ADR-004: Why Go for monitoring agent?
ADR-005: Why Podman?
ADR-006: Why Firebase Authentication?
ADR-007: Why separate telemetry storage?
```

Each ADR:

```text
Title
Context
Problem
Options considered
Decision
Consequences
```

This teaches you how real engineering teams document architectural decisions.

---

# 7. Phase 6: Security Engineering

This is where your cybersecurity specialization becomes prominent.

I would make this a **separate Secure Software Design document** rather than scattering security information everywhere.

## Security Requirements

Extend your SRS with:

```text
SEC-01 Authentication
SEC-02 Authorization
SEC-03 Role-based access control
SEC-04 Secure telemetry ingestion
SEC-05 Audit logging
SEC-06 Data confidentiality
SEC-07 Data integrity
SEC-08 Agent authentication
SEC-09 Secret management
SEC-10 Session security
```

---

# 8. Threat Modeling

This is probably the **most important artifact for CO2**.

Use **STRIDE**.

For example:

```text
Student
   │
   ↓
Frontend
   │
   ↓
Backend API
   │
   ↓
Database
```

Ask:

```text
Spoofing?
Tampering?
Repudiation?
Information Disclosure?
Denial of Service?
Elevation of Privilege?
```

---

## Threat Model Document

Include:

### Assets

```text
Student identity
Credentials
Booking information
Telemetry
Admin privileges
API credentials
Private keys
Audit logs
```

### Threat actors

```text
Malicious student
Compromised client
Compromised telemetry agent
Malicious administrator
External attacker
Compromised dependency
```

### Trust boundaries

For example:

```text
Internet
   │
   │ Trust Boundary
   ↓
Backend
   │
   │ Trust Boundary
   ↓
Database
```

---

## Attack Tree

Create attack trees for important threats.

Example:

```text
Gain unauthorized admin access
            │
       ┌────┴────┐
       ↓         ↓
Steal       Exploit
credentials authorization
              │
          ┌───┴───┐
          ↓       ↓
        IDOR    RBAC flaw
```

This is a very good CO2 artifact.

---

# 9. Security Architecture

Now take the threats and design mitigations.

For example:

| Threat               | Mitigation                 |
| -------------------- | -------------------------- |
| Credential theft     | Strong authentication      |
| IDOR                 | Object-level authorization |
| Telemetry spoofing   | Agent authentication       |
| Privilege escalation | RBAC                       |
| Data tampering       | Integrity verification     |
| Secret exposure      | Secret management          |
| API abuse            | Rate limiting              |
| Audit repudiation    | Audit logs                 |

This creates a clean chain:

```text
Requirement
     ↓
Threat
     ↓
Security Control
     ↓
Implementation
     ↓
Security Test
```

That is exactly the kind of thinking you want to demonstrate.

---

# 10. Phase 7: Database Design

Create:

## ER Diagram

Represent:

```text
User
  │
  ├── Booking
  │      │
  │      └── Lab
  │
  └── Attendance

Machine
   │
   └── Telemetry
```

Then document:

* Schema
* Collections/tables
* Relationships
* Indexes
* Constraints
* Retention policies

For InfluxDB specifically:

```text
Measurement
Tags
Fields
Timestamp
Retention
Downsampling
```

---

# 11. Phase 8: Detailed Design

Create:

## API Specification

Document endpoints such as:

```text
POST /api/auth/login
POST /api/bookings
GET  /api/bookings
PUT  /api/bookings/:id
POST /api/telemetry
GET  /api/analytics
```

For each endpoint:

```text
Method
Endpoint
Authentication
Authorization
Request
Response
Errors
Rate limits
Security considerations
```

If possible, generate an **OpenAPI/Swagger specification**.

---

# 12. Phase 9: Implementation

You already have the code, so don't artificially recreate it.

Instead create:

## Coding Standards Document

Define:

```text
Naming conventions
Directory structure
Error handling
Logging
Input validation
Authentication practices
Secret handling
Git conventions
```

---

## Git Workflow

Document your chosen workflow:

```text
main
 │
 ├── feature/booking
 ├── feature/telemetry
 ├── feature/attendance
 └── security/auth-hardening
```

Then establish:

```text
Commit conventions
Pull requests
Code review
Branch protection
Release tags
```

---

## Secure Coding Guidelines

Include things relevant to your stack:

```text
Input validation
Output encoding
Authentication
Authorization
JWT/session handling
No hardcoded secrets
Dependency management
Secure database queries
CORS
CSRF
Rate limiting
Error handling
Logging
```

---

# 13. Phase 10: Testing

Create a proper:

# Software Test Plan

Include:

```text
Testing objectives
Testing scope
Testing strategy
Test environment
Test types
Entry criteria
Exit criteria
Defect management
```

Then create:

### Unit Test Cases

```text
Cooldown calculation
Booking conflict detection
Role verification
Telemetry validation
```

### Integration Tests

```text
Frontend → Backend
Backend → MongoDB
Backend → InfluxDB
Agent → Backend
Authentication → Authorization
```

### System Tests

Test the complete workflows.

---

# 14. Security Testing

This directly maps to **CO4**.

Create a separate:

# Security Test Plan

Include:

```text
Authentication testing
Authorization testing
Input validation
API security
Session security
Injection testing
Access control
Privilege escalation
Information disclosure
Rate limiting
Security headers
Dependency vulnerabilities
Container security
```

For your application, test things like:

```text
Can Student access Admin API?

Can Student modify another student's booking?

Can Admin modify Superadmin privileges?

Can an unauthenticated user submit telemetry?

Can a fake agent submit telemetry?

Can a user bypass cooldown?

Can a user manipulate booking IDs?

Can telemetry fields be tampered with?
```

These are much more relevant to your project than generic vulnerability checklists.

---

# 15. Vulnerability Assessment

Create a:

## Vulnerability Assessment Report

Structure:

```text
Finding ID
Title
Affected Component
Description
Severity
CVSS
Evidence
Impact
Attack Scenario
Recommendation
Remediation Status
```

Example:

```text
VULN-001
Broken Object Level Authorization

Component:
Booking API

Severity:
High

Impact:
User may access another user's booking.

Recommendation:
Perform server-side ownership/role validation.
```

Don't just run tools and paste their output. Explain the vulnerability and demonstrate the security reasoning.

---

# 16. Phase 11: Containerization and Deployment

This is particularly relevant to **CO3**.

Since your project uses Podman/containerized deployment, create:

## Containerization Document

Include:

```text
Container architecture
Container images
Networking
Volumes
Environment variables
Secrets
Resource limits
Health checks
Logging
Restart policies
```

Architecture:

```text
              Host
               │
       ┌───────┼────────┐
       ↓       ↓        ↓
    Frontend Backend   Agent
               │
          ┌────┴────┐
          ↓         ↓
       MongoDB   InfluxDB
```

---

# 17. Container Security

Create a dedicated checklist/report:

```text
Non-root containers
Minimal base images
Image scanning
Dependency scanning
Read-only filesystem where possible
Dropped Linux capabilities
Resource limits
Network isolation
Secret management
Container image provenance
```

Then evaluate your actual deployment against it.

---

# 18. Security Economics

This is an interesting CO3 requirement that people often ignore.

Create a:

# Security Cost-Benefit Analysis

For example:

```text
Control:
TPM-backed agent authentication

Cost:
Implementation complexity
Hardware dependency
Maintenance

Benefit:
Higher confidence in agent identity
Resistance against credential extraction

Alternative:
API key

Cost:
Low

Risk:
Key extraction / replay
```

You can compare security controls based on:

```text
Implementation cost
Operational cost
Performance overhead
Maintenance burden
Security benefit
Residual risk
```

Don't turn this into an arbitrary numerical ranking. The goal is to understand the **trade-offs**.

---

# 19. Phase 12: Deployment

Create:

## Deployment Plan

Document:

```text
Infrastructure
Prerequisites
Installation
Configuration
Environment variables
Database initialization
Container deployment
Network configuration
TLS
Backup
Rollback
Health checks
```

Then create:

## Deployment Diagram

Include:

```text
Campus Network
      │
      ↓
Reverse Proxy
      │
      ↓
Application
   ┌──┴──┐
   ↓     ↓
Mongo  InfluxDB
   ↑
   │
Go Agents
```

---

# 20. Phase 13: Operations and Monitoring

This is particularly relevant because your project has telemetry.

Create:

## Monitoring & Observability Plan

Define:

```text
Metrics
Logs
Traces
Alerts
Dashboards
Retention
Incident response
```

For example:

```text
CPU
Memory
Disk
Network
GPU
Process usage
API latency
Error rate
Database health
Container health
```

---

# 21. Incident Response

Because you're a cybersecurity student, add:

# Incident Response Plan

Example incidents:

```text
Unauthorized admin access
Compromised telemetry agent
Database compromise
Credential leakage
Container compromise
DDoS / service disruption
Data tampering
```

For each:

```text
Detection
Containment
Eradication
Recovery
Post-incident analysis
```

This gives your project an actual **security operations dimension**.

---

# 22. Phase 14: Governance, Risk and Compliance

This directly addresses **CO4**.

Create:

## Risk Register

Example:

| Risk               | Likelihood | Impact | Mitigation                   | Residual Risk |
| ------------------ | ---------- | ------ | ---------------------------- | ------------- |
| Agent compromise   | Medium     | High   | Cryptographic authentication | Medium        |
| DB failure         | Low        | High   | Backup                       | Low           |
| Credential leakage | Medium     | High   | Secret management            | Low           |
| API abuse          | Medium     | Medium | Rate limiting                | Low           |

---

## Security Policy Documents

You don't need dozens.

Create a compact set:

```text
Authentication Policy
Authorization/RBAC Policy
Password/Credential Policy
Data Retention Policy
Logging & Audit Policy
Backup Policy
Incident Response Policy
Acceptable Use Policy
```

---

# 23. Privacy / Data Classification

This is especially useful for a lab management system.

Create:

## Data Classification Matrix

| Data                   | Classification        | Reason                  |
| ---------------------- | --------------------- | ----------------------- |
| Public lab information | Public                | Non-sensitive           |
| Booking information    | Internal              | Operational information |
| Student identity       | Confidential          | Personal information    |
| Credentials            | Highly Sensitive      | Authentication secret   |
| Telemetry              | Internal/Confidential | System/user activity    |
| Private keys           | Restricted            | Cryptographic secret    |

Then define:

```text
Who can access it?
Where is it stored?
How long is it retained?
How is it protected?
```

---

# 24. Phase 15: Maintenance and Change Management

Since you explicitly expect new requirements, this is essential.

Create:

## Change Management Process

```text
New Requirement
       ↓
Change Request
       ↓
Impact Analysis
       ↓
Security Impact Analysis
       ↓
Approval
       ↓
Implementation
       ↓
Testing
       ↓
Deployment
       ↓
Documentation Update
```

The important addition for you is:

**Security Impact Analysis**

Every future requirement should answer:

```text
Does this introduce a new asset?
Does it introduce a new trust boundary?
Does it change privileges?
Does it expose new data?
Does it introduce a new attack surface?
Does the threat model need modification?
```

This is excellent secure SDLC practice.

---

# 25. Final Phase: Project Retrospective

Finally create:

# Software Engineering Retrospective

Discuss:

```text
What went well?
What went wrong?
Which requirements changed?
Which architectural decisions changed?
What technical debt exists?
What security weaknesses remain?
What would you redesign?
What did you learn?
```

You can also maintain:

## Technical Debt Register

Example:

```text
TD-001: Authentication architecture needs improvement
TD-002: Telemetry authentication currently relies on API credentials
TD-003: Some components lack automated tests
TD-004: Deployment configuration is partially manual
TD-005: No automated vulnerability scanning in CI/CD
```

This makes your project documentation feel like a **real evolving software product**, rather than a one-time college project.

---

# Your Complete Artifact Set

If I were organizing your project repository, I'd make it look something like this:

```text
docs/
│
├── 01-project-initiation/
│   ├── project-charter.md
│   ├── problem-statement.md
│   ├── scope.md
│   ├── stakeholder-register.md
│   └── initial-risk-register.md
│
├── 02-requirements/
│   ├── SRS.md
│   ├── use-case-specifications.md
│   ├── requirements-traceability-matrix.xlsx
│   ├── acceptance-criteria.md
│   └── requirements-change-log.md
│
├── 03-feasibility-planning/
│   ├── feasibility-study.md
│   ├── project-plan.md
│   └── work-breakdown-structure.md
│
├── 04-analysis/
│   ├── use-case-diagram
│   ├── activity-diagrams/
│   ├── sequence-diagrams/
│   ├── DFD/
│   └── domain-model.md
│
├── 05-architecture/
│   ├── software-architecture.md
│   ├── deployment-architecture.md
│   ├── component-diagram
│   └── ADRs/
│
├── 06-security/
│   ├── security-requirements.md
│   ├── threat-model.md
│   ├── attack-trees/
│   ├── security-architecture.md
│   ├── data-classification.md
│   └── security-controls.md
│
├── 07-database/
│   ├── ER-diagram
│   ├── database-design.md
│   └── data-dictionary.md
│
├── 08-detailed-design/
│   ├── API-specification.md
│   ├── OpenAPI.yaml
│   └── component-design.md
│
├── 09-development/
│   ├── coding-standards.md
│   ├── git-workflow.md
│   └── secure-coding-guidelines.md
│
├── 10-testing/
│   ├── test-plan.md
│   ├── unit-tests.md
│   ├── integration-tests.md
│   ├── system-tests.md
│   └── traceability-matrix.xlsx
│
├── 11-security-testing/
│   ├── security-test-plan.md
│   ├── vulnerability-assessment.md
│   ├── penetration-testing-report.md
│   └── remediation-tracker.md
│
├── 12-containerization/
│   ├── container-architecture.md
│   ├── container-security.md
│   └── deployment-manifest/
│
├── 13-deployment/
│   ├── deployment-plan.md
│   ├── configuration-guide.md
│   ├── backup-recovery.md
│   └── rollback-plan.md
│
├── 14-operations/
│   ├── monitoring-plan.md
│   ├── logging-plan.md
│   ├── alerting.md
│   └── incident-response.md
│
├── 15-governance/
│   ├── risk-register.md
│   ├── security-policies/
│   ├── data-retention-policy.md
│   └── compliance-mapping.md
│
└── 16-maintenance/
    ├── change-management.md
    ├── technical-debt.md
    └── retrospective.md
```

You don't have to create all of these as enormous documents. Some should be **one or two pages**, while others deserve substantial treatment.

---

# Mapping this to your CDP COs

This is where I'd be particularly deliberate.

| CO                                                      | Artifacts that demonstrate it                                                                                                                      |
| ------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| **CO1: Secure system models from requirements**         | SRS, security requirements, use cases, DFD, sequence diagrams, architecture, security architecture                                                 |
| **CO2: Analysis + threat modeling**                     | DFD, trust boundaries, asset inventory, STRIDE threat model, attack trees, risk register, security controls                                        |
| **CO3: Security economics + containerized development** | Feasibility study, ADRs, security cost-benefit analysis, container architecture, container security assessment                                     |
| **CO4: Security testing + GRC**                         | Security test plan, VAPT report, remediation tracker, security policies, risk register, data classification, incident response, compliance mapping |

---

# One important thing: don't create artifacts in isolation

The **real learning value** is the traceability between artifacts.

For your project, aim for this chain:

```text
Stakeholder
    ↓
Requirement
    ↓
Use Case
    ↓
Threat
    ↓
Security Requirement
    ↓
Architecture Decision
    ↓
Implementation
    ↓
Security Control
    ↓
Test Case
    ↓
Test Result
    ↓
Risk / Residual Risk
```

For example:

```text
Stakeholder:
Lab Administrator

        ↓

Requirement:
Only authorized administrators can approve bookings.

        ↓

Use Case:
Approve Booking

        ↓

Threat:
Privilege escalation / unauthorized approval

        ↓

Security Requirement:
Server must verify administrative role.

        ↓

Architecture:
RBAC middleware

        ↓

Implementation:
authorize("ADMIN")

        ↓

Security Test:
Student attempts POST /bookings/:id/approve

        ↓

Expected:
403 Forbidden

        ↓

Result:
PASS
```

**That chain is far more valuable than having 50 disconnected diagrams and documents.**

---

# How I suggest we execute this

Since your project is already almost complete, I would **not** start by blindly generating documents from Phase 1 onward.

Instead, we can treat NEGCES as an existing system and perform a **structured reverse-engineering + secure SDLC exercise**.

I'd suggest this sequence:

```text
STEP 1
Project baseline
        ↓
STEP 2
Stakeholders + scope
        ↓
STEP 3
SRS + requirements
        ↓
STEP 4
Use cases + analysis models
        ↓
STEP 5
Architecture + ADRs
        ↓
STEP 6
Security requirements
        ↓
STEP 7
Threat model
        ↓
STEP 8
Security architecture
        ↓
STEP 9
Database + API design
        ↓
STEP 10
Testing strategy
        ↓
STEP 11
Security testing
        ↓
STEP 12
Container/security economics
        ↓
STEP 13
GRC + policies
        ↓
STEP 14
Maintenance/change management
        ↓
STEP 15
Final traceability + retrospective
```

And as you produce each artifact, we can **cross-reference it with the previous ones**. For example, when we reach threat modeling, we use the actual requirements and architecture we documented earlier instead of inventing a generic threat model.

That will give you something considerably more useful than a collection of college-format documents: essentially a **miniature professional Software Development Life Cycle + Secure SDLC dossier for a real system**, while simultaneously covering all four of your CDP outcomes.

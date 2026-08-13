## Routing Prep Plan

### Part 1: Conceptual Flow, "How Routing Works"

This will be our **main revision flow**. We will move from packet arrival to route selection to dynamic routing, introducing concepts only when they become necessary.

**1. Why Routing Exists**

* Host-to-host communication across networks
* Why a switch cannot solve everything
* Router's role
* Routing vs forwarding

**2. How a Router Decides Where to Send a Packet**

* Destination IP
* Routing table
* Network prefix
* Next hop
* Interface
* Longest Prefix Match
* Default route

**3. Where Routing Table Entries Come From**

* Directly connected routes
* Static routes
* Dynamic routes
* Why static routing doesn't scale

**4. Why Dynamic Routing Protocols Exist**

* Network changes and failures
* Automatic route discovery
* Convergence
* The fundamental routing problem: finding a good path while avoiding loops

**5. Three Fundamental Approaches to Dynamic Routing**

* Distance Vector: "What distance do you know to the destination?"
* Link State: "What does the network topology look like?"
* Path Vector: "What path/AS sequence does the route carry?"

**6. How These Approaches Solve Routing**

* Information maintained by each router
* How information is exchanged
* How routes are calculated
* How failures propagate
* Convergence and loop prevention

**7. How a Router Ultimately Chooses Between Routes**

* Prefix specificity / LPM
* Administrative Distance
* Metric
* Next hop
* FIB vs RIB at a conceptual level

**8. Where Protocols Fit**

* RIP → Distance Vector
* OSPF / IS-IS → Link State
* EIGRP → Advanced Distance Vector
* BGP → Path Vector
* IGP vs EGP
* Autonomous Systems

At the end of Part 1, you should be able to mentally trace:

> **Packet arrives → destination lookup → LPM → route selection → next hop → forwarding**

and separately:

> **Network topology changes → routing protocol detects/learns it → computes new route → routing table changes → forwarding uses the new route**

That's the foundation.

---

# Part 2: Interview-Focused Deep Dives

After the conceptual flow, we'll pick only the topics that deserve individual attention.

### 1. Distance Vector Routing

We will cover:

* Core intuition
* Routing table exchange
* Bellman-Ford idea
* Distance + direction
* Neighbor-based knowledge
* Routing updates
* Convergence
* Routing loops
* Count-to-infinity
* Split horizon
* Route poisoning
* Triggered updates
* RIP as the concrete example

**Interview questions:**
"How does distance vector routing work?"
"Why does count-to-infinity happen?"
"How does split horizon prevent loops?"

---

### 2. Link State Routing

This gets more depth because it is extremely important.

* What information routers maintain
* Link State Advertisements
* Flooding
* Link-state database
* Building the topology
* SPF calculation
* Dijkstra's algorithm
* Route calculation
* Convergence
* Scalability
* OSPF as the practical example

Key question:

> **Why does OSPF converge differently from RIP?**

---

### 3. Distance Vector vs Link State

A dedicated comparison because this is a **classic interview question**.

We'll compare:

* Knowledge of network
* Information exchanged
* Algorithm
* Convergence
* Scalability
* Loop behavior
* CPU/memory
* Failure handling
* Examples

And importantly, we'll understand **why** the differences exist rather than memorizing a table.

---

### 4. Path Vector Routing + BGP

This deserves its own session.

* Why path vector was needed
* AS-level routing
* Route advertisements
* AS_PATH
* Loop prevention
* Policy-based routing
* Why BGP is different from IGPs
* Why BGP is called a path-vector protocol
* High-level BGP route selection

We won't go deep into every BGP attribute unless the interview context demands it.

---

### 5. Longest Prefix Match + Route Selection

This is deceptively important.

We'll drill into:

* `/8`, `/16`, `/24`, etc.
* Overlapping routes
* LPM examples
* Default route
* Static vs dynamic routes
* Administrative Distance
* Metrics

For example:

```text
10.0.0.0/8
10.1.0.0/16
10.1.2.0/24
0.0.0.0/0
```

Given `10.1.2.50`, **why exactly does the router choose `/24`?**

This is the sort of question where interviewers can quickly distinguish conceptual understanding from memorization.

---

### 6. Routing Loops + Convergence

A shorter but important deep dive.

We'll connect:

**failure → stale information → inconsistent routing → loop → prevention → convergence**

And understand:

* Count-to-infinity
* Split horizon
* Poison reverse
* Route poisoning
* TTL as a packet-level protection
* Fast convergence

---

### 7. RIB vs FIB + Control Plane vs Data Plane

This is particularly relevant for a **networking/TSE role**.

We'll understand:

```text
Routing protocols
      ↓
   Control Plane
      ↓
     RIB
      ↓
 Route selection
      ↓
     FIB
      ↓
   Data Plane
      ↓
 Packet forwarding
```

No unnecessary vendor-specific implementation details.

---

## Final Interview Revision Flow

After completing everything, your mental model should essentially compress into this:

```text
                         ROUTING
                            |
          +-----------------+-----------------+
          |                                   |
    Route Discovery                     Packet Forwarding
          |                                   |
   +------+------+                            |
   |      |      |                            |
 Static   DV   Link State / Path Vector       |
          |                                   |
     How routes are learned                   |
          |                                   |
          +-------------> Routing Table       |
                              |               |
                     Route Selection          |
                              |               |
                  +-----------+-----------+   |
                  |                       |   |
                 LPM                 AD + Metric
                  |                       |   |
                  +-----------+-----------+   |
                              ↓               |
                         Best Route            |
                              ↓               |
                             FIB <-------------+
                              |
                         Next Hop
                              |
                          Forwarding
```

### What I would deliberately NOT spend much time on

For your current interview goal, we can keep these at awareness level unless an interviewer pushes further:

* Detailed OSPF packet formats
* Every BGP attribute
* EIGRP internals
* IS-IS TLVs
* Complex OSPF area types
* Vendor-specific routing implementation
* Detailed SPF optimizations
* Route redistribution edge cases

That keeps the preparation **interview-focused rather than textbook-comprehensive**.

So I suggest we start with **Part 1: the conceptual flow**, and make it sufficiently deep that the later DVR, LSR, Path Vector, LPM, etc. sessions feel like drilling into things you already understand rather than learning disconnected chapters.

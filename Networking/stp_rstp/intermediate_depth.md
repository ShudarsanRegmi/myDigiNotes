Your instinct is correct. For an interview, **STP/RSTP does not deserve the same depth as IP routing, subnetting, or TCP**. You need a strong conceptual foundation and enough protocol detail to reason through topology scenarios, but you do not need to memorize every BPDU field or implementation-specific command.

### Better version of your question

> **Teach me STP and RSTP at interview depth. Prioritize foundational concepts and practical troubleshooting knowledge, while avoiding unnecessary protocol-level details that are unlikely to matter in an interview. Give me one consolidated set of notes that I can study and revise.**

# STP and RSTP: Interview-Grade Notes

## 1. First understand the problem STP solves

Ethernet switches forward frames based primarily on their **MAC address table**.

Suppose we have:

```text
             SW1
            /   \
           /     \
         SW2-----SW3
```

Why would we physically connect switches in a triangle?

**Redundancy.**

If the SW1-SW2 link fails, traffic can potentially use:

```text
SW1 → SW3 → SW2
```

But now we have a problem.

If all three links are forwarding, a broadcast frame can circulate indefinitely:

```text
SW1 → SW2 → SW3 → SW1 → SW2 → ...
```

Ethernet frames do **not have a TTL field** like IP packets.

Therefore, a Layer 2 loop can cause:

### 1. Broadcast storms

A broadcast gets continuously replicated around the loop.

### 2. MAC-table instability

A switch may repeatedly learn the same source MAC address from different ports.

For example:

```text
MAC A → Port 1
MAC A → Port 2
MAC A → Port 1
MAC A → Port 2
...
```

The switch keeps changing its forwarding information.

### 3. Duplicate frames

The same frame may reach a destination through multiple paths.

### Core idea

**STP allows physical redundancy while preventing Layer 2 forwarding loops.**

It does this by logically placing some redundant ports into a non-forwarding state.

---

# 2. What STP actually builds

STP stands for **Spanning Tree Protocol**.

Traditional STP is standardized as **IEEE 802.1D**.

Its goal is to create a **loop-free logical topology** called a spanning tree.

Consider:

```text
             SW1
            /   \
           /     \
         SW2-----SW3
```

STP might logically choose:

```text
             SW1
            /   \
           /     \
         SW2     SW3
```

and prevent the SW2-SW3 path from forwarding.

The physical connection still exists.

Only its **forwarding behavior** is suppressed.

This is important:

> **STP does not necessarily remove the redundant link. It prevents that link from participating in the active forwarding topology.**

If the SW1-SW3 link later fails, STP can use the previously blocked path.

---

# 3. The four things you absolutely need to understand

For interviews, these are the heart of STP:

1. **Root Bridge**
2. **Root Port**
3. **Designated Port**
4. **Blocked/non-forwarding port**

Everything else largely exists to determine these.

---

# 4. Root Bridge

STP first elects one switch as the **Root Bridge**.

Think of the Root Bridge as the reference point for the spanning tree.

Every other switch determines:

> "What is my best path toward the Root Bridge?"

The root bridge is selected using the **Bridge ID (BID)**.

Conceptually:

```text
Bridge ID = Bridge Priority + MAC Address
```

The switch with the **lowest Bridge ID wins**.

### Priority comes first

If:

```text
SW1 priority = 32768
SW2 priority = 32768
```

then MAC address breaks the tie.

Therefore:

> **Lowest priority wins. If priority is equal, lowest MAC address wins.**

Modern STP implementations commonly include the VLAN ID in the priority field through the **Extended System ID**, but the interview-level rule remains:

**Lowest Bridge ID wins.**

---

# 5. Root Port

Once the Root Bridge is elected, every **non-root switch** needs its best path toward the Root Bridge.

The port providing that best path is called the:

> **Root Port (RP)**

Important rule:

**Every non-root switch has exactly one Root Port.**

The Root Bridge itself has:

**No Root Port.**

Example:

```text
             SW1
            Root
           /    \
          /      \
        SW2      SW3
```

On SW2:

```text
SW2 → SW1 = Root Port
```

On SW3:

```text
SW3 → SW1 = Root Port
```

---

# 6. How does a switch choose its Root Port?

The switch chooses the port with the **best path toward the Root Bridge**.

The primary criterion is:

> **Lowest Root Path Cost**

Path cost represents the cost of reaching the Root Bridge.

In simplified interview reasoning:

```text
Higher bandwidth → lower STP cost
Lower bandwidth  → higher STP cost
```

So if a switch has:

```text
Path 1 → cost 4
Path 2 → cost 19
```

it chooses:

```text
Path 1
```

as the Root Port path.

### If costs are equal?

STP uses additional tie-breakers.

For interview purposes, remember the broad sequence:

1. Lowest Root Path Cost
2. Lowest upstream Bridge ID
3. Lowest upstream Port ID

You don't usually need to memorize every bit-level detail unless you're interviewing specifically for a switching/networking role.

---

# 7. Designated Port

Now we need another concept.

For every network segment, STP chooses the switch/port that provides the **best path toward the Root Bridge**.

That port becomes the:

> **Designated Port (DP)**

The Designated Port is allowed to forward traffic on that segment.

Example:

```text
             SW1
            ROOT
           /    \
          /      \
        SW2      SW3
```

The ports connected to SW1 will generally be Designated Ports on those segments because SW1 is the Root Bridge.

A useful mental model:

**Root Port = my best way toward the root.**

**Designated Port = the best port for this particular segment.**

---

# 8. What happens to the remaining port?

Now consider:

```text
             SW1
            ROOT
           /    \
          /      \
        SW2------SW3
```

SW2 and SW3 already have paths to the Root.

The SW2-SW3 link creates a potential loop.

STP therefore needs to prevent one side of this segment from forwarding.

One side becomes:

```text
Designated Port
```

and the other becomes:

```text
Non-designated / blocked
```

The exact terminology differs between classic STP terminology and RSTP terminology, so don't get excessively attached to "blocked port" as a formal role.

The important concept is:

> **One redundant path is prevented from forwarding so that the active topology remains loop-free.**

---

# 9. A complete STP example

Consider:

```text
                  SW1
                 Root
                /    \
               /      \
             SW2------SW3
```

Suppose:

```text
SW1-SW2 cost = 4
SW1-SW3 cost = 4
SW2-SW3 cost = 4
```

### Step 1: Elect Root Bridge

Suppose SW1 has the lowest BID.

Therefore:

```text
SW1 = Root Bridge
```

### Step 2: Choose Root Ports

SW2 sees:

```text
SW2 → SW1 = cost 4
SW2 → SW3 → SW1 = cost 8
```

Therefore:

```text
SW2 → SW1 = Root Port
```

Similarly:

```text
SW3 → SW1 = Root Port
```

### Step 3: Determine the SW2-SW3 segment

Both switches already have a path to the Root.

STP chooses one side as the Designated Port.

The other side becomes non-forwarding.

Result:

```text
                  SW1
                 ROOT
                /    \
              RP      RP
              /        \
            SW2--------SW3
              DP       blocked
```

Now there is no Layer 2 forwarding loop.

But the physical link remains available as redundancy.

---

# 10. BPDUs: How do switches know all this?

This is one of the most important interview questions.

**STP switches exchange BPDUs.**

BPDU:

> **Bridge Protocol Data Unit**

BPDUs carry information that allows switches to construct the spanning tree.

A switch essentially tells neighboring switches:

> "Here is the Root Bridge I believe exists, the cost to reach it, and information about me."

The important information conceptually includes:

* Root Bridge ID
* Root Path Cost
* Sender Bridge ID
* Sender Port ID

You don't need to memorize the entire BPDU structure for a normal interview.

### Very important

STP is not based on switches simply "looking at the topology."

They **exchange control information using BPDUs** and use that information to calculate the spanning tree.

---

# 11. Who sends BPDUs?

A common misconception is:

> "Only the Root Bridge sends BPDUs."

Not exactly.

In classic STP, switches participate in BPDU propagation. The Root Bridge originates the spanning-tree information, and downstream switches propagate updated information through their interfaces.

For interview purposes, say:

> **STP-enabled switches exchange BPDUs to build and maintain the spanning tree, with the Root Bridge serving as the reference for the topology.**

That is safer and more accurate than saying "only the root sends BPDUs."

---

# 12. STP port states

Traditional STP has these states:

```text
Blocking
   ↓
Listening
   ↓
Learning
   ↓
Forwarding
```

There is also:

```text
Disabled
```

### Blocking

The port:

* Does not forward user traffic
* Does not learn MAC addresses
* Processes BPDUs

Purpose:

**Prevent loops.**

### Listening

The switch is determining the spanning-tree topology.

It:

* Processes BPDUs
* Does not forward user frames
* Does not learn MAC addresses

### Learning

The switch begins learning MAC addresses.

But:

* It still does not forward normal user traffic.

### Forwarding

Normal operation.

The port:

* Forwards frames
* Learns MAC addresses
* Processes BPDUs

---

# 13. Why was traditional STP slow?

Classic STP deliberately waited before moving a port into forwarding.

The traditional timers include:

| Timer         |    Default |
| ------------- | ---------: |
| Hello         |  2 seconds |
| Forward Delay | 15 seconds |
| Max Age       | 20 seconds |

This can produce convergence on the order of **tens of seconds**, commonly described as around **30 to 50 seconds depending on the failure and topology**.

The important interview point isn't the arithmetic.

It's:

> **Traditional STP uses timer-driven state transitions, which makes convergence relatively slow.**

And that leads directly to RSTP.

---

# 14. RSTP

RSTP = **Rapid Spanning Tree Protocol**

Standard:

> **IEEE 802.1w**

RSTP was designed to provide much faster convergence than traditional 802.1D STP.

The key idea is not simply:

> "Make STP timers smaller."

RSTP fundamentally improves the **convergence mechanism**.

---

# 15. RSTP port roles

RSTP uses:

### Root Port

Best path toward Root Bridge.

Same basic concept as STP.

### Designated Port

Forwarding port for a segment.

Same basic concept.

### Alternate Port

A backup path toward the Root Bridge.

Example:

```text
             SW1
            ROOT
           /    \
          /      \
        SW2------SW3
```

SW2 might have:

```text
SW2 → SW1 = Root Port
SW2 → SW3 → SW1 = Alternate Port
```

The Alternate Port is essentially:

> **A backup path toward the Root Bridge that can take over if the current Root Port fails.**

This is a very useful interview concept.

### Backup Port

A less common role used when there are redundant paths to the same shared segment, typically involving a hub/shared-media situation.

For modern switched Ethernet, **Alternate Port is much more important to know**.

---

# 16. RSTP port states

RSTP simplifies the states to:

```text
Discarding
Learning
Forwarding
```

Compare:

```text
STP:
Blocking
Listening
Learning
Forwarding

RSTP:
Discarding
Learning
Forwarding
```

RSTP essentially combines the old Blocking and Listening behavior into **Discarding**.

---

# 17. The biggest RSTP improvement: Proposal/Agreement

This is probably the most important RSTP-specific mechanism to understand.

Imagine a new link between switches.

RSTP can use a:

```text
Proposal → Agreement
```

process to rapidly establish a safe forwarding path.

Conceptually:

```text
Switch A
   |
   | Proposal
   ↓
Switch B
   |
   | Agreement
   ↓
Switch A
```

The switches synchronize their spanning-tree information and confirm that it is safe to transition the appropriate port toward forwarding.

The key idea:

> **RSTP uses a handshake-based mechanism to rapidly establish forwarding without waiting for the long traditional STP timers.**

You don't need to memorize every BPDU flag involved for a normal interview.

But if the interviewer asks:

**"Why is RSTP faster than STP?"**

A strong answer is:

> "RSTP does not rely primarily on the long timer-based convergence mechanism of traditional 802.1D. It uses mechanisms such as proposal/agreement and explicit backup port roles to rapidly transition a suitable alternate path into forwarding."

---

# 18. Edge Ports

RSTP introduces the concept of an:

> **Edge Port**

An edge port is essentially a port connected to an end device rather than another switch.

For example:

```text
Switch
   |
   |
 Laptop
```

There is normally no Layer 2 switching loop through the laptop.

Therefore, the port can transition rapidly to forwarding.

This is commonly associated with **PortFast** in Cisco terminology.

### Important interview warning

Do **not** blindly enable PortFast/edge behavior on switch-to-switch links.

Why?

Because if you connect switches and bypass normal spanning-tree protection, you can potentially create a Layer 2 loop before STP can protect the topology.

---

# 19. STP vs RSTP

This is worth memorizing.

| Feature            | STP                                       | RSTP                                |
| ------------------ | ----------------------------------------- | ----------------------------------- |
| Standard           | 802.1D                                    | 802.1w                              |
| Main goal          | Loop prevention                           | Loop prevention + rapid convergence |
| Convergence        | Slow                                      | Much faster                         |
| Port states        | Blocking, Listening, Learning, Forwarding | Discarding, Learning, Forwarding    |
| Alternate Port     | No explicit RSTP role                     | Yes                                 |
| Backup Port        | No explicit RSTP role                     | Yes                                 |
| Proposal/Agreement | No                                        | Yes                                 |
| Edge Port concept  | Not part of classic STP                   | Yes                                 |
| TCN handling       | Separate mechanism                        | Improved/integrated mechanism       |

---

# 20. What happens when a link fails?

This is an excellent interview scenario.

Consider:

```text
                 SW1
                ROOT
               /    \
              /      \
            SW2------SW3
```

Initially:

```text
SW2 → SW1 = Root Port
SW2 → SW3 = Alternate
```

Now:

```text
SW2 -----X----- SW1
          link failure
```

SW2 loses its Root Port.

But it already knows:

```text
SW2 → SW3 → SW1
```

is an alternative path.

With RSTP, the Alternate Port can rapidly become the new forwarding path.

Conceptually:

```text
Before:

SW2 → SW1       Forwarding
SW2 → SW3       Alternate


After failure:

SW2 → SW1       Failed
SW2 → SW3       Forwarding
```

This is one of the strongest reasons RSTP is operationally preferable to classic STP.

---

# 21. Topology Change

Suppose a topology changes:

```text
Switch A ---- Switch B
```

and the link changes state.

STP/RSTP needs to ensure that forwarding information such as MAC address learning remains consistent with the new topology.

Classic STP has a **Topology Change Notification (TCN)** mechanism.

The important interview-level understanding is:

> **A topology change can require switches to update or age out MAC forwarding information because the path through which hosts are reachable may have changed.**

You do not need to memorize the exact TCN BPDU propagation process unless the job specifically focuses on STP internals.

---

# 22. STP does not replace routing

This distinction matters.

STP operates at:

```text
Layer 2
```

Routing protocols operate at:

```text
Layer 3
```

For example:

```text
             Router
            /      \
          SW1------SW2
```

STP is concerned with preventing **Ethernet switching loops**.

Routing protocols such as OSPF/BGP/EIGRP are concerned with **IP routing paths**.

Don't say:

> "STP finds the shortest path."

A better statement is:

> **STP constructs a loop-free Layer 2 topology by selecting a Root Bridge and determining the preferred forwarding ports based on path cost and tie-breakers.**

---

# 23. STP does not mean "one path everywhere"

Another common misunderstanding.

Suppose:

```text
             Root
            /    \
           /      \
         SW2------SW3
```

STP doesn't mean that the entire network can have only one physical path.

It means:

> **At a given moment, the forwarding topology must be loop-free.**

Redundant links can remain physically present and can be activated when the topology changes.

That's the entire point of spanning tree:

**redundancy without an active forwarding loop.**

---

# 24. VLANs and STP

This becomes important in real networks.

A switch may run different spanning-tree instances for different VLANs.

For example:

```text
VLAN 10 → Tree 1
VLAN 20 → Tree 2
```

This allows different links to carry traffic for different VLANs.

Cisco environments commonly use:

* PVST+
* Rapid PVST+

Other common standards/approaches include:

* RSTP
* MSTP

### MSTP

**Multiple Spanning Tree Protocol**

It allows multiple VLANs to be mapped to a smaller number of spanning-tree instances.

For interview purposes, know the purpose:

> **MSTP reduces the number of independent spanning-tree instances by mapping multiple VLANs to common instances.**

You don't need to go deeply into MST region configuration unless the job description specifically mentions it.

---

# 25. What you should actually memorize

For your interview preparation, I would divide STP/RSTP into three levels.

## Must know cold

These should be automatic:

```text
STP
↓
Prevent Layer 2 loops

Root Bridge
↓
Lowest Bridge ID

Bridge ID
↓
Priority + MAC

Root Port
↓
Best path from a non-root switch toward Root

Designated Port
↓
Best forwarding port on a segment

Non-forwarding/blocked path
↓
Prevents loop

BPDU
↓
STP control message used to exchange topology information

RSTP
↓
802.1w, faster convergence

RSTP roles
↓
Root
Designated
Alternate
Backup

RSTP states
↓
Discarding
Learning
Forwarding

RSTP fast convergence
↓
Proposal/Agreement + alternate paths + reduced dependence on timers

Edge Port
↓
Port connected to an end device
```

---

# 26. Know enough to solve topology diagrams

This is probably more valuable than memorizing definitions.

Given:

```text
                 SW1
                  |
             ------------
             |          |
            SW2--------SW3
             |          |
             ------------
```

you should be able to reason:

1. Which switch becomes Root?
2. What is each switch's Root Port?
3. Which ports are Designated?
4. Which redundant port becomes non-forwarding?
5. What happens if a particular link fails?
6. Which path becomes active?
7. Why does RSTP recover faster?

If you can do this confidently, you understand STP rather than merely memorizing it.

---

# 27. High-value interview questions

These are the questions I would specifically prepare.

### Q1. Why is STP required?

**Answer:**

STP prevents Layer 2 forwarding loops in Ethernet networks while allowing physical redundancy. Without STP, redundant switch links can cause broadcast storms, MAC-table instability, and duplicate frames.

### Q2. How is the Root Bridge elected?

**Answer:**

The switch with the lowest Bridge ID becomes the Root Bridge. Bridge ID is based primarily on bridge priority and MAC address. Lower priority wins; if priority is equal, the lower MAC address wins.

### Q3. What is a Root Port?

**Answer:**

The Root Port is the port on a non-root switch that provides the best path toward the Root Bridge. Each non-root switch has one Root Port.

### Q4. Can the Root Bridge have a Root Port?

**Answer:**

No. The Root Bridge is the reference point, so it does not need a port toward another root.

### Q5. What is a Designated Port?

**Answer:**

The Designated Port is the port selected to forward traffic for a particular Layer 2 segment based on the best path toward the Root Bridge.

### Q6. What is BPDU?

**Answer:**

A BPDU is a Bridge Protocol Data Unit used by STP/RSTP-enabled switches to exchange spanning-tree information and determine the loop-free topology.

### Q7. Why is RSTP faster than STP?

**Answer:**

RSTP uses mechanisms such as proposal/agreement, explicit alternate paths, and faster port transitions rather than relying primarily on the long timer-driven convergence process of traditional STP.

### Q8. What is an Alternate Port?

**Answer:**

An Alternate Port is an RSTP port that provides an alternate path toward the Root Bridge and can become the forwarding Root Port if the current Root Port fails.

### Q9. What is an Edge Port?

**Answer:**

An Edge Port is a port connected to an end device where a Layer 2 switching loop is not expected. RSTP can transition it rapidly to forwarding.

### Q10. What happens if the Root Bridge fails?

**Answer:**

The remaining switches detect that the current Root Bridge is no longer reachable, elect a new Root Bridge based on Bridge ID, and recalculate the spanning tree. RSTP performs this reconvergence much faster than traditional STP.

---

# 28. The one mental picture I want you to retain

If you remember only one diagram, remember this:

```text
                    ROOT
                     SW1
                   /    \
                  /      \
             Root Port  Root Port
                /          \
              SW2----------SW3
                 \        /
                  \______/

              One redundant
              forwarding path
              is suppressed
```

Then remember the algorithm conceptually:

```text
Physical topology
       ↓
Elect Root Bridge
       ↓
Find best path to Root
       ↓
Select Root Ports
       ↓
Select Designated Ports
       ↓
Suppress redundant forwarding paths
       ↓
Loop-free Layer 2 topology
       ↓
If topology changes
       ↓
Recalculate / activate backup path
```

And RSTP is essentially the **faster, more sophisticated version of this same fundamental idea**.

## What I would NOT spend much time on

For your current interview preparation, I would deliberately **not** go deep into:

* Every BPDU bit and flag
* Exact BPDU packet byte layout
* Historical STP implementations
* Detailed TCN propagation
* Every possible STP timer edge case
* Shared-media/hub-specific Backup Port scenarios
* Vendor-specific STP commands
* Deep MSTP configuration
* obscure 802.1D implementation details

Those are diminishing-return topics unless the Arista interview specifically pushes you toward switching protocol internals.

### Your target depth

For this topic, I'd aim for:

**Conceptual foundation: 40%**
**Topology reasoning: 30%**
**RSTP mechanisms: 20%**
**Packet/timer minutiae: 10%**

That is a much better investment for an interview than trying to memorize the entire 802.1D/802.1w specification.

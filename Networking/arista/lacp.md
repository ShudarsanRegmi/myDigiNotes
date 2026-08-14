<img width="1402" height="1122" alt="image" src="https://github.com/user-attachments/assets/19eddcaa-3446-4867-8ed6-241c5633d8e5" />



Absolutely. LACP is a good one-shot topic for your Arista prep because the **core concept is simple**, but there are a few interview-worthy details worth knowing.

# LACP: From Zero to Interview-Ready

## 1. First, what problem are we solving?

Suppose we have two switches:

```text
Switch A ---------------- Switch B
```

Now imagine we want more bandwidth and redundancy between them.

We could connect two physical links:

```text
Switch A ================= Switch B
          Link 1

Switch A ================= Switch B
          Link 2
```

But there is a problem.

If both links are ordinary Layer 2 connections, **Spanning Tree Protocol (STP)** may consider the second link redundant and block it to prevent a Layer 2 loop.

So instead of treating these as two independent links, we can make them behave logically as **one larger link**.

That is the idea behind **Link Aggregation**.

---

# 2. Link Aggregation

Link aggregation means:

> **Combining multiple physical network links into one logical link.**

For example:

```text
Physical:

A ======== B
A ======== B
A ======== B
A ======== B
```

can logically appear as:

```text
A ================= B
       LAG
```

LAG = **Link Aggregation Group**

So instead of the network thinking:

```text
4 separate links
```

it thinks:

```text
1 logical link containing 4 physical links
```

This gives us:

* increased aggregate bandwidth
* redundancy
* link-level failure tolerance
* simpler logical topology

---

# 3. Important terminology: LAG, LACP, Port-Channel

These three terms are related but **not identical**.

### LAG

The logical group of physical links.

```text
4 physical links
       ↓
      LAG
```

### LACP

**Link Aggregation Control Protocol**

It is the protocol used by devices to **negotiate and maintain** the link aggregation.

### Port-channel

A common vendor term for the logical interface representing the aggregated links.

For example, on many network devices you might see:

```text
Ethernet1
Ethernet2
Ethernet3
Ethernet4
       ↓
   Port-Channel1
```

So:

> **LAG is the logical aggregation concept. LACP is the protocol used to negotiate it. Port-channel is a common name for the resulting logical interface.**

---

# 4. Why not just manually configure the links?

You can statically configure a link aggregation group.

But then both sides have to agree manually about:

```text
Which interfaces belong to the group?
Are they compatible?
Should this link participate?
Did a link fail?
Should it be removed from the group?
```

LACP automates this coordination.

Instead of blindly assuming:

```text
"These four ports belong together."
```

the devices communicate and negotiate:

```text
"Hey, I want to aggregate these links."

"Okay, I agree."

"Are our parameters compatible?"

"Yes."

"Then let's form the aggregation."
```

---

# 5. Where does LACP operate?

LACP operates between the **two directly connected devices**.

For example:

```text
Switch A                         Switch B

Ethernet1 ==================== Ethernet1
Ethernet2 ==================== Ethernet2
Ethernet3 ==================== Ethernet3
Ethernet4 ==================== Ethernet4
```

LACP messages are exchanged between A and B.

It is not a routing protocol.

It is not an application protocol.

It is a **link-management/control protocol** for link aggregation.

---

# 6. What does LACP actually do?

LACP primarily determines:

> **Which physical links can legitimately participate in the same aggregation group.**

Suppose:

```text
Switch A                         Switch B

Port 1 ======================== Port 1
Port 2 ======================== Port 2
Port 3 ======================== Port 3
Port 4 ======================== Port 4
```

LACP helps the devices determine:

```text
Port 1 → eligible
Port 2 → eligible
Port 3 → eligible
Port 4 → eligible
```

and form:

```text
Port-Channel 1
```

If something changes, LACP can also detect that and remove a failed/incompatible member.

---

# 7. LACP uses LACPDUs

LACP communicates using special control frames called:

**LACPDUs**

LACPDU = **LACP Data Unit**

Conceptually:

```text
Switch A                     Switch B
   |                            |
   | ------ LACPDU ----------> |
   | <----- LACPDU ----------- |
   |                            |
```

These frames carry information that allows the two sides to identify themselves and determine whether the links can be aggregated.

You don't need to memorize the complete LACPDU format for your interview.

Just remember:

> **LACP communicates using LACPDUs.**

---

# 8. Active and Passive mode

This is one of the most commonly asked LACP questions.

LACP has two modes:

```text
Active
Passive
```

## Active

The device actively sends LACPDUs and tries to establish LACP.

Think:

> "I will initiate LACP."

## Passive

The device waits for LACP packets from the other side.

Think:

> "I won't initiate, but I'll respond if you initiate."

---

# 9. The famous Active/Passive combinations

| Side A  | Side B  | LACP forms? |
| ------- | ------- | ----------- |
| Active  | Active  | Yes         |
| Active  | Passive | Yes         |
| Passive | Passive | **No**      |

Why?

Because:

```text
Passive + Passive

"I'll wait for you."

"I'll wait for you."

Nothing happens.
```

Whereas:

```text
Active + Passive

Active → sends LACPDU
Passive → responds
```

So the important rule is:

> **At least one side must be Active.**

This is a very common interview question.

---

# 10. LACP does NOT increase the speed of one individual flow

This is an extremely important nuance.

Suppose we aggregate:

```text
4 × 10 Gbps links
```

The aggregate capacity is approximately:

```text
40 Gbps
```

But don't conclude:

> "One TCP connection can now transmit at 40 Gbps."

Usually, traffic is distributed across the physical links using a **hashing algorithm**.

For example:

```text
Flow A → Link 1
Flow B → Link 2
Flow C → Link 3
Flow D → Link 4
```

The exact hashing inputs depend on the device/configuration and can include things such as:

* source MAC
* destination MAC
* source IP
* destination IP
* source/destination TCP/UDP ports

The switch calculates a hash and selects a member link.

---

# 11. Why hashing?

Imagine we have:

```text
LAG
 |
 +---- Link 1
 +---- Link 2
 +---- Link 3
 +---- Link 4
```

The switch needs a deterministic way to decide:

> "Which physical link should carry this traffic?"

It hashes selected fields from the packet.

Conceptually:

```text
Packet
  ↓
Extract fields
  ↓
Hash
  ↓
Result
  ↓
Select member link
```

For example:

```text
10.1.1.10:5000 → 10.2.2.20:443
                  ↓
                hash
                  ↓
               Link 3
```

Another flow:

```text
10.1.1.11:5001 → 10.2.2.20:443
                  ↓
                hash
                  ↓
               Link 1
```

So multiple flows can utilize multiple physical links.

---

# 12. Why doesn't LACP simply split one packet across all links?

Because that would create significant complexity.

Suppose packets of one flow were sent:

```text
Packet 1 → Link 1
Packet 2 → Link 4
Packet 3 → Link 2
Packet 4 → Link 3
```

They could arrive out of order.

Reordering packets can hurt performance, especially for TCP.

Therefore, implementations generally maintain **flow affinity**:

> A particular flow tends to remain on the same physical member link.

So:

```text
Flow A → Link 1
```

rather than:

```text
Flow A → randomly changing links
```

This is why LACP provides **aggregate bandwidth across multiple flows**, not necessarily the sum of all link speeds for one flow.

---

# 13. What happens if one link fails?

Suppose:

```text
4 × 10 Gbps

Link 1 ✓
Link 2 ✓
Link 3 ✓
Link 4 ✓
```

Aggregate capacity:

```text
40 Gbps
```

Now Link 3 fails:

```text
Link 1 ✓
Link 2 ✓
Link 3 ✗
Link 4 ✓
```

The LAG remains operational.

Remaining capacity:

```text
30 Gbps
```

Traffic can be redistributed across the surviving links.

This gives LACP/LAG an important property:

> **Link-level redundancy without requiring the entire logical connection to fail when one physical link fails.**

---

# 14. But what if all links don't have the same characteristics?

This is where LACP becomes more than simply "put multiple cables together."

The member links need to be compatible enough to participate in the same aggregation.

For example, parameters such as:

* speed
* duplex
* VLAN configuration
* LACP configuration
* aggregation parameters

need to be compatible according to the platform and configuration.

You generally don't want:

```text
Link 1 → VLAN 10,20
Link 2 → VLAN 30,40
```

inside the same logical aggregation.

The idea is that the physical members should behave consistently as parts of one logical interface.

---

# 15. LACP has an important concept: System ID

LACP devices need to identify themselves.

An LACP **System ID** is formed using:

```text
System Priority + System MAC Address
```

Conceptually:

```text
Switch A
System ID
   ↓
Priority + MAC

Switch B
System ID
   ↓
Priority + MAC
```

You don't need to memorize every field inside LACP yet.

But you should recognize **System ID** if it appears in an interview or EOS output.

---

# 16. What is the LACP key?

LACP also uses a concept called an **LACP Key**.

The key helps identify which ports are compatible for aggregation.

You can think of it roughly as:

> "These ports have compatible aggregation characteristics and can belong to the same aggregation."

Again, don't over-focus on the exact internal calculation.

For your level:

```text
System ID
→ identifies the LACP system

LACP Key
→ helps determine aggregation compatibility
```

is sufficient.

---

# 17. LACP vs EtherChannel

You may encounter another term:

**EtherChannel**

This is Cisco terminology for link aggregation.

Conceptually:

```text
EtherChannel
      ≈
Link aggregation
```

Cisco commonly uses:

```text
Port-Channel
```

Arista EOS also uses the concept of a **Port-Channel**.

The underlying standards-based protocol for dynamic negotiation is LACP.

Historically, Cisco also had **PAgP**, a proprietary aggregation protocol.

You don't need to spend much time on PAgP for modern Arista preparation.

---

# 18. LACP vs static LAG

There are two broad approaches.

### Static aggregation

You manually configure both sides to form the same aggregation.

No LACP negotiation is required.

```text
Switch A                  Switch B

"These ports are members." 
"These ports are members."
```

### LACP-based aggregation

The devices negotiate:

```text
Switch A
   ↕
 LACP
   ↕
Switch B
```

This gives better protection against configuration mistakes and allows the devices to dynamically detect membership/state changes.

For an interview:

> **LACP is a negotiation protocol; link aggregation itself can also be configured statically without LACP.**

That's an important distinction.

---

# 19. What does LACP protect you from?

Consider this bad configuration:

```text
Switch A                      Switch B

Port 1 ===================== Port 1
Port 2 ===================== Port 2
```

Suppose Switch A thinks:

```text
Port 1 + Port 2 = LAG
```

but Switch B thinks:

```text
Port 1 = one network
Port 2 = another network
```

You could create serious forwarding problems.

LACP provides a mechanism for the devices to negotiate and verify aggregation membership rather than blindly assuming everything is correct.

---

# 20. LACP and STP

This is a very useful interview connection.

Without aggregation:

```text
Switch A
  |\
  | \
  |  \
  |   \
Switch B
```

Multiple Layer 2 paths can create loops.

STP may block redundant links.

With LAG:

```text
Switch A
   ||
   ||  ← one logical link
   ||
Switch B
```

The multiple physical links are treated as **one logical connection** from the perspective of higher-level protocols.

Therefore STP sees the LAG/Port-Channel as one logical link rather than seeing every physical member as an independent topology path.

This allows the physical links inside the LAG to be simultaneously active.

---

# 21. LACP is not load balancing itself

This is a subtle distinction.

LACP's primary job is:

```text
Negotiation
Membership
Synchronization
Link state
```

The actual decision:

```text
Which member link carries this flow?
```

is generally handled by the switch's **load-balancing/hash mechanism**.

So don't say:

> "LACP load-balances packets."

Better:

> **LACP establishes and maintains the aggregated link, while the switch's hashing/load-balancing mechanism distributes traffic across the member links.**

That sounds much more technically precise.

---

# 22. LACP in a server-to-switch scenario

LACP isn't limited to:

```text
Switch ↔ Switch
```

You can also have:

```text
Server
  ||
  ||  multiple NIC links
  ||
Switch
```

The server can form a LAG with the switch.

This is useful for:

* server redundancy
* increased aggregate bandwidth
* network interface failure tolerance

The server and switch need to support compatible link aggregation behavior.

---

# 23. LACP in an Arista data-center

For your Arista interview, you will probably encounter scenarios like:

```text
       Spine
       /   \
      /     \
   Leaf     Leaf
     ||       ||
   Server   Server
```

or:

```text
Leaf ================= Leaf
       multiple links
```

LACP can be used to aggregate multiple physical Ethernet links into a Port-Channel.

In Arista EOS, you will encounter interfaces such as:

```text
Ethernet1
Ethernet2
Ethernet3
```

being members of something conceptually like:

```text
Port-Channel1
```

You don't need to memorize EOS CLI yet unless the job description explicitly emphasizes configuration.

---

# 24. One important Arista-related concept: MLAG

This is worth knowing because **Arista environments commonly use MLAG**.

Ordinary LACP aggregation usually looks like:

```text
Server
  || 
  ||
Switch A
```

But what if we want the server to connect redundantly to **two different switches**?

```text
             Server
             /    \
            /      \
        Switch A  Switch B
```

Normally, these are two separate devices.

How can the server treat them as one logical LAG?

That's where **MLAG**, or Multi-Chassis Link Aggregation, comes in.

Conceptually:

```text
                 Server
                /      \
               /        \
          Switch A ==== Switch B
```

Switch A and Switch B coordinate so that the server can form one logical LAG across both switches.

This is an important Arista-specific area, but **don't dive into MLAG yet**.

For your one-shot LACP preparation, just recognize:

> **LACP normally negotiates aggregation between two systems. MLAG extends the concept so that a device can form an aggregated connection to multiple physical switches that cooperate as a logical pair.**

We'll treat MLAG separately if it appears in your Arista prep list.

---

# 25. Interview questions you should be ready for

### What is LACP?

> LACP is a standards-based protocol used to dynamically negotiate and maintain a Link Aggregation Group between two network devices.

### Why use LACP?

> To combine multiple physical links into one logical link, providing aggregate bandwidth and link-level redundancy while dynamically managing the member links.

### What are LACP active and passive modes?

> Active actively sends LACPDUs to establish aggregation, while passive waits for LACPDUs. Active-Active and Active-Passive can form an LACP relationship, but Passive-Passive cannot.

### Does LACP make one connection use the bandwidth of all links?

> Generally no. Traffic is distributed across member links using hashing, usually maintaining flow affinity. Therefore aggregate bandwidth increases across multiple flows, but a single flow is typically limited to one physical member link.

### What happens when one member link fails?

> LACP removes the failed member from the active aggregation and traffic continues over the remaining members.

### Is LACP the same thing as link aggregation?

> No. Link aggregation is the concept of combining links; LACP is a protocol used to negotiate and maintain the aggregation dynamically.

### Does LACP perform load balancing?

> LACP establishes and maintains the LAG. The switch's hashing mechanism generally determines which physical member carries each flow.

---

# 26. The mental model

Keep this picture:

```text
              LOGICAL LINK

Switch A ========================== Switch B
             Port-Channel
                  |
       +----------+----------+
       |          |          |
     Link 1     Link 2     Link 3
     10G        10G        10G
```

LACP operates between the two devices:

```text
Switch A  <--------- LACP --------->  Switch B
```

It determines which physical links can participate.

Then the switch distributes traffic:

```text
Flow A → Link 1
Flow B → Link 2
Flow C → Link 3
```

If Link 2 dies:

```text
Flow A → Link 1
Flow B → Link 3
Flow C → Link 3
```

The logical Port-Channel can remain up.

---

# What you need to remember for Arista

### Must know

```text
Link aggregation
LAG
LACP
Port-Channel
LACPDU
Active / Passive
Active-Active
Active-Passive
Passive-Passive = no formation
Link failure handling
Flow hashing
Aggregate bandwidth vs single-flow bandwidth
LACP vs static LAG
LACP vs STP
```

### Know conceptually

```text
System ID
LACP Key
LACP synchronization
EtherChannel
MLAG
```

### Don't spend time on

```text
Every LACPDU field
Exact state-machine implementation
Every LACP timer/state detail
Vendor-specific EOS configuration
```

## Final one-liner

> **LACP dynamically negotiates multiple physical Ethernet links into one logical link, giving redundancy and aggregate bandwidth, while traffic is distributed across the member links using hashing.**

For your Arista prep, **LACP itself can stop here**. The next worthwhile concept would be **MLAG**, because that is where LACP becomes particularly interesting in a data-center environment.

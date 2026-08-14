# VXLAN: From Zero to Interview-Ready

## 0. First, the vocabulary you need

Before understanding VXLAN, we need to understand four terms that are commonly used in data-center networking.

### 0.1 Leaf switch

A **leaf switch** is a switch that directly connects to servers, storage systems, firewalls, or other devices at the edge of the data-center network.

For example:

```text
Server A
   |
   |
Leaf Switch
```

The leaf is therefore where server traffic enters and leaves the data-center network.

In a traditional network, you may simply call this an access switch. In modern data centers, leaf switches are usually part of a **leaf-spine architecture**.

---

### 0.2 Spine switch

A **spine switch** is a high-speed switch used to connect leaf switches together.

For example:

```text
              Spine
             /     \
          Leaf     Leaf
           |         |
        Server A   Server B
```

The important idea is:

> Leaf switches connect to end devices. Spine switches connect leaf switches.

A typical spine does not directly connect to servers.

---

### 0.3 Leaf-spine architecture

A **leaf-spine network** is a network architecture where:

```text
        Spine 1       Spine 2
          / \          / \
         /   \        /   \
      Leaf 1 Leaf 2 Leaf 3 Leaf 4
        |      |       |      |
      Servers Servers Servers Servers
```

Each leaf normally connects to multiple spine switches.

This provides:

* multiple paths
* redundancy
* predictable connectivity
* good scalability
* high bandwidth between servers

The exact implementation is not important for VXLAN yet.

Just remember:

> **Leaf = connects to devices**
>
> **Spine = connects the leaves**

---

### 0.4 Network fabric

You will frequently hear people say:

> "The data-center fabric"

or

> "The IP fabric"

Here, **fabric** simply means the interconnected network infrastructure that provides connectivity.

For example:

```text
        Spine 1
       /       \
    Leaf 1 ---- Leaf 2
       \       /
        Spine 2
```

This collection of switches and their links can be called the **network fabric**.

When we say **IP fabric**, we generally mean that this underlying network provides connectivity using IP routing.

Don't think of "fabric" as some new protocol.

It is essentially a term for the interconnected network architecture.

---

# 1. Now, the actual problem VXLAN solves

Let's forget VXLAN for a moment.

Suppose we have two servers:

```text
Server A                         Server B
    |                                |
 Switch 1                         Switch 2
```

Suppose both servers belong to VLAN 10.

Because they are in the same VLAN, they can communicate at Layer 2.

Now imagine that our physical network becomes larger:

```text
Server A
   |
Switch 1
   |
Switch 2
   |
Switch 3
   |
Server B
```

We can extend VLAN 10 through all these switches.

But modern data centers increasingly prefer to build the physical network using **Layer 3 routing**.

Why?

Because a large Layer 2 network has scalability and failure-domain limitations, whereas a routed network can be designed with multiple paths and better scalability.

So imagine this:

```text
Server A
   |
 Leaf 1
   |
   | Layer 3
   |
 Spine
   |
   | Layer 3
   |
 Leaf 2
   |
Server B
```

The links between these switches are routed IP links.

Now we have a problem.

Server A and Server B may logically need to be in the same Layer 2 network, but the physical network between them is Layer 3. 

How can we carry a Layer 2 Ethernet frame through this Layer 3 network?

This is the fundamental problem VXLAN addresses.

---

# 2. The fundamental idea of VXLAN

VXLAN stands for:

**Virtual Extensible LAN**

Its fundamental purpose is:

> **VXLAN allows a Layer 2 network to be carried across a Layer 3 IP network by encapsulating the original Ethernet frame inside an IP packet.**

This is the sentence you should understand, not merely memorize.

Consider:

```text
Server A
   |
 Leaf 1
   |
   |        Layer 3 IP network
   |
 Spine
   |
   |
 Leaf 2
   |
Server B
```

From the physical network's perspective, the packet traveling between Leaf 1 and Leaf 2 is an IP packet.

But inside that IP packet is the original Ethernet frame from Server A.

Therefore:

```text
Original Ethernet frame
          ↓
     VXLAN encapsulation
          ↓
       IP packet
          ↓
     Layer 3 network
          ↓
      Destination
          ↓
      Decapsulation
          ↓
Original Ethernet frame
```

That is VXLAN.

---

# 3. Why do we need this?

There are two major reasons you should know.

## 3.1 VLAN scalability

A VLAN identifier is 12 bits.

That gives approximately:

```text
2^12 = 4096
```

possible values, although not all are usable as ordinary VLAN IDs.

VXLAN uses a **24-bit VNI**.

VNI means:

**VXLAN Network Identifier**

Therefore:

```text
2^24 ≈ 16.7 million
```

possible VXLAN segments.

So VXLAN provides a much larger logical segmentation space.

You can think of it as:

```text
Traditional VLAN
        ↓
12-bit VLAN ID

VXLAN
        ↓
24-bit VNI
```

---

## 3.2 Layer 2 over a Layer 3 network

This is arguably the more fundamental reason.

We want the physical data-center network to be a scalable Layer 3 network:

```text
        Spine
       /     \
    Leaf     Leaf
      |       |
   Server   Server
```

But we may still want servers to appear as if they belong to the same logical Layer 2 network.

VXLAN creates that logical Layer 2 overlay.

---

# 4. Underlay and overlay

These two terms are essential.

## Underlay

The **underlay** is the actual physical network that provides connectivity.

For example:

```text
Server
  |
Leaf
  |
Spine
  |
Leaf
  |
Server
```

If the links between the switches use IP routing, we have an **IP underlay**.

Its job is basically:

> "Can I deliver an IP packet from one VXLAN endpoint to another?"

The underlay does not need to understand the tenant's logical Layer 2 network.

---

## Overlay

The **overlay** is the logical network created on top of the underlay.

Conceptually:

```text
Server A ================= Server B
          logical network
```

The physical path might actually be:

```text
Server A
   |
Leaf 1
   |
Spine
   |
Leaf 2
   |
Server B
```

The overlay makes the two endpoints appear logically connected even though the physical network between them is different.

Therefore:

> **Underlay = physical network that transports the traffic**
>
> **Overlay = logical network carried over that physical network**

This distinction is extremely important in VXLAN.

---

# 5. VTEP

Now we need one more important term.

**VTEP = VXLAN Tunnel Endpoint**

A VTEP is the device that performs VXLAN encapsulation and decapsulation.

In many data-center designs, the leaf switch acts as the VTEP.

Consider:

```text
Server A
   |
Leaf 1
(VTEP 1)
   |
   | IP network
   |
(VTEP 2)
Leaf 2
   |
Server B
```

Leaf 1 can take an Ethernet frame and encapsulate it into VXLAN.

Leaf 2 can receive that VXLAN packet and remove the VXLAN encapsulation.

So:

```text
VTEP 1
Ethernet frame
      ↓
Encapsulation
      ↓
VXLAN packet
      ↓
IP network
      ↓
VTEP 2
      ↓
Decapsulation
      ↓
Ethernet frame
```

The VTEPs are therefore the endpoints of the VXLAN tunnel.

---

# 6. What exactly happens to a packet?

This is the most important part of the topic.

Suppose:

```text
Server A
MAC = AA:AA

Server B
MAC = BB:BB
```

Server A wants to send an Ethernet frame to Server B.

Initially the frame looks conceptually like:

```text
+-------------------------+
| Ethernet Header         |
| Src MAC = AA:AA        |
| Dst MAC = BB:BB        |
+-------------------------+
| Payload                 |
+-------------------------+
```

Leaf 1 receives this frame.

If Leaf 1 knows that Server B is reachable through another VTEP, it encapsulates the frame.

The resulting packet conceptually looks like:

```text
+-------------------------+
| Outer Ethernet Header   |
+-------------------------+
| Outer IP Header         |
+-------------------------+
| UDP Header              |
+-------------------------+
| VXLAN Header            |
+-------------------------+
| Original Ethernet Frame |
+-------------------------+
| Original Payload        |
+-------------------------+
```

The original Ethernet frame becomes the **inner packet/frame**.

The newly added headers are the **outer headers**.

---

# 7. Why does the outer IP header matter?

The physical network is a Layer 3 network.

Routers forward packets based on the destination IP address.

Therefore, VXLAN creates an outer IP packet that says, conceptually:

```text
Source IP = VTEP 1
Destination IP = VTEP 2
```

The underlay network simply routes this packet.

For example:

```text
             Underlay

VTEP 1
  |
  | Outer IP packet
  ↓
Spine
  |
  ↓
VTEP 2
```

The spine does not need to understand the original Server A to Server B Ethernet frame.

It simply routes the outer IP packet toward VTEP 2.

This is a very important insight:

> **The underlay transports the VXLAN packet using ordinary IP routing.**

---

# 8. Why UDP?

VXLAN uses UDP as its transport protocol.

The standard VXLAN destination UDP port is:

```text
4789
```

So the packet looks conceptually like:

```text
Outer Ethernet
      ↓
Outer IP
      ↓
UDP
      ↓
VXLAN
      ↓
Original Ethernet
```

The exact UDP mechanics are not important for your first pass.

Just remember:

**VXLAN uses UDP port 4789.**

---

# 9. What is the VXLAN header?

The VXLAN header is 8 bytes.

The most important field inside it is the:

**VNI**

VNI means:

**VXLAN Network Identifier**

For example:

```text
VNI 10000 → logical network A
VNI 20000 → logical network B
VNI 30000 → logical network C
```

The VNI tells the receiving VTEP which VXLAN segment the traffic belongs to.

So you can roughly think:

```text
VLAN 10
   ↓
local Layer 2 segment

VNI 10000
   ↓
VXLAN logical segment
```

Do not interpret VNI as simply "a bigger VLAN ID". The two serve related but different roles in the overall architecture.

---

# 10. What happens at the destination?

Eventually the packet reaches the destination VTEP.

For example:

```text
VTEP 1
   |
   | VXLAN packet
   ↓
IP underlay
   |
   ↓
VTEP 2
```

VTEP 2 recognizes the VXLAN packet.

It removes:

```text
Outer Ethernet
Outer IP
UDP
VXLAN header
```

What remains is the original Ethernet frame:

```text
+-------------------------+
| Original Ethernet       |
| Src = AA:AA             |
| Dst = BB:BB             |
+-------------------------+
| Payload                 |
+-------------------------+
```

VTEP 2 then forwards that frame toward Server B.

So the complete process is:

```text
Server A
   ↓
Ethernet frame
   ↓
VTEP 1
   ↓
VXLAN encapsulation
   ↓
IP underlay
   ↓
VTEP 2
   ↓
VXLAN decapsulation
   ↓
Ethernet frame
   ↓
Server B
```

This is the core of VXLAN.

---

# 11. What is a VXLAN tunnel?

The logical path between two VTEPs is called a **VXLAN tunnel**.

For example:

```text
VTEP 1 ================= VTEP 2
          VXLAN tunnel
```

It does not necessarily mean there is a dedicated physical cable between them.

The actual packet may travel through several physical switches:

```text
VTEP 1
   |
Spine 1
   |
Spine 2
   |
VTEP 2
```

The VXLAN tunnel is a logical overlay relationship.

The underlay carries the actual packets.

---

# 12. What about VLANs?

This is another important point.

A server may still connect to a leaf using a traditional VLAN.

For example:

```text
Server
   |
VLAN 100
   |
Leaf
   |
VXLAN
   |
VNI 10100
```

The leaf can map local VLAN traffic into a VXLAN segment.

Therefore, don't think:

> "VXLAN completely replaces VLAN."

A better mental model is:

> **VLAN can be used for local Layer 2 segmentation, while VXLAN extends the logical network across the IP underlay.**

The exact VLAN-to-VNI mapping depends on the network design.

---

# 13. How does the VTEP know where the destination is?

Now we reach an important distinction.

Suppose Server A wants to reach Server B.

Leaf 1 needs to know:

> "Which VTEP currently has Server B?"

VXLAN itself primarily defines the **data-plane encapsulation**.

It does not by itself provide a sophisticated control plane for distributing all endpoint reachability information.

Historically, VXLAN could use a mechanism called:

**Flood-and-learn**

Modern data-center deployments commonly use:

**EVPN**

with VXLAN.

This is why you frequently hear:

> **EVPN-VXLAN**

---

# 14. Flood-and-learn

Imagine Leaf 1 doesn't know where the destination MAC address exists.

Traditional Ethernet networks deal with unknown destinations by flooding the frame.

VXLAN can extend this behavior across the overlay.

There is also a category of traffic called **BUM** traffic.

BUM means:

```text
B = Broadcast
U = Unknown Unicast
M = Multicast
```

VXLAN networks need a way to handle BUM traffic.

Older VXLAN designs commonly used multicast mechanisms in the underlying network.

You do not need to go deep into multicast VXLAN implementation for your current Arista preparation.

Know the conceptual progression:

```text
VXLAN
  ↓
Can encapsulate traffic

Flood-and-learn
  ↓
One way to discover/handle remote destinations

EVPN
  ↓
Modern control-plane approach
```

---

# 15. VXLAN + EVPN

This is where the architecture becomes much more powerful.

Think of the two technologies as solving different problems.

### VXLAN

Primarily provides the **data-plane encapsulation**.

It answers:

> "How can I carry this logical network traffic across the IP network?"

### EVPN

Provides the **control plane**.

It answers questions such as:

> "Where is this MAC address?"

> "Which VTEP has this endpoint?"

> "Which IP prefix belongs to which location?"

So conceptually:

```text
             EVPN
              |
       Control plane
              |
       "Where is X?"
              |
              ↓
            VXLAN
              |
         Data plane
              |
       "Carry traffic"
```

This distinction is one of the most valuable things to understand before studying EVPN.

---

# 16. What is a Layer 3 VNI?

So far we have mostly discussed carrying Layer 2 networks.

VXLAN can also be used to create Layer 3 tenant networks.

You will therefore encounter:

**L2 VNI**

and

**L3 VNI**

For your first pass:

### L2 VNI

Represents a logical Layer 2 VXLAN segment.

```text
L2 network
   ↓
L2 VNI
```

### L3 VNI

Used for Layer 3 routing between VXLAN segments, particularly in multi-tenant architectures.

```text
Tenant routing
      ↓
   L3 VNI
```

The detailed mechanisms around L3 VNI, VRFs, IRB, symmetric IRB, and anycast gateways belong more naturally in the EVPN section.

Don't try to memorize them yet.

---

# 17. Why VXLAN is useful in modern data centers

Let's now connect all the pieces.

A modern data center can build its physical network as:

```text
             Spine
            /     \
         Leaf     Leaf
          |         |
       Servers    Servers
```

The physical network can operate as a routed IP network.

This gives us a scalable **underlay**.

Then VXLAN creates logical networks over it:

```text
       Logical VXLAN network
Server A ================= Server B
          VNI 10000
```

So we get:

```text
Physical network
      ↓
Layer 3 IP underlay
      ↓
VXLAN overlay
      ↓
Logical Layer 2 / Layer 3 networks
      ↓
Multiple isolated tenants/applications
```

This separation is one of the major architectural advantages.

---

# 18. What problems does VXLAN solve?

For interview purposes, remember these four.

### 1. Layer 2 over Layer 3

It allows Layer 2 traffic to traverse a Layer 3 IP network.

### 2. VLAN scalability

It provides a 24-bit VNI instead of the traditional 12-bit VLAN identifier space.

### 3. Data-center network scalability

It allows a routed IP underlay to coexist with large logical overlay networks.

### 4. Network virtualization and multi-tenancy

Different logical networks can coexist over the same physical infrastructure.

For example:

```text
Physical infrastructure
        |
        +---- VNI 10000 → Tenant A
        |
        +---- VNI 20000 → Tenant B
        |
        +---- VNI 30000 → Tenant C
```

The tenants can remain logically isolated while sharing the same physical switches and links.

---

# 19. What VXLAN does NOT mean

Avoid these common misconceptions.

### "VXLAN is a replacement for IP."

No.

VXLAN normally runs over an IP underlay.

---

### "VXLAN eliminates VLANs."

No.

VLANs can still exist at the local/server-facing side.

VXLAN provides the overlay mechanism.

---

### "VXLAN itself tells switches where every server is."

Not really.

The VXLAN data plane handles encapsulation.

The control plane, commonly EVPN, distributes reachability information.

---

### "The spine understands the tenant's Ethernet network."

Not necessarily.

The spine can simply route the outer IP packet.

The VXLAN VTEPs handle the overlay.

---

# 20. The complete architecture

Now that all the terms have been introduced, this diagram should make sense:

```text
                    VXLAN OVERLAY

        Server A ================= Server B
           |          VNI             |
           |                           |
        Leaf 1                       Leaf 2
        VTEP 1                       VTEP 2
           |                           |
           +-----------+---------------+
                       |
                  IP UNDERLAY
                       |
                 Spine switches
```

More realistically:

```text
                         Spine 1
                        /       \
                       /         \
                 Leaf 1           Leaf 2
                 VTEP 1           VTEP 2
                   |                 |
               Server A          Server B


        <--------- VXLAN --------->

        <------ IP underlay ------>

```

The terminology now has a clear meaning:

**Server:** End device generating/receiving traffic.

**Leaf:** Switch connecting servers and often acting as a VTEP.

**Spine:** Switch connecting the leaf switches.

**Fabric:** The interconnected data-center switching infrastructure.

**Underlay:** The physical/routed IP network.

**Overlay:** The logical network running over the underlay.

**VTEP:** Device that encapsulates and decapsulates VXLAN traffic.

**VNI:** 24-bit identifier for a VXLAN segment.

**VXLAN:** Encapsulation mechanism carrying overlay traffic across the IP underlay.

**EVPN:** Control-plane technology commonly used with VXLAN to distribute endpoint reachability information.

---

# 21. The packet journey you should be able to explain in an interview

If an interviewer asks:

> "Explain how VXLAN works."

A strong fresher-level answer would be:

VXLAN allows a Layer 2 overlay to operate over a Layer 3 IP underlay. The leaf switches commonly act as VXLAN tunnel endpoints. When a frame needs to reach a remote VXLAN segment, the source VTEP encapsulates the original Ethernet frame inside a VXLAN header, UDP header, and outer IP header. The IP underlay routes this packet toward the destination VTEP. The destination VTEP removes the outer encapsulation and forwards the original Ethernet frame to the destination host. The VNI identifies the logical VXLAN segment, and modern deployments commonly use EVPN as the control plane to distribute endpoint reachability information.

That is already a solid interview answer.

---

# 22. What you actually need to remember for Arista

For your one-shot treatment, I would prioritize these.

## Must know

```text
Why VXLAN exists
Layer 2 over Layer 3
Underlay
Overlay
Leaf
Spine
Leaf-spine architecture
VTEP
VNI
VXLAN encapsulation
Packet journey
VXLAN vs VLAN
24-bit VNI
UDP 4789
```

## Know conceptually

```text
BUM traffic
Flood-and-learn
Multicast-based VXLAN
L2 VNI
L3 VNI
VXLAN + EVPN
```

## Don't spend much time on yet

```text
Every VXLAN header bit
Detailed multicast tree construction
Hardware forwarding pipeline
Vendor-specific VXLAN configuration
Advanced EVPN route types
Detailed IRB mechanisms
```

We will selectively cover those later when they become relevant.

---

# Final mental model

Reduce the entire topic to this:

```text
             LOGICAL OVERLAY
       Server A ============ Server B
                  VXLAN
                    |
                    |
             Physical network
                    |
              IP UNDERLAY
                    |
             Leaf -- Spine -- Leaf
```

The problem:

> "I want a logical Layer 2 network, but I want my physical data-center network to be a scalable Layer 3 network."

The solution:

> **VXLAN carries the Layer 2 traffic across that Layer 3 network.**

The key components:

```text
Leaf
  ↓
often acts as VTEP

VTEP
  ↓
encapsulates / decapsulates

VNI
  ↓
identifies the VXLAN segment

Underlay
  ↓
carries the outer IP packet

Overlay
  ↓
logical network carried over the underlay

EVPN
  ↓
commonly provides the control plane
```

If this mental model is solid, you have the foundation required to move to **EVPN**, which is the part I would recommend studying at a somewhat greater depth for an Arista interview.

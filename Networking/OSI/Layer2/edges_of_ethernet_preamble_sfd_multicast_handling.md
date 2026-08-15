These are exactly the right doubts to clear because they get into the boundary between **Layer 1 signaling** and **Layer 2 framing**. Let's take them one by one.

## 1. Why does Ethernet need a preamble?

The key point is: **the receiver needs to synchronize its physical-layer clock with the incoming bitstream.**

Ethernet is ultimately receiving a stream of electrical/optical/radio signals that encode bits. The receiver has to determine:

1. Where the signal starts
2. The timing of each bit
3. When actual frame information begins

The preamble helps primarily with **clock/bit synchronization**, not with identifying the Layer 2 frame fields.

The Ethernet preamble is:

```text
10101010 10101010 10101010 ...
```

7 bytes of `0x55`.

That alternating pattern produces frequent signal transitions, which gives the receiver's physical circuitry a predictable pattern from which it can establish timing.

Then comes:

```text
10101011
   SFD
```

The final two bits differ from the regular preamble pattern, allowing the receiver to recognize:

> "Synchronization is complete. The next bit is the beginning of the actual Ethernet frame."

### The important conceptual distinction

Don't think of the preamble as:

> "Layer 2 needs a header before its header."

Think of it as:

> **PHY needs synchronization before the MAC frame can be interpreted.**

That's a much stronger interview answer.

### How to answer this in an interview

You don't need to explain PLLs, clock recovery circuits, Manchester encoding, etc. unless the interviewer goes deeper.

A good answer would be:

> "The Ethernet preamble is primarily a physical-layer synchronization mechanism. It provides a predictable alternating bit pattern that allows the receiver to synchronize its clock with the incoming signal before processing the MAC frame. The SFD then indicates the exact boundary where the Ethernet frame begins."

That's technically solid without pretending you're a PHY designer.

### One subtle point

The preamble is conventionally shown as part of the Ethernet frame format, but **it is not normally considered part of the MAC frame itself**.

The MAC frame begins effectively at the Destination MAC field after the SFD.

So:

```text
PHY-related
      ↓
Preamble | SFD | Destination MAC | Source MAC | ...
                    ↑
              MAC frame
```

This distinction is worth remembering.

---

# 2. Why does Ethernet need an SFD?

Your intuition is correct:

> "Why doesn't every protocol need an explicit start delimiter?"

Because **not every protocol receives data from the physical medium in the same way Ethernet does.**

The SFD solves a very specific problem at the Ethernet PHY/MAC boundary.

Consider the receiver seeing:

```text
101010101010101010101010101010101010101010101010...
```

This is the preamble.

The receiver uses it to synchronize.

But now there is a problem:

**At what exact bit does the actual frame begin?**

That's what the SFD answers.

The sequence is:

```text
Preamble:
10101010 10101010 10101010 ... 10101010

SFD:
10101011
         ↑
         boundary
```

The SFD deliberately has a pattern different from the preceding preamble.

So the receiver can detect:

```text
"That's the end of synchronization.
The next bit is Destination MAC."
```

### Why doesn't IP have something similar?

Because IP isn't directly receiving a raw physical bitstream.

IP receives a packet from the Layer 2 protocol beneath it.

For example:

```text
Ethernet
   ↓
Destination MAC
Source MAC
EtherType
   ↓
IPv4 packet
   ↓
IP header
```

By the time IPv4 receives the packet, Ethernet has **already established the frame boundary**.

Similarly, TCP doesn't need to delimit the Ethernet frame because IP has already given TCP a properly identified IP segment.

So each layer doesn't independently need to solve the physical framing problem.

### This is the important hierarchy

```text
Physical medium
       ↓
Preamble
       ↓
SFD
       ↓
Ethernet frame boundary established
       ↓
Ethernet MAC processing
       ↓
EtherType
       ↓
IPv4 / IPv6 / ARP
       ↓
Transport protocol
```

The SFD is therefore not some universal requirement of Layer 2.

It's an **Ethernet-specific mechanism associated with the PHY/MAC interface**.

---

# 3. How does Layer 2 multicast work?

This is a very good question.

You're thinking:

> "If there are multiple receivers, how can one frame have multiple destination MAC addresses?"

It **doesn't**.

That's the crucial point.

A multicast Ethernet frame still has **exactly one Destination MAC field**.

The trick is that the destination MAC represents a **multicast group**, rather than one particular host.

For example:

```text
Source MAC
    |
    v
AA:AA:AA:AA:AA:AA

Destination MAC
    |
    v
01:00:5E:xx:xx:xx
```

That destination MAC means:

> "This frame belongs to a particular multicast group."

Multiple hosts can be members of that group.

---

## Think of it like a group address

Suppose:

```text
Host A
Host B
Host C
Host D
```

B, C and D are interested in multicast group X.

They join:

```text
Multicast Group X
```

The sender sends **one Ethernet frame**:

```text
Destination MAC = multicast MAC for Group X
```

The network delivers that frame to the hosts interested in that multicast group.

Conceptually:

```text
                 ┌── Host B
                 │
Host A ── Switch ├── Host C
                 │
                 └── Host D
```

There is still only **one destination MAC in the frame**.

---

# How does the switch know which ports want it?

This is where multicast-specific mechanisms come in.

For IPv4 multicast, hosts use **IGMP** to communicate multicast group membership.

For IPv6, the equivalent is **MLD**.

A switch can observe this membership information, often through **IGMP snooping**, and construct multicast forwarding state.

For example:

```text
Multicast MAC: 01:00:5E:xx:xx:xx

Interested ports:
    Port 2
    Port 5
    Port 8
```

When the multicast frame arrives:

```text
Destination =
01:00:5E:xx:xx:xx
```

the switch forwards it to:

```text
Port 2
Port 5
Port 8
```

instead of sending it to every port.

That's called **multicast forwarding**.

---

# What happens without multicast snooping?

This is another important interview detail.

If the switch doesn't know which ports contain multicast receivers, it may treat the multicast traffic somewhat like broadcast traffic and **flood it within the VLAN**, depending on the switch's multicast handling.

So:

```text
Broadcast
    ↓
Everyone

Unknown multicast
    ↓
Potentially many/all ports

Known multicast
    ↓
Only interested ports
```

The exact behavior depends on the switch implementation and configuration.

---

# IPv4 multicast MAC mapping

IPv4 multicast addresses are mapped to Ethernet multicast MAC addresses.

The Ethernet prefix is:

```text
01:00:5E
```

The remaining bits are derived from the IPv4 multicast address.

Here's the interesting part:

**IPv4 multicast-to-MAC mapping is not one-to-one.**

IPv4 multicast has 28 significant group-address bits, but the Ethernet mapping uses only 23 bits.

Therefore:

```text
2^5 = 32
```

different IPv4 multicast addresses can map to the same Ethernet multicast MAC.

That's a nice deeper interview fact.

---

# IPv6 multicast MAC

IPv6 multicast Ethernet addresses use:

```text
33:33:xx:xx:xx:xx
```

The lower 32 bits are derived from the IPv6 multicast address.

Again, multiple IPv6 multicast addresses can map to the same Ethernet multicast MAC because the mapping does not preserve the entire multicast address.

---

# Broadcast vs Multicast

This distinction is important.

### Broadcast

Destination:

```text
FF:FF:FF:FF:FF:FF
```

Meaning:

> Every host in the Layer 2 broadcast domain.

No membership is required.

---

### Multicast

Destination:

```text
01:00:5E:...
```

for IPv4 multicast.

Meaning:

> Hosts belonging to a particular multicast group.

Membership matters.

---

### Unicast

Destination:

```text
specific host MAC
```

Meaning:

> One receiver.

---

# The bigger picture

You can visualize Layer 2 addressing as:

```text
                 Ethernet Destination MAC
                         |
          ┌──────────────┼──────────────┐
          ↓              ↓              ↓
       Unicast        Multicast      Broadcast
          |              |              |
     One device      Group members    Everyone
```

And importantly:

**The frame always contains only one Destination MAC field.**

The network infrastructure determines which physical ports receive copies of that frame.

---

## One final interview-level distinction

Don't say:

> "Multicast sends the frame to multiple MAC addresses."

That's technically incorrect.

Say:

> **"A multicast Ethernet frame has a single multicast destination MAC address representing a multicast group. Switches can replicate and forward the frame to multiple ports where hosts belonging to that multicast group are connected."**

That's the kind of wording that demonstrates you understand what is actually happening rather than just memorizing "multicast = many receivers."

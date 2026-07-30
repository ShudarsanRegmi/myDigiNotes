**Rephrased question:**

> Teach me the **Layer 2 Ethernet frame header** in depth. Explain every field, why it exists, how switches and NICs use it, the byte sizes, important values, and interview-relevant details. Also explain how VLAN tagging modifies the header.

<img width="1149" height="1369" alt="image" src="https://github.com/user-attachments/assets/0a66a108-535b-435b-af40-716097f78dee" />


---

# Ethernet II Frame Structure

The most common Layer 2 frame today is the **Ethernet II frame**.

```
+----------+-----+-----------+-----------+-----------+---------+---------+
| Preamble | SFD | Dest MAC  | SourceMAC | EtherType | Payload |   FCS   |
| 7 Bytes  |1 B  |  6 Bytes  |  6 Bytes  |  2 Bytes  |46-1500B | 4 Bytes |
+----------+-----+-----------+-----------+-----------+---------+---------+
```

Total frame size (without preamble and SFD):

* Minimum: **64 Bytes**
* Maximum: **1518 Bytes**
* With VLAN: **1522 Bytes**

---

# 1. Preamble (7 Bytes)

```
10101010
10101010
10101010
...
```

Actually:

```
0x55 55 55 55 55 55 55
```

### Purpose

Used for **clock synchronization**.

When bits travel over copper or fiber, the receiver doesn't know where each bit begins.

The alternating

```
10101010...
```

allows the receiver PLL (Phase Locked Loop) to synchronize its clock with the sender.

Think of it as

> "Get ready. Data is coming."

Switches usually don't inspect this.

NIC hardware handles it.

---

# 2. SFD (Start Frame Delimiter)

1 Byte

```
10101011
```

Hex

```
0xD5
```

Purpose

Marks

> "The Ethernet frame starts NOW."

The receiver detects this byte and starts interpreting the next bytes as actual frame data.

Without SFD,

the receiver wouldn't know exactly where the frame begins.

---

# 3. Destination MAC Address

6 Bytes

Example

```
00:1A:2B:3C:4D:5E
```

This is the most important field for switches.

The switch looks here first.

Example

```
PC A
↓

Switch

↓

PC B
```

Destination MAC determines

which switch port should receive the frame.

---

## Types

### Unicast

One receiver

Example

```
00:11:22:33:44:55
```

---

### Broadcast

```
FF:FF:FF:FF:FF:FF
```

Forwarded to every port within the VLAN.

Used by

* ARP Request
* DHCP Discover

---

### Multicast

Starts with specific prefixes

Example

```
01:00:5E
```

IPv4 multicast.

IPv6

```
33:33
```

---

# First Byte Special Bits

Example

```
00
```

Binary

```
00000000
```

The first byte contains two important bits.

## I/G Bit

Individual / Group

0

Unicast

1

Multicast

---

## U/L Bit

Universal / Local

0

Manufacturer assigned

1

Locally administered

Example

Virtual Machines often generate locally administered MACs.

---

# 4. Source MAC

6 Bytes

Identifies sender.

Example

```
AA:BB:CC:DD:EE:FF
```

Switch learns

```
Source MAC
↓

Incoming Port
```

This is how CAM tables are built.

Important

Switches never learn from Destination MAC.

Only Source MAC.

Interview favourite.

---

# 5. EtherType

2 Bytes

Tells Layer 2

"What protocol is inside the payload?"

Examples

| EtherType | Protocol    |
| --------- | ----------- |
| 0x0800    | IPv4        |
| 0x0806    | ARP         |
| 0x86DD    | IPv6        |
| 0x8100    | 802.1Q VLAN |
| 0x88CC    | LLDP        |
| 0x8847    | MPLS        |

Suppose

```
EtherType = 0x0800
```

NIC knows

Payload contains an IPv4 packet.

If

```
0x86DD
```

Pass payload to IPv6 stack.

---

## Why EtherType?

Without it,

Layer 2 wouldn't know which Layer 3 protocol to hand the payload to.

Think of it like a file extension.

```
photo.jpg

document.pdf

video.mp4
```

EtherType identifies the payload type.

---

# VLAN Tagged Frame

Normally

```
Dest MAC
Source MAC
EtherType
Payload
```

With VLAN

```
Dest MAC
Source MAC

802.1Q Tag

EtherType

Payload
```

The VLAN tag is inserted between Source MAC and EtherType.

---

# 802.1Q VLAN Tag

4 Bytes

```
+------+------+
|TPID  |  TCI |
|2 B   |2 B   |
+------+------+
```

---

## TPID

Tag Protocol Identifier

Usually

```
0x8100
```

Tells switch

"This frame contains VLAN information."

---

## TCI

Tag Control Information

Contains three fields.

### PCP

Priority Code Point

3 bits

Quality of Service

Values

0–7

Higher value

Higher priority.

Voice traffic often gets higher priority.

---

### DEI

Drop Eligible Indicator

1 bit

Congestion hint.

If network is overloaded,

frames with DEI=1 can be dropped first.

---

### VLAN ID

12 bits

Range

1–4094

0 reserved

4095 reserved

Examples

```
VLAN 10

VLAN 20

VLAN 100
```

Maximum

4094 VLANs.

---

# 6. Payload

Usually Layer 3 packet.

Can contain

* IPv4
* IPv6
* ARP
* MPLS
* Others

Minimum

46 Bytes

Maximum

1500 Bytes

---

## Why minimum 46 Bytes?

Ethernet minimum frame

```
64 Bytes
```

Subtract

```
Destination MAC = 6

Source MAC = 6

EtherType = 2

FCS = 4

Total = 18
```

```
64 − 18 = 46 Bytes
```

If payload smaller

Padding is added.

---

# Padding

Suppose ARP packet

Only 28 Bytes.

Need

46 Bytes.

Switch/NIC automatically adds

18 Bytes of padding.

Receiver ignores padding.

---

# Maximum Payload

1500 Bytes

This defines Ethernet MTU.

```
MTU = 1500
```

Larger IP packet?

Layer 3 fragments it (if allowed) or relies on Path MTU Discovery.

---

# Jumbo Frames

Payload around

9000 Bytes.

Used in

* SANs
* Data centers
* HPC clusters
* VMware
* Large database replication

Advantages

* Lower CPU overhead
* Fewer interrupts
* Better throughput

Disadvantage

All devices on the path must support jumbo frames.

---

# 7. Frame Check Sequence (FCS)

4 Bytes

Contains CRC-32.

Sender computes CRC over the frame (excluding the preamble/SFD and the FCS itself) and appends the result.

Receiver recomputes the CRC.

If

```
Calculated CRC ≠ Received CRC
```

Frame is discarded.

No retransmission happens at Layer 2 Ethernet itself. Recovery, if needed, is handled by higher-layer protocols such as TCP.

---

# Why CRC Instead of Checksum?

CRC is much better at detecting

* Burst errors
* Multiple bit flips
* Random corruption

Very high probability of detecting transmission errors.

---

# What Does the Switch Actually Read?

When a frame arrives, a switch primarily uses:

1. Destination MAC → Decide where to forward.
2. Source MAC → Learn and update the CAM table.
3. VLAN Tag (if present) → Determine the VLAN/broadcast domain.
4. EtherType → Usually not needed for basic forwarding, but may be examined for features like ACLs, QoS, or protocol-specific handling.

It generally does **not** inspect the Layer 3 payload for ordinary Layer 2 switching.

---

# Ethernet II vs IEEE 802.3

This is a classic interview question.

## Ethernet II

```
Destination MAC

Source MAC

EtherType
```

Modern networks.

Used almost everywhere.

---

## IEEE 802.3

```
Destination MAC

Source MAC

Length

LLC

Payload
```

Instead of EtherType,

it contains

Length.

LLC determines protocol.

Today,

Ethernet II dominates.

---

# Interview Facts to Remember

* Destination MAC is used for forwarding.
* Source MAC is used for learning.
* Broadcast MAC = `FF:FF:FF:FF:FF:FF`.
* EtherType identifies the encapsulated Layer 3 protocol.
* The 802.1Q VLAN tag is inserted between the Source MAC and EtherType.
* Minimum Ethernet payload = **46 Bytes**.
* Standard Ethernet MTU = **1500 Bytes**.
* Minimum Ethernet frame = **64 Bytes**.
* Maximum standard Ethernet frame = **1518 Bytes** (or **1522 Bytes** with a VLAN tag).
* FCS uses **CRC-32** for error detection, not correction.
* Preamble and SFD are handled by the physical interface and are generally not considered part of the frame for switching decisions.
* Modern LANs use **Ethernet II**, while IEEE 802.3 with LLC is mostly of historical interest in enterprise Ethernet.

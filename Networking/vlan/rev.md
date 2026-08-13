<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/10d5a4b5-9d22-457c-b6cc-7b345e14a813" />


# VLAN Technical Revision Notes

## 1. VLAN Fundamentals

**VLAN: Virtual Local Area Network**

A VLAN is a **Layer 2 logical segmentation mechanism** that divides a physical switched network into multiple independent **broadcast domains**.

### Core properties

* VLAN operates primarily at **Layer 2**.
* Each VLAN represents a separate **Layer 2 broadcast domain**.
* Broadcast, unknown-unicast, and multicast flooding is normally constrained to the VLAN.
* VLANs allow logical segmentation without requiring separate physical switches.
* Communication between different VLANs requires **Layer 3 routing**.
* VLAN membership is maintained by the switch.

### Important distinction

```text
VLAN
  → Layer 2 segmentation

IP subnet
  → Layer 3 addressing

Routing
  → Communication between different IP networks/VLANs
```

A common enterprise mapping is:

```text
VLAN 10 → 192.168.10.0/24
VLAN 20 → 192.168.20.0/24
VLAN 30 → 192.168.30.0/24
```

However:

**VLAN ≠ IP subnet**

They are different concepts that are commonly mapped one-to-one.

---

# 2. VLAN Membership

A switch associates incoming traffic with a VLAN based on the interface and VLAN configuration.

Typical access-port model:

```text
Port 1 → VLAN 10
Port 2 → VLAN 10
Port 3 → VLAN 20
Port 4 → VLAN 30
```

Frames arriving through Port 1 are classified into VLAN 10.

The end host normally does not need to know that the switch has assigned its traffic to VLAN 10.

---

# 3. Access Port

An **access port** carries traffic for a single VLAN.

Typical use:

* PCs
* Printers
* Servers
* Cameras
* Other end devices

Conceptually:

```text
Host
  |
Untagged Ethernet
  |
Access Port
  |
VLAN 10
```

### Ingress

```text
Untagged frame
      ↓
Access port
      ↓
Classified into configured access VLAN
```

### Egress

```text
VLAN frame
      ↓
Access port
      ↓
VLAN tag normally removed
      ↓
Untagged frame
      ↓
Host
```

An ordinary end host connected to an access port therefore normally sends and receives **untagged Ethernet frames**.

---

# 4. Trunk Port

A **trunk port** carries traffic belonging to multiple VLANs over a single physical link.

Typical use:

* Switch-to-switch links
* Switch-to-router links
* Switch-to-Layer 3 switch links
* Other infrastructure links

Example:

```text
Switch A ================= Switch B
            Trunk
         VLAN 10,20,30
```

A trunk normally uses **IEEE 802.1Q tagging** to identify VLAN membership.

```text
VLAN 10 frame → VLAN ID 10
VLAN 20 frame → VLAN ID 20
VLAN 30 frame → VLAN ID 30
```

---

# 5. Access vs Trunk

| Property            | Access Port           | Trunk Port             |
| ------------------- | --------------------- | ---------------------- |
| Typical VLANs       | One                   | Multiple               |
| Typical device      | End host              | Network infrastructure |
| Host-facing traffic | Usually untagged      | Usually tagged         |
| VLAN identification | Port configuration    | 802.1Q tag             |
| Typical purpose     | Connect endpoint      | Transport VLANs        |
| Native VLAN concept | Not normally relevant | Relevant               |

---

# 6. IEEE 802.1Q

**802.1Q** is the IEEE standard used for VLAN tagging.

The VLAN tag is inserted into the Ethernet frame between the Source MAC address and the original EtherType/Length field.

Conceptually:

```text
┌──────────┬──────────┬────────────┬──────────┬─────────┐
│ Dest MAC │ Src MAC  │ 802.1Q Tag │ EtherType│ Payload │
└──────────┴──────────┴────────────┴──────────┴─────────┘
```

The 802.1Q tag is **4 bytes**.

### 802.1Q tag structure

```text
16 bits          16 bits
┌───────────────┬──────────────────────────────┐
│ TPID          │ TCI                          │
│               │ PCP | DEI | VLAN ID          │
└───────────────┴──────────────────────────────┘
```

### TPID

**Tag Protocol Identifier**

Typically:

```text
0x8100
```

It identifies the frame as carrying an IEEE 802.1Q VLAN tag.

### TCI

**Tag Control Information**

Contains:

* PCP
* DEI
* VLAN ID

### PCP

**Priority Code Point**

* 3 bits
* Values: 0 to 7
* Used for Layer 2 traffic prioritization / QoS marking.

### DEI

**Drop Eligible Indicator**

* 1 bit
* Indicates whether the frame may be considered eligible for dropping during congestion.

### VLAN ID

* 12 bits
* Theoretical values: 0 to 4095
* Conventional usable VLAN IDs: **1 to 4094**
* VLAN 0 and VLAN 4095 have special/reserved purposes.

Therefore:

```text
2^12 = 4096 possible values
```

but not all are ordinary assignable VLAN IDs.

---

# 7. Frame Journey Across a Trunk

Typical path:

```text
Host
  ↓
Untagged frame
  ↓
Access port
  ↓
VLAN classification
  ↓
Switch forwarding
  ↓
802.1Q tagging
  ↓
Trunk
  ↓
802.1Q tag inspected
  ↓
VLAN identified
  ↓
Switch forwarding
  ↓
Access port
  ↓
Tag removed
  ↓
Untagged frame
  ↓
Host
```

Example:

```text
PC-A
VLAN 10
   |
   | untagged
   ↓
Switch A
   |
   | [802.1Q VLAN 10]
   ↓
Trunk
   |
   ↓
Switch B
   |
   | untagged
   ↓
PC-B
VLAN 10
```

The VLAN identity is preserved while crossing the trunk.

---

# 8. Native VLAN

A trunk has a **native VLAN**.

By default, traffic belonging to the native VLAN is transmitted **untagged** on an 802.1Q trunk.

Example:

```text
Native VLAN = 99

VLAN 10 → tagged
VLAN 20 → tagged
VLAN 30 → tagged
VLAN 99 → untagged
```

Therefore:

**Not every frame crossing an 802.1Q trunk is necessarily tagged.**

The native VLAN is the principal exception.

### Native VLAN mismatch

Example:

```text
Switch A native VLAN = 99
Switch B native VLAN = 10
```

An untagged frame sent across the trunk may be interpreted as belonging to different VLANs on the two sides.

Possible consequences:

* Connectivity problems
* Unexpected traffic leakage
* Security vulnerabilities
* STP inconsistencies depending on platform/protocol

Native VLAN configuration should therefore be deliberate and consistent.

---

# 9. VLAN-Aware MAC Learning

A switch does not conceptually maintain only:

```text
MAC → Port
```

It maintains forwarding information within a VLAN context:

```text
VLAN + MAC → Port
```

Example:

```text
VLAN 10
AA:AA:AA:AA:AA:AA → Port 1
BB:BB:BB:BB:BB:BB → Port 2

VLAN 20
AA:AA:AA:AA:AA:AA → Port 7
CC:CC:CC:CC:CC:CC → Port 8
```

The same MAC address can therefore exist in different VLAN contexts.

### Learning process

When a frame arrives:

```text
Source MAC
    ↓
Switch learns source MAC
    ↓
Associates MAC with VLAN + ingress port
```

Then the destination MAC is looked up within the relevant VLAN.

---

# 10. VLAN Forwarding

For a known unicast:

```text
Destination MAC known
       ↓
Lookup within VLAN
       ↓
Forward toward destination port
```

For an unknown unicast:

```text
Destination MAC unknown
       ↓
Flood within VLAN
```

For a broadcast:

```text
Destination MAC =
FF:FF:FF:FF:FF:FF
       ↓
Flood within VLAN
```

The flooding domain is constrained by VLAN membership.

---

# 11. Broadcast Domain

A VLAN creates a separate broadcast domain.

Example:

```text
VLAN 10
 ├── PC1
 ├── PC2
 └── PC3

VLAN 20
 ├── PC4
 └── PC5
```

A broadcast originating in VLAN 10 is not normally flooded into VLAN 20.

Therefore:

```text
VLAN 10 broadcast domain
        ≠
VLAN 20 broadcast domain
```

This is one of the most important VLAN interview facts.

---

# 12. VLANs Across Multiple Switches

Suppose:

```text
Switch A                     Switch B

VLAN 10 ─────────────────── VLAN 10
VLAN 20 ─────────────────── VLAN 20
VLAN 30 ─────────────────── VLAN 30
```

The inter-switch link is a trunk.

The trunk allows multiple VLANs to share one physical link.

```text
                Trunk
       ┌─────────────────────┐
       │ VLAN 10             │
       │ VLAN 20             │
       │ VLAN 30             │
       └─────────────────────┘
```

A VLAN therefore does not have to be confined to a single physical switch.

---

# 13. Allowed VLANs

A trunk can restrict which VLANs are permitted across it.

Example:

```text
Allowed VLANs:
10,20,30
```

Then:

```text
VLAN 10 → allowed
VLAN 20 → allowed
VLAN 30 → allowed
VLAN 40 → not allowed
VLAN 50 → not allowed
```

Benefits:

* Limits unnecessary traffic
* Reduces broadcast propagation
* Reduces VLAN exposure
* Improves segmentation
* Helps reduce attack surface

Best practice:

**Do not blindly allow every VLAN across every trunk.**

---

# 14. Inter-VLAN Communication

A Layer 2 switch does not route between VLANs.

Example:

```text
VLAN 10
192.168.10.0/24

        X

VLAN 20
192.168.20.0/24
```

Communication between them requires a Layer 3 device.

```text
VLAN 10
   |
   ↓
Layer 3 device
   |
   ↓
VLAN 20
```

This is called:

**Inter-VLAN routing**

---

# 15. Why Different VLANs Usually Use Different Subnets

Typical design:

```text
VLAN 10 → 192.168.10.0/24
VLAN 20 → 192.168.20.0/24
VLAN 30 → 192.168.30.0/24
```

Each subnet has its own default gateway:

```text
VLAN 10 → 192.168.10.1
VLAN 20 → 192.168.20.1
VLAN 30 → 192.168.30.1
```

This creates a clean mapping:

```text
VLAN
 ↓
Layer 2 broadcast domain
 ↓
IP subnet
 ↓
Default gateway
```

This is common enterprise architecture, not a fundamental requirement that VLAN ID and subnet number must numerically correspond.

---

# 16. Router-on-a-Stick

Router-on-a-Stick provides inter-VLAN routing using:

* One physical router interface
* Multiple router subinterfaces
* One trunk between router and switch

Architecture:

```text
                 Router
              ┌──────────┐
              │ G0/0     │
              │          │
              │ G0/0.10  │ VLAN 10
              │ G0/0.20  │ VLAN 20
              │ G0/0.30  │ VLAN 30
              └────┬─────┘
                   │
                 Trunk
                   │
                Switch
```

Example:

```text
G0/0.10 → 192.168.10.1
G0/0.20 → 192.168.20.1
G0/0.30 → 192.168.30.1
```

Each subinterface corresponds to a VLAN.

---

# 17. Layer 3 Switch and SVI

A Layer 3 switch can perform inter-VLAN routing internally.

**SVI = Switch Virtual Interface**

Example:

```text
interface VLAN 10
IP: 192.168.10.1

interface VLAN 20
IP: 192.168.20.1

interface VLAN 30
IP: 192.168.30.1
```

These SVIs act as default gateways.

```text
PC
192.168.10.20
     |
     ↓
Default Gateway
192.168.10.1
     |
     ↓
SVI VLAN 10
     |
     ↓
Layer 3 routing
     |
     ↓
SVI VLAN 20
192.168.20.1
     |
     ↓
Destination
```

### Router-on-a-Stick vs L3 Switch

| Feature                | Router-on-a-Stick                    | L3 Switch            |
| ---------------------- | ------------------------------------ | -------------------- |
| Routing device         | Router                               | Layer 3 switch       |
| Physical link          | Usually one trunk                    | Can route internally |
| VLAN interface         | Router subinterface                  | SVI                  |
| Inter-VLAN performance | Limited by router/trunk architecture | Generally higher     |
| Common enterprise use  | Smaller/simple environments          | Enterprise networks  |

---

# 18. Default Gateway Relationship

For a host in VLAN 10:

```text
Host:
192.168.10.50/24

Gateway:
192.168.10.1
```

The gateway belongs to the Layer 3 interface associated with VLAN 10.

For example:

```text
VLAN 10
    |
    └── SVI 192.168.10.1
```

When the destination is outside the local subnet:

```text
Host
 ↓
Default Gateway
 ↓
Router/L3 Switch
 ↓
Routing
```

---

# 19. VLAN and ARP

ARP is a broadcast-based Layer 2 mechanism in IPv4.

Example:

```text
Host A
192.168.10.10

ARP:
Who has 192.168.10.20?
```

The ARP broadcast is flooded within the relevant VLAN.

It does not normally cross directly into another VLAN.

For inter-VLAN communication:

```text
VLAN 10
    ↓
Default gateway
    ↓
Routing
    ↓
VLAN 20
```

The Layer 3 device maintains separate Layer 2 contexts on its VLAN interfaces.

---

# 20. VLAN and STP

VLANs create separate Layer 2 broadcast domains.

STP prevents Layer 2 switching loops.

Depending on the STP implementation, spanning-tree instances may exist per VLAN or multiple VLANs may be mapped to a shared STP instance.

Examples:

* PVST+
* Rapid PVST+
* MST

### Important relationship

```text
VLAN
 ↓
Layer 2 topology
 ↓
STP prevents loops
```

Different VLANs can potentially have different STP forwarding behavior depending on the STP architecture.

This can be used for load distribution in some designs.

---

# 21. Voice VLAN

A switch port can support separate data and voice VLANs.

Example:

```text
Port
 ├── Data VLAN 10
 └── Voice VLAN 20
```

Typical architecture:

```text
          IP Phone
             |
             |
          Switch
             |
          Data VLAN 10
          Voice VLAN 20
```

Purpose:

* Separate voice and data traffic
* Apply QoS policies
* Improve segmentation
* Simplify voice network management

---

# 22. VLAN Hopping

**VLAN hopping** refers to techniques intended to bypass normal VLAN segmentation and gain access to traffic in another VLAN.

Two classical techniques:

### Switch spoofing

Attacker attempts to make an access interface behave as a trunk.

Potential result:

```text
Attacker
   ↓
Trunk
   ↓
Multiple VLANs
```

### Double tagging

Frame contains two VLAN tags:

```text
┌─────────────┬─────────────┬─────────┐
│ Outer Tag   │ Inner Tag   │ Payload │
└─────────────┴─────────────┴─────────┘
```

Under specific conditions involving native VLAN behavior, the outer tag can be removed while the inner tag remains.

Potentially:

```text
Attacker
   ↓
Double-tagged frame
   ↓
First switch removes outer tag
   ↓
Inner VLAN tag remains
   ↓
Frame may be interpreted as another VLAN
```

---

# 23. VLAN Security Mitigations

Common controls:

### Access ports

Explicitly configure user-facing ports as access ports rather than relying on dynamic negotiation.

### Disable unnecessary trunk negotiation

Prevent unauthorized endpoints from negotiating trunk status.

### Restrict allowed VLANs

```text
Allowed:
10,20

Not allowed:
30,40,50
```

### Native VLAN

Use a dedicated, unused VLAN as the native VLAN where appropriate.

Example:

```text
Native VLAN = 999
```

and do not assign normal user devices to VLAN 999.

### Native VLAN consistency

Ensure both ends of a trunk agree on the native VLAN.

### Additional controls

* Port security
* DHCP snooping
* Dynamic ARP Inspection
* IP Source Guard
* BPDU Guard
* Storm control

These are complementary Layer 2 security mechanisms, not VLAN mechanisms themselves.

---

# 24. VLAN Is Not a Security Boundary by Itself

A VLAN provides Layer 2 segmentation, but it should not automatically be treated as a complete security boundary.

For example:

```text
VLAN 10 → Users
VLAN 20 → Servers
```

Routing between VLANs may still be permitted.

A firewall or ACL can enforce policy:

```text
Users → Servers
       ↓
Allow HTTPS
Allow DNS
Deny everything else
```

Therefore:

```text
VLAN
= segmentation

ACL / Firewall
= traffic policy enforcement
```

---

# 25. VLAN Creation vs VLAN Assignment

Two different operations:

### Create VLAN

The VLAN must exist in the switch's VLAN database/configuration.

Example:

```text
VLAN 10
Name: SALES
```

### Assign port to VLAN

```text
Port 1
Mode: access
Access VLAN: 10
```

Creating VLAN 10 does not automatically make every switch port part of VLAN 10.

---

# 26. Trunk VLAN Propagation

For VLAN 10 to work across multiple switches:

```text
Switch A
VLAN 10
   |
   | trunk allows VLAN 10
   |
Switch B
VLAN 10
```

Multiple things must align:

```text
VLAN exists
     +
Port membership correct
     +
Trunk operational
     +
VLAN permitted on trunk
     +
Native VLAN consistent where relevant
     +
STP permits forwarding
```

A VLAN can therefore exist locally while still failing to propagate across the network.

---

# 27. Common VLAN Failure Scenarios

## Case 1: Same VLAN, same switch, cannot communicate

Check:

```text
1. Link status
2. Access VLAN
3. Port configuration
4. Host IP/subnet
5. MAC learning
6. Port security
7. STP state
```

## Case 2: Same VLAN, different switches, cannot communicate

Additionally check:

```text
1. Trunk status
2. VLAN existence on both switches
3. Allowed VLAN list
4. Native VLAN configuration
5. STP
6. MAC learning
7. Physical link
```

## Case 3: Different VLANs cannot communicate

Check:

```text
1. VLAN existence
2. IP addressing
3. Default gateway
4. SVI/subinterface status
5. IP routing enabled
6. ACL/firewall policy
7. Routing table
```

## Case 4: One VLAN works across trunk, another does not

Immediately inspect:

```text
Allowed VLAN list
```

Example:

```text
Allowed:
10,20

VLAN 30:
Not permitted
```

---

# 28. Important VLAN Terminology

| Term               | Meaning                                                 |
| ------------------ | ------------------------------------------------------- |
| VLAN               | Logical Layer 2 broadcast domain                        |
| Access Port        | Port associated with one VLAN                           |
| Trunk Port         | Port carrying multiple VLANs                            |
| 802.1Q             | IEEE VLAN tagging standard                              |
| VLAN ID            | 12-bit VLAN identifier                                  |
| Native VLAN        | VLAN transmitted untagged on an 802.1Q trunk by default |
| Allowed VLANs      | VLANs permitted over a trunk                            |
| SVI                | Switch Virtual Interface                                |
| Inter-VLAN Routing | Layer 3 communication between VLANs                     |
| Router-on-a-Stick  | Router subinterfaces connected through a trunk          |
| Voice VLAN         | VLAN designated for voice traffic                       |
| VLAN Hopping       | Attempt to bypass VLAN segmentation                     |
| Broadcast Domain   | Set of devices receiving a Layer 2 broadcast            |
| MAC Table          | Layer 2 forwarding database                             |
| STP                | Prevents Layer 2 switching loops                        |

---

# 29. Core Interview Facts

Memorize these relationships:

```text
VLAN
→ Layer 2
→ Broadcast domain
→ MAC switching context
→ Flooding boundary
```

```text
Access Port
→ One VLAN
→ Usually untagged toward host
```

```text
Trunk
→ Multiple VLANs
→ 802.1Q tagging
```

```text
Native VLAN
→ Untagged on 802.1Q trunk by default
```

```text
802.1Q
→ 4-byte tag
→ TPID + TCI
→ PCP + DEI + VLAN ID
→ VLAN ID = 12 bits
```

```text
Different VLANs
→ Different Layer 2 broadcast domains
→ Require Layer 3 routing for communication
```

```text
Inter-VLAN Routing
→ Router-on-a-Stick
OR
→ Layer 3 switch + SVI
```

```text
VLAN propagation
→ Trunk
→ VLAN permitted
→ VLAN exists
→ STP forwarding
```

```text
VLAN security
→ Access-port hardening
→ Restrict trunks
→ Native VLAN management
→ Prevent trunk negotiation
→ VLAN hopping mitigation
```

---

# 30. The Most Important Frame-Level Model

Keep this model in your head:

```text
              ACCESS                TRUNK                 ACCESS

Host ───────> Switch A ═══════════> Switch B ───────────> Host
              │                       │
              │                       │
              │                       │
         VLAN classification     802.1Q tag
              │                       │
              │                       │
         Untagged ingress        VLAN identity
                                      │
                                      ↓
                               Tag interpreted
                                      │
                                      ↓
                               Untagged egress
```

And for routing:

```text
VLAN 10
   |
   | Layer 2
   ↓
Gateway / SVI
   |
   | Layer 3 routing
   ↓
Gateway / SVI
   |
   | Layer 2
   ↓
VLAN 20
```

The single most useful mental equation is:

```text
VLAN = Layer 2 segmentation
Trunk = VLAN transport
802.1Q = VLAN identification
SVI/Router = VLAN boundary crossing
STP = Layer 2 loop prevention
```


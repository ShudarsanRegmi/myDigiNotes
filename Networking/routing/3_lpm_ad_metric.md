
<img width="1181" height="1332" alt="image" src="https://github.com/user-attachments/assets/c85219ce-1a9a-4695-93ae-38c3fbd097b5" />


Your refined question: **"Let's move to Topic 2: route selection, especially how LPM, Administrative Distance, and metrics interact when multiple routes exist."**

# 2. Route Selection: LPM → Preference → Metric

We already know the first question a router asks:

> **Which routes match the destination?**

Now we need to answer:

> **If multiple routes exist, which one actually gets installed and used?**

This is where **LPM, Administrative Distance, and metrics** come into play.

---

## 1. First: Longest Prefix Match

Suppose the router has:

```text
10.0.0.0/8       → R1
10.20.0.0/16     → R2
10.20.5.0/24     → R3
```

Destination:

```text
10.20.5.100
```

All three match.

The `/24` is the most specific:

```text
/24 > /16 > /8
```

So:

```text
10.20.5.0/24 → R3
```

wins.

**LPM is about prefix specificity.**

---

# 2. What if Two Routes Have the Same Prefix?

Now consider:

```text
10.20.5.0/24 → OSPF
10.20.5.0/24 → BGP
```

Both routes describe exactly the same destination.

LPM cannot distinguish them because both are `/24`.

Now the router needs to determine:

> **Which routing source should I trust/prefer?**

This is where **Administrative Distance (AD)** comes in, particularly in systems that use AD as the cross-protocol preference mechanism.

---

# 3. Administrative Distance

Administrative Distance represents how much a router **prefers one source of routing information over another**.

For example, conceptually:

```text
Static route
OSPF
RIP
BGP
```

may all provide information about the same destination.

AD allows the router to say:

> "I prefer information learned from source A over source B."

### Important:

**Lower AD = more preferred.**

A commonly memorized Cisco-style set is:

| Route source |  AD |
| ------------ | --: |
| Connected    |   0 |
| Static       |   1 |
| eBGP         |  20 |
| EIGRP        |  90 |
| OSPF         | 110 |
| RIP          | 120 |
| iBGP         | 200 |

These values are **vendor/platform conventions**, not a universal property of routing protocols.

For interview purposes, know the concept and the common Cisco values if the role expects them.

---

# 4. AD Is NOT the Same as Metric

This distinction is important.

### Administrative Distance

Answers:

> **"Which routing source do I prefer?"**

For example:

```text
OSPF vs RIP
```

### Metric

Answers:

> **"According to this routing protocol, which path is better?"**

For example, OSPF might compare:

```text
Path A → cost 10
Path B → cost 30
```

OSPF prefers:

```text
cost 10
```

So:

```text
AD     → preference between route sources
Metric → preference between paths within a routing protocol
```

---

# 5. Think of It as Two Different Questions

Imagine:

```text
10.20.5.0/24
```

is reachable through:

```text
OSPF:
    Path A → cost 20
    Path B → cost 50

RIP:
    Path C → 2 hops
```

There are two levels of decision-making.

### Level 1

Which routing source should provide the route?

```text
OSPF vs RIP
```

AD helps here.

### Level 2

Once OSPF is being considered:

```text
OSPF Path A → cost 20
OSPF Path B → cost 50
```

OSPF's metric chooses Path A.

So:

```text
Route source
     ↓
Administrative Distance
     ↓
Protocol's best route
     ↓
Metric
```

The exact implementation can vary by platform and protocol, so this is best treated as a **conceptual model**, not a universal literal sequence for every routing stack.

---

# 6. A More Accurate Mental Model

Keep these three concepts separate:

```text
              DESTINATION
                   |
                   ↓
       Which prefixes match?
                   |
                   ↓
        LONGEST PREFIX MATCH
                   |
          Most specific prefix
                   |
                   ↓
      Multiple sources for it?
             /          \
           No            Yes
           |              |
           |             AD /
           |          route preference
           |              |
           |              ↓
           |       Preferred source
           |              |
           +------+-------+
                  |
                  ↓
        Protocol-specific selection
                  |
               Metric etc.
                  |
                  ↓
             Best route
                  |
                  ↓
                 FIB
                  |
                  ↓
             Forward packet
```

Don't get too attached to the exact ordering of the final stages. The crucial hierarchy is:

**prefix specificity is fundamentally different from route-source preference and protocol metrics.**

---

# 7. A Classic Interview Trap

Suppose:

```text
Route A: 10.0.0.0/8       OSPF
Route B: 10.1.0.0/16     RIP
```

Which one wins for:

```text
10.1.2.5
```

A common wrong answer is:

> "OSPF, because OSPF has a lower AD than RIP."

**Wrong.**

First notice:

```text
10.0.0.0/8
10.1.0.0/16
```

Both match, but `/16` is more specific.

Therefore:

```text
10.1.0.0/16
```

wins because of **LPM**.

The fact that the `/16` came from RIP does not make the broader OSPF `/8` preferable.

This is an excellent interview question.

---

# 8. Another Important Scenario

Suppose:

```text
Route A:
10.1.0.0/16 → OSPF

Route B:
10.1.0.0/16 → Static
```

Same prefix.

Now LPM cannot distinguish them.

So route-source preference becomes relevant.

Conceptually:

```text
Same prefix
    ↓
Which source is preferred?
    ↓
Static
```

On Cisco-style systems, static has AD 1 while OSPF has AD 110.

Therefore the static route is preferred.

---

# 9. Floating Static Route

This gives us a useful practical application of AD.

Suppose:

```text
Primary:
10.1.0.0/16 → OSPF

Backup:
10.1.0.0/16 → Static
```

Normally, static would win because of its lower AD.

But an administrator can deliberately configure the static route with a **higher AD** than OSPF.

For example:

```text
OSPF static preference → AD 110
Backup static route    → AD 200
```

Now:

```text
Normal condition:
OSPF route available → use OSPF

OSPF route disappears:
                    ↓
             backup static route
                    ↓
                  used
```

This is called a **floating static route**.

The static route "floats" until the preferred route disappears.

You don't need to go much deeper than this for now.

---

# 10. Metrics Are Protocol-Specific

Don't think there is one universal routing metric.

Different protocols measure "better" differently.

| Protocol | Typical metric concept   |
| -------- | ------------------------ |
| RIP      | Hop count                |
| OSPF     | Cost                     |
| EIGRP    | Composite metric         |
| BGP      | Path attributes / policy |

For example:

```text
RIP:
2 hops < 5 hops

OSPF:
cost 10 < cost 30
```

So you should ask:

> **"Metric according to which routing protocol?"**

This is a good interview habit.

---

# 11. One More Important Distinction: Control Plane vs Forwarding

Everything we've discussed so far is primarily about **choosing the route**.

Once the best route is determined, forwarding takes over.

Conceptually:

```text
Routing information
       ↓
Route selection
       ↓
Best route
       ↓
FIB
       ↓
Packet arrives
       ↓
Destination lookup / LPM
       ↓
Next hop + interface
       ↓
Forward
```

This distinction becomes important when we later discuss **RIB vs FIB** and network-device architecture.

---

# Interview-Level Summary

If the interviewer asks:

### "How does a router choose between multiple routes?"

A strong concise answer would be:

> **The router first considers the destination prefix and uses longest prefix match to prefer the most specific matching route. If multiple routes exist for the same prefix, route-source preference such as Administrative Distance can determine which source is preferred. Within a routing protocol, the protocol's own metric and selection rules determine the best path. The resulting route is then installed into the forwarding information used by the data plane.**

### The three concepts to keep crystal clear:

```text
LPM
"What destination prefix is most specific?"

AD / Route Preference
"Which source of routing information do I trust/prefer?"

Metric
"Which path does this routing protocol consider better?"
```

That's enough for this topic. **Don't spend more time memorizing route-selection edge cases yet.** The high-value concepts are LPM, AD vs metric, and the distinction between inter-protocol and intra-protocol decisions.

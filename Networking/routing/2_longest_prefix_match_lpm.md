Your refined question: **"Let's start with Topic 1: Longest Prefix Match and routing-table lookup. Teach it at an interview-focused depth, with enough examples to make the lookup process intuitive."**

# 1. LPM + Routing-Table Lookup

This is one of those topics that looks trivial initially, but interviewers can use it to test whether you actually understand how a router forwards packets.

The core question is:

> **A packet arrives at a router. How does the router decide where to send it?**

---

## 1. Start with the routing table

Suppose a router has:

| Destination prefix | Next hop           | Interface |
| ------------------ | ------------------ | --------- |
| `192.168.1.0/24`   | Directly connected | eth0      |
| `10.0.0.0/8`       | `192.168.1.2`      | eth0      |
| `10.20.0.0/16`     | `192.168.1.3`      | eth1      |
| `0.0.0.0/0`        | `192.168.1.1`      | eth2      |

Now a packet arrives:

```text
Destination IP = 10.20.5.10
```

The router asks:

> "Which routing-table entries match this destination?"

Let's check.

### Route 1

```text
10.0.0.0/8
```

Matches `10.20.5.10`.

### Route 2

```text
10.20.0.0/16
```

Also matches.

### Default route

```text
0.0.0.0/0
```

Also matches, because `/0` essentially means "any IPv4 address."

So we have:

```text
10.0.0.0/8
10.20.0.0/16
0.0.0.0/0
```

Which one should the router use?

**The most specific one.**

That is LPM.

---

# 2. What Does "Longest Prefix" Actually Mean?

Take these prefixes:

```text
10.0.0.0/8
10.20.0.0/16
10.20.5.0/24
```

The `/` number tells us how many **leading bits identify the network/prefix**.

Therefore:

```text
/8   → 8 bits of prefix
/16  → 16 bits of prefix
/24  → 24 bits of prefix
```

A larger prefix length means a **more specific route**.

So:

```text
/24 > /16 > /8 > /0
```

in terms of specificity.

Therefore:

> **Longest Prefix Match means: among all routes that match the destination IP, choose the route with the largest prefix length.**

---

# 3. Concrete Example

Routing table:

```text
10.0.0.0/8
10.20.0.0/16
10.20.5.0/24
0.0.0.0/0
```

Destination:

```text
10.20.5.100
```

Matches:

```text
10.0.0.0/8        ✓
10.20.0.0/16      ✓
10.20.5.0/24      ✓
0.0.0.0/0         ✓
```

The most specific matching prefix is:

```text
10.20.5.0/24
```

Therefore:

```text
10.20.5.0/24 → chosen
```

The router does **not** choose the first matching route.

It chooses the **longest matching prefix**.

---

# 4. Why Is LPM Necessary?

Imagine you have a broad route:

```text
10.0.0.0/8 → ISP-A
```

This says:

> "For anything in 10.0.0.0/8, send it toward ISP-A."

But later you add:

```text
10.20.5.0/24 → Router-B
```

Now you are effectively saying:

> "Generally, send 10.x.x.x toward ISP-A, **except this particular subnet**, which should go toward Router-B."

LPM allows the more specific route to override the broader route.

This is extremely useful for:

* hierarchical routing
* subnetting
* route aggregation
* exceptions to broad routes
* Internet routing

---

# 5. LPM Is About Prefix Matching, Not "Numerically Largest IP"

This is a common misunderstanding.

Suppose:

```text
10.0.0.0/8
10.20.0.0/16
```

You don't compare the numerical values of the network addresses.

You ask:

> **Which prefix shares the longest matching sequence of bits with the destination?**

The `/16` route is more specific because it identifies 16 bits of the destination rather than only 8.

---

# 6. What About the Default Route?

The default route:

```text
0.0.0.0/0
```

has a prefix length of **zero**.

So it is the least specific possible IPv4 route.

Suppose:

```text
Routing table:

192.168.1.0/24 → R1
10.0.0.0/8     → R2
0.0.0.0/0      → ISP
```

Destination:

```text
8.8.8.8
```

Neither `/24` nor `/8` matches.

But:

```text
0.0.0.0/0
```

matches.

Therefore:

```text
8.8.8.8 → ISP
```

This is why the default route is called the **route of last resort**.

---

# 7. The Actual Lookup Flow

For interview purposes, remember this sequence:

```text
Packet arrives
      ↓
Read destination IP
      ↓
Search routing/forwarding entries
      ↓
Find all matching prefixes
      ↓
Choose longest prefix match
      ↓
Determine next hop / output interface
      ↓
Forward packet
```

For example:

```text
Destination = 10.20.5.100

       ↓

10.0.0.0/8       matches
10.20.0.0/16     matches
10.20.5.0/24     matches
0.0.0.0/0        matches

       ↓

Longest prefix = /24

       ↓

Use 10.20.5.0/24 route

       ↓

Forward toward its next hop
```

---

# 8. One Important Distinction: LPM vs Best Route

This is where interviews can get slightly tricky.

Suppose you have:

```text
10.0.0.0/8
```

learned through OSPF, and another:

```text
10.0.0.0/8
```

learned through BGP.

They have the **same prefix length**.

LPM alone cannot distinguish them because both are `/8`.

Now other route-selection mechanisms become relevant, such as:

* Administrative Distance / route preference
* Metric
* Protocol-specific selection rules

So don't say:

> "The router always chooses the route with the lowest metric."

That's incomplete.

The router first has to deal with **prefix specificity**.

A useful conceptual distinction is:

```text
Different prefix lengths
        ↓
LPM determines specificity

Same destination prefix
        ↓
Route preference / metric / protocol rules
```

We'll study those route-selection mechanisms separately.

---

# 9. LPM and Route Aggregation

LPM also explains why **route summarization** works.

Imagine a router has:

```text
192.168.0.0/24
192.168.1.0/24
192.168.2.0/24
192.168.3.0/24
```

These can potentially be summarized as:

```text
192.168.0.0/22
```

Instead of advertising four separate routes, a router can advertise one broader route.

But if a more specific route exists:

```text
192.168.2.0/24
```

LPM allows that specific route to take precedence over the summary.

So:

> **Aggregation provides broad reachability; LPM allows specific routes to override it.**

This is a very useful networking intuition.

---

# 10. Interview Questions You Should Be Able to Answer

### Q1. What is Longest Prefix Match?

> LPM is the process of selecting the most specific routing-table entry that matches a packet's destination IP. The route with the largest prefix length is selected.

### Q2. Why does `/24` beat `/16`?

> Because `/24` specifies 24 bits of the network prefix, making it more specific than a `/16` prefix.

### Q3. Does the first matching route get selected?

> No. The router considers matching prefixes and selects the longest, most specific prefix.

### Q4. Why does `0.0.0.0/0` act as a default route?

> Because it matches every IPv4 destination but has zero prefix bits, making it the least specific route. It is therefore used when no more specific route exists.

### Q5. What happens if two routes have the same prefix length?

> LPM cannot distinguish them. The router then uses its route-preference and metric mechanisms, along with protocol-specific rules, to select the preferred route.

---

# The Mental Model to Keep

Don't memorize LPM as merely:

> "Biggest `/number` wins."

Think of it as:

```text
                  DESTINATION IP
                        |
               Which prefixes match?
                        |
             +----------+----------+
             |          |          |
            /8         /16        /24
             |          |          |
             +----------+----------+
                        |
                  Most specific
                        |
                       /24
                        |
                   Next hop
                        |
                    Forward
```

**Core rule:**

> **Among all matching routes, the most specific prefix wins.**

That is the heart of LPM.

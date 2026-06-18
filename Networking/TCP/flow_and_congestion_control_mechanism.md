## TCP Flow and congetion control mechanism

Perfect. Since you already have the intuition, let's make this a **revision-note style** focused on technical details and interview recall.

# TCP Flow Control

## Purpose

Prevent receiver buffer overflow.

Question being solved:

```text
Can the receiver handle more data?
```

---

## Mechanism

TCP uses:

```text
Receive Window (rwnd)
```

advertised in the TCP header's Window Size field.

Receiver tells sender:

```text
I can currently accept N more bytes.
```

---

## Key Components

### Receive Buffer

Located at receiver.

Stores incoming bytes before application consumes them.

```text
Network -> TCP Receive Buffer -> Application
```

---

### Advertised Window (rwnd)

Represents:

```text
Available Receive Buffer Space
```

Receiver computes:

```text
rwnd = ReceiveBufferSize - OccupiedBytes
```

---

## Sliding Window

Sender may transmit up to rwnd bytes without waiting.

Example:

```text
rwnd = 5000 bytes
```

Sender can have:

```text
≤ 5000 unacknowledged bytes in flight
```

---

## Dynamic Window

As application consumes data:

```text
Buffer frees
rwnd increases
```

As packets arrive:

```text
Buffer fills
rwnd decreases
```

---

## Zero Window

Receiver buffer completely full.

Advertises:

```text
Window = 0
```

Sender stops sending data.

---

## Persist Timer

Problem:

```text
Window Update Packet Lost
```

Both sides may wait forever.

Solution:

```text
Persist Timer
```

Sender periodically sends:

```text
Zero Window Probe
```

to check whether space became available.

---

## Important Formula

Sender obeys:

---

# TCP Congestion Control

## Purpose

Prevent network congestion and router queue overflow.

Question being solved:

```text
Can the network handle more data?
```

---

## Mechanism

TCP maintains:

```text
Congestion Window (cwnd)
```

Sender-side variable.

Unlike rwnd:

```text
Not advertised by receiver
```

Calculated by sender.

---

## Effective Sending Window

Sender must obey BOTH:

* rwnd
* cwnd

Actual sending limit:

---

## Congestion Signals

TCP infers congestion indirectly.

### Packet Loss

Strongest signal.

---

### Timeout

Severe congestion.

---

### Triple Duplicate ACK

Moderate congestion.

Usually indicates:

```text
Single packet loss
```

while network still operational.

---

# Congestion Control Phases

## 1. Slow Start

Initial phase.

Starts with small cwnd.

Typical:

```text
cwnd = 1 MSS
```

(MSS = Maximum Segment Size)

Growth:

```text
1
2
4
8
16
32
...
```

Exponential growth.

---

## Why?

TCP initially doesn't know available bandwidth.

Slow Start rapidly probes capacity.

---

# 2. Slow Start Threshold (ssthresh)

Boundary between:

```text
Slow Start
and
Congestion Avoidance
```

When:

```text
cwnd >= ssthresh
```

switch mode.

---

# 3. Congestion Avoidance

Linear growth.

Instead of doubling:

```text
16
17
18
19
20
...
```

Approx:

```text
+1 MSS per RTT
```

---

## AIMD

Core TCP principle:

```text
Additive Increase
Multiplicative Decrease
```

Increase slowly.

Reduce aggressively.

---

# Packet Loss Handling

Two cases.

---

## Case 1: Timeout

Assume severe congestion.

Actions:

```text
ssthresh = cwnd / 2
cwnd = 1 MSS
```

Restart Slow Start.

---

## Case 2: Triple Duplicate ACK

Assume isolated packet loss.

---

### Why Duplicate ACKs Occur

Packets:

```text
1 2 3 4 5
```

Packet 3 lost.

Receiver gets:

```text
1 2 4 5
```

Receiver repeatedly sends:

```text
ACK = 3
ACK = 3
ACK = 3
```

Meaning:

```text
Still waiting for byte 3
```

---

# Fast Retransmit

After:

```text
3 Duplicate ACKs
```

Sender retransmits immediately.

No timeout waiting.

---

# Fast Recovery

Instead of:

```text
cwnd -> 1 MSS
```

TCP reduces cwnd moderately.

Avoids wasting available bandwidth.

---

# Congestion Window Evolution

Typical graph:

```text
cwnd

|
|              /\
|             /  \
|            /    \
|           /      \
|__________/        \____
|
+-------------------------> Time
```

Exponential growth

↓

Linear growth

↓

Loss

↓

Reduction

↓

Growth resumes

---

# Flow Control vs Congestion Control

| Feature       | Flow Control     | Congestion Control      |
| ------------- | ---------------- | ----------------------- |
| Protects      | Receiver         | Network                 |
| Window        | rwnd             | cwnd                    |
| Controlled By | Receiver         | Sender                  |
| Based On      | Buffer Space     | Network Conditions      |
| Signal        | Available Memory | Loss/RTT/Duplicate ACKs |
| Scope         | End Host         | Entire Network          |

---

# Interview Nuggets

### Why both rwnd and cwnd?

Because:

```text
Fast Receiver ≠ Uncongested Network
```

and

```text
Uncongested Network ≠ Fast Receiver
```

Both constraints must be satisfied.

---

### Who advertises rwnd?

```text
Receiver
```

via TCP Window field.

---

### Who calculates cwnd?

```text
Sender
```

using TCP congestion algorithms.

---

### What causes Fast Retransmit?

```text
3 Duplicate ACKs
```

---

### What causes TCP Timeout?

```text
ACK not received before RTO
```

(Retransmission Timeout)

---

### Most Important Formula of TCP

If you remember only one formula from flow control + congestion control, remember that one. It captures the interaction between the receiver's capacity and the network's capacity.

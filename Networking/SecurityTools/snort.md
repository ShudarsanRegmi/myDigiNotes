**“Explain Snort in an exam-ready format covering definition, architecture, modes, rule structure, and workflow.”**

---

## :sd

### What is Snort?

**Snort** is an **open-source Network Intrusion Detection and Prevention System (NIDS/NIPS)** developed by Cisco.

It performs **real-time traffic analysis** and **packet logging**, and can **detect malicious activity** such as port scans, buffer overflow attempts, and protocol violations using **rule-based inspection**.

---

### Core Functions

* **Packet sniffing**
* **Packet logging**
* **Intrusion detection (IDS)**
* **Intrusion prevention (IPS)**

---

### Snort Modes

1. **Sniffer Mode**

   * Reads packets and displays them on console
   * Example use: quick inspection

2. **Packet Logger Mode**

   * Logs packets to disk
   * Useful for forensics and later analysis

3. **Network Intrusion Detection Mode (NIDS)**

   * Analyzes traffic against rules
   * Generates alerts on suspicious activity

---

### Snort Architecture

<img width="702" height="473" alt="image" src="https://github.com/user-attachments/assets/4d3770f9-f510-4740-98ab-f98d37ce01e9" />


Snort follows a **modular pipeline architecture**:

```
Network Traffic
      ↓
Packet Decoder
      ↓
Preprocessors
      ↓
Detection Engine
      ↓
Logging & Alerting System
      ↓
Output Modules
```

#### Components Explained:

* **Packet Decoder**

  * Captures packets from network interfaces
  * Identifies protocols (TCP, UDP, ICMP)

* **Preprocessors**

  * Normalize traffic (e.g., defragment IP packets, reassemble TCP streams)
  * Detect anomalies early

* **Detection Engine**

  * Heart of Snort
  * Matches traffic against **rules/signatures**

* **Logging & Alerting System**

  * Generates alerts when rules are triggered

* **Output Modules**

  * Stores logs (files, databases, SIEM tools)

---

### Snort Rule Structure

Snort uses **rule-based detection**.

**General Format:**

```
action protocol src_ip src_port -> dest_ip dest_port (options)
```

#### Example:

```
alert tcp any any -> 192.168.1.10 80 (msg:"Possible attack"; sid:1001;)
```

#### Breakdown:

* **action** → alert, log, drop
* **protocol** → tcp/udp/ip
* **src/dest** → IP and ports
* **options** → message, signature ID (sid), content matching

---

### Detection Techniques

* **Signature-based detection**

  * Matches known attack patterns
* **Anomaly-based detection (limited)**

  * Detects unusual behavior

---

### Working Flow (Stepwise)

1. Network packets are captured
2. Packet decoder identifies protocol
3. Preprocessors normalize traffic
4. Detection engine applies rules
5. If match found → alert generated
6. Logs stored via output modules

---

### Advantages

* Open-source and highly customizable
* Real-time detection
* Large community rule sets

---

### Limitations

* Signature-based → cannot detect unknown attacks well
* High false positives if poorly configured
* Requires tuning for performance

---

## :ol

Snort is an open-source IDS/IPS that analyzes network traffic in real time using rule-based detection to identify and respond to malicious activity.

---

If you want next level depth, we can go into:

* how Snort rules are actually parsed internally (AST-style matching)
* how it compares with Suricata
* writing advanced rules (content, pcre, flowbits)

Just tell.

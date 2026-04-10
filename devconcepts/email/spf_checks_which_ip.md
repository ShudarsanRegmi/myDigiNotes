**Refined version:**
“During email spoofing, what infrastructure does the attacker actually use to send the email? Specifically, when SPF checks the sender IP, which IP is being evaluated, and where does that IP originate from?”

Good. This is a **critical pivot point** in understanding spoofing vs authentication.

---

# :da → SHORT CORE ANSWER FIRST

* Attacker **does NOT use MUA IP**
* SPF checks the **IP of the SMTP server that directly connects to the receiver**
* That IP = **sending MTA (last hop before receiver)**

---

# 1. WHAT INFRASTRUCTURE ATTACKER USES

Attacker has multiple options:

---

## CASE A: OWN SMTP SERVER (RAW SPOOFING)

Attacker runs:

* Postfix / Exim
* Or even manual SMTP via telnet

```text
Attacker machine → acts as MTA → connects to victim MTA
```

👉 Here:

* Sender IP = attacker’s server IP

---

## CASE B: COMPROMISED SMTP SERVER

* Hacked mail server
* Open relay

👉 Sender IP = legitimate server IP

---

## CASE C: LEGIT EMAIL SERVICE ABUSE

* Gmail / SendGrid / AWS SES

👉 Sender IP = trusted provider IP

---

# 2. WHERE DOES “SENDER IP” COME FROM?

This is your main confusion. Let’s be precise.

---

## SPF checks THIS connection:

```text
[Sending MTA] ───────> [Receiving MTA]
           ↑
        THIS IP
```

---

### Example:

Attacker sends:

```text
MAIL FROM: ceo@company.com
```

But connection is:

```text
203.0.113.45 → receiver.com
```

👉 SPF checks:

```text
Is 203.0.113.45 allowed to send for company.com?
```

---

# 3. WHY NOT MUA IP?

Because:

👉 MUA NEVER talks to receiver directly

Flow:

```text
MUA → SMTP submission server → MTA → receiver
```

So:

* MUA IP is irrelevant
* It’s hidden behind SMTP server

---

# 4. HOW RECEIVER KNOWS SENDER IP?

From TCP connection:

```text
socket.getpeername()
```

And recorded in header:

```text
Received: from attacker.com (203.0.113.45)
```

---

# 5. HOW SPF VALIDATION WORKS (STEP-BY-STEP)

---

## Step 1: Extract domain

```text
MAIL FROM: ceo@company.com
          → company.com
```

---

## Step 2: Query DNS

```bash
dig TXT company.com
```

Example:

```text
v=spf1 ip4:192.168.1.10 include:_spf.google.com -all
```

---

## Step 3: Compare IP

```text
Sender IP = 203.0.113.45
Allowed? → NO
```

---

## Step 4: Result

```text
SPF FAIL
```

---

# 6. HOW ATTACKER BYPASSES SPF

---

## METHOD 1: USE AUTHORIZED SERVER

If attacker uses:

* Gmail SMTP
* AWS SES

Then:

```text
Sender IP ∈ SPF record
```

👉 SPF PASSES

---

## METHOD 2: COMPROMISED SERVER

* Legit domain server hacked

👉 SPF passes because IP is valid

---

## METHOD 3: MISCONFIGURED SPF

```text
v=spf1 +all
```

👉 Everyone allowed

---

# 7. CRITICAL INSIGHT (THIS IS THE CORE)

```text
SPF DOES NOT VERIFY IDENTITY
SPF ONLY CHECKS SENDING SERVER AUTHORIZATION
```

---

# 8. WHY SPOOFING STILL WORKS EVEN WITH SPF

Because attacker can:

```text
Use legit infrastructure
+
Forge visible “From” header
```

---

### Example:

```text
MAIL FROM: attacker@gmail.com  ← SPF OK
From: ceo@company.com         ← user sees this
```

👉 SPF passes
👉 User gets fooled

---

# 9. WHERE DKIM + DMARC ENTER

---

## DKIM

* Verifies domain actually signed message

---

## DMARC

* Enforces:

```text
Header From == SPF/DKIM domain
```

---

# 10. FINAL MENTAL MODEL

Think:

* SPF = “Is this server allowed?”
* NOT = “Is this person real?”

---

# 11. ONE LINE MEMORY LOCK

**SPF checks the server that sends the email, not the person who claims to send it.**

---

# 12. VOCAB UPGRADE

* **Originating IP** → actual sending server
* **Envelope sender** → SMTP-level identity
* **Header spoofing** → visible identity forgery
* **Authorization vs authentication** → key distinction

---

If you want next level, I strongly suggest:

* Live spoofing demo + SPF failure observation
* OR deep dive into DMARC alignment (this is where real defense happens)

That will complete your security understanding.

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/1ae3311e-8498-44ac-aa72-a83a3f9d2729" />

A clearer version of your question:

> **“Teach me Content Security Policy (CSP) in depth, including how it works, its directives, nonces and hashes, CSP headers, common bypasses and misconfigurations, and how to implement and test CSP in a real web application.”**

# CSP, in depth

## 1. What is CSP?

**Content Security Policy (CSP)** is a browser security mechanism that lets a website define **which sources of content the browser is allowed to load or execute**.

Its primary purpose is to reduce the impact of attacks such as:

* Cross-Site Scripting (XSS)
* Malicious script injection
* Unauthorized resource loading
* Some forms of data exfiltration

The core idea is:

```text
Website
   ↓
Sends security policy
   ↓
Browser
   ↓
Only allows content matching the policy
```

For example:

```http
Content-Security-Policy: script-src 'self'
```

means roughly:

> "Only execute JavaScript originating from this site's own origin."

---

# 2. Why do we need CSP?

Imagine an application contains an XSS vulnerability.

A legitimate page:

```html
<script src="/js/app.js"></script>
```

But an attacker manages to inject:

```html
<script src="https://evil.example/steal.js"></script>
```

Without CSP:

```text
Injected JavaScript
       ↓
Browser executes it
       ↓
Attacker's code runs in page context
```

With:

```http
Content-Security-Policy: script-src 'self'
```

the browser evaluates:

```text
https://evil.example/steal.js
        ↓
Is evil.example allowed?
        ↓
NO
        ↓
Browser blocks execution
```

So CSP provides an additional **defense-in-depth layer**.

It does **not** magically eliminate XSS vulnerabilities.

---

# 3. CSP is enforced by the browser

This is similar to CORS in one important sense.

The server sends a policy:

```http
Content-Security-Policy: ...
```

The browser enforces it.

For example:

```text
Server
  |
  | CSP header
  ↓
Browser
  |
  +---- script allowed?
  |
  +---- image allowed?
  |
  +---- stylesheet allowed?
  |
  +---- frame allowed?
  |
  ↓
Allow / Block
```

A tool such as:

```text
curl
Python requests
Burp
Postman
```

doesn't enforce CSP.

CSP is fundamentally a **browser-side security control**.

---

# 4. CSP is a policy language

A CSP consists of **directives**.

Example:

```http
Content-Security-Policy:
    default-src 'self';
    script-src 'self';
    style-src 'self';
    img-src 'self';
```

Each directive controls a particular category of resource.

Think:

```text
directive → what it controls
```

---

# 5. `default-src`

This is the fallback policy.

Example:

```http
Content-Security-Policy: default-src 'self'
```

It says that, unless a more specific directive overrides it, resources should come from the site's own origin.

Conceptually:

```text
default-src
     |
     +-- scripts
     +-- images
     +-- styles
     +-- fonts
     +-- etc.
```

But specific directives take precedence.

For example:

```http
default-src 'self';
script-src 'unsafe-inline';
```

`script-src` controls scripts rather than falling back to `default-src`.

---

# 6. `script-src`

This is one of the most important CSP directives.

```http
script-src 'self'
```

allows scripts from the same origin.

You could also specify trusted external sources:

```http
script-src 'self' https://cdn.example.com
```

Meaning:

```text
Allowed:
    your site
    cdn.example.com

Not allowed:
    random-attacker.example
```

---

# 7. The dangerous `'unsafe-inline'`

You may encounter:

```http
script-src 'self' 'unsafe-inline'
```

This allows inline JavaScript such as:

```html
<script>
    alert("hello");
</script>
```

and potentially inline event handlers such as:

```html
<button onclick="doSomething()">
```

The problem is obvious:

```text
XSS payload
     ↓
Inline JavaScript
     ↓
CSP allows inline scripts
     ↓
Attack has much more room to execute
```

Therefore, `'unsafe-inline'` significantly weakens script protection.

You should understand this phrase very well for interviews:

> **`'unsafe-inline'` permits inline script execution and can substantially weaken CSP's protection against XSS.**

---

# 8. `'unsafe-eval'`

Another important keyword:

```http
script-src 'self' 'unsafe-eval'
```

This permits JavaScript evaluation mechanisms such as:

```javascript
eval(...)
```

and related dynamic code generation mechanisms.

Why is this dangerous?

Because executing strings as code expands the attack surface.

So, generally:

```text
'unsafe-inline'  → weakens inline-script protection

'unsafe-eval'    → weakens protection against dynamic code execution
```

---

# 9. `style-src`

Controls stylesheets.

Example:

```http
style-src 'self'
```

You can allow a specific stylesheet provider:

```http
style-src 'self' https://fonts.example.com
```

There is also:

```http
style-src 'unsafe-inline'
```

which allows inline styles.

Note that script and style policies have different security implications.

---

# 10. `img-src`

Controls image sources.

Example:

```http
img-src 'self' https://images.example.com
```

You may also see:

```http
img-src 'self' data:
```

which permits images represented using `data:` URLs.

---

# 11. `font-src`

Controls font sources.

```http
font-src 'self' https://fonts.example.com
```

---

# 12. `connect-src`

This one is especially important for modern web applications.

It controls destinations to which browser APIs can make network connections.

For example:

```http
connect-src 'self' https://api.example.com
```

This can affect mechanisms such as:

```text
fetch()
XMLHttpRequest
WebSocket
EventSource
```

So for a React application:

```text
React
  |
  | fetch()
  ↓
https://api.example.com
```

your CSP might need:

```http
connect-src 'self' https://api.example.com
```

---

# 13. `frame-src`

Controls what your page is allowed to load inside frames.

Example:

```http
frame-src https://youtube.com
```

This controls resources loaded by:

```html
<iframe src="...">
```

---

# 14. `frame-ancestors`

This is different and extremely important.

It controls **who is allowed to embed your page**.

Example:

```http
frame-ancestors 'none'
```

means:

```text
Nobody can embed this page in an iframe.
```

This is useful against **clickjacking**.

For example:

```text
Attacker page
     |
     ↓
<iframe src="https://bank.example">
```

If the bank sends:

```http
frame-ancestors 'none'
```

the browser blocks the embedding.

---

# 15. `object-src`

Controls plugins/objects such as:

```html
<object>
<embed>
```

A strong common setting is:

```http
object-src 'none'
```

because modern applications generally don't need these legacy mechanisms.

---

# 16. `base-uri`

Controls the URL used by the HTML `<base>` element.

For example:

```http
base-uri 'self'
```

or:

```http
base-uri 'none'
```

This helps prevent certain attacks involving manipulation of the document's base URL.

---

# 17. `form-action`

Controls where forms can submit.

Example:

```http
form-action 'self'
```

So:

```html
<form action="https://evil.example">
```

could be blocked by the browser.

---

# 18. `media-src`

Controls sources for:

```text
<audio>
<video>
```

Example:

```http
media-src 'self' https://media.example.com
```

---

# 19. `worker-src`

Controls sources for web workers:

```javascript
new Worker(...)
```

Example:

```http
worker-src 'self'
```

---

# 20. `manifest-src`

Controls web application manifests:

```html
<link rel="manifest" href="/manifest.json">
```

Example:

```http
manifest-src 'self'
```

---

# 21. The big picture

You don't need to memorize every directive immediately.

Understand the major ones:

| Directive         | Controls                     |
| ----------------- | ---------------------------- |
| `default-src`     | Fallback policy              |
| `script-src`      | JavaScript                   |
| `style-src`       | CSS                          |
| `img-src`         | Images                       |
| `font-src`        | Fonts                        |
| `connect-src`     | fetch/XHR/WebSocket etc.     |
| `frame-src`       | Frames your page loads       |
| `frame-ancestors` | Who can frame your page      |
| `object-src`      | `<object>`, `<embed>`        |
| `form-action`     | Form submission destinations |
| `base-uri`        | `<base>` URL                 |
| `media-src`       | Audio/video                  |
| `worker-src`      | Web workers                  |

---

# 22. The most important concept: Nonces

Now we reach the really interesting part.

Suppose you have:

```html
<script>
    initializeApplication();
</script>
```

But you don't want:

```http
script-src 'unsafe-inline'
```

because that weakens CSP.

Instead, you can use a **nonce**.

Nonce means a cryptographically random, unpredictable value intended for one use.

Server generates:

```text
r4nd0m-value-123
```

Then sends:

```http
Content-Security-Policy:
    script-src 'nonce-r4nd0m-value-123'
```

And HTML contains:

```html
<script nonce="r4nd0m-value-123">
    initializeApplication();
</script>
```

Browser checks:

```text
Script nonce
      |
      ↓
r4nd0m-value-123

CSP nonce
      |
      ↓
r4nd0m-value-123

MATCH
      ↓
Execute
```

Injected script:

```html
<script>
    maliciousCode();
</script>
```

has no valid nonce:

```text
nonce?
  ↓
missing
  ↓
BLOCK
```

---

# 23. Nonce must be unpredictable

This is critical.

Bad:

```text
nonce="123"
```

Bad:

```text
nonce="admin"
```

Bad:

```text
nonce="static-value"
```

A nonce must be generated securely and should be fresh for each response.

Think:

```text
Secure random value
        ↓
CSP header
        +
HTML script
        ↓
Browser verifies
```

---

# 24. CSP hashes

Another mechanism is a **hash**.

Suppose your page contains:

```html
<script>
    console.log("Hello");
</script>
```

You can calculate a cryptographic hash of the script content.

Then CSP might contain:

```http
script-src 'sha256-...'
```

The browser hashes the script and compares it with the declared hash.

Conceptually:

```text
Script content
      ↓
SHA-256
      ↓
Hash A

CSP declared hash
      ↓
Hash A

MATCH → execute
```

If an attacker changes:

```javascript
console.log("Hello");
```

to:

```javascript
alert(document.cookie);
```

the hash changes.

Therefore:

```text
Hash mismatch
      ↓
Browser blocks script
```

---

# 25. Nonce vs hash

| Nonce                                         | Hash                                 |
| --------------------------------------------- | ------------------------------------ |
| Random value                                  | Hash of exact content                |
| Usually generated per response                | Usually static for unchanged content |
| Good for dynamically generated inline scripts | Good for static inline scripts       |
| Must be unpredictable                         | Must match exact content             |

For interviews:

> **A nonce authorizes a specific script instance, while a hash authorizes specific script content.**

---

# 26. CSP and XSS

The relationship is:

```text
XSS vulnerability
       ↓
Attacker injects content
       ↓
Browser attempts to execute it
       ↓
CSP evaluates it
       ↓
Allowed?
   /       \
 YES        NO
 ↓          ↓
Execute    Block
```

This is why CSP is **defense in depth**.

You should still fix the XSS vulnerability.

Don't think:

> "We have CSP, therefore XSS isn't a problem."

Instead:

> "CSP reduces the exploitability and impact of certain XSS conditions."

---

# 27. CSP reporting

CSP can also report policy violations.

You may encounter:

```http
Content-Security-Policy-Report-Only:
```

This is extremely useful when deploying a new policy.

Instead of immediately blocking resources:

```text
Violation
   ↓
Report
   ↓
Don't enforce
```

This lets developers discover:

```text
What legitimate resources are we currently using?
```

before switching to enforcement.

---

# 28. Enforced vs Report-Only

### Enforcement

```http
Content-Security-Policy: ...
```

The browser enforces the policy.

### Report-only

```http
Content-Security-Policy-Report-Only: ...
```

The browser reports violations but does not enforce the policy.

A practical deployment strategy is:

```text
Develop policy
      ↓
Report-Only
      ↓
Observe violations
      ↓
Fix legitimate dependencies
      ↓
Tighten policy
      ↓
Enforce CSP
```

---

# 29. CSP violation example

Suppose:

```http
Content-Security-Policy:
    script-src 'self'
```

but the page attempts:

```html
<script src="https://evil.example/x.js"></script>
```

Browser sees:

```text
script source
https://evil.example
        ↓
script-src
        ↓
'self' only
        ↓
NOT ALLOWED
        ↓
BLOCK
```

The browser can generate a CSP violation report depending on the reporting configuration.

---

# 30. A realistic CSP

A simple policy could look like:

```http
Content-Security-Policy:
    default-src 'self';
    script-src 'self';
    style-src 'self';
    img-src 'self' data:;
    font-src 'self';
    connect-src 'self' https://api.example.com;
    object-src 'none';
    frame-ancestors 'none';
    base-uri 'self';
    form-action 'self';
```

This establishes a reasonably restrictive baseline.

But CSP must be tailored to the actual application's dependencies.

For example, if your frontend uses:

```text
Google Fonts
Stripe
Firebase
CDN
analytics
WebSocket
external APIs
```

the policy must account for those legitimate sources.

---

# 31. CSP and React

For a React application, a common misconception is:

> "React automatically protects me with CSP."

No.

React provides various protections against unsafe rendering patterns, but CSP is a **separate browser security control**.

Your application may need things like:

```http
script-src ...
connect-src ...
img-src ...
style-src ...
font-src ...
```

depending on your architecture.

For a React + Express application:

```text
React
   |
   +-- JavaScript
   +-- CSS
   +-- images
   +-- fetch()
   |
   ↓
CSP controls browser behavior
   |
   ↓
Express/API
```

---

# 32. CSP vs CORS

Since you just learned CORS, this distinction is important.

| CORS                                        | CSP                                         |
| ------------------------------------------- | ------------------------------------------- |
| Cross-Origin Resource Sharing               | Content Security Policy                     |
| Controls cross-origin browser access        | Controls permitted content/resources        |
| Mainly about reading cross-origin responses | Mainly about what the page can load/execute |
| Server sends CORS headers                   | Server sends CSP policy                     |
| Uses `Access-Control-*` headers             | Uses `Content-Security-Policy`              |
| Example: API access                         | Example: script execution                   |
| Helps control cross-origin data access      | Helps mitigate XSS/resource injection       |

A useful mental distinction:

```text
CORS:
"Which other origins can my JavaScript access?"

CSP:
"What content is my browser allowed to load or execute?"
```

---

# 33. CSP vs CSRF

Again, three different concepts:

```text
CORS
 ↓
Cross-origin response access

CSP
 ↓
Content/resource execution policy

CSRF
 ↓
Unauthorized state-changing requests
```

They address different threat classes.

You don't replace one with another.

---

# 34. Common CSP mistakes

### Mistake 1

```http
script-src *
```

Very permissive.

---

### Mistake 2

```http
script-src 'unsafe-inline'
```

Weakens protection against injected inline scripts.

---

### Mistake 3

```http
script-src 'unsafe-eval'
```

Allows dynamic code evaluation.

---

### Mistake 4

Overly broad trusted domains:

```http
script-src 'self' *.example.com
```

If an attacker can control content or JavaScript on a trusted subdomain, the security boundary may become much weaker.

---

### Mistake 5

Using CSP but forgetting:

```http
object-src 'none'
```

when the application doesn't need legacy object/plugin content.

---

### Mistake 6

Using `default-src 'self'` and assuming everything is adequately protected.

A good CSP requires understanding the application's actual resource flows.

---

# 35. CSP bypass mindset

As a security engineer, don't stop at:

> "There is a CSP header."

Ask:

```text
What does the policy actually permit?
```

For example:

```http
script-src 'self' https://trusted.example
```

Then investigate:

```text
Can attacker-controlled JavaScript exist on trusted.example?

Can JSONP-like behavior turn trusted.example into script execution?

Are there unsafe inline scripts?

Is unsafe-eval enabled?

Are wildcard sources used?

Are dangerous schemes allowed?

Are third-party dependencies trustworthy?

Can an attacker inject HTML that uses an allowed resource?
```

The security boundary is the **effective policy**, not merely the existence of a CSP header.

---

# 36. CSP from a Product Security perspective

When reviewing an application, think in layers:

```text
                 Application
                      |
        +-------------+-------------+
        |             |             |
     Secure       Input          Output
     coding      validation      encoding
        |
        ↓
       XSS
        |
        ↓
       CSP
        |
        ↓
 Browser defense-in-depth
```

CSP is therefore not:

```text
"Fix XSS"
```

It is:

```text
"Reduce the browser-side impact
if malicious content reaches the page."
```

---

# 37. Interview-quality definition

If an interviewer asks:

> **"What is CSP?"**

A strong answer would be:

> **"Content Security Policy is a browser-enforced security mechanism that allows a web application to specify which sources of scripts, styles, images, connections, frames, and other resources are permitted. Its primary purpose is to reduce the impact of attacks such as XSS by restricting what the browser can load or execute. CSP is a defense-in-depth control, not a replacement for secure coding or input/output validation."**

That demonstrates much more understanding than:

> "CSP prevents XSS."

---

# 38. The mental model to remember

```text
                    SERVER
                      |
                      | Content-Security-Policy
                      ↓
                   BROWSER
                      |
          +-----------+-----------+
          |           |           |
       script       image       connect
          |           |           |
          ↓           ↓           ↓
     script-src    img-src    connect-src
          |
          ↓
      ALLOWED?
       /     \
     YES      NO
      |        |
   Execute    Block
```

And the most important security hierarchy:

```text
Secure coding
      ↓
Prevent XSS
      ↓
CSP
      ↓
Limit what injected content can execute
      ↓
Defense in depth
```

**Core vocabulary to retain:** `directive`, `source expression`, `nonce`, `hash`, `preflight` belongs to CORS, while `report-only`, `enforcement`, `allowlist`, `trusted source`, `XSS mitigation`, and `defense in depth` are central CSP concepts.

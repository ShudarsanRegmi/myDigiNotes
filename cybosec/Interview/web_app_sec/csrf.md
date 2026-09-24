<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/f6ce60c3-6dde-45eb-b3fb-eb67023fb48a" />


> **“Teach me CSRF comprehensively: how a CSRF attack works, why browsers automatically send cookies, how CSRF tokens prevent attacks, synchronizer tokens vs double-submit cookies, SameSite cookies, Origin/Referer validation, CORS, common bypasses, and how to test and defend against CSRF in modern web applications.”**

# CSRF: Cross-Site Request Forgery

## 1. What is CSRF?

**Cross-Site Request Forgery (CSRF)** is an attack where an attacker tricks a victim's browser into sending an **authenticated request to a target application**, causing an unwanted state-changing action.

The crucial idea is:

> **The browser may automatically attach the victim's authentication credentials to a request, even though the request was initiated from an attacker's website.**

Example:

```text
Victim
  |
  | logged into bank.com
  ↓
Browser has:
session=abc123
  |
  | visits evil.com
  ↓
Attacker causes request
  |
  ↓
bank.com/transfer
```

The bank sees:

```text
Cookie: session=abc123
```

and may believe:

> "This is an authenticated request from the user."

But the user never intentionally initiated the transfer.

---

# 2. The fundamental condition for CSRF

CSRF generally requires three things:

```text
1. Victim is authenticated
          +
2. Browser automatically sends authentication credentials
          +
3. Attacker can cause a request to the target
```

Therefore:

```text
Authenticated victim
        +
Attacker-controlled request
        +
Automatically attached credentials
        ↓
       CSRF
```

This is the mental model you should remember.

---

# 3. Why are cookies important?

Suppose you log into:

```text
https://bank.example
```

The server gives you:

```http
Set-Cookie: session=abc123
```

Your browser stores it.

Later you visit:

```text
https://bank.example/profile
```

The browser automatically sends:

```http
Cookie: session=abc123
```

JavaScript doesn't need to manually add it.

That's the crucial property that CSRF abuses.

---

# 4. The classic CSRF attack

Suppose the bank has:

```http
POST /transfer
```

with:

```text
amount=10000
recipient=attacker
```

The victim is already logged in.

The attacker creates:

```html
<form action="https://bank.example/transfer" method="POST">
    <input type="hidden" name="amount" value="10000">
    <input type="hidden" name="recipient" value="attacker">
</form>

<script>
    document.forms[0].submit();
</script>
```

Victim visits:

```text
https://evil.example
```

The browser submits:

```http
POST /transfer HTTP/1.1
Host: bank.example
Cookie: session=abc123
Content-Type: application/x-www-form-urlencoded

amount=10000&recipient=attacker
```

The attacker doesn't know:

```text
session=abc123
```

but doesn't need to.

The browser supplies it.

That's the essence of CSRF.

---

# 5. Why can't the attacker simply use JavaScript?

This is where people often confuse CSRF with CORS.

Suppose:

```javascript
fetch("https://bank.example/transfer", {
    method: "POST",
    body: "amount=10000"
});
```

The browser's **Same-Origin Policy/CORS restrictions** may prevent the attacker's JavaScript from reading the response.

But that's not necessarily enough to stop the request itself from being sent.

CSRF doesn't fundamentally require:

```text
Read response
```

It only needs:

```text
Cause state-changing request
```

Therefore:

> **CORS is not a CSRF defense.**

---

# 6. This distinction is extremely important

Think about three separate questions:

### CORS

```text
Can evil.com JavaScript read
the response from bank.com?
```

### CSRF

```text
Can evil.com cause the victim's browser
to perform an authenticated action on bank.com?
```

### CSP

```text
What resources/content is the browser
allowed to load or execute?
```

Different problems.

---

# 7. CSRF doesn't necessarily require JavaScript

This is important.

An attacker can use ordinary HTML.

For example:

```html
<form action="https://bank.example/change-email"
      method="POST">

    <input type="hidden"
           name="email"
           value="attacker@example.com">

</form>

<script>
    document.forms[0].submit();
</script>
```

Even without JavaScript, other HTML mechanisms can trigger requests:

```html
<img src="https://example.com/...">
```

```html
<a href="https://example.com/...">
```

```html
<form ...>
```

The exact attack depends on the target endpoint and browser cookie policies.

---

# 8. Why GET requests are dangerous for CSRF

Consider:

```http
GET /delete-account
```

That's terrible application design.

HTTP semantics generally distinguish:

```text
GET
```

as a safe/read operation, while:

```text
POST
PUT
PATCH
DELETE
```

are typically used for state changes.

If an application performs destructive operations through GET, an attacker may be able to trigger them through simple navigation or resource loading.

For example:

```html
<img src="https://bank.example/delete-account">
```

The browser may request that URL.

So:

> **State-changing operations should not be implemented as GET requests.**

---

# 9. The CSRF token defense

Now we get to the most important part.

The server generates an unpredictable token:

```text
csrf_token =
9f82a7c1d8e4...
```

The legitimate page contains:

```html
<form method="POST" action="/transfer">

    <input
        type="hidden"
        name="csrf_token"
        value="9f82a7c1d8e4..."
    >

    <input name="amount">
    <input name="recipient">

    <button>Transfer</button>
</form>
```

When the user submits:

```http
POST /transfer
Cookie: session=abc123

csrf_token=9f82a7c1d8e4...
&amount=10000
&recipient=bob
```

The server verifies the token.

---

# 10. Why does this stop CSRF?

The attacker can create:

```html
<form action="https://bank.example/transfer">
```

but doesn't know the legitimate CSRF token.

They can send:

```http
amount=10000
recipient=attacker
```

but:

```text
csrf_token = ?
```

The attacker cannot normally read the legitimate bank page because of the browser's same-origin restrictions.

Therefore:

```text
Attacker
   |
   | knows endpoint
   | knows parameters
   |
   X doesn't know CSRF token
   |
   ↓
Request rejected
```

That's the fundamental security property.

---

# 11. CSRF token is a second credential

A useful mental model:

```text
Session cookie
     +
CSRF token
     ↓
Authenticated state-changing request
```

The cookie proves:

> "This browser has an authenticated session."

The CSRF token proves:

> "This request originated through a legitimate application flow that had access to the token."

It's not authentication in the traditional sense, but it adds **request authenticity context**.

---

# 12. The synchronizer token pattern

This is the classic CSRF defense.

Server stores:

```text
session:
    user = Alice
    csrf_token = XYZ123
```

Server renders:

```html
<input type="hidden"
       name="csrf_token"
       value="XYZ123">
```

Request:

```text
Cookie: session=abc
csrf_token=XYZ123
```

Server:

```text
Does submitted token == session's token?
             |
        +----+----+
        |         |
       YES        NO
        |         |
      allow      reject
```

This is called the **Synchronizer Token Pattern**.

---

# 13. Why must the token be unpredictable?

Suppose:

```text
csrf_token=123
```

That's useless.

An attacker could guess it.

You want something generated using a cryptographically secure random generator.

For example:

```text
32 bytes random
```

or another sufficiently strong construction.

The important properties are:

```text
Unpredictable
High entropy
Difficult to guess
Properly generated
```

---

# 14. Does the CSRF token need to be secret forever?

No.

Its security comes from preventing an attacker from obtaining the token for the victim's legitimate session/request flow.

Tokens can be:

```text
Per-session
```

or:

```text
Per-request
```

Per-request tokens provide stronger isolation but can introduce usability complications such as browser back-button problems and multiple-tab synchronization.

Many applications use:

```text
one token per session
```

because it's simpler and still effective when properly implemented.

---

# 15. Double-submit cookie pattern

Another approach is the **Double Submit Cookie** pattern.

The server sets:

```http
Set-Cookie: csrf_token=XYZ123
```

and also expects the client to submit:

```http
X-CSRF-Token: XYZ123
```

So the request contains the token twice:

```text
Cookie:
csrf_token=XYZ123

Header:
X-CSRF-Token: XYZ123
```

The server compares them.

```text
Cookie token
     |
     | compare
     ↓
Request token
     |
     ↓
MATCH?
```

If they don't match:

```text
Reject
```

---

# 16. Why does double-submit work?

The attacker may be able to cause the browser to send:

```text
Cookie: csrf_token=XYZ123
```

but normally cannot read the cookie value from another origin and therefore cannot construct:

```http
X-CSRF-Token: XYZ123
```

in the required request.

This gives the server two values to compare.

However, the exact security of the pattern depends heavily on cookie configuration and whether an attacker can manipulate the cookie.

A properly designed **signed double-submit cookie** is stronger than a naive implementation.

---

# 17. Synchronizer vs double-submit

|                     | Synchronizer Token               | Double Submit                  |
| ------------------- | -------------------------------- | ------------------------------ |
| Server stores token | Yes                              | Not necessarily                |
| Token in request    | Yes                              | Yes                            |
| Token in cookie     | Not required                     | Yes                            |
| Token comparison    | Against server-side value        | Cookie vs request              |
| Common use          | Traditional server-rendered apps | Stateless/API-oriented designs |
| Main concern        | Token storage/management         | Cookie injection/manipulation  |

The important concept isn't memorizing the names.

Understand **where the server obtains the expected token**.

---

# 18. CSRF with SPAs

Modern React applications complicate the picture.

Suppose:

```text
React
https://app.example.com

API
https://api.example.com
```

You might use:

```javascript
fetch("/api/profile", {
    method: "POST",
    headers: {
        "X-CSRF-Token": csrfToken
    }
});
```

The server checks:

```http
X-CSRF-Token: ...
```

This works particularly well when the API requires a **custom request header** that an attacker cannot simply cause a cross-origin HTML form to set.

But you still need a secure way for the legitimate application to obtain the token.

---

# 19. Why custom headers help

Consider:

```http
X-CSRF-Token: abc123
```

An attacker cannot normally create a standard HTML form that sends:

```http
X-CSRF-Token: abc123
```

as an arbitrary custom header.

Using JavaScript:

```javascript
fetch(url, {
    headers: {
        "X-CSRF-Token": token
    }
});
```

would encounter browser cross-origin restrictions when trying to perform such a request cross-origin.

That can provide an additional barrier.

But don't reduce the whole defense to:

> "Custom header = CSRF solved."

The overall authentication and CORS configuration still matter.

---

# 20. SameSite cookies

Modern browsers provide another major CSRF defense:

```http
Set-Cookie: session=abc123; SameSite=Lax
```

The `SameSite` attribute controls when cookies are sent in cross-site contexts.

Three important values:

```text
Strict
Lax
None
```

---

# 21. `SameSite=Strict`

```http
Set-Cookie: session=abc123; SameSite=Strict
```

The browser applies very restrictive cross-site cookie behavior.

Conceptually:

```text
same-site request
    ↓
cookie sent

cross-site request
    ↓
cookie generally withheld
```

This provides strong CSRF resistance but can affect legitimate cross-site flows.

---

# 22. `SameSite=Lax`

```http
Set-Cookie: session=abc123; SameSite=Lax
```

This provides a balance between security and usability.

It allows cookies in some top-level navigation scenarios while restricting many cross-site request contexts.

For many ordinary web applications, `Lax` is a useful default.

But you should understand that:

> **SameSite is not a universal substitute for understanding the application's request flows.**

---

# 23. `SameSite=None`

If you specify:

```http
SameSite=None
```

the cookie is allowed in cross-site contexts.

Modern browsers require:

```http
Secure
```

with `SameSite=None`.

So:

```http
Set-Cookie: session=abc123; SameSite=None; Secure
```

can increase CSRF exposure because the cookie is available in cross-site contexts.

If you genuinely need cross-site cookies, you should pair this with appropriate CSRF protections.

---

# 24. SameSite vs CSRF tokens

Think of them as layers.

```text
SameSite cookies
       +
CSRF token
       +
Origin validation
       +
secure application design
```

A mature application can use multiple controls rather than depending on one mechanism.

---

# 25. Origin validation

The server can inspect:

```http
Origin: https://app.example.com
```

and determine whether the request came from an expected origin.

For example:

```text
Allowed:
https://app.example.com

Received:
https://evil.example

              ↓

Reject
```

This can be especially useful for state-changing requests.

---

# 26. Referer validation

Another signal is:

```http
Referer: https://app.example.com/account
```

The server can check whether the request originated from an expected site.

However, `Referer` can be absent or affected by browser privacy controls and `Referrer-Policy`.

Therefore:

> **Origin is generally a more useful signal when available.**

Don't build a security model that assumes the Referer header will always exist.

---

# 27. Why can't attackers simply set the Origin header?

A malicious webpage cannot freely forge browser-controlled security headers in the same way a server-side HTTP client can.

For example, the attacker cannot simply make the browser say:

```http
Origin: https://bank.example
```

while actually originating from:

```text
https://evil.example
```

The browser controls these headers.

This is one reason Origin validation can be useful as a CSRF defense.

---

# 28. CORS does NOT equal CSRF protection

This deserves repetition.

Suppose:

```text
evil.com
    |
    | POST /transfer
    ↓
bank.com
```

The bank might respond:

```http
Access-Control-Allow-Origin:
https://bank.example
```

and therefore the attacker cannot read the response.

But the request may still have been processed.

So:

```text
CORS
    ↓
controls cross-origin response access

CSRF defense
    ↓
controls unauthorized state-changing requests
```

Different security properties.

---

# 29. CSRF and authentication type

CSRF is particularly associated with **browser-managed credentials**.

For example:

```text
Cookie-based session
```

is naturally exposed to CSRF because the browser automatically attaches the cookie.

Consider a bearer token stored only in JavaScript memory:

```javascript
Authorization: Bearer abc123
```

An attacker cannot simply cause a normal HTML form submission to add that header.

That changes the CSRF threat model.

However, moving tokens into browser-accessible storage introduces other security considerations, especially XSS.

So don't conclude:

> "JWT = no security problems."

Instead:

```text
Cookie authentication
    → CSRF is a major consideration

Browser-managed bearer header
    → CSRF characteristics differ
    → XSS/token theft becomes a major concern
```

---

# 30. Login CSRF

CSRF isn't limited to:

```text
money transfer
password change
email change
```

Consider a login endpoint:

```http
POST /login
username=attacker
password=attackerPassword
```

An attacker could potentially trick a victim into logging into the attacker's account.

Then the victim might upload:

```text
personal information
private documents
credit card details
```

into what they believe is their own account.

But they're actually operating inside:

```text
attacker's account
```

This is called **login CSRF**.

So CSRF can affect authentication flows too.

---

# 31. CSRF against password change

Suppose:

```http
POST /change-password

new_password=attacker123
```

If the endpoint only relies on the victim's session cookie:

```text
Victim cookie
     +
attacker-triggered request
     ↓
Password changed
```

That's a serious CSRF vulnerability.

Sensitive state-changing operations should require appropriate protections.

---

# 32. CSRF against account settings

Potential targets include:

```text
Change email
Change password
Add payment method
Delete account
Change shipping address
Enable forwarding
Change notification settings
Transfer funds
Create API keys
Modify permissions
```

A useful security-review question is:

> **"Which authenticated endpoints change server-side state?"**

Then assess their CSRF protections.

---

# 33. JSON APIs and CSRF

People sometimes say:

> "Our API accepts JSON, so CSRF isn't possible."

That's an oversimplification.

If the endpoint requires:

```http
Content-Type: application/json
```

an ordinary HTML form cannot naturally generate that exact request body/content type.

That can make traditional CSRF attacks harder.

But the application still needs to consider:

```text
CORS
authentication
content-type handling
browser behavior
endpoint alternatives
misconfigured APIs
```

Don't use content type alone as your entire security model.

---

# 34. A subtle danger: accepting multiple content types

Suppose an API expects:

```http
Content-Type: application/json
```

but also accepts:

```text
application/x-www-form-urlencoded
multipart/form-data
text/plain
```

Now an attacker may find a way to trigger a request using mechanisms available to cross-site HTML.

So strict request parsing can contribute to CSRF resistance.

---

# 35. XSS defeats many CSRF defenses

This is a critical relationship.

Suppose your application has XSS:

```text
XSS
 ↓
Attacker JavaScript executes
inside trusted origin
 ↓
Can access page/token
 ↓
Can make legitimate-looking requests
```

If the attacker can execute JavaScript inside:

```text
https://bank.example
```

then browser same-origin restrictions no longer protect the application from that script.

The attacker may be able to retrieve:

```text
CSRF token
```

and submit:

```text
valid CSRF token
+
authenticated session
```

Therefore:

> **CSRF defenses do not compensate for XSS.**

And conversely:

> **CSP can reduce XSS impact, which indirectly strengthens the overall defense against CSRF-related attacks.**

---

# 36. The complete defense stack

A mature application might use:

```text
                 Web Application
                        |
          +-------------+-------------+
          |             |             |
       SameSite       CSRF         Origin
        Cookies       Token        Validation
          |             |             |
          +-------------+-------------+
                        |
                 State-changing
                    request
                        |
                  Server validates
                        |
                   Allow / Reject
```

And alongside that:

```text
Input validation
Output encoding
CSP
Authentication
Authorization
Secure cookie attributes
```

Each solves a different problem.

---

# 37. Secure cookie attributes

For session cookies, you should understand:

```http
Set-Cookie: session=abc123;
    Secure;
    HttpOnly;
    SameSite=Lax
```

### `Secure`

Cookie is sent only over HTTPS.

### `HttpOnly`

JavaScript cannot access the cookie through:

```javascript
document.cookie
```

This helps reduce cookie theft through some XSS scenarios.

### `SameSite`

Controls cross-site cookie behavior.

These attributes are complementary.

---

# 38. A practical secure flow

Imagine:

```text
React
   |
   | POST /transfer
   | X-CSRF-Token: XYZ
   ↓
Express API
```

Browser automatically sends:

```http
Cookie: session=ABC
```

Request:

```http
POST /transfer
Origin: https://app.example.com
Cookie: session=ABC
X-CSRF-Token: XYZ
Content-Type: application/json
```

Server validates:

```text
1. Is session authenticated?
             ↓
2. Is Origin trusted?
             ↓
3. Is CSRF token valid?
             ↓
4. Is user authorized?
             ↓
5. Is request valid?
             ↓
6. Perform operation
```

That's a robust security pipeline.

---

# 39. CSRF testing

As a product security engineer, you should test state-changing endpoints.

Look for:

```text
POST
PUT
PATCH
DELETE
```

and also suspicious:

```text
GET /delete
GET /change-password
GET /update-email
```

Then ask:

```text
Does the endpoint rely on cookies?
Does it change server state?
Is a CSRF token required?
Is the token unpredictable?
Is the token validated server-side?
Are SameSite cookies configured?
Is Origin checked?
Can the request be triggered cross-site?
Does the API accept form-encoded requests?
```

---

# 40. Basic CSRF testing methodology

Suppose:

```http
POST /api/change-email
Cookie: session=ABC

email=new@example.com
```

Try removing:

```text
CSRF token
```

If it still succeeds:

```text
Potential CSRF vulnerability
```

Then construct a proof-of-concept page:

```html
<form action="https://target.example/api/change-email"
      method="POST">

    <input type="hidden"
           name="email"
           value="attacker@example.com">

</form>

<script>
    document.forms[0].submit();
</script>
```

Then test in an authorized environment.

The key question is:

> **Can a cross-site attacker cause the victim's authenticated browser to perform the state-changing action without possessing a required unpredictable anti-CSRF value?**

---

# 41. Burp Suite mindset

In Burp, identify:

```text
Request
    ↓
Cookie
    ↓
State-changing method
    ↓
CSRF token?
    ↓
Origin?
    ↓
SameSite?
```

For example:

```http
POST /api/profile HTTP/1.1
Host: target.example
Cookie: session=ABC
Content-Type: application/x-www-form-urlencoded

email=test@example.com
```

If there is:

```text
No CSRF token
No meaningful Origin validation
Weak SameSite configuration
```

investigate whether the request can actually be triggered cross-site.

Don't declare vulnerability merely from the absence of a token. The application's complete browser behavior matters.

---

# 42. Common CSRF mistakes

### Mistake 1: "We use POST, so we're safe."

False.

CSRF can target POST.

---

### Mistake 2: "We use CORS."

False.

CORS does not inherently prevent state-changing requests.

---

### Mistake 3: "We use JWT."

Incomplete.

The threat depends on how the credential is transported and stored.

---

### Mistake 4: "The CSRF token is hidden."

The token being hidden in HTML isn't the security property.

It needs to be:

```text
unpredictable
properly associated with the session/request
validated by the server
```

---

### Mistake 5: "We have SameSite."

Good, but understand your browser/client compatibility and cross-site flows.

Defense in depth is preferable for sensitive operations.

---

### Mistake 6: "GET is harmless."

GET should not cause state changes.

---

# 43. CSRF attack vs XSS

This distinction is interview gold.

### CSRF

Attacker:

```text
controls the request
```

but generally does not need to execute JavaScript inside the trusted application origin.

### XSS

Attacker:

```text
executes JavaScript
inside the trusted application's context
```

Therefore:

```text
CSRF
Attacker → causes request

XSS
Attacker → executes code
```

XSS generally gives the attacker a much stronger position because same-origin protections may no longer protect the application from malicious code running within its origin.

---

# 44. CSRF attack flow

Memorize this:

```text
                Victim
                   |
            logged into bank
                   |
            session cookie
                   |
                   ↓
             visits evil.com
                   |
                   ↓
        attacker-controlled form
                   |
                   ↓
        POST https://bank.com/transfer
                   |
                   ↓
      Browser automatically adds cookie
                   |
                   ↓
              bank.com
                   |
             authenticates user
                   |
                   ↓
          State-changing action
```

Now add the defense:

```text
Attacker request
       |
       ↓
Missing CSRF token
       |
       ↓
Server rejects
```

That's the entire concept.

---

# 45. The deepest mental model

Think of authentication and CSRF separately:

```text
Authentication:

"Who is making this request?"

        ↓

Session cookie
        ↓
        Alice
```

CSRF defense asks:

```text
"Did this state-changing request
come through an expected interaction
with my application?"
```

The CSRF token provides an unpredictable value that an unrelated origin normally cannot obtain.

So:

```text
Authentication
       +
Request-origin assurance
       ↓
Safer state-changing request
```

---

# 46. Interview-quality definition

If an interviewer asks:

> **"What is CSRF?"**

A strong answer:

> **"CSRF is an attack where an attacker causes a victim's browser to send an unintended state-changing request to an application in which the victim is authenticated. It primarily exploits browser-managed credentials such as cookies that are automatically attached to requests. Common defenses include unpredictable CSRF tokens, SameSite cookies, Origin validation, and careful request design, while CORS should not be treated as a CSRF defense."**

And if they ask:

> **"How does a CSRF token prevent it?"**

Say:

> **"The server requires an unpredictable token that the attacker-controlled origin cannot normally obtain. The legitimate application includes that token in the state-changing request, and the server validates it against the expected value. The attacker's forged request therefore lacks the required token and is rejected, even though the browser may still automatically attach the victim's session cookie."**

That shows the actual mechanism rather than just memorizing "use CSRF tokens."

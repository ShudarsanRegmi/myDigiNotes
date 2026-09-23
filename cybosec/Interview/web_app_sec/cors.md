<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/2faae1be-38c7-4be6-a67f-32130990f05e" />


> **“Teach me CORS in depth, starting from the browser’s same-origin policy, then explain preflight requests, CORS headers, credentials, common misconfigurations, and how to debug and secure CORS in a real application.”**

# CORS, in depth

CORS stands for **Cross-Origin Resource Sharing**. The easiest way to understand it is:

> **CORS is a browser-enforced mechanism that allows a web server to explicitly permit a web page from another origin to access its resources.**

The key word is **origin**.

---

## 1. First understand "origin"

An origin is the combination of:

```text
scheme + host + port
```

For example:

```text
https://example.com:443
│      │           │
scheme host        port
```

These are different origins:

```text
https://example.com
https://api.example.com
http://example.com
https://example.com:8080
```

Even though they may belong to the same organization, the browser treats them as different origins.

### Example

Suppose your React frontend runs at:

```text
http://localhost:5173
```

and your API runs at:

```text
http://localhost:3000
```

They have different ports:

```text
localhost:5173
localhost:3000
```

Therefore:

```text
Different origins
```

---

# 2. Why does CORS exist?

This comes from the browser's **Same-Origin Policy (SOP)**.

SOP is a fundamental browser security boundary.

Imagine you're logged into:

```text
https://bank.com
```

Your browser has your bank session cookie.

Now you visit:

```text
https://evil.com
```

Suppose JavaScript on `evil.com` could freely do:

```javascript
fetch("https://bank.com/account")
```

and read the response.

That could expose your bank account information.

So browsers impose restrictions on cross-origin JavaScript requests.

This is the **Same-Origin Policy**.

CORS provides a controlled exception:

```text
SOP
 ↓
Cross-origin access normally restricted
 ↓
Server explicitly says:
"Requests from this origin are allowed."
 ↓
Browser permits JavaScript to read the response
```

---

# 3. Important distinction: CORS is primarily a browser mechanism

This is one of the most important concepts.

Suppose:

```text
React
http://localhost:5173
        |
        | fetch()
        ↓
API
http://localhost:3000
```

The browser evaluates the CORS policy.

But if you use:

```bash
curl http://localhost:3000/api/users
```

CORS does not stop you.

Similarly:

```text
Python requests
Postman
curl
Burp Suite
backend-to-backend requests
```

don't inherently enforce browser CORS rules.

So:

> **CORS is not an API access-control mechanism.**

It does not prevent someone from directly calling your API.

Authentication and authorization still need to be implemented separately.

---

# 4. What exactly happens?

Suppose:

```text
Frontend:
https://app.example.com

API:
https://api.example.com
```

JavaScript:

```javascript
fetch("https://api.example.com/users");
```

The browser sends something like:

```http
GET /users HTTP/1.1
Host: api.example.com
Origin: https://app.example.com
```

The important header is:

```http
Origin: https://app.example.com
```

The server might respond:

```http
HTTP/1.1 200 OK
Access-Control-Allow-Origin: https://app.example.com
```

The browser sees:

```text
Request Origin:
https://app.example.com

Allowed Origin:
https://app.example.com

MATCH
```

Therefore JavaScript is allowed to access the response.

---

# 5. What if the server doesn't allow it?

Suppose the server responds:

```http
HTTP/1.1 200 OK
```

but does not provide the appropriate CORS header.

The request may actually reach the server and the server may even process it.

But the browser prevents JavaScript from accessing the response.

Conceptually:

```text
Browser
   |
   | GET /users
   ↓
Server
   |
   | 200 OK
   ↓
Browser
   |
   X
JavaScript cannot read response
```

This distinction is extremely important.

CORS doesn't necessarily mean:

> "The request never reached the server."

It often means:

> "The browser refuses to expose the response to the requesting JavaScript."

---

# 6. The main CORS headers

You should know these extremely well.

## `Access-Control-Allow-Origin`

Specifies which origins may access the resource.

Example:

```http
Access-Control-Allow-Origin: https://app.example.com
```

Or:

```http
Access-Control-Allow-Origin: *
```

The wildcard means broadly:

```text
Any origin
```

But there are important restrictions when credentials are involved.

---

## `Access-Control-Allow-Methods`

Specifies allowed HTTP methods.

```http
Access-Control-Allow-Methods: GET, POST, PUT, DELETE
```

---

## `Access-Control-Allow-Headers`

Specifies which request headers the browser is allowed to send in a CORS request.

Example:

```http
Access-Control-Allow-Headers: Content-Type, Authorization
```

This becomes important with requests such as:

```javascript
fetch(url, {
    headers: {
        "Authorization": "Bearer token",
        "Content-Type": "application/json"
    }
});
```

---

## `Access-Control-Allow-Credentials`

Controls whether credentials can be included in a cross-origin request.

```http
Access-Control-Allow-Credentials: true
```

Credentials can include things such as:

```text
Cookies
HTTP authentication
TLS client certificates
```

---

## `Access-Control-Expose-Headers`

By default, JavaScript cannot access every response header.

The server can explicitly expose additional headers:

```http
Access-Control-Expose-Headers: X-Request-ID, X-RateLimit-Remaining
```

Then JavaScript can access them.

---

## `Access-Control-Max-Age`

Tells the browser how long it can cache the result of a preflight request.

```http
Access-Control-Max-Age: 3600
```

Meaning approximately:

```text
Cache preflight result for 3600 seconds
```

---

# 7. Simple requests vs preflighted requests

This is where CORS becomes much more interesting.

Not every cross-origin request requires a preflight.

There are broadly two cases:

```text
Cross-origin request
       |
       +---- Simple request
       |
       +---- Preflighted request
```

---

# 8. Simple request

A request can qualify as a **CORS-safelisted request** when it meets specific conditions around method, headers, and content type.

Typical methods:

```text
GET
HEAD
POST
```

For example:

```javascript
fetch("https://api.example.com/users");
```

Browser can directly send:

```http
GET /users HTTP/1.1
Origin: https://app.example.com
```

Server:

```http
Access-Control-Allow-Origin: https://app.example.com
```

No `OPTIONS` request is necessary.

---

# 9. Preflight request

Now imagine:

```javascript
fetch("https://api.example.com/users", {
    method: "DELETE",
    headers: {
        "Authorization": "Bearer abc123"
    }
});
```

The browser may first ask the server:

> "If I send a DELETE request from this origin with this header, will you allow it?"

It sends:

```http
OPTIONS /users HTTP/1.1
Host: api.example.com
Origin: https://app.example.com
Access-Control-Request-Method: DELETE
Access-Control-Request-Headers: authorization
```

This is the **preflight request**.

---

# 10. Server's preflight response

The server responds:

```http
HTTP/1.1 204 No Content

Access-Control-Allow-Origin: https://app.example.com
Access-Control-Allow-Methods: GET, POST, DELETE
Access-Control-Allow-Headers: Authorization
```

Browser checks:

```text
Origin allowed?
        ↓
YES

DELETE allowed?
        ↓
YES

Authorization header allowed?
        ↓
YES
```

Then:

```text
Browser
   |
   | actual DELETE
   ↓
Server
```

---

# 11. Why `OPTIONS`?

`OPTIONS` is an HTTP method used for querying supported communication options.

For CORS, browsers use it as the **preflight mechanism**.

So when you see:

```http
OPTIONS /api/users
```

in Burp or DevTools, don't immediately assume the application itself is doing something strange.

It may simply be the browser performing CORS preflight.

---

# 12. A complete flow

Suppose:

```text
Frontend
https://app.example.com

Backend
https://api.example.com
```

Frontend:

```javascript
fetch("https://api.example.com/users", {
    method: "POST",
    headers: {
        "Content-Type": "application/json",
        "Authorization": "Bearer xyz"
    },
    body: JSON.stringify({
        name: "Alice"
    })
});
```

Browser:

```text
                OPTIONS
Frontend --------------------> API
           preflight

       <---------------------
       CORS permissions

                POST
Frontend --------------------> API

       <---------------------
             response
```

This is the mental model you should remember.

---

# 13. Credentials make CORS more sensitive

Consider:

```javascript
fetch("https://api.example.com/profile", {
    credentials: "include"
});
```

This tells the browser to include credentials such as cookies where applicable.

The server needs:

```http
Access-Control-Allow-Credentials: true
```

And the server generally cannot respond with:

```http
Access-Control-Allow-Origin: *
```

for a credentialed CORS response.

Instead, it needs a specific origin, such as:

```http
Access-Control-Allow-Origin: https://app.example.com
Access-Control-Allow-Credentials: true
```

This is a crucial security distinction.

---

# 14. The classic dangerous CORS mistake

Imagine a server does this:

```javascript
const origin = req.headers.origin;

res.setHeader(
    "Access-Control-Allow-Origin",
    origin
);
```

It essentially says:

```text
Whatever Origin you send,
I'll allow it.
```

An attacker could host:

```text
https://evil.example
```

and make requests to your API.

If the API also supports credentials and the configuration is otherwise permissive, this can become a serious cross-origin data exposure issue.

---

# 15. Another common mistake

Bad:

```http
Access-Control-Allow-Origin: *
Access-Control-Allow-Credentials: true
```

This combination is not valid for credentialed CORS responses.

Instead, use an explicit allowlist:

```text
https://app.example.com
https://admin.example.com
```

---

# 16. Origin reflection

A particularly important vulnerability pattern is:

```text
Request:

Origin: https://attacker.example

Server:

Access-Control-Allow-Origin:
https://attacker.example
```

If the server blindly reflects the supplied `Origin`, it has effectively converted:

```text
Origin supplied by attacker
        ↓
Origin trusted by server
```

This is why CORS configuration should use an **allowlist**, not blind reflection.

For example:

```javascript
const allowedOrigins = [
    "https://app.example.com",
    "https://admin.example.com"
];
```

Then:

```text
incoming Origin
       |
       ↓
Is it in allowlist?
       |
   +---+---+
   |       |
  YES      NO
   |       |
allow     reject
```

---

# 17. CORS is not authentication

This is another interview-level distinction.

Bad reasoning:

> "Only my frontend can call the API because CORS allows only my frontend."

No.

An attacker can bypass browser CORS enforcement with:

```bash
curl
```

or:

```text
Burp Suite
Postman
Python
custom HTTP client
```

So your API must still enforce:

```text
Authentication
Authorization
Input validation
CSRF protection where applicable
Rate limiting
etc.
```

CORS is primarily about **which browser origins can read cross-origin responses**.

---

# 18. CORS vs CSRF

These are often confused.

### CORS

Concern:

> Can JavaScript from another origin read a cross-origin response?

### CSRF

Concern:

> Can an attacker cause a victim's browser to perform an authenticated action against another site?

For example:

```text
Victim logged into bank.com
        |
        ↓
Visits evil.com
        |
        ↓
evil.com causes request to bank.com
```

Cookies may automatically accompany certain requests depending on cookie attributes and browser behavior.

CORS does not replace CSRF defenses.

Typical CSRF defenses include:

```text
SameSite cookies
CSRF tokens
Origin/Referer validation
appropriate request design
```

---

# 19. CORS vs SOP

Think of the relationship like this:

```text
Same-Origin Policy
        |
        | browser security boundary
        ↓
Cross-origin access restricted
        |
        ↓
CORS
        |
        | controlled exception
        ↓
Server explicitly permits
specific cross-origin access
```

So:

**SOP is the security boundary.**

**CORS is the mechanism for controlled cross-origin resource sharing.**

---

# 20. CORS in a MERN application

This is especially relevant to you.

Suppose:

```text
React/Vite
localhost:5173

Express
localhost:5000
```

Your browser sees:

```text
localhost:5173
       ≠
localhost:5000
```

So you configure Express.

For example:

```javascript
import cors from "cors";

app.use(cors({
    origin: "http://localhost:5173"
}));
```

Now the backend can respond with an appropriate CORS header for that origin.

For multiple origins:

```javascript
const allowedOrigins = [
    "http://localhost:5173",
    "https://app.example.com"
];

app.use(cors({
    origin: allowedOrigins
}));
```

In production, you should generally use an explicit allowlist appropriate to your deployment rather than:

```javascript
origin: "*"
```

especially where authenticated browser requests are involved.

---

# 21. Debugging CORS

When you encounter:

```text
Access to fetch at ...
has been blocked by CORS policy
```

Don't randomly change headers.

Open:

```text
Browser DevTools
    ↓
Network
```

Inspect:

```text
Request Headers
Response Headers
```

Look for:

```http
Origin
Access-Control-Allow-Origin
Access-Control-Allow-Methods
Access-Control-Allow-Headers
Access-Control-Allow-Credentials
```

If preflight is involved, inspect the:

```http
OPTIONS
```

request.

---

# 22. Security testing CORS

From a product security perspective, test:

### Test 1: Trusted origin

```http
Origin: https://app.example.com
```

Expected:

```http
Access-Control-Allow-Origin: https://app.example.com
```

### Test 2: Untrusted origin

```http
Origin: https://evil.example
```

Expected:

```text
No authorization for that origin
```

### Test 3: Origin reflection

Try:

```http
Origin: https://attacker.example
```

Check whether the response blindly returns:

```http
Access-Control-Allow-Origin: https://attacker.example
```

### Test 4: Credentials

Check whether sensitive authenticated endpoints return something equivalent to:

```http
Access-Control-Allow-Origin: *
Access-Control-Allow-Credentials: true
```

or otherwise have an overly permissive credentialed configuration.

### Test 5: Preflight

Send:

```http
OPTIONS /api/user HTTP/1.1
Origin: https://attacker.example
Access-Control-Request-Method: DELETE
Access-Control-Request-Headers: Authorization
```

Then inspect the response.

---

# 23. CORS misconfiguration hierarchy

When assessing CORS, don't just ask:

> "Is CORS enabled?"

Ask:

```text
1. Which origins are trusted?
             ↓
2. How are origins validated?
             ↓
3. Which methods are allowed?
             ↓
4. Which headers are allowed?
             ↓
5. Are credentials allowed?
             ↓
6. Which response headers are exposed?
             ↓
7. Which endpoints contain sensitive data?
             ↓
8. Is the configuration different across environments?
```

This is much closer to how a product security engineer should reason about CORS.

---

# 24. The mental model I want you to retain

If you remember only one diagram, remember this:

```text
                  Browser
                     |
                     |
        Same-Origin Policy
                     |
             Cross-origin request
                     |
              Is it simple?
              /           \
            YES            NO
             |              |
         actual          OPTIONS
         request         preflight
             |              |
             |        Server evaluates
             |         CORS policy
             |              |
             +-------> permission
                            |
                     Actual request
                            |
                         Response
                            |
                    CORS response headers
                            |
                 Browser checks permission
                       /          \
                     YES           NO
                      |             |
             JS gets response   JS blocked
```

And the security principle is:

> **CORS should be treated as a browser-side cross-origin access policy, not as an authentication or authorization boundary.**

For a cybersecurity/product-security interview, that distinction is particularly important.

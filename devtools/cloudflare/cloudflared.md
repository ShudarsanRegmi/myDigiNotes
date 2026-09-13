# Cloudflare Tunnel on Linux

## 1. What is Cloudflare Tunnel?

Cloudflare Tunnel allows a service running on your machine to be exposed through Cloudflare without directly exposing your machine's public IP and without opening an inbound port on your router/firewall.

Basic architecture:

```text
                         Internet
                            |
                            v
                    +---------------+
                    |   Cloudflare  |
                    | Edge Network  |
                    +-------+-------+
                            |
                    Encrypted tunnel
                            |
                            v
                    +---------------+
                    |  cloudflared  |
                    |    Linux      |
                    +-------+-------+
                            |
                            v
                    localhost:8888
```

The local machine establishes an outbound connection to Cloudflare.

Therefore, you generally do not need:

```text
Port forwarding
Inbound port 8888
Public IP exposure
```

---

# 2. Install cloudflared

## Debian / Ubuntu

```bash
sudo apt update
sudo apt install cloudflared
```

Verify:

```bash
cloudflared --version
```

If the package is unavailable or you need a newer release, install the current package from Cloudflare's official distribution.

---

# 3. Main Tunnel Types

There are two concepts you should distinguish:

```text
Quick Tunnel
Named Tunnel
```

They solve different problems.

## Quick Tunnel

Command:

```bash
cloudflared tunnel --url http://localhost:8888
```

Cloudflare generates a temporary hostname such as:

```text
https://random-name.trycloudflare.com
```

Architecture:

```text
cloudflared
     |
     v
Quick Tunnel
     |
     v
random-name.trycloudflare.com
```

Characteristics:

* No Cloudflare account required
* Random `trycloudflare.com` hostname
* Intended for testing/development
* No uptime guarantee
* Hostname is not something you should build a persistent service around
* Restarting the Quick Tunnel can produce another hostname

Use it for:

```text
Temporary demos
Development
Testing webhooks
Quick experiments
```

Example:

```bash
cloudflared tunnel --url http://localhost:8888
```

---

# 4. Quick Tunnel Lifetime

A Quick Tunnel should be considered ephemeral.

Do not design your system around:

```text
random-name.trycloudflare.com
```

remaining valid indefinitely.

For a 24 to 36 hour requirement, a named tunnel is the better architecture.

Also remember:

```text
Quick Tunnel process stops
        |
        v
Tunnel stops
```

You can use `systemd`, `tmux`, or another supervisor to keep the process alive, but that does not turn the Quick Tunnel into a persistent named tunnel.

---

# 5. Named Tunnel

A named tunnel is a persistent tunnel object associated with your Cloudflare account.

Conceptually:

```text
Cloudflare account
       |
       +-- Named Tunnel: my-server
                    |
                    v
              cloudflared
                    |
                    v
             localhost:8888
```

Unlike a Quick Tunnel, the tunnel has a persistent identity.

A named tunnel is suitable for:

```text
Long-running services
Stable hostnames
24/7 services
24-36 hour sessions
Production-like deployments
```

---

# 6. Creating a Named Tunnel

Authenticate `cloudflared`:

```bash
cloudflared tunnel login
```

This opens a browser authentication flow.

After authentication, check:

```bash
ls -la ~/.cloudflared/
```

You will normally have Cloudflare credentials in this directory.

Create a tunnel:

```bash
cloudflared tunnel create my-server
```

Example output:

```text
Created tunnel my-server
Tunnel ID: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

List tunnels:

```bash
cloudflared tunnel list
```

Example:

```text
NAME         ID
my-server    xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

---

# 7. Tunnel Credentials

When a tunnel is created, `cloudflared` creates credentials for that tunnel.

Typically:

```text
~/.cloudflared/
```

contains something similar to:

```text
cert.pem
xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.json
```

Protect these files.

In particular, the tunnel credential file should not be committed to Git.

Add:

```gitignore
.cloudflare/
*.json
```

according to your project's structure.

---

# 8. Configure a Named Tunnel

Create:

```bash
nano ~/.cloudflared/config.yml
```

Example:

```yaml
tunnel: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx

credentials-file: /home/YOUR_USER/.cloudflared/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.json

ingress:
  - hostname: app.example.com
    service: http://localhost:8888

  - service: http_status:404
```

The final rule:

```yaml
- service: http_status:404
```

is important because it acts as the catch-all rule.

---

# 9. Validate the Configuration

Run:

```bash
cloudflared tunnel ingress validate
```

You can also inspect how a request will be routed:

```bash
cloudflared tunnel ingress rule https://app.example.com
```

---

# 10. Create DNS Routing

For:

```text
app.example.com
```

run:

```bash
cloudflared tunnel route dns my-server app.example.com
```

This creates the appropriate DNS routing to the tunnel.

Now the traffic path is:

```text
https://app.example.com
          |
          v
      Cloudflare
          |
          v
     my-server
       tunnel
          |
          v
    cloudflared
          |
          v
localhost:8888
```

---

# 11. Run the Named Tunnel

Run:

```bash
cloudflared tunnel run my-server
```

If you use `config.yml`, `cloudflared` reads the configuration and forwards:

```text
app.example.com
       |
       v
localhost:8888
```

You can explicitly specify the config:

```bash
cloudflared tunnel --config ~/.cloudflared/config.yml run my-server
```

---

# 12. Token-Based Named Tunnel

Cloudflare also supports remotely managed tunnels using a tunnel token.

You may see a command like:

```bash
cloudflared tunnel run --token eyJ...
```

The token identifies and authenticates the connector to the Cloudflare-managed tunnel.

Do not publish the token.

Treat it approximately like a secret:

```text
TOKEN = SECRET
```

If somebody obtains it, they may be able to run a connector for your tunnel.

---

# 13. `service install` and systemd

For long-running tunnels, use `systemd`.

If Cloudflare gives you a token:

```bash
sudo cloudflared service install <TUNNEL_TOKEN>
```

Then:

```bash
sudo systemctl enable cloudflared
sudo systemctl start cloudflared
```

Check:

```bash
systemctl status cloudflared
```

Follow logs:

```bash
journalctl -u cloudflared -f
```

View recent logs:

```bash
journalctl -u cloudflared --since "1 hour ago"
```

Restart:

```bash
sudo systemctl restart cloudflared
```

Stop:

```bash
sudo systemctl stop cloudflared
```

Disable automatic startup:

```bash
sudo systemctl disable cloudflared
```

---

# 14. Why systemd is Useful

Running manually:

```bash
cloudflared tunnel run my-server
```

means:

```text
Terminal
   |
   v
cloudflared
```

Close the terminal and the process may terminate.

With systemd:

```text
Linux boot
   |
   v
systemd
   |
   v
cloudflared
   |
   v
Cloudflare
```

The service can automatically restart after failures.

Check:

```bash
systemctl status cloudflared
```

---

# 15. Cleaning an Existing cloudflared Service

If another administrator previously installed `cloudflared`, you may see:

```text
cloudflared service is already installed
```

Stop it:

```bash
sudo systemctl stop cloudflared
```

Disable it:

```bash
sudo systemctl disable cloudflared
```

Uninstall the service:

```bash
sudo cloudflared service uninstall
```

Reload systemd:

```bash
sudo systemctl daemon-reload
```

Check:

```bash
systemctl status cloudflared
```

Check for remaining processes:

```bash
ps aux | grep '[c]loudflared'
```

If you intentionally want to terminate every remaining `cloudflared` process:

```bash
sudo pkill cloudflared
```

Then:

```bash
ps aux | grep '[c]loudflared'
```

---

# 16. Do Not Confuse Local Cleanup With Cloudflare Cleanup

Removing:

```text
/etc/systemd/system/cloudflared.service
```

does not necessarily delete the tunnel from your Cloudflare account.

Think of them separately:

```text
LOCAL MACHINE
-------------
cloudflared process
systemd service
config.yml
credentials


CLOUDFLARE
----------
Tunnel object
DNS routes
Hostname
Access policies
```

Deleting the local service does not automatically mean:

```text
Cloudflare tunnel deleted
```

---

# 17. Ephemeral Random Hostnames With a Named Tunnel

Suppose you want:

```text
Session 1:
abc123.example.com

Session 2:
91kx7q.example.com

Session 3:
p7m29a.example.com
```

but all sessions should ultimately reach:

```text
localhost:8888
```

A wildcard hostname can be useful:

```text
*.example.com
```

Architecture:

```text
abc123.example.com
       |
       +----------------+
                        |
91kx7q.example.com     |
       |                |
       +-------> Cloudflare
                        |
                        v
                   Named Tunnel
                        |
                        v
                 localhost:8888
```

The tunnel remains stable.

Only the hostname changes.

---

# 18. Wildcard DNS Concept

You can configure a wildcard record such as:

```text
*.example.com
```

Then:

```text
abc123.example.com
hello.example.com
session42.example.com
```

can all resolve through the same Cloudflare routing configuration.

This is useful when an application needs dynamically generated hostnames.

However:

```text
Random hostname != authentication
```

A random URL is merely difficult to guess.

It should not be treated as a security boundary.

For sensitive applications, add authentication.

---

# 19. 36-Hour Ephemeral Session Architecture

For a session-oriented application, a good architecture is:

```text
                    Cloudflare
                        |
                        v
              *.example.com
                        |
                        v
                Named Tunnel
                        |
                        v
                  cloudflared
                        |
                        v
                localhost:8888
                        |
                        v
                  Your service
```

Your application generates:

```text
session_id = random_string()
```

For example:

```text
7f91a2
```

and exposes:

```text
https://7f91a2.example.com
```

After 36 hours:

```text
session expires
       |
       v
hostname becomes invalid
       |
       v
session terminated
```

The tunnel itself does not need to be destroyed.

---

# 20. Quick Tunnel vs Named Tunnel

| Property                   | Quick Tunnel               | Named Tunnel              |
| -------------------------- | -------------------------- | ------------------------- |
| Cloudflare account         | Not required               | Required                  |
| Hostname                   | Random `trycloudflare.com` | Your domain               |
| Persistent tunnel identity | No                         | Yes                       |
| Stable hostname            | No                         | Yes                       |
| Suitable for production    | No                         | Yes                       |
| 24-36 hour service         | Not ideal                  | Recommended               |
| Custom DNS                 | No                         | Yes                       |
| systemd deployment         | Possible but not ideal     | Recommended               |
| Wildcard hostnames         | No                         | Yes                       |
| Authentication integration | Limited                    | Full Cloudflare ecosystem |
| IP hidden from visitors    | Yes                        | Yes                       |

---

# 21. Checking Tunnel Status

List tunnels:

```bash
cloudflared tunnel list
```

Inspect a tunnel:

```bash
cloudflared tunnel info my-server
```

Check service:

```bash
systemctl status cloudflared
```

Check logs:

```bash
journalctl -u cloudflared -f
```

---

# 22. Useful Diagnostics

Check cloudflared:

```bash
cloudflared --version
```

Check configuration:

```bash
cloudflared tunnel ingress validate
```

Check DNS:

```bash
dig app.example.com
```

Test the local service:

```bash
curl http://localhost:8888
```

Test the public endpoint:

```bash
curl https://app.example.com
```

Check listening ports:

```bash
ss -lntp
```

Check cloudflared processes:

```bash
ps aux | grep '[c]loudflared'
```

---

# 23. QUIC vs HTTP/2

`cloudflared` commonly uses QUIC:

```text
cloudflared
     |
     | QUIC / UDP
     v
Cloudflare
```

If the network has problems with UDP or aggressively expires idle UDP connections, you can test HTTP/2:

```bash
cloudflared tunnel --protocol http2 run my-server
```

For a Quick Tunnel:

```bash
cloudflared tunnel --protocol http2 --url http://localhost:8888
```

If QUIC repeatedly reports errors such as:

```text
timeout: no recent network activity
```

testing HTTP/2 is worthwhile.

---

# 24. QUIC Receive Buffer Warning

You may encounter:

```text
failed to sufficiently increase receive buffer size
```

Check:

```bash
sysctl net.core.rmem_max
sysctl net.core.rmem_default
```

You can increase the maximum receive buffer:

```bash
sudo tee /etc/sysctl.d/98-cloudflared.conf <<'EOF'
net.core.rmem_max=2500000
EOF
```

Apply:

```bash
sudo sysctl --system
```

Verify:

```bash
sysctl net.core.rmem_max
```

This warning is separate from the conceptual distinction between Quick and Named Tunnels.

---

# 25. Monitoring

For a long-running tunnel:

```bash
systemctl status cloudflared
```

and:

```bash
journalctl -u cloudflared -f
```

are your first troubleshooting tools.

Look for:

```text
Registered tunnel connection
```

which indicates that a connector successfully established a connection to Cloudflare.

If you see:

```text
timeout: no recent network activity
```

investigate the underlying network connection, especially if it happens repeatedly.

---

# 26. Security

## Never expose tunnel credentials

Do not commit:

```text
cert.pem
*.json
```

or tunnel tokens to Git.

Bad:

```bash
git add ~/.cloudflared/
```

Bad:

```text
TOKEN=eyJ...   # posted publicly
```

Good:

```text
Keep credentials on the machine
Use environment/secret management
Rotate leaked credentials
```

---

# 27. Random URLs Are Not Authentication

This:

```text
https://8f91ab.example.com
```

is not equivalent to:

```text
Authentication
Authorization
Access control
```

Anyone possessing the URL may potentially access the service.

For a sensitive application:

```text
Random URL
    +
Authentication
    +
Authorization
    +
Session expiration
```

is much stronger.

---

# 28. Recommended Setup for a 24-36 Hour Session

For your specific requirement:

```text
                    Internet
                       |
                       v
               Cloudflare Edge
                       |
                       v
             Random hostname
          abc123.example.com
                       |
                       v
               Named Tunnel
                       |
                       v
                cloudflared
                  systemd
                       |
                       v
               localhost:8888
```

Recommended properties:

```text
Named Tunnel             YES
Custom domain             YES
Wildcard hostname         YES, if dynamic URLs are required
systemd                   YES
Quick Tunnel              NO
Port forwarding           NO
Public port 8888          NO
Random hostname           YES, if desired
Application authentication YES
```

---

# 29. Minimal Commands Cheat Sheet

## Quick Tunnel

```bash
cloudflared tunnel --url http://localhost:8888
```

## Login

```bash
cloudflared tunnel login
```

## Create named tunnel

```bash
cloudflared tunnel create my-server
```

## List tunnels

```bash
cloudflared tunnel list
```

## Run named tunnel

```bash
cloudflared tunnel run my-server
```

## Route DNS

```bash
cloudflared tunnel route dns my-server app.example.com
```

## Validate ingress

```bash
cloudflared tunnel ingress validate
```

## Inspect tunnel

```bash
cloudflared tunnel info my-server
```

## Install systemd service using token

```bash
sudo cloudflared service install <TUNNEL_TOKEN>
```

## Start

```bash
sudo systemctl start cloudflared
```

## Enable at boot

```bash
sudo systemctl enable cloudflared
```

## Status

```bash
systemctl status cloudflared
```

## Logs

```bash
journalctl -u cloudflared -f
```

## Restart

```bash
sudo systemctl restart cloudflared
```

## Stop

```bash
sudo systemctl stop cloudflared
```

## Disable

```bash
sudo systemctl disable cloudflared
```

## Remove systemd service

```bash
sudo cloudflared service uninstall
```

## Kill manually running processes

```bash
sudo pkill cloudflared
```

---

# 30. Mental Model

The easiest way to remember everything is:

```text
QUICK TUNNEL

cloudflared
    |
    +----> random.trycloudflare.com

Temporary
Random
Testing
No stable hostname
```

versus:

```text
NAMED TUNNEL

Your domain
    |
    v
Cloudflare
    |
    v
Named Tunnel
    |
    v
cloudflared
    |
    v
localhost:8888

Persistent
Configurable
Stable
Suitable for long-running services
```

And if you want ephemeral sessions:

```text
NAMED TUNNEL
     |
     +---- *.example.com
              |
              +---- abc123.example.com
              |
              +---- 91kx7q.example.com
              |
              +---- p7m29a.example.com
```

The **session URL can be ephemeral while the underlying tunnel remains persistent**.

That is generally the cleanest architecture when you need a new random public URL for each 24-36 hour session without exposing your machine's IP.

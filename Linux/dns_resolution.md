# Understanding DNS Resolution in Linux Systems

### Using D-Bus to Make DNS Calls
```bash
dbus-send --system --print-reply \
    --dest=org.freedesktop.resolve1 \
    /org/freedesktop/resolve1 \
    org.freedesktop.resolve1.Manager.ResolveHostname \
    int32:0 string:"example.com" int32:2 uint64:0
```

### **Summary Table**
| Method | How It Works | Pros | Cons |
|--------|-------------|------|------|
| **D-Bus API (`pydbus`)** | Calls `systemd-resolved` directly | ✅ Asynchronous, DNSSEC support, rich features | ❌ Requires D-Bus |
| **glibc `getaddrinfo()`** | Standard C API for name resolution | ✅ Cross-platform, widely used | ❌ No DNSSEC validation, requires `nss-resolve` |
| **Local DNS Stub (127.0.0.53)** | Sends DNS queries to `systemd-resolved` | ✅ Works with legacy applications | ❌ No DNSSEC, missing advanced features |

### **Conclusion**
- Use **D-Bus API** if your application needs **advanced features** like **DNSSEC validation**.
- Use **`getaddrinfo()`** for standard compatibility with most platforms.
- Use **the DNS stub (`127.0.0.53`)** as a **fallback** for older applications.

### Checking System-Wide DNS Configuration
```bash
resolvectl status
```

### `/etc/resolv.conf`

![image](https://github.com/user-attachments/assets/88c65a9f-d351-4ad0-8c96-0ed34f946092)

```bash
lrwxrwxrwx 1 root root 37 Feb 13 16:12 /etc/resolv.conf -> /run/systemd/resolve/stub-resolv.conf
```

## Different Ways of Making DNS Queries in Linux

### Using `resolvectl`
```bash
resolvectl query google.com
```

### Using `dig` Command
```bash
dig google.com
dig @8.8.8.8 google.com # Querying a specific DNS server
```

### Using `nslookup`
```bash
nslookup google.com
nslookup google.com 8.8.8.8 # Mentioning a specific DNS server
```

### Preventing `resolv.conf` from Changing
```bash
sudo chattr +i /etc/resolv.conf
```

### Manually Setting Up DNS Server in `/etc/systemd/resolved.conf`
```ini
[Resolve]
DNS=8.8.8.8 1.1.1.1
FallbackDNS=9.9.9.9
```

### Restarting `systemd-resolved`
```bash
sudo systemctl restart systemd-resolved
```

### Flushing DNS Cache
```bash
sudo systemd-resolve --flush-caches
```

## Other Miscellaneous Commands to Explore DNS Servers

### Confirming if a Server is a DNS Server
```bash
nslookup ch.amrita.edu 172.19.18.2
host google.com 172.19.18.2
```

### Viewing DNS Server Logs
```bash
journalctl -u systemd-resolved --follow  # If using systemd-resolved
```

## Verifying the Existence of Stub Server `127.0.0.53:53`

### Capturing DNS Traffic on Port 53
```bash
sudo tcpdump -i lo -n port 53
```

### Making DNS Queries Using `nslookup`
```bash
nslookup google.com
```
![image](https://github.com/user-attachments/assets/3eef1211-59ce-4f38-9c28-1396c91625d6)

### Watching Live DNS Statistics Using `resolvectl`
```bash
watch resolvectl statistics
```

![image](https://github.com/user-attachments/assets/de7e7dc9-7e1b-43c0-bb4a-ddb12f9792a3)

## More Interesting Features from `resolvectl`

### Show Active DNS for a Given Interface
```bash
resolvectl dns wlp2s0
```

### Show Current DNS Search Domains
```bash
resolvectl domain wlp2s0
```

### Flushing DNS Caches
```bash
sudo resolvectl flush-caches
```

> `systemd-resolved` stores DNS cache in memory (RAM), meaning it is not written to disk. The cache is volatile and disappears when `systemd-resolved` restarts.

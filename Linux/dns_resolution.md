# Understanding DNS Resolution in Linux Systems


### Using gdus to make dns calls
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

### Checking systemwise DNS configuraiotn
```bash
resolvectl status
```

### /etc/resolve.conf

![image](https://github.com/user-attachments/assets/88c65a9f-d351-4ad0-8c96-0ed34f946092)


```
lrwxrwxrwx 1 root root 37 Feb 13 16:12 /etc/resolv.conf -> /run/systemd/resolve/stub-resolv.conf
```



## Different ways of making dns queries in linux

### Using resolvectl
```bash
 resolvectl query google.com
```
### Using dig comamnd
```bash
dig google.com
dig @8.8.8.8 google.com # querying a specific dns server
```


### Making the resolv.conf not to change
```bash
sudo chattr +i /etc/resolv.conf
```

### Manually setting up dns server in /etc/systemd/resolved.conf

```bash
[Resolve]
DNS=8.8.8.8 1.1.1.1
FallbackDNS=9.9.9.9
```

### Restarting systemd-service
```bash
sudo systemctl restart systemd-resolved
```

### Flushing DNS cache
```bash
sudo systemd-resolve --flush-caches
```

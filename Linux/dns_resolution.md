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

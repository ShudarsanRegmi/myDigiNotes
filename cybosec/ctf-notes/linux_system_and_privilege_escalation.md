# Linux System and Privilege Escalation

- An extreme example of the latter would be an admin setting vim to SUID with owner root, allowing users to execute bash commands as root within a vim session (:![shell command])

### Finding Binary with SUID bit set
```bash
find / -user root -perm -4000 2>/dev/null
```
# Tools
[GTFOBins for linux privilege escalation](https://gtfobins.github.io/gtfobins/hping3/)


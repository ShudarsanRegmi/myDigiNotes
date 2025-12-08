## SSH Tunelling

**A proper usecase of ssh tunelling**

 > You've ssh to a user to a remote host. The server is running some service internally. But the firewall blocks the port. So, there is no way to connect client from your system to that service. In this case ssh tunelling can be used to route the request to a port in your local system to another port in remote system.


> An example is illustrated below. You're running mongodb in your server. But mongodb port is not allowed by firewal. Use ssh to route teh traffic on port 27017(or 27018 as shown below) to the mongodb port in remote system(27017)

```bash
ssh -L 27018:localhost:27017 user@server-ip
ssh -L localport:localhost:serverport user@server
```


****
```bash
mongodb://mongoadmin:secret@localhost:27018
```

## Creating a socks proxy
```bash
ssh -D 1080 -C -N user@host
```
 > This command cna be used to create a socks proxy. Configuring system to proxy the trafic thorugh this socks proxy will effectively encrypt the traffic and routes it to the server. Effectively acting as a VPN Tunnel.

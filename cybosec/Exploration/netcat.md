# Exploring the TCP/IP swiss army knife

## Setting up the listener
```bash
netcat -nvlp 8080
# -n -> don't perform DNS resolution
```

## Sending request from different servers using clients for different protocols

**Setting up the listener on 22 port SSH**
```bash
sudo netcat -nvlp 8080
```

**Making connection request from SSH client**
```bash
ssh user@localhost
```

![image](https://github.com/user-attachments/assets/6bb90f6f-ff78-4613-a681-4f4acfa5e050)

### Making mysql connection request

**Setting mysql server**
```bash
sudo netcat -nvlp 3306
```

**Sending the connection request from client**
```bash
mysql -h 127.0.0.1 -u someuser -p
# -h option forces for using TCP requeset instead of unix sockets
```

![image](https://github.com/user-attachments/assets/eb5f0120-dbbd-4367-bce1-6551445dae97)

### Making netcat as HTTP server and manually writing HTTP responses

**Setting up the http server**
```bash
netcat -nvlp 8080
```
**Sending HTTP request using curl**
```bash
curl -v localhost:8080
```
**Manually writing HTTP response**
```
HTTP/1.1 200 OK
Content-Length: 13
type: text/plain

Hello, World!
```

![image](https://github.com/user-attachments/assets/77129986-f170-40fa-91cc-38ec8f0c8db1)



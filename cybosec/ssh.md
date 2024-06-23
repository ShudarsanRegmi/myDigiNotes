# SSH and OpenSSH


# How connection is initiated

- Client uses ephemeral port number to the server to connect to port number 22.
- Server can accept multiple connections at the same port number 22 while identifying each of the tcp connections by something known as socket. Socket is identified by (server_ip:server_port -- client_ip:client_port)
- All key exchanges and communications happens on the same socket. Unlike FTP, it doesn't open any other port for exchanging data.
- 

-  Host keys are crucial for establishing secure connections, as they are used to identify the server to the client and to encrypt the communication between the client and the server.

ssh-keygen
  ○ Generates new key pair
● ssh-copy-id
  ○ Copies your public key to remote server
● ssh-add
  ○ Adds a private key to the list of keys that
ssh will try to connect to remote servers
with by default


## Local Port Forwarding

### Usecase: Accessing the database server on another network by making ssh connection to a host on that network
```bash
ssh -L 3307:db.example.com:3306 user@bastion.example.com
```
-L 3307:db.example.com:3306: Sets up local port forwarding. It forwards traffic from port 3307 on your local machine to port 3306 on db.example.com through bastion.example.com.
After establishing the SSH tunnel, you can connect to the remote database as if it were running on your local machine on port 3307.
** For example using the mysql client**
```bash
mysql -h 127.0.0.1 -P 3307 -u dbuser -p
```
![image](https://github.com/ShudarsanRegmi/myDigiNotes/assets/65646203/9e86fbdc-2df4-468a-b820-97a6821d420c)
dIn local port forwarding, the forwarding starts from the local machine, and in remote port forwarding, the forwarding starts from the remote machine.arsanRegmi/myDigiNotes/assets/65646203/9e86fbdc-2df4-468a-b820-97a6821d420c)
Local Port Forwarding

** This technique can be used to**
- Accessing internal api
- Accessing web application that is only accessible to local network
- Accessing the remote databse

  ### Local Port Forwarding Vs. Remote Port Forwarding
  **Local port forwarding** allows you to forward a port from your local machine (the client) to a port on a remote machine through an SSH connection.

```bash
  ssh -L 5001:api.example.com:5000 user@bastion.example.com
```
Traffic sent to localhost:5001 on your local machine is forwarded through the SSH connection to api.example.com:5000. Hence the name local port forwarding.
**Local Port Forwarding**
```
+------------------+                      +------------------+                      +------------------+
| Local Machine    |                      | SSH Server       |                      | Remote Host      |
| (Your Computer)  |                      | (bastion.example)|                      | (api.example.com)|
|------------------|            In local port forwarding, the forwarding starts from the local machine, and in remote port forwarding, the forwarding starts from the remote machine.          |------------------|                      |------------------|
| localhost:5001 --|---- SSH Tunnel ----> |                  |---- Forward ---->    | port 5000        |
|                  |                      |                  |                      |                  |
+------------------+                      +------------------+                      +------------------+
```

**Remote Port Forwarding**
```
+------------------+                      +------------------+                      +------------------+
| Local Machine    |                      | SSH Server       |                      | Remote Host      |
| (Your Computer)  |                      | (bastion.example)|                      | (your machine)   |
|------------------|                      |------------------|                      |------------------|
|                  |<--- Forward <--------| Remote:5000      |<---- SSH Tunnel ----| localhost:3000   |
|                  |                      |                  |                      |                  |
+------------------+                      +------------------+                      +------------------+
```

In local port forwarding, the forwarding starts from the local machine, and in remote port forwarding, the forwarding starts from the remote machine.


## Remote Port Forwarding

**Traffic sent to bastion.example.com:5000 is forwarded through the SSH connection to localhost:3000 on your local machine.**
```bash
ssh -R 5000:localhost:3000 user@bastion.example.com
```

Usecase: 
If you've a server that is publicly exposed you can use that server to make your local service accessible to the internet. 

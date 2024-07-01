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

### Using SSH tunnel for socks proxy
```bash
 ssh -D 1337 -q -C -N user@ma.ttias.be
# -D = used to create socks proxy -q = Quiet, -C = Compress -N = Do not execute remote commands
```

### Generating ssh public/private key pairs with ssh-keygen
**ssh-keygen** is an openssh key utility

```bash
ssh-keygen -t rsa -b 4096 -C "email@gmail.com"
# -t -> key type( RSA default) 
```
- ssh-keygen can create keys for use by SSH protocol version 2.
- ssh-keygen is also used to generate groups for use in Diffie-Hellman group exchange (DH-GEX).
- ssh-keygen will by default write keys in an OpenSSH-specific format
- 


## ssh-copy-id
ssh-copy-id is a handy utility for securely installing SSH keys(public key) on remote servers. It simplifies the process of adding your SSH public key to a remote server's authorized_keys file, allowing you to authenticate without needing to enter a password each time you connect via SSH.

```bash
ssh-copy-id -i ~/.ssh/my_key.pub user@remote-server
```



### Material to read later
[Differences between known_hosts and authorized_keys file](https://security.stackexchange.com/questions/20706/what-is-the-difference-between-authorized-keys-and-known-hosts-file-for-ssh/20710#20710)

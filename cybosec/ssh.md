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


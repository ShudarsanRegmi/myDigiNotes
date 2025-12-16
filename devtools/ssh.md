## SSH Notes

**Generate the key pairs on client**

```bash
ssh-keygen -t ed25519 -C "comment"
```

**Copy public key to Server**
```bash
ssh-copy-id user@remote_ip # if public key is in CWD

# If mention the public key name explicitly is the n  eed then use below command
ssh-copy-id -i ~/.ssh/mykey.pub user@remote_ip
```

**SSH Hardening**

```bash
sudo vim /etc/ssh/sshd_config
```

**Update the following lines**
```bash
PasswordAuthentication no
PubkeyAuthentication yes
```


**To avoid -i every time you connect**

**Add this entry to `~/.ssh/config`**

```bash
Host lab
  HostName lab
  User labuser
  IdentityFile ~/.ssh/id_lab
```

**Todo: Find way to verfiy password login doesn't work from the same client**

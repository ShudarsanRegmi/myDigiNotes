# Linux User management

### Creating a new user
```bash
sudo useradd <user_name>
```

### Setting up password
```bash
sudo passwd <user_name>
```

### If the home directory is not created by default
```bash
sudo useradd -m username
```
### Adding users to specific groups
```bash
sudo useradd -m -G sudo username
```
### To lock a user account
```bash
sudo usermod -L username
```

### To unlock a user account
```bash
sudo usermod -U username
```
### Deleting a user and their home directory
```bash
sudo userdel -r username
```


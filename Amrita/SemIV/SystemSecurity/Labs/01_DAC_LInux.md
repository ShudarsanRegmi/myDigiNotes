# System Security Lab 1


## Implementing the discretionary access control (DAC) mechanism in operating Systems (Linux)


### Checking for a file Permission
```bash
ls -lah
```

![image](https://github.com/user-attachments/assets/74b66150-9614-472f-902e-260e40d85976)

**No. of hard links **
![image](https://github.com/user-attachments/assets/81eadd76-9e36-4dbd-a76c-f1d4b5d665b4)
>Directories typically have multiple links because of their inherent structure (. and ..), whereas regular files usually have one unless explicitly linked using the ln command.



### Checking for parent directory permission
```bash
ls -ld
```

![image](https://github.com/user-attachments/assets/7218a17c-30cb-4909-82a9-c61621925e31)

## Changing the permission of a file

- u -> Users
- o -> Owner
- g -> Group
- a -> All

### Changing file permissions
```bash
chmod u+x file.txt
```

```bash
chmod g+x file2.txt
```

```bash
chmod o+x file2.txt
chmod o-x file2.txt
chmod o+rwx file.txt
chmod o-rwx file.txt

```

```bash
chmod a-rwx file.txt
```

![image](https://github.com/user-attachments/assets/53319103-cca4-4132-9004-512a729aad22)
![image](https://github.com/user-attachments/assets/78262237-d3da-495d-8524-b794583810ca)

## Using chmod number with permission
```bash
chmod uog file.txt
u = rwx bits (111) = 7
o = rwx bits (111) = 7
g = rwx bits (111) = 7
chmod 777 
```

## Changing permission recursively
```bash
chmod -R uog file.txt
chmod -R 444 file.txt
```


## Changing the Ownership of a file

### Changing the user
```bash
sudo chown user file.txt
```
![image](https://github.com/user-attachments/assets/03559960-3eb8-4181-9140-e63e40ae5745)

### Changing the grop
groups aparichit
```bash
sudo chgrp developers flie.txt
```

### changing both the user and group
```bash
sudo chown user:developers file.txt
```
![image](https://github.com/user-attachments/assets/688e497a-cbb4-40b6-97cf-81a07cb39dc3)

## SUID, SGID and Sticky Bits Summary
![image](https://github.com/user-attachments/assets/706f7515-4d35-4645-8f97-249602429d66)


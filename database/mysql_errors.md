# Handling Different mysql Errors


## Opening Remote connection for the server


**/etc/mysql/mysql.conf.d/mysqld.cnf**

![image](https://github.com/user-attachments/assets/07498935-04ed-4e5d-96e6-b34dee776192)

```
bind-address            = 0.0.0.0
```


**Created a new user and gave the privilege**
![image](https://github.com/user-attachments/assets/1e022106-03d2-4944-ac84-2093f1b397bf)

```
CREATE USER 'maang'@'%' IDENTIFIED BY 'maang';
GRANT ALL PRIVILEGES ON *.* TO 'maang'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;
```

**Making connection from client**
```bash
mysql -h $host -u $user -p
```

![image](https://github.com/user-attachments/assets/4629af26-7b23-4d62-888f-badd6613aad1)




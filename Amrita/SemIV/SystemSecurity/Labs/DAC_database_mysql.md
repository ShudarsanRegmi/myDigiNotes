# Discretionay Access Control in Database : mysql


### Login as root user
```sql
sudo mysql
```

### Showing the current user
```sql
SELECT CURRENT_USER();
```

### Creating user
```sql
CREATE USER 'ma'@'localhost' identified by 'ma@localhost';
```
![image](https://github.com/user-attachments/assets/6dc2b47a-981b-477b-9779-59cd522a40a7)

### Showing the grants for the current user

```sql
CREATE USER 'ma'@'localhost' identified by 'ma@localhost';
```
![image](https://github.com/user-attachments/assets/e7c371da-0133-42e1-911a-4ff982124ed9)

### Creating database by newly created user
```sql
create database ma_ko_database
```
![image](https://github.com/user-attachments/assets/125f01df-14f4-43a3-85ec-291f813e3b2a)


### Granting Privileges from root user
![image](https://github.com/user-attachments/assets/3b840899-2cc4-43f0-b10c-c8bc450ffe48)

### Creating database after the permission has been granted
![image](https://github.com/user-attachments/assets/b28a0ddc-19f9-4d1e-8256-2cda1ee9fb68)


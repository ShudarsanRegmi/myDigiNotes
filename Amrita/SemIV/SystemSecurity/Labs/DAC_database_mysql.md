# Discretionay Access Control in Database : mysql

![image](https://github.com/user-attachments/assets/9921d444-33a2-4524-807d-f36ba46a8d39)![image](https://github.com/user-attachments/assets/e56b43fa-882d-4273-8316-f9d6b46e9d6e)


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


### Creating role

```sql
CREATE ROLE 'role1';
```
### Granting privileges to a rle
```sql
GRANT SELECT ON *.* TO role1;
```

![image](https://github.com/user-attachments/assets/a224dd02-fb3d-4e56-9577-8d1a49dc3f52)

### Assigning role to a particular user
```sql
GRANT 'role1' to 'ma'@'localhost';
```


### Exercise

Exercise:
Create a database “AmritaChennai”.
Create a table “CYSStudents” with any number of fields of your choice.
Create a user account “abc” with a password.
Grant all privileges to the account “abc”.
“abc” user account wants to grant to account “xyz” the privilege to insert and
delete tuples in the table “CYSStudents”. However, “abc” does not want “xyz” to be able to
propagate these privileges to additional accounts. Write the command for this and demonstrate.
Suppose that “abc” wants to allow account “rst’ to retrieve information from the table 
“CYSStudents” and also to be able to propagate the SELECT privilege to other accounts. Write the 
command for this and demonstrate.
Suppose that “abc” decides to revoke the SELECT privilege on the “CYSStudents”
table from “rst”. Write the command for this and demonstrate.

![image](https://github.com/user-attachments/assets/39b8ca83-904a-40ab-98d4-2eefb72f2776)


---

### **Step 1: Create a Database**
```sql
CREATE DATABASE AmritaChennai;
```

---

### **Step 2: Create a Table**
```sql
USE AmritaChennai;

CREATE TABLE CYSStudents (
    StudentID INT PRIMARY KEY,
    StudentName VARCHAR(50),
    Course VARCHAR(30),
    Year INT
);
```

---

### **Step 3: Create a User Account `abc` with a Password**
```sql
CREATE USER 'abc'@'localhost' IDENTIFIED BY 'abc_password';
```

---

### **Step 4: Grant All Privileges to User `abc`**
```sql
GRANT ALL PRIVILEGES ON AmritaChennai.* TO 'abc'@'localhost';
```

---

### **Step 5: Grant Insert and Delete Privileges from `abc` to `xyz` Without Grant Option**
User `abc` logs in and executes:
```sql
CREATE USER 'xyz'@'localhost' IDENTIFIED BY 'xyz_password';

GRANT INSERT, DELETE ON AmritaChennai.CYSStudents TO 'xyz'@'localhost';
```

- The absence of `WITH GRANT OPTION` ensures `xyz` cannot propagate these privileges.

---

### **Step 6: Grant SELECT Privilege from `abc` to `rst` With Grant Option**
User `abc` logs in and executes:
```sql
CREATE USER 'rst'@'localhost' IDENTIFIED BY 'rst_password';

GRANT SELECT ON AmritaChennai.CYSStudents TO 'rst'@'localhost' WITH GRANT OPTION;
```

- `WITH GRANT OPTION` allows `rst` to propagate the `SELECT` privilege to other accounts.

---

### **Step 7: Revoke SELECT Privilege from `rst`**
User `abc` logs in and executes:
```sql
REVOKE GRANT OPTION FOR SELECT ON AmritaChennai.CYSStudents FROM 'rst'@'localhost';
REVOKE SELECT ON AmritaChennai.CYSStudents FROM 'rst'@'localhost';
```

- The first command removes the ability of `rst` to propagate the `SELECT` privilege.
- The second command completely revokes the `SELECT` privilege from `rst`.

---

## Roles in mysql

![image](https://github.com/user-attachments/assets/779aed80-d47f-4ed3-90c2-d22ef85994b8)

```bash
create role reader;
```

```bash
grant select on *.* to reader;
```

```bash
show grants for reader;
```

```bash
grant reader to 'user1'@'localhost';
```

```bash
 revoke reader from 'user1'@'localhost';
```



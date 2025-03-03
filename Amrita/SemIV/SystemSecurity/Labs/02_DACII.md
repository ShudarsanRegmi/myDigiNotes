![image](https://github.com/user-attachments/assets/21dc67e3-c8b8-4020-bb0f-b18657dcaf7f)
## Login with Root user

```bash
sudo mysql
```

![image](https://github.com/user-attachments/assets/ade079c9-8b1f-4340-b005-3e71cdbe3b95)


## Enlist All Users
```mysql
select user from mysql.user;
```

![image](https://github.com/user-attachments/assets/fc6b1467-c368-430e-b5fc-f4fec891a796)

## Showing Current User
```mysql
select current_user();
```
![image](https://github.com/user-attachments/assets/776cc950-6369-42dc-9037-d73a1343d90c)

## Create a User 

```mysql
create user 'user'@'host" identified by <password>;
create user myuser@localhost identified by  userpass;
```
![image](https://github.com/user-attachments/assets/66de659a-7f68-43ac-88b9-09734ae31fbd)

## Login from the newly created user
```bash
mysql -u myuser -p
>myuser@localhost
```
![image](https://github.com/user-attachments/assets/ee5246f6-2f03-468d-9a0b-bf27962e00f7)


## Try to Create a database
```mysql
create database myuser_db;
```

![image](https://github.com/user-attachments/assets/379f996d-b65a-465d-8cb0-8d1150c68f63)

<p style="color: red;">Access Denied!</p>

## Showing Grants for the current user
![image](https://github.com/user-attachments/assets/a7289463-25e6-4575-a221-4f68838a5840)


**GRANT Usage**
>This means that the user myuser has the USAGE privilege. The USAGE privilege essentially means "no specific privileges" or "no special rights." It is typically granted to users with no further privileges, meaning they can't perform any actions unless additional permissions (like SELECT, INSERT, etc.) are granted explicitly.

[GRANT : mysql docs](https://dev.mysql.com/doc/refman/8.4/en/grant.html)

## Granting CREATE privileges (root)
```mysql
GRANT CREATE ON *.* TO 'myuser'@'localhost';
```
![image](https://github.com/user-attachments/assets/2a33b3c0-53fa-40ad-b450-fe959cf7ddb3)


## Showing Grants (myuser)
```mysql
show grants for 'myuser'@'localhost';
```
![image](https://github.com/user-attachments/assets/4f938841-c7c4-4ae0-9c9e-d9a5b804070c)

> Might have to log out and log in from the current user to see the changes

## Relogin and creating databse again
![image](https://github.com/user-attachments/assets/d2b1a0a5-4186-4c82-aaac-cfffbecfcab5)
```mysql
create database mydb;
use mydb;
create table mytable (column1 int primary key, column2 varchar(20) );
```

>With create privileges the user can create database and tables

## Inserting into a table (myuser)
![image](https://github.com/user-attachments/assets/81b7c658-eccd-45d5-9db7-cd600b3e0fe0)
```mysql
insert into mytable values (1,'ram');
```

## Providing INSERT Grant (root user)
```mysql
 grant insert on mydb.mytable to 'myuser'@'localhost';
```
![image](https://github.com/user-attachments/assets/25e03999-2ad1-4662-9fef-cf742373aa2e)

## Inserting into a table (myuser)

![image](https://github.com/user-attachments/assets/0dade03b-5609-4f78-a4fd-9108a6e88ace)

```mysql
insert into mytable values (1,'ram');
```

## Revoking privileges

## Revoking insert privileges
```mysql
revoke insert on mydb.mytable from 'myuser'@'localhost';
```
![image](https://github.com/user-attachments/assets/3612c96a-a2cc-416c-9e08-15845f461c3c)
![image](https://github.com/user-attachments/assets/a719a07a-ae33-44a8-923c-a260edfbccc5)


## Trying to insert after revoking privileges (myuser)
![image](https://github.com/user-attachments/assets/22f59961-6c6c-49b1-8e49-2aa31a15d2a7)

## Granting all privileges to a user (root)
```mysql
grant all privileges on *.* to 'myuser'@'localhost';
```

## Viewing all Grants
![image](https://github.com/user-attachments/assets/94cddbed-6b6e-4508-bb3a-dd06f38f4a6d)


## Creating Roles in mysql

### Creating a role
```mysql
 create role 'read_only'@'localhost';
```
![image](https://github.com/user-attachments/assets/4641d1b4-4405-4c72-b27c-dfa3bfcf29d9)

### Granting privilege to a role
```mysql
grant select on *.* to 'read_only'@'localhost';
```

### Listing grants for a role
```mysql
show grants for 'read_only'@'localhost'
```

### Assigning a role to a user
```mysql
 grant 'read_only' to 'myuser'@'localhost';
```

### Revoking a role assignment from a user
```mysql
revoke 'read_only' from 'myuesr'@'localhost';
```

![image](https://github.com/user-attachments/assets/f04a6708-5a7e-42f5-9455-a40dc9d8a766)

![image](https://github.com/user-attachments/assets/eace87b7-5e3d-427a-b2a6-cac0a52e929b)

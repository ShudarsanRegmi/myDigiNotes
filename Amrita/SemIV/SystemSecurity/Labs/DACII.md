


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
create user myuser@localhost identified by
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

<p style='color:red> Access Denied ! </p>

## Showing Grants for the current user
![image](https://github.com/user-attachments/assets/a7289463-25e6-4575-a221-4f68838a5840)

```
GRANT USAGE:
This means that the user myuser has the USAGE privilege. The USAGE privilege essentially means "no specific privileges" or "no special rights." It is typically granted to users with no further privileges, meaning they can't perform any actions unless additional permissions (like SELECT, INSERT, etc.) are granted explicitly.
```



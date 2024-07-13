# MySQL Notes

## Creating user and granting permissions

### Login in with root
```bash
mysql -u root -p
# Enter blank password
```

### Creating user
```mysql
CREATE USER 'new_user'@'localhost' IDENTIFIED BY 'password';
```
### Granting privileges
```mysql
GRANT ALL PRIVILEGES ON * . * TO 'new_user'@'localhost'; # Granting all permissions
GRANT CREATE, SELECT ON * . * TO 'user_name'@'localhost'; # Granting specific permissions
```
### Flushing privileges to see the effect immediately
```mysql
FLUSH PRIVILEGES;
```

## Displaying privileges
```mysql
SHOW GRANTS FOR 'user_name'@'localhost';
```

## Revoking Permission
### Revoking all permissions
```mysql
REVOKE ALL PRIVILEGES ON * . * FROM 'user_name'@'localhost';
```
### Revoking specific permission
```mysql
REVOKE PERMISSION_TYPE ON database_name.table_name FROM ‘user_name’@‘localhost’;
```

### Removing the user
```mysql
DROP USER ‘user_name’@‘localhost’;
```


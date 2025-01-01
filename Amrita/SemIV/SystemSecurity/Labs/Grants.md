# GRANTS IN MYSQL

In MySQL, user privileges (or grants) determine the level of access a user has to the database. These grants are associated with different operations such as SELECT, INSERT, UPDATE, DELETE, and more. Grants can be applied at different levels: global, database, table, column, or routine.

### Types of Grants for a MySQL User:

1. **Global Privileges**  
   These privileges apply to the entire MySQL server and affect all databases. They are granted using the `*.*` notation (for all databases and tables).

   - `ALL PRIVILEGES`: Grants all privileges available (combines most of the other grants).
   - `CREATE`: Allows creating databases and tables.
   - `DROP`: Allows dropping databases and tables.
   - `PROCESS`: Allows viewing information about threads executing in the server.
   - `SUPER`: Allows the user to perform administrative operations (like killing threads, shutting down MySQL, etc.).
   - `RELOAD`: Allows reloading of privileges or other system tasks (e.g., flushing logs).
   - `SHOW DATABASES`: Allows listing databases.
   - `REPLICATION SLAVE`: Required for replication slaves to connect to the master.
   - `REPLICATION CLIENT`: Required to monitor the replication status.
   - `CREATE USER`: Allows creating, altering, or dropping MySQL users.
   - `SHUTDOWN`: Allows shutting down the MySQL server.

2. **Database Privileges**  
   These apply to a specific database (e.g., `mydatabase.*`) and determine what actions can be performed on the tables in that database.

   - `SELECT`: Allows reading data from tables (e.g., `SELECT` queries).
   - `INSERT`: Allows inserting data into tables.
   - `UPDATE`: Allows modifying existing data in tables.
   - `DELETE`: Allows deleting data from tables.
   - `CREATE`: Allows creating new tables or databases.
   - `DROP`: Allows dropping tables or databases.
   - `ALTER`: Allows modifying table structures (e.g., adding/removing columns).
   - `INDEX`: Allows creating or dropping indexes.
   - `CREATE ROUTINE`: Allows creating stored procedures or functions.
   - `ALTER ROUTINE`: Allows altering or dropping stored procedures/functions.
   - `EXECUTE`: Allows executing stored procedures or functions.
   - `GRANT OPTION`: Allows granting or revoking privileges to other users.
   - `REFERENCES`: Allows creating foreign keys in tables.

3. **Table Privileges**  
   These apply to specific tables in a database (e.g., `mydatabase.mytable`) and control access to the data and structure of a table.

   - `SELECT`: Allows reading data from the table.
   - `INSERT`: Allows inserting data into the table.
   - `UPDATE`: Allows updating rows in the table.
   - `DELETE`: Allows deleting rows from the table.
   - `INDEX`: Allows creating or dropping indexes on the table.
   - `ALTER`: Allows altering the structure of the table.
   - `DROP`: Allows dropping the table.

4. **Column Privileges**  
   These apply to specific columns within a table (e.g., `mydatabase.mytable(column_name)`) and control access to the columns.

   - `SELECT`: Allows reading data from the column.
   - `INSERT`: Allows inserting data into the column.
   - `UPDATE`: Allows modifying data in the column.

5. **Routine Privileges**  
   These apply to stored procedures and functions (routines) within a database.

   - `EXECUTE`: Allows executing a stored procedure or function.
   - `ALTER ROUTINE`: Allows modifying or dropping routines.
   - `CREATE ROUTINE`: Allows creating stored procedures or functions.

6. **Event Privileges**  
   These apply to event scheduling in MySQL.

   - `EVENT`: Allows creating, altering, or dropping events (used for event scheduler).

7. **File Privileges**  
   These relate to file operations and can control whether a user can access or modify files on the server's file system.

   - `FILE`: Allows reading and writing files on the server (for example, importing or exporting data).

8. **Proxy Privileges**  
   These privileges are used when a user can act on behalf of another user.

   - `PROXY`: Allows a user to impersonate another user.

---

### Granting Privileges

To grant privileges to a user in MySQL, the `GRANT` statement is used. For example:

```sql
GRANT SELECT, INSERT, UPDATE ON mydatabase.* TO 'username'@'localhost' IDENTIFIED BY 'password';
```

This grants the user `username` the ability to perform `SELECT`, `INSERT`, and `UPDATE` operations on all tables in the `mydatabase` database from the localhost.

You can also use `GRANT ALL PRIVILEGES` to give the user full access to the database:

```sql
GRANT ALL PRIVILEGES ON mydatabase.* TO 'username'@'localhost' IDENTIFIED BY 'password';
```

After making changes to user privileges, it's a good practice to run:

```sql
FLUSH PRIVILEGES;
```

This reloads the privilege tables and applies the changes.

### Revoking Privileges

To revoke privileges, the `REVOKE` statement is used. For example:

```sql
REVOKE SELECT, INSERT ON mydatabase.* FROM 'username'@'localhost';
```

This revokes the `SELECT` and `INSERT` privileges on the `mydatabase` database from the specified user.

---

### Viewing Grants

To see the privileges assigned to a user, you can use:

```sql
SHOW GRANTS FOR 'username'@'localhost';
```

This command will display the exact grants and privileges for that user.

### Conclusion

MySQL provides a fine-grained system for controlling access to databases, tables, columns, and routines. The `GRANT` system allows for specifying exactly what a user can and cannot do, and privileges can be assigned at various levels based on the user's role and requirements.

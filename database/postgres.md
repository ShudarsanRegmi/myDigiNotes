# Postgres Database Notes

### Connecting to a database
```postgres
\c <db_name>
```
### Listing all the databases
```postgres
\l
```
### List all the tables in the current database
```postgres
\dt
```
### List all schemas
```postgres
\dn\q

```

### List all columns in a specified table
```postgres
\d <table_name>
```

### Describe the table structure
```postgres
\d+ <table_name>
```
### List all users/roles
```postgres
\du
```
 ## Running SQL Queries
 ```sql
SELECT * FROM <table_name>
```
>Running sql queries is almost same as in other databases like mysql

## Miscellaneous Commands

### Getting current database connection info
```posgtgres
\conninfo
```
### Clearing the screen
```postgres
\! clear
```

### Getting help
```postgres
\?
```
### Quitting the shell
```postgres
\q
```


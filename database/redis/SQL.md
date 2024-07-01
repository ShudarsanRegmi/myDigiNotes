# SQL Note

## Select Query
```sql
SELECT <COLUMN_NAME> FROM <TABLE> WHERE <CONSTRAINTS>
COLUMN_NAME = COL1, COL2
COLUMN_NAME = * (for all columns)
CONSTRAINTS = conditions to filter the output
```

## Removing duplicate fetches
```sql
SELECT DISTINCT CITY FROM STATION WHERE MOD(ID,2) = 0;
# fetch all cities from station where id is even. Fetch without duplicates.
```



## Some Real Usecases



## Looking for row with odd or even column.
```sql
# mysql postgres and oracle
SELECT * FROM my_table WHERE MOD(my_column, 2) = 0;
SELECT * FROM my_table WHERE MOD(my_column, 2) <> 0;
# mssql
SELECT * FROM my_table WHERE my_column % 2 = 0;
SELECT * FROM my_table WHERE my_column % 2 <> 0;
```


## Important Notes
- White space matters or not depends upon the configuration. (Ref)[https://stackoverflow.com/questions/2501704/does-sql-standard-allows-whitespace-between-function-names-and-parenthesis]

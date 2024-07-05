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
## LIKE Operator
- There are only two wildcards with LIKE Operator
- % represents zero, one or multiple characters
- _ only one single character

### Having Caluse
Having caluse was added to sql because where keyword cannot be used with aggregate functions
```sql
SELECT column_name(s)
FROM table_name
WHERE condition
GROUP BY column_name(s)
HAVING condition
ORDER BY column_name(s);
```

### Aggregate functions
An aggregate function is a function that performs a calculation on a set of values, and returns a single value.
Example: min(), max(), avg(), count(), sum(), etc.

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



## Functions
**LENGTH()** --> FINDS THE LENGTH OF A COLUMN.


## Some Points for further studying
**union all** vs. **union** => `union all` includes all duplicate fetches while `union` doesn't

## 

## Important Notes
- White space matters or not depends upon the configuration. (Ref)[https://stackoverflow.com/questions/2501704/does-sql-standard-allows-whitespace-between-function-names-and-parenthesis]

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

## Group By Clause Working
The SQL engine processes a query with a GROUP BY clause by first parsing and checking the syntax of the query. It then identifies the columns specified for grouping and scans the table to collect the values of these columns. Rows with identical values in the specified columns are grouped together. If aggregate functions are present, the engine computes these functions for each group. Any HAVING clause is then applied to filter the groups based on specified conditions. Finally, the engine generates and returns the result set, which includes one row per group and any computed aggregate values

Without aggregate function group by clause can be used as below. But using aggregate function is its most common use case.

```sql
SELECT Department
FROM Employees
GROUP BY Department;
```

## JOIN Statements
Used to join two tables
- Inner Join
- Outer Join
  - Left Join
  - Right Join
  - Full Outer Join

JOIN = INNER JOIN

Left Join = Inner Join + unmatching rows in left column
Right join = Outer Join + unmatching rows in right column



### Lab questions
21. select Customer, Order_date, max(purch_amt) from Orders group by customers, Order_date;
22. select max(Purch_amt) from Orders where  Order_date='2016-8-17' group by Salesman_id having Salesman_id is not null;
22. select max(Purch_amt) from Orders group by Salesman_id having Order_date=''; ( doubt) 
23. select  Customer_id, max(Purch_amt) Order_date from Orders group by Customer_id having Purch_amt>=2000;
24. select count(Order_date) from Orders where Order_date='17-08-2012';
 

## Important Notes
- White space matters or not depends upon the configuration. (Ref)[https://stackoverflow.com/questions/2501704/does-sql-standard-allows-whitespace-between-function-names-and-parenthesis]

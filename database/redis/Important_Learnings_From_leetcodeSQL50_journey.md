# Important Learning from LeetCode SQL50 journey

- Use Self join with proper conditions to perform operations b/w rows.
- group by col1, col2 can have multiple columns for col1 but only a single column from col2
- Check for null cases too in the cases when the value can be optional such as bonus less than 1000, etc.
- We can modify the column in our way and group by based on the modified column (Transaction-I)
- When using GROUP BY, including a non-aggregated column that has the same values within a group won't cause an error, but it can lead to ambiguity. For clarity and best practice, either aggregate the column or include it in the GROUP BY clause.
- When using UNION with individual ORDER BY clauses and LIMIT within each SELECT statement, it's necessary to wrap each SELECT part in parentheses. This way, the LIMIT and ORDER BY apply only to the respective SELECT queries and not to the final UNION result.
- The query you provided has an issue due to the use of the cumwtm alias in the WHERE clause. In SQL, you cannot reference an alias defined in the SELECT clause in the same level of the query where it's defined.
- Remember: Use WHERE to filter raw data before aggregation (no aliases), and use HAVING to filter aggregated results where you can reference aliases.
- Incorrect Aggregation: You can't use an aggregate function like MIN() directly in a CASE statement without a subquery or Common Table Expression (CTE).




# Technical aspects
- DATEDIFF() function two find differnce between two dates. E.g. DATEDIFF(activity_date, '2019-07-27') < 30
- coalesce() function to provide substitue values for null values
- year(), month(), date(), DATE_FORMAT(date, "%Y-%m"), etc.
- Aggregation function can be used even after having clause
- GROUP_CONCAT(column SEPARATOR order by column ',') for comma separated values between rows of aggregated columns, STRING_AGG(column_name, ',') for sql server, postgres


# Question I need to revise Again
-  1141. User Activity for the Past 30 Days I
- 1070. Product Sales Analysis (solved using cte, need to solve using subqueries)


# Some queries to Look again

```sql
select class from courses group by class having count(student) >= 5;
```

##### Using windowing funciton to find the moving average of past 7 days
```sql
# Write your MySQL query statement below
SELECT visited_on, amount, ROUND(amount/7, 2) average_amount
FROM (
    SELECT DISTINCT visited_on, 
    SUM(amount) OVER(ORDER BY visited_on RANGE BETWEEN INTERVAL 6 DAY   PRECEDING AND CURRENT ROW) amount, 
    MIN(visited_on) OVER() 1st_date 
    FROM Customer
) t
WHERE visited_on>= 1st_date+6;
```

##### Bringing the grouped columns in a single column
```sql

SELECT 
    sell_date, 
    COUNT(distinct product) AS num_sold, 
    GROUP_CONCAT(distinct product order by product SEPARATOR ',') AS products 
FROM 
    activities 
GROUP BY 
    sell_date 
ORDER BY 
    sell_date, product;
```

##### Dangerous uses of subquery
```sql
# Primary department for each employee
SELECT 
    e1.employee_id,
    e1.department_id
FROM employee e1
WHERE e1.primary_flag = 'Y'
OR 
    e1.primary_flag = 'N' AND NOT EXISTS (
        SELECT 
			1 
        FROM employee e2
        WHERE e2.employee_id = e1.employee_id AND e2.primary_flag = 'Y');
```
##### Use of ROW_NUMBER() windowing function
```sql
SELECT 
    a.employee_id,
    a.department_id
FROM (
    SELECT 
        e.employee_id,
        e.department_id,
        ROW_NUMBER() OVER (PARTITION BY employee_id ORDER BY primary_flag) AS rn
    FROM employee e
) a 
WHERE a.rn = 1;
```

```sql
SELECT 
    e1.employee_id,
    (
        CASE
            WHEN e2.primary_flag IS NULL THEN e1.department_id
            WHEN e2.primary_flag IS NOT NULL AND e2.primary_flag = 'Y' THEN e2.department_id
        END
    ) AS department_id
FROM employee e1
LEFT JOIN (
    SELECT 
        * 
    FROM employee
    WHERE primary_flag = 'Y'
) AS e2 
ON e1.employee_id = e2.employee_id
GROUP BY e1.employee_id;
```

```
# I don't know about this IF Syntax
SELECT *, IF(x+y>z and y+z>x and z+x>y, "Yes", "No") as triangle FROM Triangle
```


# Some Invalid Queries that my brain interpretes as valid

```sql
with cte as(
select *, 
rank() over (partition by customer_id order by order_date) as rk
from delivery where rk = 1;
)
select * from cte;
```

```sql
# alias won't work for windowing function
mysql> SELECT  *,  concat(lat,lon) as geo, count(geo) over (partition by geo) as pidc from insurance;
ERROR 1054 (42S22): Unknown column 'geo' in 'field list'
```
```sql
select num from mynumbers where count(num) = 1 group by num;
```

```sql
# ERROR 3594 (HY000): You cannot use the alias 'cumwt' of an expression containing a window function in this context.'
select *, sum(weight) over(order by turn) as cumwtm from queue where cumwtm <= 1000;
```

```sql
 select *, sum(weight) over(order by turn) as cumwtm from queue group by person_id having cumwtm <=1000;
```

```sql
select user_id, count(user_id) as cnt from movierating group by user_id having user_id = max(cnt);
```

# Queries that looks odd to me but are actually correct

```sql
SELECT MAX(num) AS num
FROM (
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(num) = 1
) AS unique_numbers;
```
```sql
# "Yes, it is not necessary to select additional counts or columns because SQL processes HAVING after grouping. This allows you to focus on the results that matter most. Embrace this insight—each query you tackle brings you closer to mastery! Keep going; you’ve got this
SELECT customer_id
FROM customer
GROUP BY customer_id
HAVING COUNT(DISTINCT product_key) = (SELECT COUNT(product_key) FROM product);
```


### limit 1 : A Technique to pick the min and mad supported by sorting
```sql
SELECT (SELECT num FROM MyNumbers GROUP BY num HAVING COUNT(num) = 1 ORDER BY num DESC LIMIT 1) AS num;
```

### Some Dangerous looking queries encountered
```sql
select
    case
        when id = (select max(id) from seat) and id % 2 = 1
            then id
        when id % 2 = 1
            then id + 1
        else id - 1
        end as id, student from seat order by id;
```

```sql
(
SELECT name AS results
FROM movierating t1
LEFT JOIN users t2 ON t1.user_id = t2.user_id 
GROUP BY t1.user_id 
ORDER BY COUNT(t1.user_id) DESC, name 
LIMIT 1
)
UNION ALL
(
SELECT title AS results
FROM movierating t1
JOIN movies t2 ON t1.movie_id = t2.movie_id 
WHERE YEAR(created_at) = '2020' AND MONTH(created_at) = '02' 
GROUP BY t1.movie_id 
ORDER BY AVG(rating) DESC, title 
LIMIT 1
);
```

```sql
(
    select
        Users.name as results
    from 
        MovieRating left join Users
    on 
        MovieRating.user_id = Users.user_id 
    group by
        Users.user_id
    order by
        count(MovieRating.movie_id) desc, 
        Users.name
    limit 1
) 
union all
(
    select 
        Movies.title as results
    from 
        MovieRating  left join Movies 
    on
        MovieRating.movie_id = Movies.movie_id
    where 
        MovieRating.created_at like '2020-02%'
    group by
        MovieRating.movie_id
    order by
        avg(MovieRating.rating) desc, 
        Movies.title 
    limit 1
)
```

### Smart Solutions

##### Exchange Seats - Medium
```sql

SELECT 
    id,
    CASE
        WHEN id % 2 = 0 THEN LAG(student) OVER(ORDER BY id)
        ELSE COALESCE(LEAD(student) OVER(ORDER BY id), student)
    END AS student
FROM Seat
```

```
SELECT *
FROM Patients
WHERE LOCATE('DIAB1', conditions) = 1
   OR LOCATE(' DIAB1', conditions) != 0;
```

##### Delete duplicate emails
```
DELETE p1 FROM Person p1,
    Person p2
WHERE
    p1.Email = p2.Email AND p1.Id > p2.Id
```

#### Second Highest Salary or else null
```sql
SELECT MAX(salary) AS SecondHighestSalary 
FROM Employee
WHERE salary < (SELECT MAX(salary) FROM Employee);
```
### Crafted by me

```sql
# friends count (finding the total in both columns)
SELECT 
    uid as id,
    (SELECT COUNT(*) FROM RequestAccepted WHERE requester_id = ids.uid) +
    (SELECT COUNT(*) FROM RequestAccepted WHERE accepter_id = ids.uid) AS num
FROM (
    SELECT 
        requester_id AS uid 
    FROM 
        RequestAccepted 
    UNION 
    SELECT 
        accepter_id AS uid 
    FROM 
        RequestAccepted
) AS ids
GROUP BY uid
ORDER BY num DESC
LIMIT 1;

```

```sql
select max(salary) as SecondHighestSalary from employee where salary < (select max(salary) from employee);
```

```sql
# Count Salary Categories
SELECT 'Low Salary' AS category, COUNT(income) AS accounts_count
FROM accounts
WHERE income < 20000

UNION ALL

SELECT 'Average Salary' AS category, COUNT(income) AS accounts_coun
FROM accounts
WHERE income >= 20000 AND income <= 50000

UNION ALL

SELECT 'High Salary' AS category, COUNT(income) AS accounts_counts
FROM accounts
WHERE income > 50000;
```

```
# Moving average
SELECT DISTINCT 
    dt.visited_on,
    (SELECT SUM(amount) 
     FROM customer 
     WHERE visited_on BETWEEN DATE_SUB(dt.visited_on, INTERVAL 6 DAY) AND dt.visited_on) AS amount,
    (SELECT ROUND(SUM(amount) / 7, 2) 
     FROM customer 
     WHERE visited_on BETWEEN DATE_SUB(dt.visited_on, INTERVAL 6 DAY) AND dt.visited_on) AS average_amount
FROM 
    (SELECT DISTINCT visited_on FROM customer) AS dt 
WHERE 
    dt.visited_on >= (SELECT MIN(visited_on) FROM customer) + INTERVAL 6 DAY;

```

# Bus Boarding problem: Last Person to fit the bus

```sql
# Bus Boarding max weight
SELECT 
    q1.person_name
FROM Queue q1 JOIN Queue q2 ON q1.turn >= q2.turn
GROUP BY q1.turn
HAVING SUM(q2.weight) <= 1000
ORDER BY SUM(q2.weight) DESC
LIMIT 1

# Using subquery
SELECT person_name from (SELECT person_name,turn,
sum(weight) over (order by turn) AS cum FROM queue) p1
where cum<=1000 order by turn DESC limit 1;

```
## Dangerous Queries crated by me

### Subqueries hell
```sql

SELECT round(SUM(tiv_2016),2) as tiv_2016
FROM insurance i 
WHERE i.pid IN (
    SELECT l3dt.pid 
    FROM (
        SELECT dt2.pid 
        FROM (
            SELECT t1.pid, 
                   (SELECT COUNT(*) 
                    FROM insurance AS t2 
                    WHERE t1.lat = t2.lat AND t1.lon = t2.lon) AS matche 
            FROM insurance AS t1
        ) AS dt2 
        WHERE dt2.matche = 1
    ) AS l3dt 
    WHERE l3dt.pid IN (
        SELECT dt.pid 
        FROM (
            SELECT t1.pid, 
                   (SELECT COUNT(*) 
                    FROM insurance t2 
                    WHERE t1.tiv_2015 = t2.tiv_2015) AS tiv_count 
            FROM insurance t1
        ) AS dt 
        WHERE dt.tiv_count != 1
    )
);

```

## Questions that I need to look again
```sql
select distinct product_id, 10 as price from Products where product_id not in(select distinct product_id from Products where change_date <='2019-08-16' )
union 
select product_id, new_price as price from Products where (product_id,change_date) in (select product_id , max(change_date) as date from Products where change_date <='2019-08-16' group by product_id);
```


## Cases That I need to learn to handle
- choosing a row of one column based on some data in another column



---

## String Functions in mysql

### MySQL String Functions Overview

1. **`CONCAT(str1, str2, ...)`**: Joins multiple strings together.  
   ```sql
   SELECT CONCAT('Hello', ' ', 'World'); -- Result: 'Hello World'
   ```

2. **`LENGTH(str)`**: Returns the length of a string in bytes.
   ```sql
   SELECT LENGTH('text'); -- Result: 4
   ```

3. **`CHAR_LENGTH(str)`**: Returns the number of characters in a string.
   ```sql
   SELECT CHAR_LENGTH('text'); -- Result: 4
   ```

4. **`UPPER(str)` / `LOWER(str)`**: Converts all characters to uppercase or lowercase.
   ```sql
   SELECT UPPER('hello'); -- Result: 'HELLO'
   SELECT LOWER('WORLD'); -- Result: 'world'
   ```

5. **`SUBSTRING(str, pos, len)`**: Extracts a substring from a specified position for a certain length.
   ```sql
   SELECT SUBSTRING('MySQL', 2, 3); -- Result: 'ySQ'
   ```

6. **`TRIM([LEADING | TRAILING | BOTH] trim_char FROM str)`**: Removes specified characters (default is whitespace) from the start, end, or both sides of a string.
   ```sql
   SELECT TRIM(BOTH 'x' FROM 'xxHello Worldxx'); -- Result: 'Hello World'
   ```

7. **`REPLACE(str, from_str, to_str)`**: Replaces occurrences of `from_str` with `to_str`.
   ```sql
   SELECT REPLACE('Hello World', 'World', 'MySQL'); -- Result: 'Hello MySQL'
   ```

8. **`INSTR(str, substr)`**: Returns the position of the first occurrence of `substr` in `str`.
   ```sql
   SELECT INSTR('database', 'base'); -- Result: 5
   ```

9. **`REVERSE(str)`**: Reverses the characters in a string.
   ```sql
   SELECT REVERSE('hello'); -- Result: 'olleh'
   ```

10. **`LPAD(str, len, padstr)` / `RPAD(str, len, padstr)`**: Pads a string on the left or right to a specified length with a padding string.
    ```sql
    SELECT LPAD('MySQL', 8, '*'); -- Result: '***MySQL'
    SELECT RPAD('SQL', 5, 'x'); -- Result: 'SQLxx'
    ```

11. **`FORMAT(number, decimals)`**: Formats a number as a string with commas for thousands.
    ```sql
    SELECT FORMAT(12345.678, 2); -- Result: '12,345.68'
    ```

These functions allow flexible manipulation, formatting, and analysis of string data in MySQL.


## Material to refer
- [Sovle nth ranking problem in 5 ways](https://leetcode.com/problems/second-highest-salary/solutions/1168444/summary-five-ways-to-solve-the-top-n-nth-problems/?envType=study-plan-v2&envId=top-sql-50)

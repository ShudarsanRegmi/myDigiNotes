# Important Learning from LeetCode SQL50 journey

- Use Self join with proper conditions to perform operations b/w rows.
- group by col1, col2 can have multiple columns for col1 but only a single column from col2
- Check for null cases too in the cases when the value can be optional such as bonus less than 1000, etc.
- We can modify the column in our way and group by based on the modified column (Transaction-I)
- When using GROUP BY, including a non-aggregated column that has the same values within a group won't cause an error, but it can lead to ambiguity. For clarity and best practice, either aggregate the column or include it in the GROUP BY clause.
- When using UNION with individual ORDER BY clauses and LIMIT within each SELECT statement, it's necessary to wrap each SELECT part in parentheses. This way, the LIMIT and ORDER BY apply only to the respective SELECT queries and not to the final UNION result.




# Technical aspects
- DATEDIFF() function two find differnce between two dates. E.g. DATEDIFF(activity_date, '2019-07-27') < 30
- coalesce() function to provide substitue values for null values
- year(), month(), date(), DATE_FORMAT(date, "%Y-%m"), etc.
- Aggregation function can be used even after having clause


# Question I need to revise Again
-  1141. User Activity for the Past 30 Days I
- 1070. Product Sales Analysis (solved using cte, need to solve using subqueries)


# Some queries to Look again

```sql
select class from courses group by class having count(student) >= 5;
```

# Some Invalid Queries that my brain interpretes as valid

```sql
select num from mynumbers where count(num) = 1 group by num;
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

```
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
``

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

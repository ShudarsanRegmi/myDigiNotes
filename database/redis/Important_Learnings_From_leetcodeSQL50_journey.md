# Important Learning from LeetCode SQL50 journey

- Use Self join with proper conditions to perform operations b/w rows.
- group by col1, col2 can have multiple columns for col1 but only a single column from col2
- Check for null cases too in the cases when the value can be optional such as bonus less than 1000, etc.
- We can modify the column in our way and group by based on the modified column (Transaction-I)




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

# Ambigious SQL

>Following are the ambigious topics in SQL


```sql
select name from customer where referee_id != 2;
```
- will it fetch the rows where referee_id is null. This is a very obvious scenario as there can be customers where are not referred by anyone.

```

Customer table:
+----+------+------------+
| id | name | referee_id |
+----+------+------------+
| 1  | Will | null       |
| 2  | Jane | null       |
| 3  | Alex | 2          |
| 4  | Bill | null       |
| 5  | Zack | 1          |
| 6  | Mark | 2          |
+----+------+------------+
```



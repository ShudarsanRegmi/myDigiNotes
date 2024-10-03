# Ambigious SQL

>Following are the ambigious topics in SQL


```sql
select name from customer where referee_id != 2;
```
- will it fetch the rows where referee_id is null. This is a very obvious scenario as there can be customers where are not referred by anyone.


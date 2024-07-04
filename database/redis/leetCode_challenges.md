# My soution for leetCode challenges

### Duplicate Emails: Easy
- Fetch the emails from Person table who is having duplicate entires 
```sql
select distinct email as Email from Person where email in (select email from Person group by email having count(*)> 1);
```

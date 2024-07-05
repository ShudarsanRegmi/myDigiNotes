# My soution for leetCode challenges

### Duplicate Emails: Easy
- Fetch the emails from Person table who is having duplicate entires 
```sql
select distinct email as Email from Person where email in (select email from Person group by email having count(*)> 1);
```
### Recycable and low fat products: easy: 1757
```sql
select product_id from Products where low_fats='Y' and recyclable='Y';
```
### 2356. Number of Unique Subjects Taught by Each Teacher: Easy
```sql
select teacher_id, count(distinct subject_id) as cnt from Teacher group by teacher_id;
```
### 1741. Find Total Time Spent by Each Employee: Easy
```sql
select event_day as day, emp_id, sum(out_time-in_time) as total_time from Employees group by event_day,emp_id;
```

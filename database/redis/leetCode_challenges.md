# My soution for leetCode challenges

## Gheu Points
- Look for `null` if you're not looking something.(Eg. customer who've never ordered)

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
### 175. Combine Two Tables: Easy
```sql
select Person.firstName, Person.lastName, Address.city, Address.state from Person left join Address on Person.personId=Address.personId;
```
### 1587. Account Summamry: Easy :Rev
```sql
 select u.name as NAME,sum(t.amount) as BALANCE
from Users u inner join Transactions t on u.account=t.account group by u.account having BALANCE>=10000;
```
### 1068. Product Sales Analysis :Easy :conf in left or inner join
```sql
select p.product_name, s.year, s.price
from Sales s inner join Product p on s.product_id=p.product_id;
```

### 577. Employee Bonus :Easy
```sql
select e.name, b.bonus
from
employee e left join bonus b on e.empId=b.empId having b.bonus<1000 or b.bonus is null;
```

# I'll learn subqueries now onwards

## Join based leet code problems

### 183. Customers who've never ordered
```sql
select C.name as Customers from Customers C left join Orders O on C.id = O.customerId where O.id is null;
```
```sql
select user_id,count(distinct follower_id) as followers_count from Followers group by user_id order by user_id asc;
```

172, 595, 1581, 

Problems given in class: Sat 25th Aug
1050, 1251, 1280

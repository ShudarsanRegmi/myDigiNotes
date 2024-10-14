# Common Table Expression in SQL

** Theory and examples **

# Practice Questions

#### Setup

```sql
REATE TABLE emp2 (
    id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department VARCHAR(100),
    salary DECIMAL(10, 2),
    manager_id INT
);

INSERT INTO emp2 (id, first_name, last_name, department, salary, manager_id) VALUES
(1, 'Angelika', 'Voules', 'Marketing', 5293.74, 2),
(2, 'Rozelle', 'Swynley', 'Marketing', 8295.08, 18),
(3, 'Warren', 'Willey', 'Engineering', 9126.72, 19),
(4, 'Lynelle', 'Whiten', 'Management Board', 10716.15, NULL),
(5, 'Consolata', 'Roman', 'Legal', 8456.06, 4),
(6, 'Hoebart', 'Baldock', 'Research and Development', 4817.34, 20),
(7, 'Starlene', 'Watkiss', 'Accounting', 6541.48, 4),
(8, 'Barde', 'Ribbens', 'Marketing', 4852.87, 2),
(9, 'Lorne', 'Philipsen', 'Engineering', 7235.59, 3),
(10, 'Pedro', 'Naldrett', 'Research and Development', 5471.62, 20),
(11, 'Brina', 'Dillinger', 'Marketing', 6512.17, 2),
(12, 'Verile', 'Sonley', 'Research and Development', 4574.41, 20),
(13, 'Noble', 'Geerling', 'Research and Development', 8391.18, 20),
(14, 'Garey', 'MacAdam', 'Accounting', 3829.88, 7),
(15, 'Theo', 'Sorrell', 'Engineering', 6441.67, 3),
(16, 'Erminie', 'Gelling', 'Research and Development', 8590.70, 20),
(17, 'Loralie', 'Koop', 'Accounting', 5248.46, 7),
(18, 'Cal', 'Andrey', 'Management Board', 11258.82, NULL),
(19, 'Quincey', 'Gamell', 'Management Board', 11366.52, NULL),
(20, 'Janith', 'McGiffie', 'Research and Development', 7428.83, 19);

```

```sql
mysql> select * from emp2;
+----+------------+-----------+--------------------------+----------+------------+
| id | first_name | last_name | department               | salary   | manager_id |
+----+------------+-----------+--------------------------+----------+------------+
|  1 | Angelika   | Voules    | Marketing                |  5293.74 |          2 |
|  2 | Rozelle    | Swynley   | Marketing                |  8295.08 |         18 |
|  3 | Warren     | Willey    | Engineering              |  9126.72 |         19 |
|  4 | Lynelle    | Whiten    | Management Board         | 10716.15 |       NULL |
|  5 | Consolata  | Roman     | Legal                    |  8456.06 |          4 |
|  6 | Hoebart    | Baldock   | Research and Development |  4817.34 |         20 |
|  7 | Starlene   | Watkiss   | Accounting               |  6541.48 |          4 |
|  8 | Barde      | Ribbens   | Marketing                |  4852.87 |          2 |
|  9 | Lorne      | Philipsen | Engineering              |  7235.59 |          3 |
| 10 | Pedro      | Naldrett  | Research and Development |  5471.62 |         20 |
| 11 | Brina      | Dillinger | Marketing                |  6512.17 |          2 |
| 12 | Verile     | Sonley    | Research and Development |  4574.41 |         20 |
| 13 | Noble      | Geerling  | Research and Development |  8391.18 |         20 |
| 14 | Garey      | MacAdam   | Accounting               |  3829.88 |          7 |
| 15 | Theo       | Sorrell   | Engineering              |  6441.67 |          3 |
| 16 | Erminie    | Gelling   | Research and Development |  8590.70 |         20 |
| 17 | Loralie    | Koop      | Accounting               |  5248.46 |          7 |
| 18 | Cal        | Andrey    | Management Board         | 11258.82 |       NULL |
| 19 | Quincey    | Gamell    | Management Board         | 11366.52 |       NULL |
| 20 | Janith     | McGiffie  | Research and Development |  7428.83 |         19 |
+----+------------+-----------+--------------------------+----------+------------+
20 rows in set (0.00 sec)
```

####  1. Find the Average Salary by Department


```sql
with avg_salary as (
select department,  avg(salary) as avg_sal
from emp2  group by department
)
select e.first_name, e.last_name, avgs.department, avgs.avg_sal
from emp2 e inner join avg_salary avgs on
e.department = avgs.department order by department;
```


##### Output

```
+------------+-----------+--------------------------+--------------+
| first_name | last_name | department               | avg_sal      |
+------------+-----------+--------------------------+--------------+
| Starlene   | Watkiss   | Accounting               |  5206.606667 |
| Garey      | MacAdam   | Accounting               |  5206.606667 |
| Loralie    | Koop      | Accounting               |  5206.606667 |
| Warren     | Willey    | Engineering              |  7601.326667 |
| Lorne      | Philipsen | Engineering              |  7601.326667 |
| Theo       | Sorrell   | Engineering              |  7601.326667 |
| Consolata  | Roman     | Legal                    |  8456.060000 |
| Lynelle    | Whiten    | Management Board         | 11113.830000 |
| Cal        | Andrey    | Management Board         | 11113.830000 |
| Quincey    | Gamell    | Management Board         | 11113.830000 |
| Angelika   | Voules    | Marketing                |  6238.465000 |
| Rozelle    | Swynley   | Marketing                |  6238.465000 |
| Barde      | Ribbens   | Marketing                |  6238.465000 |
| Brina      | Dillinger | Marketing                |  6238.465000 |
| Hoebart    | Baldock   | Research and Development |  6545.680000 |
| Pedro      | Naldrett  | Research and Development |  6545.680000 |
| Verile     | Sonley    | Research and Development |  6545.680000 |
| Noble      | Geerling  | Research and Development |  6545.680000 |
| Erminie    | Gelling   | Research and Development |  6545.680000 |
| Janith     | McGiffie  | Research and Development |  6545.680000 |
+------------+-----------+--------------------------+--------------+
20 rows in set (0.00 sec)
```

***Alterntive approach using windowing functions***

```sql
 select first_name, department, avg(salary) over (partition by department) as sal_avg from emp2;
```

##### Output

```
mysql> select first_name, department, avg(salary) over (partition by department) as sal_avg from emp2;
+------------+--------------------------+--------------+
| first_name | department               | sal_avg      |
+------------+--------------------------+--------------+
| Starlene   | Accounting               |  5206.606667 |
| Garey      | Accounting               |  5206.606667 |
| Loralie    | Accounting               |  5206.606667 |
| Warren     | Engineering              |  7601.326667 |
| Lorne      | Engineering              |  7601.326667 |
| Theo       | Engineering              |  7601.326667 |
| Consolata  | Legal                    |  8456.060000 |
| Lynelle    | Management Board         | 11113.830000 |
| Cal        | Management Board         | 11113.830000 |
| Quincey    | Management Board         | 11113.830000 |
| Angelika   | Marketing                |  6238.465000 |
| Rozelle    | Marketing                |  6238.465000 |
| Barde      | Marketing                |  6238.465000 |
| Brina      | Marketing                |  6238.465000 |
| Hoebart    | Research and Development |  6545.680000 |
| Pedro      | Research and Development |  6545.680000 |
| Verile     | Research and Development |  6545.680000 |
| Noble      | Research and Development |  6545.680000 |
| Erminie    | Research and Development |  6545.680000 |
| Janith     | Research and Development |  6545.680000 |
+------------+--------------------------+--------------+
20 rows in set (0.00 sec)
```

###. Find the highest salary by department


```
mysql> with rank_tbl as (
    -> select *, rank() over (partition by department order by salary desc) as sal_rank
    -> from emp2 )
    -> select * from rank_tbl r where r.sal_rank = 2;
+----+------------+-----------+--------------------------+----------+------------+----------+
| id | first_name | last_name | department               | salary   | manager_id | sal_rank |
+----+------------+-----------+--------------------------+----------+------------+----------+
| 17 | Loralie    | Koop      | Accounting               |  5248.46 |          7 |        2 |
|  9 | Lorne      | Philipsen | Engineering              |  7235.59 |          3 |        2 |
| 18 | Cal        | Andrey    | Management Board         | 11258.82 |       NULL |        2 |
| 11 | Brina      | Dillinger | Marketing                |  6512.17 |          2 |        2 |
| 13 | Noble      | Geerling  | Research and Development |  8391.18 |         20 |        2 |
+----+------------+-----------+--------------------------+----------+------------+----------+
5 rows in set (0.00 sec)
```


--- 

### Recursive CTE Examples

####. Generating sequence upto 10 without using any function
```
WITH RECURSIVE num as (
select 1 as n

union all 
select n+1 as n from num where n<10

) 

select * from num;
```
#####. Output
```
+------+
| n    |
+------+
|    1 |
|    2 |
|    3 |
|    4 |
|    5 |
|    6 |
|    7 |
|    8 |
|    9 |
|   10 |
+------+
10 rows in set (0.00 sec)
```

####. Create simple database for understanding manager hierarchy

```sql
CREATE TABLE emp3 (
    emp_id INT NOT NULL PRIMARY KEY,
    emp_name VARCHAR(50) NOT NULL,
    manager_id INT
);

INSERT INTO emp3 (emp_id, emp_name, manager_id) VALUES
(1, 'Madhav', NULL),
(2, 'Sam', 1),
(3, 'Tom', 2),
(4, 'Arjun', NULL),  -- Changed manager_id to NULL since 6 does not exist
(5, 'Shiva', 4),
(6, 'Keshav', 1),
(7, 'Damodar', 5);

```

####. Creating manager hierarchy
```
select * from man;

with recursive man as (

select * from emp3 where emp_id = 7 

union all

select emp3.* from emp3 inner join man on emp3.emp_id = man.manager_id
)
select * from man;
```
#####. Output
```
+--------+----------+------------+
| emp_id | emp_name | manager_id |
+--------+----------+------------+
|      7 | Damodar  |          5 |
|      5 | Shiva    |          4 |
|      4 | Arjun    |       NULL |
+--------+----------+------------+
3 rows in set (0.00 sec)
```


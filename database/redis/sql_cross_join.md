# Learning cross join in SQL

#### 1. Creating a table and inserting data to work with
```sql
create table A ( A varchar(20);
insert into A valus ('A'), ('B');
```

```
mysql> select * from A;
+------+
| A    |
+------+
| A    |
| B    |
+------+
2 rows in set (0.00 sec)
```

#### 2. Creating all order pairs
**Rows count: n^2**

```sql
select * from A a1 cross join A a2;
```

##### Output
```
mysql> select * from A a1 cross join A a2;
+------+------+
| A    | A    |
+------+------+
| B    | A    |
| A    | A    |
| B    | B    |
| A    | B    |
+------+------+
4 rows in set (0.00 sec)
```

---

#### 3. Creating all permutations
```sql
select * from A a1 cross join A a2 on a1.A < a2.A;
select * from A a1 cross join A a2 on a1.A > a2.A;
```

##### Output
```
mysql> select * from A a1 cross join A a2 on a1.A < a2.A;
+------+------+
| A    | A    |
+------+------+
| A    | B    |
+------+------+
1 row in set (0.00 sec)

mysql> select * from A a1 cross join A a2 on a1.A > a2.A;
+------+------+
| A    | A    |
+------+------+
| B    | A    |
+------+------+
1 row in set (0.00 sec)
```

### Summary
- The `CROSS JOIN` without any condition would normally return all ordered pairs (`(A, A)`, `(A, B)`, `(B, A)`, `(B, B)`).
- By applying the condition `a1.A < a2.A`, you filter out all pairs where the first value is not less than the second, leaving only `(A, B)`.
- By applying the condition `a1.A > a2.A`, you filter out all pairs where the first value is not greater than the second, leaving only `(B, A)`.

These queries do **not generate all possible ordered pairs**, but instead filter out pairs based on the condition (`<` or `>`), leaving only valid permutations where the order matters.

NOTE> I'm not entirely clearn with this

---

### Famous Questions that are important for placements exams and interview

- Create a round robin of teams. Eg. IPL teams (done in class)
- 


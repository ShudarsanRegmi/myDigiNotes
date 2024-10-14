# Join Practice


# Setup prac env

```
CREATE TABLE Students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(50),
    age INT,
    department VARCHAR(50)
);

INSERT INTO Students (student_id, student_name, age, department)
VALUES 
(1, 'John Doe', 20, 'Computer Science'),
(2, 'Jane Smith', 22, 'Mathematics'),
(3, 'Robert Brown', 21, 'Physics'),
(4, 'Lucy White', 23, 'Mathematics'),
(5, 'Michael Green', 20, 'Computer Science');

CREATE TABLE Courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(50),
    teacher_id INT
);

INSERT INTO Courses (course_id, course_name, teacher_id)
VALUES
(101, 'Database Systems', 1),
(102, 'Calculus', 2),
(103, 'Physics 101', 3),
(104, 'Machine Learning', 1),
(105, 'Linear Algebra', 2);

CREATE TABLE Teachers (
    teacher_id INT PRIMARY KEY,
    teacher_name VARCHAR(50),
    department VARCHAR(50)
);

INSERT INTO Teachers (teacher_id, teacher_name, department)
VALUES
(1, 'Dr. Alan Turing', 'Computer Science'),
(2, 'Dr. Isaac Newton', 'Mathematics'),
(3, 'Dr. Marie Curie', 'Physics');

CREATE TABLE Enrollments (
    enrollment_id INT PRIMARY KEY,
    student_id INT,
    course_id INT,
    enrollment_date DATE
);

INSERT INTO Enrollments (enrollment_id, student_id, course_id, enrollment_date)
VALUES
(1, 1, 101, '2023-01-15'),
(2, 1, 104, '2023-02-10'),
(3, 2, 102, '2023-01-20'),
(4, 3, 103, '2023-03-05'),
(5, 4, 105, '2023-01-25'),
(6, 5, 101, '2023-01-17'),
(7, 5, 104, '2023-03-12');

```

```
mysql> show tables;
+-----------------+
| Tables_in_joinp |
+-----------------+
| courses         | 
| enrollments     |
| students        |
| teachers        |
+-----------------+
4 rows in set (0.00 sec)

mysql> select * from students;
+------------+---------------+------+------------------+
| student_id | student_name  | age  | department       |
+------------+---------------+------+------------------+
|          1 | John Doe      |   20 | Computer Science |
|          2 | Jane Smith    |   22 | Mathematics      |
|          3 | Robert Brown  |   21 | Physics          |
|          4 | Lucy White    |   23 | Mathematics      |
|          5 | Michael Green |   20 | Computer Science |
+------------+---------------+------+------------------+
5 rows in set (0.00 sec)

mysql> select * from teachers;
+------------+------------------+------------------+
| teacher_id | teacher_name     | department       |
+------------+------------------+------------------+
|          1 | Dr. Alan Turing  | Computer Science |
|          2 | Dr. Isaac Newton | Mathematics      |
|          3 | Dr. Marie Curie  | Physics          |
+------------+------------------+------------------+
3 rows in set (0.00 sec)

mysql> select * from courses;
+-----------+------------------+------------+
| course_id | course_name      | teacher_id |
+-----------+------------------+------------+
|       101 | Database Systems |          1 |
|       102 | Calculus         |          2 |
|       103 | Physics 101      |          3 |
|       104 | Machine Learning |          1 |
|       105 | Linear Algebra   |          2 |
+-----------+------------------+------------+
5 rows in set (0.00 sec)

mysql> select * from enrollments;
+---------------+------------+-----------+-----------------+
| enrollment_id | student_id | course_id | enrollment_date |
+---------------+------------+-----------+-----------------+
|             1 |          1 |       101 | 2023-01-15      |
|             2 |          1 |       104 | 2023-02-10      |
|             3 |          2 |       102 | 2023-01-20      |
|             4 |          3 |       103 | 2023-03-05      |
|             5 |          4 |       105 | 2023-01-25      |
|             6 |          5 |       101 | 2023-01-17      |
|             7 |          5 |       104 | 2023-03-12      |
+---------------+------------+-----------+-----------------+
7 rows in set (0.00 sec)
```

#### 1. List all the students along with the courses they are enrolled in 

```
select s.student_name, c.course_name, e.enrollment_date
from students s inner join enrollments e on s.student_id =e.student_id
inner join courses c on e.course_id = c.course_id;
```

##### Output
```
+---------------+-----------+------------------+-----------------+
| student_name  | course_id | course_name      | enrollment_date |
+---------------+-----------+------------------+-----------------+
| John Doe      |       101 | Database Systems | 2023-01-15      |
| John Doe      |       104 | Machine Learning | 2023-02-10      |
| Jane Smith    |       102 | Calculus         | 2023-01-20      |
| Robert Brown  |       103 | Physics 101      | 2023-03-05      |
| Lucy White    |       105 | Linear Algebra   | 2023-01-25      |
| Michael Green |       101 | Database Systems | 2023-01-17      |
| Michael Green |       104 | Machine Learning | 2023-03-12      |
+---------------+-----------+------------------+-----------------+
7 rows in set (0.00 sec)
```

#### 2. Select students who have not enrolled in any courses

```sql
select s.* , e.* from students s left join enrollments e on s.student_id = e.student_id having e.student_id is null;
```

##### Output

```sql
# an entry was inserted for the student; He didn't enroll any course
mysql> select s.* , e.* from students s left join enrollments e on s.student_id = e.student_id having e.student_id is null;
+------------+--------------+------+---------------+---------------+------------+-----------+-----------------+
| student_id | student_name | age  | department    | enrollment_id | student_id | course_id | enrollment_date |
+------------+--------------+------+---------------+---------------+------------+-----------+-----------------+
|          6 | ram          |   20 | Cybersecurity |          NULL |       NULL |      NULL | NULL            |
+------------+--------------+------+---------------+---------------+------------+-----------+-----------------+
1 row in set (0.00 sec)
```

  #### 3. Get a list of all courses along with the names of their teachers.

```sql
SELECT course_name, teacher_name
FROM Courses
INNER JOIN Teachers ON Courses.teacher_id = Teachers.teacher_id;
```




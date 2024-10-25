# Note for SubQueries



## Purpose
- Filtering rows
- Calculating aggregate values
- They can be used in the SELECT, WHERE, FROM, and HAVING clauses and can return single or multiple rows and columns.

## Types
- Single row Sub Query - used for comparision of single values
- 

## Lab Setup


```sql
-- Step 1: Create a Database
CREATE DATABASE PracticeDB;
USE PracticeDB;

-- Step 2: Create Tables

-- 1. Departments Table
CREATE TABLE departments (
    department_id INT PRIMARY KEY AUTO_INCREMENT,
    department_name VARCHAR(50) NOT NULL,
    location VARCHAR(50)
);

-- 2. Employees Table
CREATE TABLE employees (
    employee_id INT PRIMARY KEY AUTO_INCREMENT,
    employee_name VARCHAR(50) NOT NULL,
    department_id INT,
    salary DECIMAL(10, 2),
    hire_date DATE,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

-- 3. Products Table
CREATE TABLE products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(50) NOT NULL,
    category VARCHAR(50),
    price DECIMAL(10, 2)
);

-- 4. Orders Table
CREATE TABLE orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    product_id INT,
    quantity INT,
    order_date DATE,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Step 3: Insert Sample Data

-- 1. Insert Data into Departments
INSERT INTO departments (department_name, location) VALUES
    ('Sales', 'New York'),
    ('Engineering', 'San Francisco'),
    ('HR', 'London'),
    ('Marketing', 'Berlin'),
    ('Support', 'New York');

-- 2. Insert Data into Employees
INSERT INTO employees (employee_name, department_id, salary, hire_date) VALUES
    ('Alice Johnson', 1, 75000, '2018-05-23'),
    ('Bob Smith', 2, 120000, '2017-08-11'),
    ('Carol White', 2, 105000, '2019-11-17'),
    ('Dave Brown', 3, 67000, '2020-01-12'),
    ('Eve Black', 1, 85000, '2016-03-15'),
    ('Frank Green', 4, 54000, '2021-09-25'),
    ('Grace Lee', 5, 62000, '2019-12-20'),
    ('Henry Miller', 1, 76000, '2018-07-30');

-- 3. Insert Data into Products
INSERT INTO products (product_name, category, price) VALUES
    ('Laptop', 'Electronics', 1200.00),
    ('Smartphone', 'Electronics', 800.00),
    ('Desk', 'Furniture', 150.00),
    ('Chair', 'Furniture', 100.00),
    ('Tablet', 'Electronics', 300.00),
    ('Bookcase', 'Furniture', 200.00),
    ('Headphones', 'Accessories', 50.00),
    ('Smartwatch', 'Electronics', 250.00);

-- 4. Insert Data into Orders
INSERT INTO orders (product_id, quantity, order_date) VALUES
    (1, 5, '2023-02-15'),
    (2, 3, '2023-02-16'),
    (3, 10, '2023-02-17'),
    (4, 4, '2023-02-18'),
    (5, 2, '2023-02-19'),
    (6, 6, '2023-02-20'),
    (7, 8, '2023-02-21'),
    (8, 3, '2023-02-22');
```


Here's a comprehensive guide on SQL subqueries, designed to help you explore subquery types, use cases, and advanced techniques. We’ll cover the basics to advanced concepts and add hands-on practice questions for each type.

### Overview of SQL Subqueries
A subquery (also called an inner query or nested query) is a query embedded within another SQL query. Subqueries help with retrieving data for specific purposes, such as filtering rows or calculating aggregate values. They can be used in the `SELECT`, `WHERE`, `FROM`, and `HAVING` clauses and can return single or multiple rows and columns.

#### Basic Structure of a Subquery
A subquery is often enclosed within parentheses `()` and can be placed within:
- `SELECT`: For retrieving data to be used as columns.
- `WHERE`: For filtering rows based on complex conditions.
- `FROM`: For treating the subquery result as a table (called an inline view).
- `HAVING`: For setting conditions on aggregate data.

**Syntax Example**:
```sql
SELECT column_name
FROM table_name
WHERE column_name OPERATOR (SELECT column_name FROM another_table);
```

### Types of Subqueries
1. **Single Row Subquery**
2. **Multiple Row Subquery**
3. **Multiple Column Subquery**
4. **Correlated Subquery**
5. **Exists Subquery**
6. **Nested Subquery**

### 1. Single Row Subquery
A **Single Row Subquery** returns a single value (one row and one column) and can be used with comparison operators such as `=`, `<`, `>`, `<=`, and `>=`.

**Example**:
```sql
SELECT employee_name
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);
```

#### Practice Question:
- **Find employees whose salary is higher than the average salary of the department.**
    - *Hint*: Use a subquery in the `WHERE` clause to get the average department salary.

### 2. Multiple Row Subquery
**Multiple Row Subquery** returns multiple values (more than one row, single column) and requires operators such as `IN`, `ANY`, or `ALL`.

**Example with IN**:
```sql
SELECT employee_name
FROM employees
WHERE department_id IN (SELECT department_id FROM departments WHERE location = 'New York');
```

#### Practice Questions:
- **Retrieve the names of employees who work in departments located in 'London' or 'Berlin'.**
- **Find products whose price is higher than the price of any product in category 'A'.**

### 3. Multiple Column Subquery
A **Multiple Column Subquery** returns more than one column and can be used with operators like `IN` or compared with tuples.

**Example**:
```sql
SELECT employee_name, department_id
FROM employees
WHERE (department_id, salary) IN (SELECT department_id, MAX(salary) FROM employees GROUP BY department_id);
```

#### Practice Questions:
- **Find employees who have the maximum salary in their department.**
- **Retrieve pairs of employees and departments where the department has the highest average employee age.**

### 4. Correlated Subquery
A **Correlated Subquery** refers to columns in the outer query, meaning it is evaluated once for each row processed by the outer query.

**Example**:
```sql
SELECT employee_name, salary
FROM employees e1
WHERE salary > (SELECT AVG(salary) FROM employees e2 WHERE e2.department_id = e1.department_id);
```

#### Practice Questions:
- **List employees whose salary is higher than the average salary of their department.**
- **Retrieve employees who have worked on more projects than the average number of projects for all employees.**

### 5. EXISTS Subquery
The **EXISTS** keyword is used to check the presence of rows returned by a subquery. If the subquery returns any rows, EXISTS evaluates to true; otherwise, it returns false.

**Example**:
```sql
SELECT department_name
FROM departments d
WHERE EXISTS (SELECT 1 FROM employees e WHERE e.department_id = d.department_id);
```

#### Practice Questions:
- **Find departments that have employees.**
- **Retrieve products that have been ordered at least once.**

### 6. Nested Subqueries
A **Nested Subquery** is simply a subquery within another subquery and is evaluated from the innermost to the outermost.

**Example**:
```sql
SELECT employee_name
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees WHERE department_id = 
    (SELECT department_id FROM departments WHERE department_name = 'Sales'));
```

#### Practice Questions:
- **Retrieve employees with a salary higher than the average salary of those in the 'Engineering' department.**
- **List products that have a price greater than the average price of products in the same category as 'ProductX'.**

### Advanced Subquery Use Cases
1. **Using Subquery in FROM Clause (Inline Views)**:
   Inline views are subqueries in the `FROM` clause that act as temporary tables.

   **Example**:
   ```sql
   SELECT department_id, AVG(salary)
   FROM (SELECT department_id, salary FROM employees WHERE hire_date > '2020-01-01') AS recent_hires
   GROUP BY department_id;
   ```

2. **Using Subqueries with Aggregations and GROUP BY**:
   Subqueries can calculate values to use in `GROUP BY` clauses.

   **Example**:
   ```sql
   SELECT department_id, COUNT(*)
   FROM employees
   GROUP BY department_id
   HAVING COUNT(*) > (SELECT AVG(emp_count) FROM (SELECT department_id, COUNT(*) AS emp_count FROM employees GROUP BY department_id) AS dept_counts);
   ```

#### Practice Questions:
- **Find departments with a number of employees above the average department employee count.**
- **Calculate the difference between each employee’s salary and the average salary of their department.**

### Tips for Working with Subqueries
1. **Identify the Purpose**: Decide what the subquery should return (single value, multiple values, multiple columns).
2. **Choose the Right Operator**: Use `IN` for multiple rows, `EXISTS` for checking existence, and `=`, `>`, etc., for single values.
3. **Optimize for Performance**: For large data sets, try to minimize the use of correlated subqueries and prefer `JOIN` where possible.
4. **Debug Incrementally**: Test subqueries independently before adding them into the main query.

### Practice Setup Questions

To make this hands-on:
1. **Create a Database**:
   - Set up tables: `employees`, `departments`, `products`, `orders`, etc., with some data.

2. **Data Insertion Exercise**:
   - Insert data into `employees` with columns for `id`, `name`, `department_id`, `salary`, `hire_date`, etc.
   - Add departments with `id`, `name`, `location`.
   - Populate `products` with `id`, `name`, `category`, `price`.

3. **Practice Query Set**:
   - Retrieve employee details based on various department conditions.
   - Find top-paid employees, average salaries, and comparisons.
   - Test the results of `EXISTS` subqueries by removing specific data (e.g., deleting orders for a product) and rerunning the query.

These exercises will solidify your understanding by providing diverse examples across use cases. Let me know if you'd like further examples on specific subquery types!

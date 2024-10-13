# Notes for windowing funtions in SQL

### Windowing Functions in SQL: A Beginner’s Guide

Windowing functions in SQL are powerful tools that allow you to perform calculations across a set of table rows related to the current row. Unlike aggregate functions (like `SUM`, `AVG`, etc.), which return a single result for a group of rows, window functions return a result for **every row** in the result set.

Let’s start with the basics:

### 1. **What is a Window Function?**
A **window function** operates over a window of rows, meaning it can compute values based on the data from multiple rows but still returns a value for each row. The key idea is that these functions give you a “moving window” of data to operate on, based on how you define the "window".

Window functions require two components:
- **An aggregate or ranking function** (like `SUM()`, `ROW_NUMBER()`, etc.)
- **A window** defined by the `OVER` clause, which specifies how rows are grouped or ordered for the calculation.

### 2. **Basic Syntax of Window Functions**
```sql
<window_function>() OVER (
    [PARTITION BY <column(s)>]
    [ORDER BY <column(s)>]
    [frame_specification]
)
```

### 3. **Key Components of Window Functions**

#### a. `PARTITION BY`
The `PARTITION BY` clause divides the result set into partitions or groups. The window function is applied to each partition independently. It’s like grouping data but without collapsing it into a single row like `GROUP BY`.

#### b. `ORDER BY`
The `ORDER BY` clause defines the order in which the rows are processed within each partition (or across the whole dataset if there’s no partition). This is crucial for functions like `ROW_NUMBER()` or `RANK()` that require an ordered list.

#### c. `Frame Specification`
The frame specification defines the range of rows the window function should consider. You can think of this as defining the size and direction of the "window" of rows for each calculation. Some common options are:
- `ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`
- `ROWS BETWEEN 1 PRECEDING AND CURRENT ROW`

### 4. **Types of Window Functions**

Here are the most common window functions you'll encounter:

#### a. **Aggregate Functions as Window Functions**
These include functions like `SUM()`, `AVG()`, `COUNT()`, `MIN()`, and `MAX()`. When used with a window, they don’t collapse the result into a single row like normal aggregates, but instead provide a running total or calculation for each row.

Example:
```sql
SELECT 
    employee_name,
    salary,
    SUM(salary) OVER (PARTITION BY department_id ORDER BY salary) AS cumulative_salary
FROM employees;
```

- **PARTITION BY**: Groups the rows by department.
- **ORDER BY**: Orders rows by salary within each department.
- **SUM()**: Calculates a running sum for each row in the partition.

#### b. **Ranking Functions**
These functions assign a rank or number to each row based on its position in a sorted list:
- `ROW_NUMBER()`: Assigns a unique row number to each row.
- `RANK()`: Assigns a rank, but ties get the same rank, and the next rank is skipped.
- `DENSE_RANK()`: Similar to `RANK()`, but the next rank is not skipped for ties.

Example:
```sql
SELECT 
    employee_name,
    department_id,
    salary,
    ROW_NUMBER() OVER (PARTITION BY department_id ORDER BY salary DESC) AS row_number,
    RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) AS rank,
    DENSE_RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) AS dense_rank
FROM employees;
```

- **ROW_NUMBER()**: Sequential row numbers, even for ties.
- **RANK()**: Gives the same rank to tied rows, but skips ranks.
- **DENSE_RANK()**: Gives the same rank to tied rows but does not skip ranks.

#### c. **Value Functions**
- `LAG()`: Returns the value of a previous row in the result set, based on the current row.
- `LEAD()`: Returns the value of a subsequent row in the result set, based on the current row.
  
Example:
```sql
SELECT 
    employee_name,
    salary,
    LAG(salary, 1) OVER (ORDER BY hire_date) AS previous_salary,
    LEAD(salary, 1) OVER (ORDER BY hire_date) AS next_salary
FROM employees;
```

- **LAG(salary, 1)**: Returns the salary of the previous row (in the order specified).
- **LEAD(salary, 1)**: Returns the salary of the next row.

### 5. **Understanding Frame Specifications**

The frame specifies the subset of rows within a partition that the window function should operate on. For example, you can define a moving window for a running total or a moving average.

Common options include:
- `ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`: Includes all rows from the start of the partition to the current row.
- `ROWS BETWEEN 1 PRECEDING AND CURRENT ROW`: Includes the current row and the one before it.

Example of cumulative sum:
```sql
SELECT 
    employee_name,
    salary,
    SUM(salary) OVER (ORDER BY hire_date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_total
FROM employees;
```
Here, for each row, `SUM()` will compute the sum of all rows up to and including the current row, creating a running total.

### 6. **Practical Examples**

#### a. **Calculating a Running Total**
```sql
SELECT 
    customer_id,
    order_date,
    amount,
    SUM(amount) OVER (ORDER BY order_date) AS running_total
FROM orders;
```

#### b. **Finding the Nth Highest Salary**
```sql
SELECT * FROM (
    SELECT 
        employee_name,
        salary,
        DENSE_RANK() OVER (ORDER BY salary DESC) AS salary_rank
    FROM employees
) ranked_salaries
WHERE salary_rank = 3;
```
This will return the employee(s) with the 3rd highest salary.

### 7. **When to Use Window Functions?**
- When you need to perform calculations across a set of rows without reducing the number of rows (unlike `GROUP BY`).
- To calculate running totals, moving averages, or cumulative sums.
- To rank or number rows within a specific partition or dataset.
- To access values from preceding or following rows in the result set.

### Conclusion

Window functions are essential for writing efficient and expressive SQL queries. They allow you to perform complex calculations over sets of rows while maintaining the individual row structure. By mastering `PARTITION BY`, `ORDER BY`, and frame specifications, you’ll have more control over your SQL queries and gain the ability to write powerful, insightful reports.

---
# Getting  Hands Dirty

Great! Let's dive into some hands-on examples of SQL window functions. We'll create a sample database with a couple of tables and populate them with data. You'll then be able to practice using window functions on this data.

### Sample Tables

We'll create two tables:

1. **Employees**: Contains employee details such as their names, department IDs, salaries, and hire dates.
2. **Sales**: Contains sales records, including the sales amount and the date of the sale.

### Step 1: Create the Tables

Here's the SQL to create the two tables:

```sql
-- Create Employees table
CREATE TABLE Employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(100),
    department_id INT,
    salary DECIMAL(10, 2),
    hire_date DATE
);

-- Create Sales table
CREATE TABLE Sales (
    sale_id INT PRIMARY KEY,
    employee_id INT,
    sale_date DATE,
    amount DECIMAL(10, 2),
    FOREIGN KEY (employee_id) REFERENCES Employees(employee_id)
);
```

### Step 2: Insert Sample Data

Now, let's insert some sample data into these tables.

```sql
-- Insert data into Employees
INSERT INTO Employees (employee_id, employee_name, department_id, salary, hire_date) VALUES
(1, 'Alice', 1, 60000.00, '2020-01-15'),
(2, 'Bob', 1, 50000.00, '2019-03-22'),
(3, 'Charlie', 2, 70000.00, '2021-07-30'),
(4, 'David', 2, 55000.00, '2018-05-15'),
(5, 'Eva', 1, 62000.00, '2022-02-01');

-- Insert data into Sales
INSERT INTO Sales (sale_id, employee_id, sale_date, amount) VALUES
(1, 1, '2023-01-05', 2000.00),
(2, 1, '2023-01-10', 3000.00),
(3, 2, '2023-01-08', 1500.00),
(4, 2, '2023-01-15', 2500.00),
(5, 3, '2023-01-12', 4000.00),
(6, 3, '2023-01-20', 3500.00),
(7, 4, '2023-01-25', 1800.00),
(8, 5, '2023-01-30', 3200.00);
```

### Step 3: Practice Queries Using Window Functions

Now that you have the tables and data set up, here are some practice queries using window functions.

#### 1. **Calculate Running Total of Sales**
This query calculates a running total of sales amounts for each employee based on the sale date.

```sql
SELECT 
    employee_id,
    sale_date,
    amount,
    SUM(amount) OVER (PARTITION BY employee_id ORDER BY sale_date) AS running_total
FROM Sales
ORDER BY employee_id, sale_date;
```

#### 2. **Rank Employees by Salary**
This query assigns a rank to each employee based on their salary within each department.

```sql
SELECT 
    employee_id,
    employee_name,
    department_id,
    salary,
    RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) AS salary_rank
FROM Employees
ORDER BY department_id, salary_rank;
```

#### 3. **Find Previous Sale Amount**
This query shows each sale along with the previous sale amount for the same employee.

```sql
SELECT 
    employee_id,
    sale_date,
    amount,
    LAG(amount, 1) OVER (PARTITION BY employee_id ORDER BY sale_date) AS previous_sale
FROM Sales
ORDER BY employee_id, sale_date;
```

#### 4. **Calculate Average Salary by Department**
This query calculates the average salary of employees within each department and displays it alongside each employee's salary.

```sql
SELECT 
    employee_id,
    employee_name,
    department_id,
    salary,
    AVG(salary) OVER (PARTITION BY department_id) AS avg_salary
FROM Employees
ORDER BY department_id, employee_id;
```

#### 5. **Calculate Cumulative Sales Amount by Date**
This query computes the cumulative sales amount across all employees, ordered by the sale date.

```sql
SELECT 
    sale_date,
    SUM(amount) OVER (ORDER BY sale_date) AS cumulative_sales
FROM Sales
ORDER BY sale_date;
```

### Step 4: Run and Experiment

1. **Create the tables** in your SQL environment using the provided SQL commands.
2. **Insert the sample data** into the tables.
3. **Execute each of the practice queries** to see the results. 
4. Feel free to modify the queries or add new data to see how the window functions behave under different scenarios.

### Conclusion

By working through these exercises, you'll get hands-on experience with window functions in SQL. If you have any questions about the queries or need further examples, feel free to ask!

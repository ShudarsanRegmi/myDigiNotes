# Architecture of DBMS

![image](https://github.com/user-attachments/assets/d8e850ca-186f-4a3a-a6f9-ea646897cb79)

The diagram illustrates the architecture of a **Database Management System (DBMS)**, showing how different components interact within the system. Let’s go step by step, following the workflow from top to bottom:

### 1. **DBA (Database Administrator)**
   - The DBA is responsible for managing the **database schema** (structure of the database). The DBA provides the schema to the **DDL Compiler**.

### 2. **Users**
   - Users interact with the system by sending **queries** to retrieve or modify data. These queries are processed by the **Query Processor**.

### 3. **Application Programs**
   - Applications interact with the database through a **DML (Data Manipulation Language) Compiler**. Application programs generate commands to insert, update, or delete data, which are processed by the DBMS.

### 4. **DDL Compiler (Data Definition Language Compiler)**
   - The DDL compiler takes the **schema definitions** provided by the DBA and compiles them. These compiled definitions are stored in the **Data Dictionary**, which is managed by the **Data Dictionary Manager**.
   - The **Data Dictionary Manager** stores metadata about the database, including details about tables, relationships, constraints, etc.

### 5. **Data Dictionary Manager**
   - This component maintains the **Data Dictionary**, which is essential for managing database schema information. It provides the necessary metadata to other components like the **Authorization Control**.

### 6. **Authorization Control**
   - This ensures that only authorized users can access or modify the data. It checks whether the user has the necessary permissions to execute the commands or queries.

### 7. **Query Processor**
   - This component handles the **queries** coming from users. It parses the queries and ensures they are correctly structured.
   - After parsing, the **Query Optimizer** optimizes the query to ensure efficient execution by finding the best strategy to access data (e.g., choosing the fastest path for retrieving data from tables).

### 8. **Query Optimizer**
   - This module optimizes SQL queries by analyzing various execution strategies. It ensures the queries are executed in the most efficient manner, based on factors like data storage and indexing.

### 9. **Command Processor**
   - This is the central unit that coordinates the processing of the user commands after authorization and query optimization. The command processor interacts with the **Transaction Manager** and **Integrity Checker**.

### 10. **Integrity Checker**
   - This module ensures the integrity of the data. It checks that operations like insertions or updates do not violate integrity constraints (e.g., foreign key constraints, data types, etc.).

### 11. **Transaction Manager**
   - It manages the execution of transactions. A transaction is a set of operations that must either all succeed or fail (atomicity). The **Transaction Manager** ensures **ACID properties** (Atomicity, Consistency, Isolation, Durability) are maintained, guaranteeing reliable execution of transactions.

### 12. **Scheduler**
   - This component handles the scheduling of tasks and transactions. It ensures **concurrency control**, meaning it manages the order of transactions to avoid conflicts, especially when multiple users are accessing or modifying the data at the same time.

### 13. **Recovery Manager**
   - This is responsible for **recovering the database** in case of a system failure. It ensures that any incomplete or failed transactions are properly rolled back or that committed transactions are not lost.

### 14. **Buffer Manager**
   - The **Buffer Manager** handles the **buffering of data** in memory to optimize data access from the disk. It acts as an interface between the **physical data storage (data files)** and the in-memory data that is processed by the DBMS.
   
### 15. **Data Files + Data Dictionary**
   - These are the physical storage units where the actual data and metadata are stored. The **Data Manager** oversees interaction with these files to read, write, or update data.

### Summary of Workflow:
- **DBA** defines the schema → **DDL Compiler** compiles schema → stored in **Data Dictionary**.
- **Users** issue queries → **Query Processor** processes the query → **Authorization Control** checks permissions → **Command Processor** coordinates execution with the **Query Optimizer** and other components.
- The **Integrity Checker** ensures constraints are respected. The **Transaction Manager** ensures transactions are processed correctly, and the **Scheduler** manages concurrency.
- **Data** is retrieved/updated from **Data Files** through the **Buffer Manager**, and in case of failures, the **Recovery Manager** ensures the database is restored to a consistent state.

This layered architecture ensures that a DBMS can efficiently manage, store, and retrieve large volumes of data while ensuring security, integrity, and reliability.

# Hands on

Since you have worked with MySQL, you're already familiar with how to use the database on the surface. To explore the **underlying architecture** of MySQL, we can perform several practical tasks to understand how MySQL handles **storage**, **queries**, **transactions**, **buffering**, and **recovery**. I'll guide you through these tasks, focusing on MySQL's internal components like storage engines, buffer pools, transaction handling, and query optimization.

Here's a breakdown of the hands-on exploration:

### 1. **Explore MySQL Storage Engines**
   MySQL supports various storage engines, such as **InnoDB**, **MyISAM**, etc. Each storage engine has its unique way of handling data storage, indexes, and transactions.

   #### Task:
   - **Check available storage engines:**
     You can check what storage engines are available in your MySQL installation using this query:
     ```sql
     SHOW ENGINES;
     ```
     This will give you a list of supported engines like **InnoDB**, **MyISAM**, and others. Pay attention to their support for transactions, foreign keys, and more.

   - **Check storage engine of a table:**
     To check which storage engine a specific table is using, run:
     ```sql
     SHOW TABLE STATUS LIKE 'your_table_name';
     ```
     This will display information about the table, including the storage engine used.

   - **Switch storage engines:**
     You can create tables using different engines and observe their behavior. For example:
     ```sql
     CREATE TABLE test_innodb (
       id INT PRIMARY KEY,
       name VARCHAR(50)
     ) ENGINE=InnoDB;

     CREATE TABLE test_myisam (
       id INT PRIMARY KEY,
       name VARCHAR(50)
     ) ENGINE=MyISAM;
     ```

     Compare how **InnoDB** supports transactions and foreign keys, while **MyISAM** doesn’t.

### 2. **Query Optimizer and Execution Plans**
   The MySQL **Query Optimizer** plays a key role in determining how queries are executed. You can use the **EXPLAIN** command to see how MySQL is planning to execute a query.

   #### Task:
   - **Use EXPLAIN to view query execution plans:**
     ```sql
     EXPLAIN SELECT * FROM test_innodb WHERE name = 'John';
     ```
     This will give you details about the execution plan, such as which indexes are being used, whether a full table scan is performed, etc.

   - **Optimize Queries:**
     Create an index on your table and run the **EXPLAIN** command again to see how MySQL changes its query execution strategy:
     ```sql
     CREATE INDEX idx_name ON test_innodb(name);
     EXPLAIN SELECT * FROM test_innodb WHERE name = 'John';
     ```

     You should notice that MySQL will now use the index, making the query more efficient.

### 3. **Buffer Pool (Memory Management)**
   MySQL uses a **Buffer Pool** to store frequently accessed data in memory, reducing disk I/O. Exploring how the buffer pool works can help you understand performance optimizations.

   #### Task:
   - **Monitor the Buffer Pool:**
     First, ensure that you are using the **InnoDB** storage engine, as the buffer pool is an InnoDB feature. Run the following command to view buffer pool status:
     ```sql
     SHOW ENGINE INNODB STATUS;
     ```

     This command provides detailed information about the buffer pool size, page hits, and how efficiently the buffer pool is working. The more hits you have, the less MySQL needs to read from disk.

   - **Change Buffer Pool Size:**
     You can modify the buffer pool size in your MySQL configuration file (`my.cnf`) to see how it affects performance. Increase or decrease the size of the buffer pool, restart MySQL, and monitor query performance.
     ```ini
     [mysqld]
     innodb_buffer_pool_size=1G
     ```

### 4. **Transactions and ACID Properties**
   MySQL’s **InnoDB** storage engine supports transactions and guarantees **ACID properties** (Atomicity, Consistency, Isolation, Durability). You can explore these by running multiple transactions and observing how MySQL handles them.

   #### Task:
   - **Test Transactions:**
     ```sql
     START TRANSACTION;
     INSERT INTO test_innodb (id, name) VALUES (1, 'Alice');
     -- Run this and then do NOT commit the transaction yet.
     ```

     In a separate terminal, check if the row is visible:
     ```sql
     SELECT * FROM test_innodb WHERE id = 1;
     ```

     You will see that the uncommitted transaction is not visible to other connections. Now commit or roll back the transaction:
     ```sql
     COMMIT;  -- Or ROLLBACK;
     ```

   - **Observe Locking Behavior:**
     Try running two transactions that attempt to modify the same row and observe how MySQL handles locking to maintain **isolation**:
     ```sql
     -- First transaction
     START TRANSACTION;
     UPDATE test_innodb SET name = 'Bob' WHERE id = 1;

     -- Second transaction in a different connection
     START TRANSACTION;
     UPDATE test_innodb SET name = 'Charlie' WHERE id = 1;
     -- This will block until the first transaction is committed or rolled back.
     ```

### 5. **Recovery Manager**
   MySQL ensures data durability through logging and recovery mechanisms like the **InnoDB redo log**. In case of crashes, it recovers to the last consistent state.

   #### Task:
   - **Crash Recovery Simulation:**
     - Enable the **innodb_flush_log_at_trx_commit** variable to see how MySQL handles durability. Set it to `1` for full durability:
       ```sql
       SET GLOBAL innodb_flush_log_at_trx_commit = 1;
       ```
     - Simulate a crash by stopping the MySQL service abruptly:
       ```bash
       sudo service mysql stop
       ```
     - Restart MySQL and check if it recovers the last committed transaction:
       ```bash
       sudo service mysql start
       ```

### 6. **Analyze Logs for Recovery**
   MySQL maintains logs for transactions, errors, and slow queries. These logs are important for understanding how MySQL handles **recovery** and performance.

   #### Task:
   - **View the Error Log:**
     ```bash
     cat /var/log/mysql/error.log
     ```

     Look for information related to startup, shutdown, and any issues encountered during recovery.

   - **Analyze the Slow Query Log:**
     Enable slow query logging to identify slow queries:
     ```ini
     [mysqld]
     slow_query_log = 1
     slow_query_log_file = /var/log/mysql/mysql-slow.log
     long_query_time = 2  # Log queries taking longer than 2 seconds
     ```

     Restart MySQL and execute slow queries to see them logged in the slow query log file.

---

### Summary of Hands-On Tasks:
- **Storage Engines:** Experiment with different engines like InnoDB and MyISAM.
- **Query Optimizer:** Use **EXPLAIN** to analyze and optimize query execution plans.
- **Buffer Pool:** Explore the **InnoDB buffer pool** and how it impacts performance.
- **Transactions and ACID:** Test how transactions behave and maintain **isolation** using InnoDB.
- **Crash Recovery:** Simulate a MySQL crash and observe how it recovers.
- **Logs:** Monitor the error log, slow query log, and recovery logs for insights into MySQL’s internal operations.

By exploring these hands-on tasks, you'll gain a deeper understanding of how MySQL manages its internal architecture, ensuring performance, reliability, and transaction safety.

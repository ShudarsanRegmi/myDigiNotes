# Choosing the right no sql database


## My Key Ovservations
- Identifying read heavy, write heavy tasks
- Looking for the need of flexible structure and fixed schema
- If there is heavy relationship between datas then graph based database is more suitable
- 



The data model is chosen based on the type of data the component would be dealing with.

This step begins by identifying the most suitable NoSQL category below for each component of the eCommerce system:

a) Key-value stores
b) Column-family stores
c) Document-oriented databases
d) Graph-based databases

### For Basic Overview
![{3BCCAC44-093C-4B6B-A2F1-06EB4ABD998B}](https://github.com/user-attachments/assets/a11c3f7b-bf87-4fa1-a009-2718109ab964)

## Key Value Stores
- Can scale out details into multiple machines
- Way faster than sql based databases as data is stored in disk

### Characterisitcs of a key value stores
- Key is unique and can store value that can be xml, json, binary, text using key-value stores
- Quick lookups (similar to dictionary search)
- Best suited for storing user sessions, customer preferences, browsing patterns and so on
- Data can be distributed among multiple machines

### Limitation: 
- Do not allows retreiving by values or updating only part of the values. Updating, searching and deleting has to be done through keys
- In the scenario when search has to be done based on value then, key-value store cannot be used. In such scenario, column family stores are used

## Column Family Store

## Usecases

- Logging

Problem: Searching Customer by Location
- Key-value stores allow retrieval only by the key (customer_id) and are therefore not suitable
- A better query support is required which is provided by column family stores

## Characteristics of column-family stores

- These databases are structured into group of related columns called Column-Families
- Each column family is a set of data that is often accessed together, for example, customer profile
- These are highly scalable with the ability to take up loads to any extent
- **In column family stores, every row can have a different set of columns unlike relational databases**
- **Very useful for sparsely populated tables (most of the columns having NULL values) and wide rows having too many columns**
- Column family stores optimize memory by ignoring columns with NULL values as illustrated below

![{123ACDE7-0C44-453E-8E69-9B850C6D54E2}](https://github.com/user-attachments/assets/643ed70b-6688-48e6-8500-8f85a58b8f94)

## Limitations of column-family stores 
- It is not possible to query on non-indexed fields, for example, age (assume only customer_id and email_id are the indexed fields)
- Support for read operations is limited compared to SQL. For example, group by operation is not available 
- Also, not suitable for queries involving multiple fields. For example, search for customers with age>20 and city='Chennai'. Use document-oriented databases instead


## Document Oriented Database

### Need or Emergence

For key look ups, key-value stores are fastest.

- For frequently updating data and searching by primary key or indexed keys, column families work very well.
- **But for queries involving multiple fields, creating indexes on many fields is not a good practice. It is also a very costly operation. Hence column family stores are not recommended - - for the given scenario.**
- For scenarios where millions of customers are frequently searching for products based on various criteria (read heavy workloads), document-oriented databases are most suitable.

## Business Need
Requirement 1: Require a flexible structure to store products with varied attributes
Requirement 2: Querying options such as sorting by price, filtering by brand and so on

## Why not SQL? 
- There are products which has varied parameters in terms of type and number. For. Eg. If the product is car set of information related with will be different and if this is mobile set of information associated with it will be different. Even for the same category there can be the need of varied schema. For example.. feature parameter in one phone might not be available in another phone. Therefore, a fixed schema is not helpful in these scenario. We need a flexible schema.

## Why use document-oriented databases?  

- These databases are schema-less - attributes of products in the catalog are varied and keep changing 
- Allows querying by non-indexed fields too - search by any given attribute of the product e.g., model, price
- Supports very rich query language including storing, fetching, modifying, deleting, sorting, and grouping data
- Support aggregations for e.g., sum, count and others string, math and set operations
- Apt for heavy reads - product details are written to the database fewer times than the number of times they are read (searched) by customers
- Hence document-oriented databases are most suitable for the product catalog component of eCommerce.

## Document Oriented Database
- These databases are similar to key-value pairs but with richer querying options that SQL provide

## Limitation
- It cannot represent complex relationship between data

---
## Quiz
There is a massive scale application that needs rich queries over a flexible data model, predictable performance, limitless throughput, and/or global distribution to provide low-latency access to any number of regions over a single data set.

Choose the most appropriate data model for the given scenario.

- SQL database
- Key-value stores
- Column-family
- Document-oriented

---

## Graph Based Databases

### Uses Cases
- Recommendation

### Need or Emergence

Assume, the online retailer wants to do the following:
Keep track of the products you have purchased and suggest which of your friends have liked the same product
Recommend which other product can be purchased along with the product you have chosen
Do you think document-oriented databases is suitable for the given scenarios?
The first requirement needs to link your orders to the orders of other related customers.
The second requirement needs to maintain information about related products.
Both are highly inter-related data.
Hence, for the given requirements, document-oriented databases are not suitable

### Business Need 
- Track related products like smart phone and cover case
- Relate millions of customers and the products they purchase

### Why not SQL?
- SQL may not be suitable for managing complex relationships between millions of customers and their purchased products, such as recommending related items like a phone cover with a smartphone, due to the time-consuming nature of joins.

### Why use Graph Database?
- These databases use simple nodes and edges to store and retrieve highly interrelated data e.g., customer and product
- Graph traversals are much faster compared to SQL joins
- In the given scenario, use graph databases as described below
  - Users and Products are represented as nodes and
  - Purchased relationships are represented as edges
- Graph databases are also used for fraud detection wherein,
  - Customers are represented as nodes and
  - Transactions are represented as edges
  - Transaction paths that are not related to any customer are identified as frauds
 
## Limitations of graph-based databases
- These databases are inappropriate for transactional data like financial accounting
- Do not scale out horizontally
- Difficulty in performing aggregations like sum and max efficiently
- Need to learn a new query language like CYPHER
- Have fewer vendors to choose from, so harder to get technical support

---

## Exercise
Given each of the following scenarios of the online platform for employees to create posts and add comments (refer to exercise 1), identify the appropriate data model based on the type of data each scenario deals with.

Manage employee profile (maintains employee details) 

Manage session (track employee details from the time of login to the time of log out)

Post articles (employees create/edit/delete articles)

Comments (employees view comments on a given post or can post their own comments)

Search (employees search for specific posts)

Recommendations (recommend employees about other related posts)

Reporting (daily/weekly/monthly/yearly usage reports)

Ans:
Appropriate data models identified for the given workloads:

Manage employee profile: Document-oriented for flexible structure  

Manage session: Key-value (maintain session details with quick access)

Post articles: Document-oriented for flexible structure

Comments: Column-family (text based)

Search: Document-oriented (text-based search on different criteria such as date_of_post, title_of_post, employee_based_search and so on)

Recommendations: Graph (highly inter-related data)

Reporting: SQL (structured)

---
## CAP Theorem:

CAP - Consistency Availability and Partition Tolerance

Consistency – An end user should be able to view the latest data at all times
Availability – Every database request must receive a response from the server while it is up and running
Partition tolerance – When two systems cannot talk to each other in the network, it leads to partitions

CAP theorem states that
Only two of the three properties can be guaranteed at the same
Partitions occur only in distributed databases which SQL is not. Hence SQL databases support Consistency and Availability only
NoSQL databases are always partition tolerant and hence you need to choose between Consistency and Availability


---
# CAP Quiz
Choose between consistency and availability for each of the following online employee platform (refer to exercise 1) scenarios:

Manage employee profile (maintains employee details) 

Manage session (track employee details from the time of login to the time of log out)

Post articles (employees create/edit/delete articles)

Comments (employees view comments on a given post or can post their own comments)

Search (employees search for specific posts)

Recommendations (recommend employees about other related posts)

Reporting (daily/weekly/monthly/yearly usage reports)

**ans:**
Choose between consistency and availability for each of the following online employee platform (refer to exercise 1) scenarios:

Manage employee profile (maintains employee details) 

Manage session (track employee details from the time of login to the time of log out)

Post articles (employees create/edit/delete articles)

Comments (employees view comments on a given post or can post their own comments)

Search (employees search for specific posts)

Recommendations (recommend employees about other related posts)

Reporting (daily/weekly/monthly/yearly usage reports)

---
# Read Write Intensive Tasks

The last step in Stage 1 identifies whether your component requires to perform:

too many reads compared to writes or

too many writes compared to reads

Outcome of this step is as shown below.

![{A3651E00-E088-4981-AEEA-A42BAAF848AC}](https://github.com/user-attachments/assets/49451d75-6c3e-4c9a-9578-2f2f9516549b)

--- 
### Quikz
Identify whether each given online employee platform (refer to exercise 1) scenario is read-intensive, write-intensive or both read/write intensive:

Manage employee profile (maintains employee details) 

Manage session (track employee details from the time of login to the time of log out)

Post articles (employees create/edit/delete articles)

Comments (employees view comments on a given post or can post their own comments)

Search (employees search for specific posts)

Recommendations (recommend employees about other related posts)

Reporting (daily/weekly/monthly/yearly usage reports)

### Ans
Manage employee profile: write-heavy as thousands of employee details are being updated onto the database  

Manage session: involves both read and write loads for retrieving session details and tracking changes made during the session

Post articles: involves both read and write loads as existing articles are read by many employees and new articles are continuously posted by various employees

Comments: involves both read and write loads as employees read existing comments on articles and post their own comments

Search: involve heavy reads as employees keep searching for various articles

Recommendations: read-heavy as the system recommends related articles which would be useful to employees

Reporting: read-heavy as reports are being used for analysis of data

### Finally
![{19E086FC-E478-4990-85E4-E9FB0621BEBF}](https://github.com/user-attachments/assets/c505b191-0697-42fa-97a9-92178702e3a5)

# Choosing the right database

In Stage 2, you will be mapping the outcome of Stage 1 to the most suitable NoSQL database based on the required characteristics you are looking for.

 


 
Shopping cart needs a key-value store with high availability and write-intensive - Riak is most suitable

Similarly, for user activity logs - Cassandra is the best fit

For product catalog - MongoDB is most suitable (though consistent by default, it is tuned for availability as required)

The recommendations component is best implemented using Neo4J

![{E5F2621C-C53B-42A8-B887-2348AF3D569C}](https://github.com/user-attachments/assets/f7c4e726-844f-408f-89a6-c67ee0d7edaa)

## Exercise
For each given online employee platform (refer to exercise 1) scenario, choose the most appropriate database.

Manage employee profile (maintains employee details) 

Manage session (track employee details from the time of login to the time of log out)

Post articles (employees create/edit/delete articles)

Comments (employees view comments on a given post or can post their own comments)

Search (employees search for specific posts)

Recommendations (recommend employees about other related posts)

Reporting (daily/weekly/monthly/yearly usage reports)

## Solution
Choosing the suitable database for each given scenario:

Manage employee profile: MongoDB 

Manage session: Redis

Post articles: MongoDB

Comments: Cassandra

Search: MongoDB

Recommendations: Neo4J

Reporting: SQL

### Final Overview
![{B0B21653-DEFA-4989-8599-24DAD004A810}](https://github.com/user-attachments/assets/412a9ab9-2000-4ee1-af44-53288e750109)
   ![{DEFC8DBE-8BB5-4976-B2DD-30A08E2B8FA3}](https://github.com/user-attachments/assets/62155011-e0b8-49be-9b09-adfb71466025)





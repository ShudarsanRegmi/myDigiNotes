# Choosing the Right NoSQL Database

## Key Observations

- Identify read-heavy and write-heavy tasks.
- Determine the need for a flexible structure versus a fixed schema.
- For data with heavy relationships, a graph-based database is more suitable.

The data model is chosen based on the type of data the component would be dealing with. This step begins by identifying the most suitable NoSQL category below for each component of the eCommerce system:

a) Key-value stores
b) Column-family stores
c) Document-oriented databases
d) Graph-based databases

### Basic Overview

![NoSQL Overview](https://github.com/user-attachments/assets/a11c3f7b-bf87-4fa1-a009-2718109ab964)

## Key-Value Stores

### Characteristics
- Can scale out details into multiple machines.
- Faster than SQL-based databases as data is stored in disk.
- Key is unique and can store values in XML, JSON, binary, or text formats.
- Quick lookups (similar to dictionary search).
- Best suited for storing user sessions, customer preferences, browsing patterns, etc.
- Data can be distributed among multiple machines.

### Limitations
- Do not allow retrieval by values or updating only part of the values. Updating, searching, and deleting have to be done through keys.
- Not suitable when searches are based on values. In such scenarios, column-family stores are used.

## Column-Family Stores

### Use Cases
- Logging.

### Problem: Searching Customer by Location
- Key-value stores allow retrieval only by the key (customer_id) and are therefore not suitable.
- A better query support is required which is provided by column-family stores.

### Characteristics
- Databases are structured into groups of related columns called Column-Families.
- Each column family is a set of data that is often accessed together, e.g., customer profile.
- Highly scalable with the ability to handle large loads.
- Every row can have a different set of columns unlike relational databases.
- Useful for sparsely populated tables (most columns having NULL values) and wide rows with many columns.
- Optimize memory by ignoring columns with NULL values.

![Column Family Example](https://github.com/user-attachments/assets/643ed70b-6688-48e6-8500-8f85a58b8f94)

### Limitations
- Not possible to query on non-indexed fields, e.g., age (assume only customer_id and email_id are indexed fields).
- Limited support for read operations compared to SQL, e.g., group by operation is not available.
- Not suitable for queries involving multiple fields, e.g., search for customers with age > 20 and city = 'Chennai'. Use document-oriented databases instead.

## Document-Oriented Databases

### Need or Emergence
- Key-value stores are fastest for key lookups.
- Column families work well for frequently updating data and searching by primary key or indexed keys.
- For queries involving multiple fields, creating indexes on many fields is not a good practice and is costly. Hence, column-family stores are not recommended for this scenario.
- For scenarios where millions of customers frequently search for products based on various criteria (read-heavy workloads), document-oriented databases are most suitable.

### Business Need
- Require a flexible structure to store products with varied attributes.
- Querying options such as sorting by price, filtering by brand, etc.

### Why not SQL?
- Products have varied parameters in terms of type and number. For example, if the product is a car, the set of information related to it will be different compared to a mobile phone. Even within the same category, there can be a need for varied schema. A fixed schema is not helpful in these scenarios; a flexible schema is needed.

### Why Use Document-Oriented Databases?
- Schema-less databases - attributes of products in the catalog are varied and keep changing.
- Allows querying by non-indexed fields too - search by any given attribute of the product e.g., model, price.
- Supports a very rich query language including storing, fetching, modifying, deleting, sorting, and grouping data.
- Supports aggregations e.g., sum, count, and other string, math, and set operations.
- Apt for heavy reads - product details are written to the database fewer times than they are read (searched) by customers.

### Limitations
- Cannot represent complex relationships between data.

## Graph-Based Databases

### Use Cases
- Recommendation systems.

### Need or Emergence
- Track related products like smartphones and cover cases.
- Relate millions of customers and the products they purchase.

### Why not SQL?
- SQL may not be suitable for managing complex relationships between millions of customers and their purchased products, such as recommending related items like a phone cover with a smartphone, due to the time-consuming nature of joins.

### Why Use Graph Database?
- Use simple nodes and edges to store and retrieve highly interrelated data, e.g., customer and product.
- Graph traversals are much faster compared to SQL joins.
- In scenarios like user-product relationships and fraud detection, graph databases are more suitable.

### Limitations
- Inappropriate for transactional data like financial accounting.
- Do not scale out horizontally.
- Difficulty in performing aggregations like sum and max efficiently.
- Need to learn a new query language like CYPHER.
- Fewer vendors to choose from, making technical support harder to obtain.

---

## Quiz

### Scenario: A massive scale application needs rich queries over a flexible data model, predictable performance, limitless throughput, and/or global distribution to provide low-latency access to any number of regions over a single data set.

Choose the most appropriate data model:

- SQL database
- Key-value stores
- Column-family
- Document-oriented

---

## CAP Theorem

### Consistency, Availability, Partition Tolerance

- **Consistency**: An end user should be able to view the latest data at all times.
- **Availability**: Every database request must receive a response from the server while it is up and running.
- **Partition Tolerance**: When two systems cannot communicate in the network, it leads to partitions.

### CAP Theorem states that only two of the three properties can be guaranteed at the same time:
- Partitions occur only in distributed databases, which SQL is not. Hence, SQL databases support Consistency and Availability only.
- NoSQL databases are always partition tolerant; hence, you need to choose between Consistency and Availability.

---

### CAP Quiz

Choose between consistency and availability for each of the following online employee platform scenarios:

- Manage employee profile (maintains employee details)
- Manage session (track employee details from the time of login to the time of logout)
- Post articles (employees create/edit/delete articles)
- Comments (employees view comments on a given post or can post their own comments)
- Search (employees search for specific posts)
- Recommendations (recommend employees about other related posts)
- Reporting (daily/weekly/monthly/yearly usage reports)

---

## Read-Write Intensive Tasks

### Identify whether your component requires:

- Too many reads compared to writes or
- Too many writes compared to reads

![Read-Write Intensive](https://github.com/user-attachments/assets/49451d75-6c3e-4c9a-9578-2f2f9516549b)

### Quiz

Identify whether each given online employee platform scenario is read-intensive, write-intensive, or both read/write intensive:

- Manage employee profile (maintains employee details)
- Manage session (track employee details from the time of login to the time of logout)
- Post articles (employees create/edit/delete articles)
- Comments (employees view comments on a given post or can post their own comments)
- Search (employees search for specific posts)
- Recommendations (recommend employees about other related posts)
- Reporting (daily/weekly/monthly/yearly usage reports)

### Answers

- Manage employee profile: Write-heavy as thousands of employee details are being updated onto the database.
- Manage session: Involves both read and write loads for retrieving session details and tracking changes made during the session.
- Post articles: Involves both read and write loads as existing articles are read by many employees and new articles are continuously posted by various employees.
- Comments: Involves both read and write loads as employees read existing comments on articles and post their own comments.
- Search: Involves heavy reads as employees keep searching for various articles.
- Recommendations: Read-heavy as the system recommends related articles which would be useful to employees.
- Reporting: Read-heavy as reports are being used for analysis of data.

![Choosing the Right Database](https://github.com/user-attachments/assets/c505b191-0697-42fa-97a9-92178702e3a5)

---

## Choosing the Right Database

In Stage 2, map the outcome of Stage 1 to the most suitable NoSQL database based on the required characteristics you are looking for.

### Example Mappings:

- Shopping cart: Needs a key-value store with high availability and write-intensive - Riak is most suitable.
- User activity logs: Cassandra is the best fit.
- Product catalog: MongoDB is most suitable (though consistent by default, it is tuned for availability as required).
- Recommendations component: Best implemented using Neo4J.

![Database Mapping](https://github.com/user-attachments/assets/f7c4e726-844f-408f-89a6-c67ee0d7edaa)

## Exercise

For each given online employee platform scenario, choose the most appropriate database:

- Manage employee profile (maintains employee details)
- Manage session (track employee details from the time of login to the time of logout)
- Post articles (employees create/edit/delete articles)
- Comments (employees view comments on a given post or can post their own comments)
- Search (employees search for specific posts)
- Recommendations (recommend employees about other related posts)
- Reporting (daily/weekly

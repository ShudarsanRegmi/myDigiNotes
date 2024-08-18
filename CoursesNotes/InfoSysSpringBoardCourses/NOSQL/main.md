# Note taken for Infosys SpringBoard NoSQL Course

# Summary
### Data Models in NoSQL Databases

1. **Key-Value Stores**:
   - **Structure**: Simple and highly scalable. Data is stored as key-value pairs, where the key is a unique identifier, and the value can be a string, JSON, or any binary object.
   - **Use Cases**: Ideal for caching, session management, and storing user profiles.
   - **Examples**: Redis, DynamoDB, Memcached.

2. **Column Family Stores**:
   - **Structure**: Data is organized into rows and columns, but unlike traditional relational databases, columns are grouped into column families. Each row can have a different number of columns.
   - **Use Cases**: Suitable for storing large datasets that require high write and read performance, such as in analytics and event logging.
   - **Examples**: Cassandra, HBase.

3. **Document Stores**:
   - **Structure**: Data is stored in documents, typically in JSON or BSON format. Each document contains fields and values, and documents can have different structures.
   - **Use Cases**: Best for content management systems, e-commerce platforms, and applications where data structures evolve.
   - **Examples**: MongoDB, CouchDB.

4. **Graph Stores**:
   - **Structure**: Data is stored in nodes, edges, and properties, representing entities and their relationships. Nodes represent entities, edges represent relationships, and properties store relevant information.
   - **Use Cases**: Ideal for social networks, recommendation engines, and fraud detection where relationships between data points are crucial.
   - **Examples**: Neo4j, Amazon Neptune, ArangoDB.

--- 



### My Notes from Course
By the end of the course, you will be able to:
Identify the right database implementation for a given business requirement

- Apply Consistency Availability Partition tolerance (CAP) theorem and business parameters to select the most appropriate NoSQL (Not only SQL) database

- You will learn this by analyzing four real life big data implementation scenarios.  

---

The two stages mentioned below help you design the database infrastructure of the eCommerce system under consideration.

- Stage 1: For each component, identify the most relevant data model, consistency level and the read/write load required

- Stage 2: Map the outcome of Stage 1 to the characteristics of few popular NoSQL databases to choose the most suitable one

---

As part of Stage 1, for each eCommerce component, you will do the following.  

1.1 Identify data model
Is your data text-based / key-value / flexible / structured / highly related to one another?

1.2 Choose consistency level
Does it require stronger consistency or higher availability?

1.3 Analyze whether operations are read/write intensive
Does it mostly involve read or write operations?

---

This step begins by identifying the most suitable NoSQL category below for each component of the eCommerce system:

a) Key-value stores

b) Column-family stores

c) Document-oriented databases

d) Graph-based databases

---

![image](https://github.com/user-attachments/assets/e1ccdadf-5384-4dd8-974c-f19fabce9843)

---

b. Column Family Stores


Why not key-value stores?
Key-value stores do not allow querying by value or updating only part of the value.

Why use column-family stores?
- Column family stores are very efficient for heavy writes

- Unlike key-value stores, they allow index creation on non-key fields. For example, create an index on email_id to query by this field apart from querying by customer_id (key)

- Also, you can retrieve or update any fields as required. For example, retrieving or updating the contact_number of the customer

![image](https://github.com/user-attachments/assets/253accc8-5041-49d8-9418-2a23b2e17256)

Limitations of column-family stores 
- It is not possible to query on non-indexed fields, for example, age (assume only customer_id and email_id are the indexed fields)

- Support for read operations is limited compared to SQL. For example, group by operation is not available 

- Also, not suitable for queries involving multiple fields. For example, search for customers with age>20 and city='Chennai'. Use document-oriented databases instead

---

For key look ups, key-value stores are fastest.

For frequently updating data and searching by primary key or indexed keys, column families work very well.

But for queries involving multiple fields, creating indexes on many fields is not a good practice. It is also a very costly operation. Hence column family stores are not recommended for the given scenario. 

For scenarios where millions of customers are frequently searching for products based on various criteria (read heavy workloads), document-oriented databases are most suitable.

---

### Document Oriented Model
The given scenario needs:

Flexible data model -> SQL databases are not suitable

Rich queries -> Key-value stores and column-family stores have limited query support, whereas document-oriented databases provide rich querying options

Hence document-oriented databases are best suited for the given scenario.

---







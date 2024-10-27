# Choosing the right database

## Key Value Database
- Redis, Numcached
- Data is stored in memory, not disks

## Wide column
- Have no fixed schema, no joins
- Just added one dimension to key value database
- Cassandra, Hbase
- It is decentralized and can scale horizantally
- Used for time series data record from iot devics, whether sensors, stock prices, user history
- Suitable for cases where writes is more frequent then reads

## Document Database
- MongoDb, Firestore, dynamodb
- Unstructured and do not require schema
- Not so idea for graphs

## Relational Database
- Has fixed schema
- Normalizes data
- ACID(Atomicity, Consistencty Isolation, Durability)

  ## Graph Database
  - Neo4j and Dgraph
 
  ## Multimodel Database
  - Fauna DB

# CAP Theorem

This step uses CAP theorem (Consistency, Availability, Partition tolerance) to identify the level of consistency required. All databases should ideally provide the following features:

Consistency – An end user should be able to view the latest data at all times

Availability – Every database request must receive a response from the server while it is up and running

Partition tolerance – When two systems cannot talk to each other in the network, it leads to partitions


CAP theorem states that:
- Only two of the three properties can be guaranteed at the same
- Partitions occur only in distributed databases which SQL is not. Hence SQL databases support Consistency and Availability only
- NoSQL databases are always partition tolerant and hence you need to choose between Consistency and Availability

  

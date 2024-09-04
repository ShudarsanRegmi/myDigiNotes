# Materials for 4NF


- Two attributes (or columns) in a table are independent of one another, but both depend on a third attribute
- A multivalued dependency always requires at least three attributes because it consists of at least two attributes that are dependent on a third.
- The table should have at least 3 attributes and B and C should be independent for A ->> B multivalued dependency. 

## Why To Eliminate Multi-Valued Dependency

Why eliminate multi-valued dependencies?

When multi-valued dependencies exist in a table, it can lead to redundancy and anomalies:

- **Redundancy:** You might repeat combinations of independent values (like hobbies and courses for a student).
- **Insertion Anomaly:** Adding a new hobby for a student might force you to add redundant information about courses, or vice versa.
- **Deletion Anomaly:** Removing a course for a student might accidentally delete information about unrelated hobbies.

## 4NF


![image](https://github.com/user-attachments/assets/0d09c0c7-0649-4056-8b01-a919542bbedb)

![image](https://github.com/user-attachments/assets/b1c84349-96b3-4be5-ab5f-480547354daf)

![image](https://github.com/user-attachments/assets/6e99e423-6cdf-4395-a39c-1e14922bebda)

![image](https://github.com/user-attachments/assets/3587ec45-3000-466f-94b7-1b3e432c41d0)
- This is read as “person multi determines mobile” and “person multi determines food_likes.” 

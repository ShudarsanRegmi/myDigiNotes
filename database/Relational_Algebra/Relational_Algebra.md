  

  

I like to take a note of basic operators in relational algebra first will get started with the very first operator called the projection operator it is denoted by **PI** and there are lots of techniques

![Please Reload/Refresh this tab.](https://storage.googleapis.com/askify-screenshot/jxRt18U7tEOkUXMS06ujdDt1d743/extension_screenshots/screenshot_default_be7f4258-e190-4bd8-9606-da004e274309.jpeg)

  

  

  

===

### Import Points:

  

  

PI (Projection):
================

  

PI -> only fetches unique rows (i.e. no duplicates)

  

  

![Please Reload/Refresh this tab.](https://storage.googleapis.com/askify-screenshot/jxRt18U7tEOkUXMS06ujdDt1d743/extension_screenshots/screenshot_default_ab2c2f32-15c1-4ccb-b8e7-c5aeacf3c6a0.jpeg)

  

  

### Sigma: Selection Operator

It is used for selection of rows.

Note: Use selection operator inside and PI operator outside

  

  

### Cross Product in Relational Algebra

*   Minimum two tables are required. They can be same though
*   At least one of the column should be common
*   No. of Columns (cross product) = No. of columns in table1 + No. of columns in table2)
*   No. of rows (Cross Product) = No. of rows in table1 \* No. of rows in table2

  

  

  

![Please Reload/Refresh this tab.](https://storage.googleapis.com/askify-screenshot/jxRt18U7tEOkUXMS06ujdDt1d743/extension_screenshots/screenshot_default_17388115-6ae0-4628-8c86-cd020d8ccd57.jpeg)

  

===

### Set Difference in Relational Algebra

A - B = A U B (comp)

Q. Find the students who are not employees

  

  

### Division Operation in Relational Algebra

The division operator is used for queries which involve the 'all'.

R1 ÷ R2 = tuples of R1 associated with all tuples of R2.

  

Q. Find the list of students who have enrolled in both the courses

  

  

### Union Operation:

*   No. of columns must be same in no.
*   Corresponding column should be of same domain
*   Column name is determined by left table

###   

### Tuple Calculus

Relational Calculus: Two types:

  

*   Tuple Relational Calculus
*   Domain Relational Calculus
*
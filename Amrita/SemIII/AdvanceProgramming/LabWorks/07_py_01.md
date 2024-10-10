# Python
<div align="center">

![Amrita Vishwa Vidyapeetham Logo](https://webfiles.amrita.edu/2024/04/WhQq1FiB-amrita-vishwa-vidyapeetham-university-logo-colored-version.svg)

# Amrita Vishwa Vidyapeetham
## Chennai Campus
337/1A, Vengal Village,  
Thiruvallur Taluk & District – 601 103,  
Tamil Nadu, India

---

### Subject: Advance Programming

**Submitted By:** Shudarsan Regmi  
**Roll No.:** CH.SC.U4CYS23055

</div>

---

# Python Programs Report

## 1. **Find the Largest Number in a List**

**Problem Statement:**

Write a Python program to find the largest number in a list of numbers.

**Code:**

```python
# Given list of numbers
numbers = [12, 45, 78, 34, 23, 89, 4]

# Finding the largest number using the max() function
largest_number = max(numbers)

# Printing the largest number
print("The largest number is:", largest_number)
```

**Output:**

```
The largest number is: 89
```

---

## 2. **Sort a Tuple in Ascending Order**

**Problem Statement:**

Write a Python program to sort a tuple in ascending order.

**Code:**

```python
# Given tuple
t = (43, 12, 98, 23, 56, 7)

# Sorting the tuple and converting it back to tuple form
sorted_tuple = tuple(sorted(t))

# Printing the sorted tuple
print("The sorted tuple is:", sorted_tuple)
```

**Output:**

```
The sorted tuple is: (7, 12, 23, 43, 56, 98)
```

---

## 3. **Check if a Particular Element is Present in a Set**

**Problem Statement:**

Write a Python program to check if a particular element is present in a set.

**Code:**

```python
# Given set and element to check
s = {23, 45, 67, 89, 12}
element = 45

# Checking if the element is in the set
if element in s:
    print(f"{element} is present in the set.")
else:
    print(f"{element} is not present in the set.")
```

**Output:**

```
45 is present in the set.
```

---

## 4. **Remove a Particular Key-Value Pair from a Dictionary**

**Problem Statement:**

Write a Python program to remove a particular key-value pair from a dictionary.

**Code:**

```python
# Given dictionary
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Key to remove
key_to_remove = 'age'

# Removing the key-value pair
if key_to_remove in my_dict:
    del my_dict[key_to_remove]

# Printing the modified dictionary
print("The dictionary after removal is:", my_dict)
```

**Output:**

```
The dictionary after removal is: {'name': 'Alice', 'city': 'New York'}
```

---

## 5. **Find Unique Values of All Keys and Values in a List of Dictionaries**

**Problem Statement:**

Write a Python program that takes a list of dictionaries as input and returns a tuple of the unique values of all the keys and values in the dictionaries.

**Code:**

```python
# List of dictionaries
dicts_list = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 30},
    {'city': 'New York', 'age': 25},
]

# Collecting unique keys and values
unique_keys = set()
unique_values = set()

# Looping through the list of dictionaries
for d in dicts_list:
    for key, value in d.items():
        unique_keys.add(key)
        unique_values.add(value)

# Creating a tuple of unique keys and values
unique_tuple = (unique_keys, unique_values)

# Printing the result
print("The unique keys and values are:", unique_tuple)
```

**Output:**

```
The unique keys and values are: ({'name', 'city', 'age'}, {'Bob', 'Alice', 'New York', 25, 30})
```

---

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

## 1. **Multiple Function Calls with Compulsory Argument**

**Problem Statement:**

Write a Python program that demonstrates multiple function calls with compulsory arguments.

**Code:**

```python
# Function that prints a message with a name
def greet(name):
    print(f"Hello, {name}! Welcome to the Python programming world.")

# Calling the function multiple times
greet("Alice")
greet("Bob")
greet("Charlie")
```

**Output:**

```
Hello, Alice! Welcome to the Python programming world.
Hello, Bob! Welcome to the Python programming world.
Hello, Charlie! Welcome to the Python programming world.
```

---

## 2. **Function with a Default Argument**

**Problem Statement:**

Write a Python program that demonstrates a function with a default argument.

**Code:**

```python
# Function that prints a message with a default greeting
def greet(name, message="Welcome!"):
    print(f"Hello, {name}! {message}")

# Calling the function with and without the default argument
greet("Alice")  # Using default message
greet("Bob", "Good morning!")  # Overriding default message
```

**Output:**

```
Hello, Alice! Welcome!
Hello, Bob! Good morning!
```

---

## 3. **Function with a Return Statement**

**Problem Statement:**

Write a Python program that demonstrates a function with a return statement.

**Code:**

```python
# Function that adds two numbers and returns the result
def add_numbers(a, b):
    result = a + b
    return result

# Using the function and storing the result
sum_value = add_numbers(5, 7)

# Printing the result
print(f"The sum of the two numbers is {sum_value}.")
```

**Output:**

```
The sum of the two numbers is 12.
```

---

## 4. **Example of a Function Returning Multiple Values**

**Problem Statement:**

Write a Python program that demonstrates a function returning multiple values.

**Code:**

```python
# Function that returns the sum and product of two numbers
def sum_and_product(a, b):
    sum_value = a + b
    product_value = a * b
    return sum_value, product_value

# Using the function and unpacking the returned values
sum_result, product_result = sum_and_product(4, 6)

# Printing the results
print(f"The sum is {sum_result} and the product is {product_result}.")
```

**Output:**

```
The sum is 10 and the product is 24.
```

---

## 5. **Find the Largest Number Among Three Numbers**

**Problem Statement:**

Write a Python program to find the largest number among three numbers.

**Code:**

```python
# Given three numbers
a = 12
b = 45
c = 32

# Finding the largest number
if a > b and a > c:
    largest = a
elif b > a and b > c:
    largest = b
else:
    largest = c

# Printing the largest number
print(f"The largest number is {largest}.")
```

**Output:**

```
The largest number is 45.
```

---

## 6. **Count the Number of Digits in a Number**

**Problem Statement:**

Write a Python program to count the number of digits in a number.

**Code:**

```python
# Given number
num = 12345

# Counting the number of digits
count = len(str(num))

# Printing the result
print(f"The number {num} has {count} digits.")
```

**Output:**

```
The number 12345 has 5 digits.
```

---

## 7. **Count the Number of Digits in a Number Using While Loop (Without Function)**

**Problem Statement:**

Write a Python program to count the number of digits in a number using a while loop (without using a function).

**Code:**

```python
# Given number
num = 123456

# Initialize count
count = 0

# Counting digits using a while loop
while num != 0:
    num = num // 10  # Remove the last digit
    count += 1  # Increment the count

# Printing the result
print(f"The number has {count} digits.")
```

**Output:**

```
The number has 6 digits.
```

---

## 8. **Compute the Factorial of a Number**

**Problem Statement:**

Write a Python program that computes the factorial of the number passed as an argument.

**Code:**

```python
# Given number
num = 5

# Initialize factorial
factorial = 1

# Calculate factorial
for i in range(1, num + 1):
    factorial *= i

# Printing the result
print(f"The factorial of {num} is {factorial}.")
```

**Output:**

```
The factorial of 5 is 120.
```

## 8. Using else with while loop

```python
numbers = [1, 3, 5, 7, 2, 9, 10, 11]

# Initialize variables
found_even = None
index = 0

# Start a while loop to search for the first non-negative even number
while index < len(numbers):
    if numbers[index] >= 0 and numbers[index] % 2 == 0:
        found_even = numbers[index]
        break  # Exit the loop if a match is found
    index += 1
else:
    print("No non-negative even number found in the list.")

# Check if a non-negative even number was found and print it
if found_even is not None:
    print(f"The first non-negative even number found is: {found_even}")

```

**Output:**

```
The first non-negative even number found is: 2
```

---

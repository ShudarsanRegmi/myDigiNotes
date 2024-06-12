# Powerful Python Lines

>This page contains the tips and tricks in python that can be used in competitive programmings to reduce the no of lines in the code and minimize your effort

# List Comprehension

## Squaring the elements of a list

```python
x = [1,2,3,4,5]
x2 = [i**2 for i in x]
```

## Filtering list elements

```python
x = [1,2,3,4,5]
x2 = [i for i in x if x%2 == 0] # get the even elements
```
## Creating a list of tuples by merging two lists

```python
x = [1,3,5,7]
y = [2,4,6,8]
a = [(i,j) for i in x for j in y] # Creating all order pairs
```

## Creating a relationship between two sets(lists)

```python
x = [1,3,5,7]
y = ['a','b','c','d']
rel = [(i,j) for i in x for j in y]
```

# Taking Input


## Taking integer input
x = int(input().strip())

## Taking a list of integers as input
```
x = list(map(int, input().strip().split())  
```



## Flattening a complex iterators based data structure
```
x = [[(1,2),(3,4)],[(5,6),(7,8)]]
flattened = [num for sublist in x for tuples in sublist for num in tuples]
```



### Increasing one of the indices of list based on condition

```python
a = [1,2,3]
condition = True
a[0 if condition else 1]
```

### Selecting one of the indices of a list out of many conditions

```python
a = [1,2,3]
condition1 = False
condition2 = False
a[0 if condition1 else 1 if condition2 else 2]
```

### Initializing a list with multiple same elements

```python
arr = [0]*10
```

### Reversing a String
```python
"string"[::-1]
```

### breaking out of two loops directly in nested loop
```python
try:
  for i in a:
    for j in b:
      raise breakLoop
except breakLooop:
  # code to execute after breakloop
  ```

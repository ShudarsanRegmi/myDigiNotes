# Powerful Python Lines

>This page contains the tips and tricks in python that can be used in competitive programmings to reduce the no of lines in the code and minimize your effort

# List Comprehension

## Squaring the elements of a list

```
x = [1,2,3,4,5]
x2 = [i**2 for i in x]
```

## Filtering list elements

```
x = [1,2,3,4,5]
x2 = [i for i in x if x%2 == 0] # get the even elements
```
## Creating a list of tuples by merging two lists

```
x = [1,3,5,7]
y = [2,4,6,8]
a = [(i,j) for i in x for j in y]
```

## Creating a relationship between two sets(lists)

```
x = [1,3,5,7]
y = ['a','b','c','d']
rel = [(i,j) for i in x for j in y]
```

# Taking Input


## Taking integer input
x = int(input().strip())

## Taking a list of integers as input
```
x = list(map(int, input().strip.split())  
```



# Some array manipulations that are useful in competitive programmign

## Array rotations

### Left Circular Rotation

```python
x = [1, 2, 3, 4, 5, 6, 7]
s=2
y = [ x[(i-s)%len(x)] for i in range(len(x))]
print(y)
```

### Left Circular Rotations

```python
# array rotation

x = [1, 2, 3, 4, 5, 6, 7]
s=2
y = [ x[(i+s)%len(x)] for i in range(len(x))]
print(y)

```

## Reversing Array

```python
arr = [2,3,4,5]
x = arr[::-1]
```

## Sorting an array 
```python
sorted(arr)
rev = True # or False
arr.sort(reverse=rev)
```

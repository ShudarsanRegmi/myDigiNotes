# Mostly Occuring Maths functions in CP


### Factorial
```python
def fact(n):
  return n*fact(n-1) if n>1 else return 1
```

### sieve of erastothenes

```python
import math
 
 
n = 200

nums = [True]*n

r = int(math.sqrt(n))

for i in range(2, r+1):
    if(nums[i]):
        for j in range(i*i, n, i):
            nums[j] = False
            
for i in range(2, n):
    if(nums[i]):
        print(i, end=' ')
```

### Check for Strong Number
>A number is strong if the sum of the factorial of its digit is equal to the number itself



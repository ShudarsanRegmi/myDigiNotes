# Exceptions in Python

## Class Hierarchy for build in exceptios in python
```
BaseException
 ├── BaseExceptionGroup
 ├── GeneratorExit
 ├── KeyboardInterrupt
 ├── SystemExit
 └── Exception
      ├── ArithmeticError
      │    ├── FloatingPointError
      │    ├── OverflowError
      │    └── ZeroDivisionError
      ├── AssertionError
      ├── AttributeError
      ├── BufferError
      ├── EOFError
      ├── ExceptionGroup [BaseExceptionGroup]
      ├── ImportError
      │    └── ModuleNotFoundError
      ├── LookupError
      │    ├── IndexError
      │    └── KeyError
      ├── MemoryError
      ├── NameError
      │    └── UnboundLocalError
      ├── OSError
      │    ├── BlockingIOError
      │    ├── ChildProcessError
      │    ├── ConnectionError
      │    │    ├── BrokenPipeError
      │    │    ├── ConnectionAbortedError
      │    │    ├── ConnectionRefusedError
      │    │    └── ConnectionResetError
      │    ├── FileExistsError
      │    ├── FileNotFoundError
      │    ├── InterruptedError
      │    ├── IsADirectoryError
      │    ├── NotADirectoryError
      │    ├── PermissionError
      │    ├── ProcessLookupError
      │    └── TimeoutError
      ├── ReferenceError
      ├── RuntimeError
      │    ├── NotImplementedError
      │    ├── PythonFinalizationError
      │    └── RecursionError
      ├── StopAsyncIteration
      ├── StopIteration
      ├── SyntaxError
      │    └── IndentationError
      │         └── TabError
      ├── SystemError
      ├── TypeError
      ├── ValueError
      │    └── UnicodeError
      │         ├── UnicodeDecodeError
      │         ├── UnicodeEncodeError
      │         └── UnicodeTranslateError
      └── Warning
           ├── BytesWarning
           ├── DeprecationWarning
           ├── EncodingWarning
           ├── FutureWarning
           ├── ImportWarning
           ├── PendingDeprecationWarning
           ├── ResourceWarning
           ├── RuntimeWarning
           ├── SyntaxWarning
           ├── UnicodeWarning
           └── UserWarning
```

## SyntaxError
```python
1var = 2
1=2
111
```

### TypError
```python
x = 'a'
y = 5
print(x+y)
```

## ValueError
```python
a = int('+')
```
## UnboundLocalError
```python
def unbound_error():
    print(x)  # ❌ UnboundLocalError: x referenced before assignment
    x = 10
```

## IndexError
```python
x = [1,2,3]
y = x[10]
```

## KeyError
```python
dic = {'name':'ram', 'age':10}
print(dic['height'])
```

## AttributeError
>Occurs when trying to access invalid attribute of an object
```python
class Human:
    def __init__(self, age, height, name):
        self.age = age
        self.height = height
        self.name = name


h1 = Human(10, 23, "falano")
print(h1.name)
print(h1.width)

```
```python
x = 5
x.upper()
```

## ImportError
```python
from math import nofunc # nofunc = any function that does not exist
```

## ModuleNotFoundError
```
import mathematics # not existing module
```

## FileNotFoundError
```python
with open('nonexistingfile.txt', 'rt') as file:
    print("reading file")
```

## ZeroDivisionError
```python
print(5/0)
```

## RecursionError
```python
def func():
  func()

func()

```

## MemoryError
```python
big_list = [1] * (10**10)  # Allocates a list of 10 billion elements
```
```python
data = []
while True:
    data.append("A" * 10**6)  # Add 1MB of data in each iteration
```

## UnicodeError
```python
b'\x80'.decode("utf-8")  # ❌ UnicodeDecodeError
```

## UniCodeEncodeError
```python
'🤣'.encode('ascii')
```

## Overflow error
```python
import math
x = math.exp(1000)  # ❌ OverflowError: math range error
```


## Lookup Error
```python
 b'xa1234'.decode('utf-i')
```








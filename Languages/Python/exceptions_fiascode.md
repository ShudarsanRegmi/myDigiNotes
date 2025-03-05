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



## TypError
```python
x = 'a'
y = 5
print(x+y)
```

## ValueError
```python
a = int('+')
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





# Quick Revision for CPP Syntax

## Topics to Learn in C++


```cpp
# Member Initializer LIst

```

### IO Functions
```cpp
std::cout << "print string" << std::endl;
```


### Installing cppman for accessing man pages in Linux
```bash
pip install cppman
cppman -c # update the database
xdg-open https://en.cppreference.com/w/ # reference website
```

### Data Types
- Int -> 2 or 4 bytes
- float -> 4 bytes
- Double -> 8 bytes
- Char -> 1 byte
- String -> not a built in data type. size are handeled dynamically by the library
- Bool -> 1 byte
bytes
### Constants
```cpp
const int x = 5;
```

### Taking user input
```cpp
int x;
cin >> x;
string ram;
cin >> ram;
```

### Taking String input
```cpp
#include <string>
std::string name;
std::cin >> name;
std::cin.ignore(); // ignoring the newline character
// Getting full ine of input including spaces
std::getline(std::cin, name);
```
**Getting Characterwise Input**
```cpp
int main() {
    char ch;
    std::cout << "Enter characters (Ctrl+D to end): ";
    while (std::cin.get(ch)) {
        std::cout << ch;
    }
    return 0;
}
```

### Strings
```cpp
/* str is an object
.length() -> returns the length
*/
```

## OOP

### Important points
- In C++, using `this->` is necessary when there is a naming conflict between a member variable and a parameter or local variable; otherwise, it is optional and can be omitted for cleaner and more readable code.
- Don't use `()` when you're not passing anything to constructor.



```creds
- .\ASE computer lab
- Amma123
```

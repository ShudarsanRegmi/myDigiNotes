# Quick Revision for CPP Syntax

### IO Functions
```cpp
std::cout << "print string" << std::endl;
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



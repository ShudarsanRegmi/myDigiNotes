### Additional Examples of Simple Inheritance

#### Example 1: Real-World Example in Software Engineering

**Scenario**: Consider a software system for a company that manages different types of employees. Each employee has some common properties and behaviors, but different types of employees might have specific attributes or actions.

```cpp
#include <iostream>
using namespace std;

// Base Class
class Employee {
public:
    string name;
    int id;

    Employee(string n, int i) : name(n), id(i) {}

    void displayInfo() {
        cout << "Name: " << name << ", ID: " << id << endl;
    }
};

// Derived Class
class Manager : public Employee {
public:
    int teamSize;

    Manager(string n, int i, int t) : Employee(n, i), teamSize(t) {}

    void displayManagerInfo() {
        displayInfo();
        cout << "Team Size: " << teamSize << endl;
    }
};

// Main Function
int main() {
    Manager mgr("Alice", 101, 10);

    mgr.displayManagerInfo();

    return 0;
}
```

**Explanation**:
- **Base Class (`Employee`)**: Represents general employee attributes.
- **Derived Class (`Manager`)**: Inherits from `Employee` and adds specific attributes like `teamSize`.

#### Example 2: Simple and Easy to Illustrate

**Scenario**: A simple example involving geometric shapes.

```cpp
#include <iostream>
using namespace std;

// Base Class
class Shape {
public:
    void draw() {
        cout << "Drawing a shape." << endl;
    }
};

// Derived Class
class Circle : public Shape {
public:
    void draw() {
        cout << "Drawing a circle." << endl;
    }
};

// Main Function
int main() {
    Circle myCircle;

    // Call method from the base class
    myCircle.Shape::draw(); // Optional: Explicitly call base class method

    // Call method from the derived class
    myCircle.draw();

    return 0;
}
```

**Explanation**:
- **Base Class (`Shape`)**: Has a method `draw()` that represents drawing a general shape.
- **Derived Class (`Circle`)**: Inherits from `Shape` and overrides the `draw()` method to represent drawing a specific shape, a circle.

These examples cover both real-world applications and simple illustrations of inheritance in C++.

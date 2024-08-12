### Multiple Inheritance in C++

Multiple inheritance occurs when a class (derived class) inherits from more than one base class. This allows the derived class to combine functionalities from multiple base classes.

#### **Real-World Example**

**Scenario**: Consider a software system for a university where we have a `Person` class, a `Teacher` class, and a `Researcher` class. A `Professor` class might need to inherit from both `Teacher` and `Researcher` because a professor is both a teacher and a researcher.

```cpp
#include <iostream>
using namespace std;

// Base Class 1
class Person {
public:
    string name;
    int age;

    Person(string n, int a) : name(n), age(a) {}

    void displayPersonInfo() const {
        cout << "Name: " << name << ", Age: " << age << endl;
    }
};

// Base Class 2
class Teacher {
public:
    void teach() const {
        cout << "Teaching a class." << endl;
    }
};

// Base Class 3
class Researcher {
public:
    void conductResearch() const {
        cout << "Conducting research." << endl;
    }
};

// Derived Class using Multiple Inheritance
class Professor : public Person, public Teacher, public Researcher {
public:
    Professor(string n, int a) : Person(n, a) {}

    void displayProfessorInfo() const {
        displayPersonInfo();
        teach();
        conductResearch();
    }
};

// Main Function
int main() {
    Professor prof("Dr. Smith", 45);

    prof.displayProfessorInfo();

    return 0;
}
```

**Explanation**:
- **Base Classes (`Person`, `Teacher`, `Researcher`)**: Each has its own attributes and methods.
- **Derived Class (`Professor`)**: Inherits from `Person`, `Teacher`, and `Researcher`. It combines functionalities from all three base classes.

#### **Simple Code Illustration**

**Scenario**: A simple example involving two base classes, `Vehicle` and `Flyable`, with a derived class `FlyingCar` that combines both functionalities.

```cpp
#include <iostream>
using namespace std;

// Base Class 1
class Vehicle {
public:
    void drive() const {
        cout << "Driving the vehicle." << endl;
    }
};

// Base Class 2
class Flyable {
public:
    void fly() const {
        cout << "Flying the vehicle." << endl;
    }
};

// Derived Class using Multiple Inheritance
class FlyingCar : public Vehicle, public Flyable {
public:
    void operate() const {
        drive();
        fly();
    }
};

// Main Function
int main() {
    FlyingCar myFlyingCar;

    myFlyingCar.operate();

    return 0;
}
```

**Explanation**:
- **Base Classes (`Vehicle`, `Flyable`)**: Represent different functionalities.
- **Derived Class (`FlyingCar`)**: Inherits from both `Vehicle` and `Flyable`, combining their functionalities. The `operate()` method calls both `drive()` and `fly()`.

### Key Points about Multiple Inheritance

1. **Ambiguity**: Multiple inheritance can lead to ambiguity if two base classes have methods with the same name. This needs to be resolved using scope resolution or virtual inheritance.
   
2. **Virtual Inheritance**: If multiple base classes share a common base class, virtual inheritance can be used to ensure only one instance of the common base class is inherited.

3. **Use Cases**: Multiple inheritance can be useful but should be used carefully to avoid complexity and ambiguity in class relationships.

Multiple inheritance allows a class to inherit behaviors from more than one base class, enabling more flexible class designs but requiring careful handling of potential ambiguities.

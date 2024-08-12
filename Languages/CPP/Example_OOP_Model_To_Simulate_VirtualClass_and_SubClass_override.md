### **OOP Model to Simulate with Virtual Functions and Subclass Overrides**

Let's create a simple Object-Oriented Programming (OOP) model to simulate an **employee management system**. The base class will be `Employee`, which will be a virtual class with a pure virtual function. We'll then create derived classes like `Manager`, `Engineer`, and `Intern` that override the methods of the `Employee` class.

### **Step-by-Step Implementation**

#### **1. Base Class: `Employee`**

- The `Employee` class will be an abstract class containing pure virtual functions. These functions will define the interface that all derived classes must implement.

```cpp
#include <iostream>
#include <string>
using namespace std;

class Employee {
protected:
    string name;
    int id;

public:
    Employee(string n, int i) : name(n), id(i) {}

    // Pure virtual function
    virtual void calculateSalary() = 0;

    // Virtual function with a default implementation
    virtual void displayDetails() {
        cout << "Employee ID: " << id << ", Name: " << name << endl;
    }

    virtual ~Employee() {} // Virtual destructor
};
```

#### **2. Derived Class: `Manager`**

- The `Manager` class will inherit from `Employee` and implement the `calculateSalary()` method specific to a manager's role.

```cpp
class Manager : public Employee {
private:
    double baseSalary;
    double bonus;

public:
    Manager(string n, int i, double salary, double b) : Employee(n, i), baseSalary(salary), bonus(b) {}

    // Override the pure virtual function
    void calculateSalary() override {
        double totalSalary = baseSalary + bonus;
        cout << "Manager's Salary: $" << totalSalary << endl;
    }

    // Optionally override displayDetails
    void displayDetails() override {
        Employee::displayDetails();
        cout << "Position: Manager" << endl;
    }
};
```

#### **3. Derived Class: `Engineer`**

- The `Engineer` class will also inherit from `Employee` and implement the `calculateSalary()` method specific to an engineer's role.

```cpp
class Engineer : public Employee {
private:
    double hourlyRate;
    int hoursWorked;

public:
    Engineer(string n, int i, double rate, int hours) : Employee(n, i), hourlyRate(rate), hoursWorked(hours) {}

    // Override the pure virtual function
    void calculateSalary() override {
        double totalSalary = hourlyRate * hoursWorked;
        cout << "Engineer's Salary: $" << totalSalary << endl;
    }

    // Optionally override displayDetails
    void displayDetails() override {
        Employee::displayDetails();
        cout << "Position: Engineer" << endl;
    }
};
```

#### **4. Derived Class: `Intern`**

- The `Intern` class will inherit from `Employee` and implement the `calculateSalary()` method specific to an intern's role.

```cpp
class Intern : public Employee {
private:
    double stipend;

public:
    Intern(string n, int i, double s) : Employee(n, i), stipend(s) {}

    // Override the pure virtual function
    void calculateSalary() override {
        cout << "Intern's Stipend: $" << stipend << endl;
    }

    // Optionally override displayDetails
    void displayDetails() override {
        Employee::displayDetails();
        cout << "Position: Intern" << endl;
    }
};
```

#### **5. Main Function: Simulating the Model**

- In the `main()` function, we can create objects of `Manager`, `Engineer`, and `Intern` and call their methods to simulate the system.

```cpp
int main() {
    Employee* emp1 = new Manager("Alice", 101, 80000, 15000);
    Employee* emp2 = new Engineer("Bob", 102, 50, 160);
    Employee* emp3 = new Intern("Charlie", 103, 1000);

    emp1->displayDetails();
    emp1->calculateSalary();

    emp2->displayDetails();
    emp2->calculateSalary();

    emp3->displayDetails();
    emp3->calculateSalary();

    // Clean up
    delete emp1;
    delete emp2;
    delete emp3;

    return 0;
}
```

### **Explanation**
1. **Base Class (`Employee`)**:
   - Contains a pure virtual function `calculateSalary()` that must be overridden by derived classes.
   - Contains a virtual function `displayDetails()` with a default implementation that derived classes can override.

2. **Derived Classes (`Manager`, `Engineer`, `Intern`)**:
   - Each derived class provides its own implementation of `calculateSalary()` to reflect different salary structures.
   - Optionally, each derived class can override `displayDetails()` to provide additional information about the employee's position.

3. **Main Function**:
   - We create pointers to the `Employee` base class and instantiate them with objects of derived classes.
   - The appropriate methods are called based on the object type, demonstrating polymorphism.

### **Output**
```
Employee ID: 101, Name: Alice
Position: Manager
Manager's Salary: $95000

Employee ID: 102, Name: Bob
Position: Engineer
Engineer's Salary: $8000

Employee ID: 103, Name: Charlie
Position: Intern
Intern's Stipend: $1000
```

This OOP model showcases how virtual functions and pure virtual functions are used in practice to create flexible, reusable, and polymorphic code structures.

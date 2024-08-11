# Pure Virtual Function And Abstract  Classes


What is the use? 
Virtual functions allow us to create a list of base class pointers and call methods of any of the derived classes without even knowing the kind of derived class object.

```cpp
// C++ program to demonstrate how a virtual function
// is used in a real life scenario

class Employee {
public:
	virtual void raiseSalary()
	{
		// common raise salary code
	}

	virtual void promote()
	{
		// common promote code
	}
};

class Manager : public Employee {
	virtual void raiseSalary()
	{
		// Manager specific raise salary code, may contain
		// increment of manager specific incentives
	}

	virtual void promote()
	{
		// Manager specific promote
	}
};

// Similarly, there may be other types of employees

// We need a very simple function
// to increment the salary of all employees
// Note that emp[] is an array of pointers
// and actual pointed objects can
// be any type of employees.
// This function should ideally
// be in a class like Organization,
// we have made it global to keep things simple
void globalRaiseSalary(Employee* emp[], int n)
{
	for (int i = 0; i < n; i++) {
		// Polymorphic Call: Calls raiseSalary()
		// according to the actual object, not
		// according to the type of pointer
		emp[i]->raiseSalary();
	}
}

```

---

### **Concept of Virtual Functions in C++**

A **virtual function** in C++ is a member function in a base class that you expect to override in derived classes. When you declare a function as `virtual`, it allows you to achieve **polymorphism**—one of the core principles of Object-Oriented Programming (OOP). 

#### **Theoretical Insights**
1. **Polymorphism**:
   - Polymorphism allows objects of different classes to be treated as objects of a common base class. The most common use of polymorphism in C++ is when a base class pointer or reference is used to refer to a derived class object. Virtual functions enable the correct function to be called based on the object type, not the pointer type.

2. **Dynamic Binding**:
   - Normally, functions are resolved at compile time (static binding). However, virtual functions are resolved at runtime, a concept known as dynamic binding or late binding. This means that the function that gets called is determined at runtime based on the type of the object pointed to by the base class pointer.

3. **Virtual Table (vtable) and Virtual Pointer (vptr)**:
   - When a class contains a virtual function, the compiler creates a **vtable** (virtual table) for that class. The vtable is an array of pointers to virtual functions. Each object of the class contains a hidden pointer called **vptr** (virtual pointer) that points to the vtable. This setup allows the correct function to be called at runtime.

4. **Pure Virtual Functions and Abstract Classes**:
   - A pure virtual function is a virtual function that has no implementation in the base class and is declared using the syntax `virtual void func() = 0;`. A class containing at least one pure virtual function is called an **abstract class** and cannot be instantiated. Derived classes must provide implementations for pure virtual functions.

#### **Object-Oriented Programming (OOP) Aspects**
- **Encapsulation**: Virtual functions are part of a class interface, ensuring that derived classes encapsulate the behavior of the base class, allowing them to be treated uniformly.
  
- **Inheritance**: Virtual functions enable derived classes to inherit the interface of the base class while allowing them to provide their own specific implementations of that interface.
  
- **Polymorphism**: This is the key aspect enabled by virtual functions, allowing objects of different types to be handled using a common interface.

#### **Code Example**

Here's an example to illustrate the concept:

```cpp
#include <iostream>
using namespace std;

class Base {
public:
    virtual void show() { // Virtual function
        cout << "Base class show function called." << endl;
    }

    void display() { // Non-virtual function
        cout << "Base class display function called." << endl;
    }
};

class Derived : public Base {
public:
    void show() override { // Override the virtual function
        cout << "Derived class show function called." << endl;
    }

    void display() { // Hide the base class display function
        cout << "Derived class display function called." << endl;
    }
};

int main() {
    Base* basePtr;
    Derived derivedObj;
    
    basePtr = &derivedObj;

    // Virtual function, resolved at runtime (dynamic binding)
    basePtr->show(); // Outputs: Derived class show function called.

    // Non-virtual function, resolved at compile time (static binding)
    basePtr->display(); // Outputs: Base class display function called.

    return 0;
}
```

**Explanation**:
- `show()` is a virtual function in the `Base` class and is overridden in the `Derived` class. When `basePtr->show()` is called, the derived class's `show()` function is invoked due to dynamic binding.
  
- `display()` is not virtual, so the base class's version is called regardless of the object type the pointer refers to. This demonstrates static binding.

#### **Use Case: When to Use Virtual Functions**
- Virtual functions are useful when you have a base class pointer pointing to derived class objects, and you want to call the derived class's version of the function rather than the base class's version.

#### **Pure Virtual Function Example**

```cpp
#include <iostream>
using namespace std;

class Shape {
public:
    virtual void draw() = 0; // Pure virtual function
};

class Circle : public Shape {
public:
    void draw() override {
        cout << "Drawing a circle." << endl;
    }
};

class Square : public Shape {
public:
    void draw() override {
        cout << "Drawing a square." << endl;
    }
};

int main() {
    Shape* shape1 = new Circle();
    Shape* shape2 = new Square();

    shape1->draw(); // Outputs: Drawing a circle.
    shape2->draw(); // Outputs: Drawing a square.

    delete shape1;
    delete shape2;

    return 0;
}
```

**Explanation**:
- `Shape` is an abstract class with a pure virtual function `draw()`. The `Circle` and `Square` classes provide implementations for the `draw()` function.
- Even though `Shape*` pointers are used, the correct `draw()` function for the specific shape (circle or square) is called, demonstrating polymorphism.

### **Conclusion**
Virtual functions are a fundamental concept in C++ that enable polymorphism, allowing you to write more flexible and reusable code. They help you achieve dynamic behavior, ensuring that the appropriate function is called based on the object type rather than the pointer type.


----

### **Key Differences**
- **Implementation**: 
  - Virtual functions can have a definition in the base class.
  - Pure virtual functions do not have a definition in the base class.

- **Abstract Classes**:
  - A class with virtual functions can be instantiated unless it has a pure virtual function.
  - A class with at least one pure virtual function becomes an abstract class and cannot be instantiated.

- **Usage**:
  - Use virtual functions when you want to allow derived classes the option to override a function, but still provide a default behavior.
  - Use pure virtual functions when you want to enforce that all derived classes must implement a specific function, effectively making the base class a blueprint (interface) for the derived classes.

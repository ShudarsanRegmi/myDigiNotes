# Friend Function in CPP

>A friend class can access private and protected members of other classes in which it is declared as a friend. It is sometimes useful to allow a particular class to access private and protected members of other classes. For example, a LinkedList class may be allowed to access private members of Node.

### Syntax:
```cpp
friend class class_name; // declared in base class
```

```cpp
class Geeks {
  friend class GFG;
}

class GFG {
  // Statements
}

```

### Code to illustrate friend class
```cpp
#include <iostream>

class classA {
private:
    int Amem;

    void static func_of_classA() {
        // since this funciton is not doing anything with non-static data member thsi can be made static
        std::cout << "This is some private method in classA";
    }
protected:
    int protected_mem1;

public:
    classA(int val) {
        Amem = val;
    }

    friend class classB;

};

class classB {
private:
    int Bmem;

    static void func2() {
        // since this funciton is not doing anything with non-static data member thsi can be made static
        std::cout << "This is some private method in classb";
    }

public:
    classB(int val) {
        Bmem = val;
    }
   static void access_mem1_of_classA(classA& obj) {
        std::cout << obj.Amem;
        // despite this function being static, tihs is allowed because obj is the reference to an instance of classA object and sinse classB is the freind of classA, method of class A can access the private member of classA
    }

};


int main() {
    classA c1(5);
    classB c2(10);
    c2.access_mem1_of_classA(c1);


    return 0;
}
```

---

### Member Function

**Global funciton as friend function**

```cpp
// using global functin as friend function

#include <iostream>

class base {
private:
    int private_variable;

protected:
    int protected_member;

public:
    base() {
        private_variable = 10;
        protected_member = 99;
    }

    friend void global_func_friend_func(base& obj);
};


void global_func_friend_func(base &obj) {
    std::cout << obj.private_variable << std::endl;
    std::cout << obj.protected_member << std::endl;
}

int main() {
    base Object1;
    global_func_friend_func(Object1);
    return 0;
}

```

**member of another function as friend function**

```cpp
#include <iostream>

class base; // forward definition needed

class anotherClass {
public:
    void memberFunction(base& obj);
};

// base class for which friend is declared
class base {
private:
    int private_variable;

protected:
    int protected_variable;

public:
    base() {
        private_variable = 10;
        protected_variable = 20;
    }

    friend void anotherClass::memberFunction(base& obj);
};


void anotherClass::memberFunction(base& obj) {
    std::cout << "Private Variable: " << obj.private_variable << std::endl;
    std::cout << "Protected Variable: " << obj.protected_variable << std::endl;
}

int main() {
    base Object1;
    anotherClass object2;
    object2.memberFunction(Object1); // object2 can call the functino of object 1 and also can access its protected and private data members
    return 0;
}
```

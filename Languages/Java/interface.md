# Interface in Java

- Interface methods are by default abstract and public
- Interface attributes are by default public, static and final


### **`implements` Keyword in Java**  

The `implements` keyword in Java is used when a class wants to inherit behavior from an **interface**. Since Java **does not support multiple inheritance** with classes, interfaces provide a way for a class to inherit multiple behaviors.

---

### **1. Syntax of `implements`**
A class uses `implements` to adopt an interface's methods:

```java
interface Animal {
    void makeSound();  // Method without implementation
}

class Dog implements Animal {
    public void makeSound() {  // Implementing the method
        System.out.println("Bark");
    }
}

public class Main {
    public static void main(String[] args) {
        Dog d = new Dog();
        d.makeSound();  // Output: Bark
    }
}
```

---

### **2. How `implements` Works**
1. **An interface** is like a contract—any class that `implements` it must define all its methods.
2. A class **can implement multiple interfaces**, providing multiple behaviors.
3. **Unlike inheritance (`extends`), which allows a class to inherit from only one class, `implements` supports multiple interfaces**.

---

### **3. Implementing Multiple Interfaces**
A class can implement multiple interfaces by separating them with commas:

```java
interface Animal {
    void eat();
}

interface Pet {
    void play();
}

// Dog class implements multiple interfaces
class Dog implements Animal, Pet {
    public void eat() {
        System.out.println("Dog is eating.");
    }

    public void play() {
        System.out.println("Dog is playing.");
    }
}

public class Main {
    public static void main(String[] args) {
        Dog d = new Dog();
        d.eat();
        d.play();
    }
}
```
**Output:**
```
Dog is eating.
Dog is playing.
```

---

### **4. Difference Between `extends` and `implements`**
| Feature | `extends` | `implements` |
|---------|----------|-------------|
| Used With | Classes and interfaces | Only interfaces |
| Number of Parents | Only one class can be extended | Multiple interfaces can be implemented |
| Inheritance Type | Inherits methods and properties | Only defines method signatures (no properties) |
| Abstract Methods | Not required in extended class | Must be implemented in the class |

Example:
```java
// Extending a class
class Animal {
    void breathe() {
        System.out.println("Breathing...");
    }
}

class Dog extends Animal {
    void bark() {
        System.out.println("Barking...");
    }
}

// Implementing an interface
interface Pet {
    void play();
}

class Cat implements Pet {
    public void play() {
        System.out.println("Cat is playing.");
    }
}
```

---

### **5. Default and Static Methods in Interfaces**
Since Java 8, interfaces can have **default methods** (with implementations) and **static methods**.

```java
interface Vehicle {
    default void start() {
        System.out.println("Vehicle is starting...");
    }
    
    static void stop() {
        System.out.println("Vehicle is stopping...");
    }
}

class Car implements Vehicle {
    // No need to override start() unless we want a custom behavior
}

public class Main {
    public static void main(String[] args) {
        Car c = new Car();
        c.start();  // Calls default method

        Vehicle.stop();  // Calls static method
    }
}
```

**Output:**
```
Vehicle is starting...
Vehicle is stopping...
```

---

### **6. Key Takeaways**
✅ **`implements` is used for interfaces, `extends` is for classes.**  
✅ **A class can implement multiple interfaces, but can extend only one class.**  
✅ **Interfaces allow defining method contracts without implementation.**  
✅ **Java 8+ allows default and static methods inside interfaces.**  

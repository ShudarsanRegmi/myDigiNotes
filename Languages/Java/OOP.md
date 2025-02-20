# Important Concepts of OOP in Java


## It is either static void func or public void func
```java
  static void myStaticMethod() {
    System.out.println("Static methods can be called without creating objects");
  }
```
```java
  // Public method
  public void myPublicMethod() {
    System.out.println("Public methods must be called by creating objects");
  }
```

## Abstract Class in Java
```java
// Code from filename: Main.java
// abstract class
abstract class Main {
  public String fname = "John";
  public int age = 24;
  public abstract void study(); // abstract method
}

// Subclass (inherit from Main)
class Student extends Main {
  public int graduationYear = 2018;
  public void study() { // the body of the abstract method is provided here
    System.out.println("Studying all day long");
  }
}
// End code from filename: Main.java

// Code from filename: Second.java
class Second {
  public static void main(String[] args) {
    // create an object of the Student class (which inherits attributes and methods from Main)
    Student myObj = new Student();

    System.out.println("Name: " + myObj.fname);
    System.out.println("Age: " + myObj.age);
    System.out.println("Graduation Year: " + myObj.graduationYear);
    myObj.study(); // call abstract method
  }
}
```

## Inheritance and the use of super keyword in Java
```java
public class Animal {
    public String category;
    public int age;
    public int height;
    public int weight;

    public Animal(String category, int age, int height, int weight) {
        this.category = category;
        this.age = age;
        this.height = height;
        this.weight = weight;
    }

    public void makeSound() {
        System.out.println("Making Sound");
    }

    public static void main(String[] args) {
        Cat cat1 = new Cat("animal", 5, 2, 2, "gray", "cute");
        cat1.makeSound();
    }
}


class Cat extends Animal {
    public String color;

    private String appearance;

    public Cat(String category, int age, int height, int weight, String color, String appearance) {
        super(category, age, height, weight);
        this.color = color;
        this.appearance = appearance;
    }

    public String getAppearance() {
        return this.appearance;
    }
    public void setAppearance(String appearance) {
        this.appearance = appearance;
    }
    @Override
    public void makeSound() {
        System.out.println("Meow..");
    }
}

class Dog extends Animal {
    public String color;
    private String appearance;

    public Dog(String category, int age, int height, int weight, String color, String appearance) {
        super(category, age, height, weight);
        this.color = color;
        this.appearance = appearance;
    }
    @Override
    public void makeSound() {
        System.out.println("Bhow Bhow..");
    }
}
```


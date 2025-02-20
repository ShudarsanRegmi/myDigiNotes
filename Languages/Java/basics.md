# Basics of Java


### Hello, World Program
```java
class main {
    public static void main(String[] args) {
        System.out.println("Hello, world");
    }
}
```

```java
public class main {
    public static void main(String[] args) {
        System.out.println("Hello, world");
    }
}
```
>The class is package-private by default, meaning it is only accessible within the same package.


## Important Points
- Every line of code that runs in Java must be inside a class. And the class name should always start with an uppercase first letter. In our example, we named the class Main.
- Java file name must match with class name
- It is owned by Oracle, and more than **3 billion** devices run Java.

## Data Types
- String
- int
- float
- boolean
- char

```java
int myNum = 5;
float myFloatNum = 5.99f;
char myLetter = 'D';
boolean myBool = true;
String myText = "Hello";
```

## Making constants : final keyword
```java
final x = 5;
```

## Primitive and non-primitive data types
- Non-primitive data types are called reference types because they refer to objects.
- Primitive types always hold a value, whereas non-primitive types can be null.
- Primitive types start with a lowercase letter (like int), while non-primitive types typically starts with an uppercase letter (like String).

## Type casting
- In Java, there are two types of casting:

- Widening Casting (automatically) - converting a smaller type to a larger type size
```
byte -> short -> char -> int -> long -> float -> double
```
- Narrowing Casting (manually) - converting a larger type to a smaller size type
```
double -> float -> long -> int -> char -> short -> byte
```

```java
double myDouble = myInt; // Automatic casting: int to double ; going to higher data type
double myDouble = 9.78d;
int myInt = (int) myDouble; // Manual casting: double to int ; going to lower data type
```



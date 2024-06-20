# Kotlin note

## Variables

```kotlin
val a = 10 // read only
var b = 5 // mutable variable
```

### Writing to stdout

```kotlin
print("String") 
println("String")
println("There are ${customers + 1} customers") // template expression
```

### Arithematic Operations

```kotlin
customers = 8
customers = customers + 3 // Example of addition: 11
customers += 7            // Example of addition: 18
customers -= 3            // Example of subtraction: 15
customers *= 2            // Example of multiplication: 30
customers /= 3            // Example of division: 10
```

### Explicitly mentioning the type

```kotlin
val d: Int
d = 3
val ram:String = "ramlal"
```

## Collections

### All collections

| Lists | Ordered collections of items                                 |
| ----- | ------------------------------------------------------------ |
| Sets  | Unique unordered collections of items                        |
| Maps  | Sets of key-value pairs where keys are unique and map to only one value |

### Creating lists

```kotlin
val readOnlyShapes = listOf("triangle", "square", "circle") // non-mutable
val shapes: MutableList<String> = mutableListOf("triangle", "square", "circle")
// casting can be done to convert mutable lists to non-mutable ones
println("circle" in readOnlyShapes) // iterating
// Extension functions like .add(), .remove(), .first(), .last() are there

```



## Control Flow

```kotlin

val check = true

if (check) {
    
} else {
}
val a = 5
val b = 10
println(if (a > b) a else b) // Returns a value: 2
```

### using when

```kotlin
val obj = "Hello"

when (obj) {
    // Checks whether obj equals to "1"
    "1" -> println("One")
    // Checks whether obj equals to "Hello"
    "Hello" -> println("Greeting")
    // Default statement
    else -> println("Unknown")     
}
// Greeting
```

```kotlin
val temp = 18
​
val description = when {
    // If temp < 0 is true, sets description to "very cold"
    temp < 0 -> "very cold"
    // If temp < 10 is true, sets description to "a bit cold"
    temp < 10 -> "a bit cold"
    // If temp < 20 is true, sets description to "warm"
    temp < 20 -> "warm"
    // Sets description to "hot" if no previous condition is satisfied
    else -> "hot"             
}
println(description)
// warm

```

### Ranges

```kotlin
1..4 // 1,2,3,4
1..<4 // 1,2,3
4 downTo 1 // 4,3,2,1
1..5 step 2 // 1,3,5

'a'..'d'
'z' downTo 's'step 2
```

### for loop

```kotlin
for i in 1...4{}
for i in collection
```

## Functions

```kotlin
fun sum(x: Int, y: Int): Int {
    return x + y
}

fun main() {
    println(sum(1, 2))
    // 3
}
```

## Classes

### Creating class

```kotlin
class Contact(val id: Int, var email: String = "example@gmail.com") {
    val category: String = "work"
}
// creating an instance
fun main() {
    val contact = Contact(1, "mary@gmail.com")
}
// accessing and all are similar to other languages
```

## Data class

Kotlin has data classes which are particularly useful for storing data. Data classes have the same functionality as classes, but they come automatically with additional member functions. These member functions allow you to easily print the instance to readable output, compare instances of a class, copy instances, and more. As these functions are automatically available, you don't have to spend time writing the same boilerplate code for each of your classes.

| `.toString()`       | Prints a readable string of the class instance and its properties. |
| ------------------- | ------------------------------------------------------------ |
| `.equals()` or `==` | Compares instances of a class.                               |
| `.copy()`           | Creates a class instance by copying another, potentially with some different properties. |

## Null safety

In Kotlin, it's possible to have a `null` value. To help prevent issues with `null` values in your programs, Kotlin has null safety in place. Null safety detects potential problems with `null` values at compile time, rather than at run time.

`?` denotes a nullable type, allowing the variable to hold a null value.

`?:` is the Elvis operator, providing a default value if the expression on the left is null.


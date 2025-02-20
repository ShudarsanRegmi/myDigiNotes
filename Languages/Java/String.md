### **Strings in Java – Complete Notes**  

#### **1. Introduction**  
A `String` in Java is a sequence of characters enclosed in double quotes (`""`). It is an **immutable** object, meaning its value cannot be changed once created. Java provides the `String` class in the `java.lang` package, which offers various methods for string manipulation.

---

#### **2. Creating Strings**  
Strings can be created in two ways:  

##### **(a) Using String Literals (Stored in String Pool)**
```java
String s1 = "Hello";  
String s2 = "Hello";  // Points to the same object as s1 in the string pool
```
- Strings created using literals are stored in the **String Pool** inside the heap memory.
- If a string already exists in the pool, Java will reuse the reference instead of creating a new object.

##### **(b) Using `new` Keyword (Stored in Heap Memory)**
```java
String s3 = new String("Hello");  // Creates a new object in the heap
```
- Even if the same string exists in the pool, `new` forces Java to create a **new** object in heap memory.

---

#### **3. Immutability of Strings**  
- Strings in Java are **immutable**, meaning their value cannot be changed after creation.
- Every modification (concatenation, replacement, etc.) creates a **new** string instead of modifying the original one.

Example:
```java
String s = "Hello";
s = s + " World";  // Creates a new string "Hello World"
```
- The original `"Hello"` string remains in memory (unless garbage collected).
- To modify a string efficiently, use `StringBuilder` or `StringBuffer`.

---

#### **4. Important String Methods**  
Java provides several built-in methods to manipulate strings:

| **Method** | **Description** | **Example** |
|------------|----------------|-------------|
| `length()` | Returns length of string | `"Java".length(); // 4` |
| `charAt(index)` | Returns character at given index | `"Java".charAt(1); // 'a'` |
| `substring(start, end)` | Extracts substring | `"Java".substring(1,3); // "av"` |
| `toUpperCase()` | Converts to uppercase | `"java".toUpperCase(); // "JAVA"` |
| `toLowerCase()` | Converts to lowercase | `"JAVA".toLowerCase(); // "java"` |
| `trim()` | Removes leading & trailing spaces | `" Java ".trim(); // "Java"` |
| `indexOf(char)` | Returns index of character | `"Java".indexOf('v'); // 2` |
| `replace(old, new)` | Replaces characters | `"Java".replace('a', 'o'); // "Jovo"` |
| `split(delimiter)` | Splits string into array | `"a,b,c".split(","); // ["a", "b", "c"]` |
| `equals(str)` | Checks string equality | `"java".equals("Java"); // false` |
| `equalsIgnoreCase(str)` | Checks equality ignoring case | `"java".equalsIgnoreCase("Java"); // true` |

---

#### **5. String Concatenation**
##### **(a) Using `+` Operator**  
```java
String s1 = "Hello" + " World";  // "Hello World"
```
- Internally optimized using `StringBuilder` for literals.

##### **(b) Using `concat()` Method**  
```java
String s2 = "Hello".concat(" World");  // "Hello World"
```

---

#### **6. Comparing Strings**
##### **(a) Using `equals()` (Checks Content)**
```java
String s1 = "Java";
String s2 = "Java";
System.out.println(s1.equals(s2));  // true
```
- Compares **actual content**.

##### **(b) Using `==` (Checks Reference)**
```java
String s3 = new String("Java");
System.out.println(s1 == s3);  // false (different objects in memory)
```
- Checks **memory reference**, not content.

##### **(c) Using `compareTo()` (Lexicographical Comparison)**
```java
System.out.println("apple".compareTo("banana"));  // Negative (-1)
System.out.println("banana".compareTo("apple"));  // Positive (1)
System.out.println("apple".compareTo("apple"));   // Zero (0)
```
- Returns `0` if equal, negative if smaller, and positive if greater.

---

#### **7. StringBuffer & StringBuilder (Mutable Strings)**
Since `String` is immutable, Java provides **mutable alternatives**:

| **Feature** | **StringBuffer** | **StringBuilder** |
|------------|----------------|----------------|
| **Mutability** | Mutable | Mutable |
| **Thread Safety** | Yes (synchronized) | No |
| **Performance** | Slower due to synchronization | Faster |

##### **Example Usage**
```java
StringBuilder sb = new StringBuilder("Hello");
sb.append(" World");  // Modifies the original string
System.out.println(sb);  // "Hello World"
```

---

#### **8. String Formatting (`String.format()`)**
```java
String name = "John";
int age = 25;
String formatted = String.format("My name is %s and I am %d years old.", name, age);
System.out.println(formatted);  // "My name is John and I am 25 years old."
```
- `%s` → String  
- `%d` → Integer  
- `%f` → Float  

---

#### **9. String Interning (Memory Optimization)**
Java maintains a **String Pool** to optimize memory usage.

```java
String s1 = "Java";
String s2 = new String("Java").intern();  // Forces storage in String Pool
System.out.println(s1 == s2);  // true
```
- The `intern()` method ensures that the string is stored in the pool.

---

#### **10. String Tokenization**
To break a string into smaller tokens:
```java
String sentence = "Java is awesome";
String[] words = sentence.split(" ");
for (String word : words) {
    System.out.println(word);
}
```
**Output:**  
```
Java
is
awesome
```

---

### **Key Takeaways**
✅ **Immutable:** String values cannot be changed.  
✅ **Efficient Storage:** Uses **String Pool** to optimize memory.  
✅ **Comparisons:** Use `.equals()`, not `==`, for content comparison.  
✅ **Performance:** Use `StringBuilder` for fast string manipulations.  
✅ **Thread Safety:** Use `StringBuffer` if synchronization is required.  

Would you like any further clarification? 🚀

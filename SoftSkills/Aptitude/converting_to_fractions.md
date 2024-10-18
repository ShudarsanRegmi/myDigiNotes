# Converting Recurring Decimals to Fractions

## Working Rule
1. Assume the given number is \(x\).
2. Multiply it by \(10^n\) so that the digits after the decimal point start repeating.
3. Multiply it by \(10^m\) (where \(m > n\)) so that the number after the decimal point is completely recurring.
4. Subtract the two equations and solve for \(x\).

---

### **Type 1: Recurring starts right after the decimal**

Example: \(x = 3.121212\ldots\)

1. Let \(x = 3.121212\ldots\)
2. Multiply both sides by 100:  
   \[
   100x = 312.121212\ldots
   \]
3. Subtract the first equation from the second:  
   \[
   100x - x = 312.121212\ldots - 3.121212\ldots
   \]
4. Simplify:  
   \[
   99x = 309
   \]
5. Solve for \(x\):  
   \[
   x = \frac{309}{99} = \frac{103}{33}
   \]

---

### **Type 2: Recurring starts after some digits**

Example: \(x = 0.123232323\ldots\)

1. Let \(x = 0.123232323\ldots\)
2. Multiply both sides by 10:  
   \[
   10x = 1.232323\ldots
   \]
3. Multiply both sides by 1000:  
   \[
   1000x = 123.232323\ldots
   \]
4. Subtract the first equation from the second:  
   \[
   1000x - 10x = 123.232323\ldots - 1.232323\ldots
   \]
5. Simplify:  
   \[
   990x = 122
   \]
6. Solve for \(x\):  
   \[
   x = \frac{122}{990}
   \]

---

### **Examples of Variants:**
1. \(0.123123123\ldots\)
2. \(0.12333333\ldots\)

---

> **Note**: This note uses MathJax formatting, which renders mathematical expressions in LaTeX style.
>

```math
SE = \frac{\sigma}{\sqrt{n}}
```

This sentence uses `$` delimiters to show math inline:  $\sqrt{3x-1}+(1+x)^2$


# Converting Recurring Decimals to Fractions

## Working Rule
1. Assume the given number is $x$.
2. Multiply it by $10^n$ so that the digits after the decimal point start repeating.
3. Multiply it by $10^m$ (where $m > n$) so that the number after the decimal point is completely recurring.
4. Subtract the two equations and solve for $x$.

---

### **Type 1: Recurring starts right after the decimal**

Example: $x = 3.\overline{12}$

1. Let $x = 3.\overline{12}$
2. Multiply both sides by 100:  
   $$
   100x = 312.\overline{12}
   $$
4. Subtract the first equation from the second:  
   $$ 100x - x = 312.\overline{12} - 3.\overline{12} $$
5. Simplify:  
   $$ 99x = 309 $$
6. Solve for $x$:  
   $$ x = \frac{309}{99} = \frac{103}{33} $$

---

### **Type 2: Recurring starts after some digits**

Example: $x = 0.1\overline{23}$

1. Let $x = 0.1\overline{23}$
2. Multiply both sides by 10:  
   $$ 10x = 1.\overline{23} $$
3. Multiply both sides by 1000:  
   $$ 1000x = 123.\overline{23} $$
4. Subtract the first equation from the second:  
   $$ 1000x - 10x = 123.\overline{23} - 1.\overline{23} $$
5. Simplify:  
   $$ 990x = 122 $$
6. Solve for $x$:  
   $$ x = \frac{122}{990} $$

---

### **Examples of Variants:**
1. $0.\overline{123}$
2. $0.1\overline{23}$
3. $0.1\overline{333}$

---

> **Note**: This note uses inline and block math expressions according to MathJax standards. For recurring decimals, the "bar" notation is used.

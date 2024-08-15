# Formulating the dual of given LPP problem

---

### **Step 1: Identify the Primal Problem Structure**

Assume the primal problem is in the following standard form:

- **Maximization Form**:
  
  ```
  Maximize Z = c1*x1 + c2*x2 + ... + cn*xn
  ```
  
  Subject to:
  
  ```
  a11*x1 + a12*x2 + ... + a1n*xn ≤ b1
  a21*x1 + a22*x2 + ... + a2n*xn ≤ b2
  ...
  am1*x1 + am2*x2 + ... + amn*xn ≤ bm
  x1, x2, ..., xn ≥ 0
  ```

Here, `x1, x2, ..., xn` are the decision variables, `c1, c2, ..., cn` are the coefficients of the objective function, `aij` are the coefficients of the constraints, and `b1, b2, ..., bm` are the right-hand side values of the constraints.

### **Step 2: Formulate the Dual Problem**

The dual problem is formulated as follows:

1. **Objective Function**:
   - If the primal is a **maximization** problem, the dual will be a **minimization** problem, and vice versa.
   - The objective function coefficients in the dual problem are the right-hand side values (`b1, b2, ..., bm`) of the primal constraints.

   Dual Objective Function:
   
   ```
   Minimize W = b1*y1 + b2*y2 + ... + bm*ym
   ```
   
   Here, `y1, y2, ..., ym` are the dual variables associated with the primal constraints.

2. **Constraints**:
   - The dual constraints are derived from the primal objective function coefficients and the primal constraint coefficients.
   - Each primal decision variable `xj` corresponds to a dual constraint.
   - The coefficients of each dual constraint are the corresponding elements in the primal constraint matrix (`aij`).

   For each `j` (where `j` ranges from 1 to `n`, the number of primal variables), the dual constraints are:
   
   ```
   a11*y1 + a21*y2 + ... + am1*ym ≥ c1
   a12*y1 + a22*y2 + ... + am2*ym ≥ c2
   ...
   a1n*y1 + a2n*y2 + ... + amn*ym ≥ cn
   ```

3. **Variable Sign Constraints**:
   - If the primal problem has a `≤` constraint, the corresponding dual variable `yi` will be `≥ 0`.
   - If the primal problem has a `≥` constraint, the corresponding dual variable `yi` will be `≤ 0`.
   - If the primal problem has an equality constraint, the corresponding dual variable `yi` can be unrestricted in sign (i.e., it can be positive, negative, or zero).

   Since in our example all primal constraints are `≤`, all dual variables `y1, y2, ..., ym ≥ 0`.

### **Step 3: Write the Dual Problem**

Given the example primal problem, the dual problem would be:

- **Dual Problem**:

  ```
  Minimize W = b1*y1 + b2*y2 + ... + bm*ym
  ```
  
  Subject to:
  
  ```
  a11*y1 + a21*y2 + ... + am1*ym ≥ c1
  a12*y1 + a22*y2 + ... + am2*ym ≥ c2
  ...
  a1n*y1 + a2n*y2 + ... + amn*ym ≥ cn
  y1, y2, ..., ym ≥ 0
  ```

### **Example:**

Let’s consider a simple example to illustrate:

- **Primal Problem**:
  
  ```
  Maximize Z = 3*x1 + 2*x2
  ```
  
  Subject to:
  
  ```
  2*x1 + x2 ≤ 4
  x1 + 2*x2 ≤ 5
  x1, x2 ≥ 0
  ```

- **Dual Problem**:
  - Objective function: Minimize `W = 4*y1 + 5*y2`
  
  - Constraints:
    
    ```
    2*y1 + y2 ≥ 3
    y1 + 2*y2 ≥ 2
    y1, y2 ≥ 0
    ```

### **Summary of Formulating the Dual:**

1. The coefficients of the primal constraints' right-hand side become the coefficients in the dual objective function.
2. The coefficients of the primal objective function become the right-hand side values in the dual constraints.
3. The inequality direction is reversed when moving from primal constraints to dual constraints.
4. The dual variables correspond to the primal constraints and are non-negative if the primal constraints are `≤` inequalities.

The dual problem provides insight into the value of resources in the primal problem and can be used to solve the primal problem indirectly.

### Summary: Two-Phase Simplex Method

The Two-Phase Simplex Method is used to solve linear programming problems, particularly when the initial basic feasible solution (BFS) is not readily available. The method consists of two phases:

#### **Phase I:**
- **Objective:** Find an initial BFS by driving all artificial variables to zero.
- **Steps:**
  1. **Artificial Objective Function:** A new objective function \( w \) is created as the sum of all artificial variables. This function is minimized subject to the original problem's constraints.
  2. **Outcomes:**
     - **Case 1:** If the minimum value of \( w \) > 0 and at least one artificial variable remains positive, the problem has no feasible solution, and the procedure terminates.
     - **Case 2:** If the minimum value of \( w = 0 \) and no artificial variables are in the basis, a BFS for the original problem is obtained, and the artificial variables are deleted for Phase II.
     - **Case 3:** If the minimum value of \( w = 0 \) and some artificial variables remain in the basis at zero level, a BFS is obtained, but these variables must be carefully managed to ensure they do not become positive during Phase II.

#### **Phase II:**
- **Objective:** Find the optimal solution to the original linear programming problem using the BFS obtained in Phase I.
- **Steps:**
  1. The final tableau from Phase I becomes the starting point for Phase II.
  2. The artificial objective function \( w \) is replaced by the original objective function, and the simplex method is applied to find the optimal solution.
  3. Artificial variables not in the basis are deleted.

#### **Remarks:**
1. Iterations in Phase I are stopped as soon as the value of the artificial objective function becomes zero, as this indicates its minimum value.
2. The artificial objective function \( w \) is always minimized, regardless of whether the original problem is a minimization or maximization problem.

---

In the Two-Phase Simplex Method, the concept of applying costs in Phase II involves transitioning from the artificial objective function (used in Phase I) to the original objective function. Here’s how this process works:

### **Phase II: Applying Costs to Variables**
- **Objective:** After Phase I has identified a basic feasible solution (BFS), the focus shifts to finding the optimal solution for the original linear programming problem. This requires reintroducing the original cost coefficients to the variables that were used in the initial problem.

- **Steps:**
  1. **Reintroducing the Original Costs:**
     - The cost coefficients (denoted as \( c_j \)) from the original problem are reassigned to the corresponding variables (e.g., \( x_1, x_2 \)) in the simplex tableau.
     - For artificial variables that remain in the basis at zero level (i.e., they have a value of zero but are still part of the solution), a cost coefficient of zero is assigned. This ensures that these variables do not influence the optimal solution but are still considered in the calculations.

  2. **Constructing the Phase II Tableau:**
     - The final tableau from Phase I becomes the starting tableau for Phase II. The cost coefficients from the original problem are placed at the top row of this tableau.
     - The \( c_j - Z_j \) row is recalculated using the new cost coefficients.

  3. **Applying the Simplex Method:**
     - The simplex method is then applied to this tableau, with the objective of optimizing the original linear programming problem using the BFS obtained from Phase I.

### **Example from the Image:**
- In the image, you see a transition to Phase II where the costs from the original problem are reintroduced:
  - The artificial variable \( A_1 \), which appeared at zero level in the basis during Phase I, is assigned a zero cost coefficient. This is noted as \( 0 \times A_1 \) in the objective function.
  - The original objective function \( Z = 2x_1 + x_2 + \frac{1}{4}x_3 + 0s_1 + 0s_2 + 0s_3 + 0A_1 \) is then used to start the simplex iterations in Phase II.

### **Why Assign Zero Costs?**
- The purpose of assigning zero cost to artificial variables that remain in the basis at zero level is to ensure that they do not affect the optimization of the original problem. These variables are retained to maintain the structure of the simplex tableau but are effectively ignored in terms of their contribution to the objective function.

### **Final Note:**
- As Phase II progresses, if any artificial variable becomes positive, special care is needed to prevent it from affecting the solution, which may involve selecting it as the outgoing variable during pivot operations. This helps in ensuring that the solution remains feasible.

This process ensures that the solution to the original problem is found efficiently, starting from a valid basic feasible solution obtained during Phase I.

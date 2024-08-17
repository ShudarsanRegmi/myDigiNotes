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

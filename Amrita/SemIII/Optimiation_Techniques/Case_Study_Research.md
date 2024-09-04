# Materials Collected for Case-Study for Optimization Techniques
Got it! Let’s take a more mathematically grounded approach to Airline Revenue Management (ARM) and stay aligned with your syllabus while addressing optimization models.

### Problem Formulation for Airline Revenue Management

In ARM, the goal is to maximize total revenue from selling seats, considering that demand fluctuates and the number of available seats is limited. We will focus on **seat allocation** across different fare classes to formulate and solve the optimization problem.

#### Notation:

Let’s define the following parameters:
- \( C \): Total number of seats on the plane (capacity constraint).
- \( n \): Number of fare classes (e.g., first class, business class, economy).
- \( p_i \): Price per seat for fare class \( i \), for \( i = 1, 2, ..., n \).
- \( x_i \): Number of seats allocated to fare class \( i \).
- \( d_i \): Expected demand for fare class \( i \).

The objective is to maximize the total revenue by optimally allocating seats to each fare class, subject to the constraint that the total number of seats allocated cannot exceed the plane’s capacity.

#### Objective Function:

The revenue for each fare class \( i \) is \( p_i \times x_i \), so the total revenue is:

\[
\text{Maximize} \; R(x) = \sum_{i=1}^{n} p_i \cdot x_i
\]

#### Constraints:

- **Capacity Constraint**: The sum of the allocated seats across all fare classes cannot exceed the total capacity:
  \[
  \sum_{i=1}^{n} x_i \leq C
  \]
  
- **Demand Constraint**: The allocated seats cannot exceed the expected demand for that fare class:
  \[
  x_i \leq d_i \quad \text{for all} \; i
  \]
  
- **Non-Negativity Constraint**: The number of seats allocated must be non-negative:
  \[
  x_i \geq 0 \quad \text{for all} \; i
  \]

### Mathematical Model:

The optimization model for ARM can be formulated as:

\[
\text{Maximize} \quad R(x) = \sum_{i=1}^{n} p_i \cdot x_i
\]
\[
\text{Subject to:}
\]
\[
\sum_{i=1}^{n} x_i \leq C \quad \text{(Capacity constraint)}
\]
\[
x_i \leq d_i \quad \text{for all} \; i \quad \text{(Demand constraint)}
\]
\[
x_i \geq 0 \quad \text{for all} \; i \quad \text{(Non-negativity constraint)}
\]

This is a **Linear Programming (LP) problem**, which can be solved using the **Simplex Method** or other numerical optimization techniques from your syllabus.

### Example: Application and Impact of Optimization

#### Case Study Example

Suppose an airline operates a plane with a capacity of \( C = 150 \) seats, and it offers tickets in three fare classes: first class, business class, and economy. The prices and expected demand for each fare class are as follows:

- **First Class**: \( p_1 = \$500 \), \( d_1 = 20 \)
- **Business Class**: \( p_2 = \$300 \), \( d_2 = 50 \)
- **Economy Class**: \( p_3 = \$100 \), \( d_3 = 100 \)

Using this information, the optimization model becomes:

\[
\text{Maximize} \quad R(x) = 500 \cdot x_1 + 300 \cdot x_2 + 100 \cdot x_3
\]
\[
\text{Subject to:}
\]
\[
x_1 + x_2 + x_3 \leq 150 \quad \text{(Capacity constraint)}
\]
\[
x_1 \leq 20, \; x_2 \leq 50, \; x_3 \leq 100 \quad \text{(Demand constraints)}
\]
\[
x_1, x_2, x_3 \geq 0 \quad \text{(Non-negativity constraints)}
\]

### Solving the Optimization Problem

To solve this problem using the Simplex Method:

1. **Initial Feasible Solution**: Start by allocating as many seats as possible to the highest-paying fare class while respecting the demand constraints.

2. **Iterative Adjustment**: Use the Simplex algorithm to adjust the allocation to maximize total revenue.

### Solution:

Given the objective and constraints, the airline should allocate seats based on the demand and revenue per seat:

1. First, allocate 20 seats to First Class (since this class has the highest price and the demand is 20).
2. Then, allocate 50 seats to Business Class (next highest price and the demand is 50).
3. The remaining \( 150 - 20 - 50 = 80 \) seats are allocated to Economy Class.

The optimal solution is:
- \( x_1 = 20 \) (First Class)
- \( x_2 = 50 \) (Business Class)
- \( x_3 = 80 \) (Economy Class)

The total revenue will be:
\[
R = 500 \cdot 20 + 300 \cdot 50 + 100 \cdot 80 = 10,000 + 15,000 + 8,000 = 33,000 \text{ dollars}
\]

### Impact of Optimization:

- **Revenue Maximization**: This allocation yields the maximum possible revenue of \$33,000, given the constraints.
- **Efficient Seat Allocation**: The optimization ensures that no seats are wasted and that the airline takes advantage of the higher-paying fare classes first, which maximizes profit.

### Conclusion:

By using optimization techniques like Linear Programming, airlines can effectively allocate seats to maximize revenue while respecting demand and capacity constraints. In this case, the Simplex Method helped identify the optimal allocation, ensuring the airline made the most out of its fixed resources. Such methods directly contribute to improving profitability and operational efficiency in the airline industry, which is crucial in the highly competitive aviation market.

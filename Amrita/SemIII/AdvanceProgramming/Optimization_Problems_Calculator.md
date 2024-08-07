# Review of Tools that are available for solving optimization Problems

## Tool 1: Wolfram Alpha lpp calculator
> It provides maximum and minimum solutions with no iteration tables
- [Wolfram Alpha Online Tool](https://www.wolframalpha.com/widgets/view.jsp?id=daa12bbf5e4daec7b363737d6d496120)
- 
![image](https://github.com/user-attachments/assets/1df2fc22-395b-4c3d-93c7-e01b530ce045)

## Tool 2: Two Phase simplex method calculator with iteration tables
- [Simplex Method Calculator Two Phase method](https://www.pmcalculators.com/simplex-method-calculator/)

![image](https://github.com/user-attachments/assets/ed4afdc3-328d-466c-8157-22a32bc2b817)
![image](https://github.com/user-attachments/assets/7855fac6-7e62-4f9b-9919-1b1a1aa9855b)

## Tool 3: Graphical Method Calculator
> Optimize 2 variable problem with graphical method
- https://www.pmcalculators.com/graphical-method-calculator/
- 
![image](https://github.com/user-attachments/assets/242829ee-2d00-4795-a2d4-92fb8081b37b)

# Industrial Softwares

## LPSolve IDE
LPSolve IDE is an integrated development environment for the LP_Solve solver, which is an open-source software tool used for solving linear programming (LP) and mixed-integer programming (MIP) problems. Here's a detailed review of its features and limitations:

### Features of LPSolve IDE:

1. **User-Friendly Interface**:
2. **Support for Standard LP and MIP Problems**:
3. **Free and Open-Source**
4. **Integration with Other Tools**:
   - **Description**: LPSolve IDE can integrate with various other tools and programming environments, including C, C++, Java, and Python.
   - **Benefit**: This allows users to incorporate LP_Solve into larger, more complex workflows and systems.

### Limitations of LPSolve IDE:

1. **Performance on Large-Scale Problems**:
   - **Description**: LP_Solve may not be as efficient as some commercial solvers (like CPLEX or Gurobi) when dealing with very large or highly complex problems.
   - **Consequence**: Users working on large-scale industrial applications might encounter performance bottlenecks.
2. **Advanced Features**:
   - **Description**: LP_Solve lacks some advanced features and heuristics found in commercial solvers, such as advanced presolve techniques, parallel processing, and sophisticated branching strategies.
   - **Consequence**: This can limit its effectiveness for very complex or specific optimization problems.

### Conclusion:
LPSolve IDE is a valuable tool for those looking to solve linear programming problems without the cost associated with commercial solvers. Its user-friendly interface and integration capabilities make it suitable for educational purposes, research, and smaller-scale industrial applications. However, its limitations in handling large-scale problems, lack of advanced features, and potential gaps in support and documentation might make it less suitable for more demanding or complex optimization tasks.

### Problem
![image](https://github.com/user-attachments/assets/50849c39-51b5-454c-bb5c-97187c470597)

```
MAX Z = 5x1 + 10x2 + 8x3
subject to
3x1 + 5x2 + 2x3 <= 60
4x1 + 4x2 + 4x3 <= 72
2x1 + 4x2 + 5x3 <= 100
and x1,x2,x3 >= 0
Optimal Solution:
```

```
Maximize Z = x=12x1+ 16x2
Subject to 10x1 + 20x2 ≤ 120
8x1 + 8x2 ≤ 80
x1 and x2 ≥ 0
Optimal Solution: x1 = 8, x2 = 2 , z = 128

12x_1 + 16x_2
10x_1 + 20x_2 <= 120,
8x_1 + 8x_2 <= 80,
x_1 >= 0, x_2>=0
Solution Link: https://www.emathhelp.net/en/calculators/linear-programming/simplex-method-calculator/?z=12x_1+%2B+16x_2&max=on&c=10x_1+%2B+20x_2+%3C%3D+120%2C%0D%0A8x_1+%2B+8x_2+%3C%3D+80%2C%0D%0Ax_1+%3E%3D+0%2C+x_2%3E%3D0&m=m
```

```
max: z = 20x1 + 30x2
2x1 +x2<=10
3x1+3x2<=20
2x1+4x2<=20
x1>=0, x2>=0
Optimal Solution: x1 = 3.34, X2 = 3.34
```
```
Maximize: Z = 40x1 + 30x2
Subject to: x1 + x2 <= 12
2x1 + x2 <= 16
x1 >= 0, x2 >= 0
Solution: Z = 400 @ x1 = 4 and x2 = 8
https://www.emathhelp.net/en/calculators/linear-programming/simplex-method-calculator/?z=40x_1+%2B+30x_2&max=on&c=x_1+%2B+x_2+%3C%3D+12%2C%0D%0A2x_1+%2B+1x_2+%3C%3D+16%2C%0D%0Ax_1+%3E%3D+0%2C+x_2%3E%3D0&m=m
```
```
Maximize: Z = 12x1 + 3x2 + x3
Subject to: 10x1 + 2x2 + x3 <= 100
7x1 + 3x2 + 2x3 <= 77
2x1 + 4x2 + x3 <= 80
x1 >= 0, x2 >= 0, x3 >= 0
Solution: Z = 122.625, x1 = 9.125, x2 = 4.375
https://www.emathhelp.net/en/calculators/linear-programming/simplex-method-calculator/?z=12x_1+%2B+3x_2+%2B+x_3&max=on&c=10x_1+%2B+2x_2+%2B+x_3+%3C%3D+100%0D%0A7x_1+%2B+3x_2+%2B+2x_3+%3C%3D+77%0D%0A2x_1+%2B+4x_2+%2B+x_3+%3C%3D+80%0D%0Ax_1+%3E%3D+0%2C+x_2+%3E%3D+0%2C+x_3+%3E%3D+0&m=m
```


```
Z = 100x1​+1900x2​+2700x3​+3400x4​
18x1​+28x2​+4x3​+5x4​−2125x5 ​≤ 0,
−8x1​+2x2​+2x3​+2x4​+5≤0
−8x1​+2x2​+2x3​+2x4​−5≤0
x1​−9x2​+x3​+x4​+5≤0
25x1​+25x2​−75x3​−75x4​+5≤0
50x1​+70x2​+130x3​+160x4​+2x5​≤15000
x1​≥0x2​≥0x3​≥0x4​≥0x5​≥0​
https://www.emathhelp.net/en/calculators/linear-programming/simplex-method-calculator/?z=100x_1+%2B+1900x_2+%2B+2700x_3+%2B+3400x_4&max=on&c=18x_1+%2B+28x_2+%2B+4x_3+%2B+5x_4+-2125x_5+%3C%3D+0%0D%0A-8x_1+%2B+2x_2+%2B+2x_3+%2B+2x_4+%2B+0x_5+%3C%3D+0%0D%0A-8x_1+%2B+2x_2+%2B+2x_3+%2B+2x_4+-+0x_5+%3C%3D+0%0D%0A1x_1+-+9x_2+%2B+1x_3+%2B+1x_4+%2B+0x_5+%3C%3D+0%0D%0A25x_1+%2B+25x_2+-+75x_3+-+75x_4+%2B+0x_5+%3C%3D+0%0D%0A50x_1+%2B+70x_2+%2B+130x_3+%2B+160x_4+%2B+2x_5+%3C%3D+15000%0D%0Ax_1+%3E%3D+0%2C+x_2+%3E%3D+0%2C+x_3+%3E%3D+0%2C+x_4+%3E%3D+0%2C+x_5+%3E%3D+0&m=m
Optimal Solution:
```
![image](https://github.com/user-attachments/assets/ee99876e-c0c9-4c3c-9c67-1878154ba213)


### Important Links
- [Case Studies](https://neos-guide.org/case-studies/)
- [Google OR Tools CPP Example](https://developers.google.com/optimization/lp/lp_example#c++)

# SciPy

>Scipy is a python library used for scientific computation.

>SciPy provides algorithms for optimization, integration, interpolation, eigenvalue problems, algebraic equations, differential equations, statistics and many other classes of problems.

>Extends NumPy providing additional tools for array computing and provides specialized data structures, such as sparse matrices and k-dimensional trees.

>SciPy is a collection of mathematical algorithms and convenience functions built on NumPy . It adds significant power to Python by providing the user with high-level commands and classes for manipulating and visualizing data.


# Constants module
>This module provides scientific constants

```
from scipy import constants
print(constants.pi)
print(constants.liter)
```

# Optimizers

>Optimizers are the set of procedures defined in SciPy that eithers provides the minimum value of a function or the roots of an equation

>Essentially, all of the algorithms in Machine Learning are nothing more than a complex equation that needs to be minimized with the help of given data.


## Defining a function
```
def func(x):
	return x**2 + x + 2
```

## Finding the root of a function
```
from scipy.optimize import root
myroot = root(eqn, 0) # 0-> initial guess of the solution
```

## Finding minima of a function

```
from scipy.optimize import minimize
mymin = minimize(eqn, 0, method='BGFS')
print(mymin.x)
```

# Sparse Data

>Sparse data is data that has mostly unused elements (elements that don't carry any information ).

>Sparse Data: is a data set where most of the item values are zero.

>Dense Array: is the opposite of a sparse array: most of the values are not zero.



**There are two types of sparce matrices that we use**

>CSC - Compressed Sparse Column. For efficient arithmetic, fast column slicing.

>CSR - Compressed Sparse Row. For fast row slicing, faster matrix vector products


## Some important operations on sparse data

```
import numpy as np
from scipy.sparse import csr_matrix
arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])
print(csr_matrix(arr).data) # getting non-zero elements
print(csr_matrix(arr).count_nonzero()) # counting non-zero elements
print(csr_matrix(arr).eliminate_zeros()) # eliminate zero entires
```

# Graphs

>Graphs are an important data structures

>from scipy.sparse.csgraph import connected_components

## Some Important Methods


>An adjacency matrix is a square matrix representing connections between vertices, where the presence of an edge between two vertices is denoted by a non-zero value in the corresponding matrix cell.

>Find all of the connected components with the connected_components() method.

>Use the dijkstra method to find the shortest path in a graph from one element to another.

>Use the floyd_warshall() method to find shortest path between all pairs of elements.


>The bellman_ford() method can also find the shortest path between all pairs of elements, but this method can handle negative weights as well.


>The depth_first_order() method returns a depth first traversal from a node.


>The breadth_first_order() method returns a breadth first traversal from a node.


**Will come back to this later**



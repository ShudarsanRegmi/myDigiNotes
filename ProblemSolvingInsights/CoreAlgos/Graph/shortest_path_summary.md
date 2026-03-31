**Better way to ask your question:**
"Can you clearly revise the three shortest path algorithms: Dijkstra, Bellman–Ford, and Floyd–Warshall, with their use-cases, differences, and complexities?"

---

## :sd Overview (quick mental map)

These three algorithms solve *shortest path problems*, but each operates in a different **computational regime**:

| Algorithm      | Type                | Handles Negative Weights? | Scope         |
| -------------- | ------------------- | ------------------------- | ------------- |
| Dijkstra       | Greedy              | No                        | Single source |
| Bellman-Ford   | Dynamic Programming | Yes                       | Single source |
| Floyd-Warshall | Dynamic Programming | Yes                       | All pairs     |

---

## 1. Dijkstra’s Algorithm

![Image](https://graphicmaths.com/img/computer-science/graph-theory/dijkstras-algorithm/algorithm-4.png)

![Image](https://www.researchgate.net/publication/382193848/figure/fig4/AS%3A11431281260077625%401720804178334/Dijkstra-algorithm-visualization-Weights-of-edges-are-written-on-them-Numbers-on.jpg)

![Image](https://graphicmaths.com/img/computer-science/graph-theory/dijkstras-algorithm/graph.png)

![Image](https://www.researchgate.net/publication/339209665/figure/fig2/AS%3A857764985327616%401581518517380/a-Weighted-Directed-Graph-b-Shortest-Path-to-vertices-B-C-from-A-c-Shortest-Path.png)

### :sd Core Idea

A **greedy** approach: always pick the node with the *currently smallest tentative distance* and expand from there.

### :ol Key Properties

* Uses **priority queue (min-heap)**
* Assumes **non-negative edge weights**
* Builds shortest path incrementally

### :oll Complexity

* `O((V + E) log V)` with heap
* Very efficient for sparse graphs

### :ol When to use

* Road networks
* Network routing
* Any graph with **non-negative weights**

---

## 2. Bellman–Ford Algorithm

![Image](https://files.codingninjas.in/article_images/bellman-ford-algorithm-3-1673202271.webp)

![Image](https://deen3evddmddt.cloudfront.net/uploads/content-images/bellman-ford-algorithm.webp)

![Image](https://images.downey.io/bellman-ford/bellman-ford-table.png)

![Image](https://www.simplilearn.com/ice9/free_resources_article_thumb/Bellman%20Ford%20Algorithm/what-is-bellman-ford-algorithm.png)

### :sd Core Idea

Repeatedly **relax all edges**. It doesn’t trust greedy assumptions, instead it systematically improves distances.

### :ol Key Properties

* Works with **negative weights**
* Can **detect negative cycles**
* Slower but more **robust**

### :oll Complexity

* `O(V * E)`

### :ol When to use

* Graphs with negative weights
* Detecting **negative cycles**
* Financial arbitrage problems

---

## 3. Floyd–Warshall Algorithm

![Image](https://deen3evddmddt.cloudfront.net/uploads/content-images/floyd-warshall-algorithm.webp)

![Image](https://files.codingninjas.in/article_images/custom-upload-1688378476-78c26c6f.webp)

![Image](https://miro.medium.com/v2/resize%3Afit%3A1400/0%2AHU7U2POPHuRlDk6r.jpg)

![Image](https://web.mit.edu/urban_or_book/www/book/chapter6/images6/form2a.gif)

### :sd Core Idea

Dynamic programming over **all pairs**.
It tries all possible intermediate nodes:

> "Is path i → k → j shorter than i → j?"

### :ol Key Properties

* Computes **all-pairs shortest path**
* Works with negative weights (but no negative cycles)
* Uses **adjacency matrix**

### :oll Complexity

* `O(V³)`

### :ol When to use

* Dense graphs
* When you need **distance between every pair**

---

## :sd Sharp Comparison (intuition builder)

Think of it like *levels of brute force vs intelligence*:

* **Dijkstra** → smart + fast, but *fragile* (breaks with negative weights)
* **Bellman-Ford** → slower but *resilient*
* **Floyd-Warshall** → brute-force DP over all pairs, *complete coverage*

---

## :sd Memory Trick (easy recall)

* **Dijkstra** → *“Don’t allow negatives”*
* **Bellman-Ford** → *“Brute relax everything”*
* **Floyd-Warshall** → *“Try every intermediate”*

---

## :sd Subtle Insight (important for interviews)

A nuanced distinction many miss:

* Dijkstra fails not because of negative weights alone
* It fails because **greedy choice becomes invalid when a future negative edge can reduce a previously finalized path**

This is a conceptual pitfall worth internalizing.


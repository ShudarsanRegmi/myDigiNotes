# DFS in Graph


```cpp
#include <iostream>
#include <list>

using namespace std;


class Graph {
    int numVertices;
    list<int> *adjLists;
    bool *visited;

public:
    Graph(int V);
    void addEdge(int src, int dest);
    void DFS(int vertex);
};

// Initialize a Graph
Graph::Graph(int vertices) {
    numVertices = vertices;
    adjLists = new list<int>[vertices];
    visited = new bool[vertices];
}

// Add edges
void Graph::addEdge(int src, int dest) {
    adjLists[src].push_front(dest);
}

// DFS Algorithm
void Graph::DFS(int vertex) {
    visited[vertex] = true;
    list<int> adjList = adjLists[vertex];
    cout << vertex << " " << endl;

    list<int>::iterator i;
    for (i = adjList.begin(); i!=adjList.end(); i++) {
        if (!visited[*i])
            DFS(*i);
    }

}



int main() {
    Graph g(4);
    g.addEdge(0,1);
    g.addEdge(0,2);
    g.addEdge(1,2);
    g.addEdge(2,3);

    g.DFS(2);
    return 0;
}
```

## Simple DFS

```cpp
#include <iostream>
#include <vector>
using namespace std;

// Function to perform DFS and print all vertices
void dfs(vector<vector<bool>> &Graph, int src, vector<bool> &visited) {
    visited[src] = true;
    cout << src << " "; // Print the current vertex

    for (int i = 0; i < Graph.size(); i++) {
        if (Graph[src][i] && !visited[i]) {
            dfs(Graph, i, visited); // Recursive call for unvisited neighbors
        }
    }
}

int main() {
    int n = 4; // Number of vertices
    vector<vector<int>> edges = {{2, 1}, {2, 3}, {2, 0}, {0, 3}};
    vector<vector<bool>> Graph(n, vector<bool>(n, false));

    // Create an adjacency matrix
    for (const auto &edge : edges) {
        int src = edge[0], dst = edge[1];
        Graph[src][dst] = true;
        Graph[dst][src] = true;
    }

    vector<bool> visited(n, false);

    cout << "DFS Traversal starting from vertex 0:" << endl;
    dfs(Graph, 0, visited); // Perform DFS starting from vertex 0

    return 0;
}

```

## GFG submission
```cpp
class Solution {
  public:
  
    void dfs(int curr, vector<bool> &visited, vector<int> &ans, vector<vector<int>> &adj) {
        // traverse its adjacency
        visited[curr] = true;
        ans.push_back(curr);
        for (int i : adj[curr]) {
            if(!visited[i]) {
                // visit it and mark as visisted
               
                dfs(i, visited, ans, adj);
            }
        }
    }
    // Function to return a list containing the DFS traversal of the graph.
    vector<int> dfsOfGraph(vector<vector<int>>& adj) {
        vector<bool> visited(adj.size(), false);
        vector<int> ans;
        dfs(0, visited, ans, adj);
        return ans;
        
    }
};
// had to fix minor error with the help of chatgpt. I had kept first two lines inside the loop
// done for final lab examp preperation
```

# BFS

```cpp
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

// Function to perform BFS and print all vertices
void bfs(vector<vector<bool>> &Graph, int start) {
    int n = Graph.size();
    vector<bool> visited(n, false);
    queue<int> q;

    visited[start] = true;
    q.push(start);

    while (!q.empty()) {
        int current = q.front();
        q.pop();
        cout << current << " "; // Print the current vertex

        for (int i = 0; i < n; i++) {
            if (Graph[current][i] && !visited[i]) {
                visited[i] = true;
                q.push(i);
            }
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

    cout << "BFS Traversal starting from vertex 0:" << endl;
    bfs(Graph, 0); // Perform BFS starting from vertex 0

    return 0;
}

```
## GFG Submission
```cpp
class Solution {
  public:
    // Function to return Breadth First Traversal of given graph.
    vector<int> bfsOfGraph(vector<vector<int>> &adj) {
        queue<int> Q;
        vector<bool> visited(adj.size(), false);
        vector<int> ans;
        Q.push(0);
        visited[0] = true;
        int t;
        while(!Q.empty()) {
            // traverse teh adj. of front element
            t = Q.front();
            for (int i : adj[t]) {
                // push the unvisited neighbors 
                if(!visited[i]) {
                    Q.push(i);
                    visited[i] = true;
                }
            }
            ans.push_back(t);
            Q.pop();
        }
        return ans;
    }
};
// could solve without external help. done for dsa lab exam prep. 
```


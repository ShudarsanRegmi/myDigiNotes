# Graph codes that should be at my fingertip always


## Graph DFS
```cpp
class Solution {
  public:
    void helper(int curr, vector<int> &ans, vector<vector<int>>& adj, vector<bool> &visited) {
        visited[curr] = true;
        ans.push_back(curr);
        
        
        // traverse adjacency and call dfs
        for (int neigh : adj[curr]) {
            if(!visited[neigh]) {
                helper(neigh, ans, adj, visited);
            }
        }
    }
    vector<int> dfs(vector<vector<int>>& adj) {
        vector<int> ans;
        vector<bool> visited(adj.size(), false);
        helper(0, ans, adj, visited);
        return ans;
    }
};
```

## Graph BFS
```cpp
class Solution {
  public:
    vector<int> bfs(vector<vector<int>> &adj) {
        int V = adj.size();
        vector<bool> visited(V, false);
        queue<int> Q;
        Q.push(0);
        visited[0] = true;
        vector<int> ans;
        
        while (!Q.empty()) {
            int t = Q.front();
            Q.pop();
            
            ans.push_back(t);
            
            // traverse it's adjacencies
            for (int neigh : adj[t]) {
                if(!visited[neigh]) {
                    Q.push(neigh);
                    visited[neigh] = true;   
                }
            }
        }
        
        return ans;
    }
};
```

## Topological Sort
```cpp

```

## Dijkistra Algorithm
**Naive**
```cpp

```

**Optimized Approach**
```cpp

```

## FLoyd Warshell Algorithm

```cpp
// User function template for C++

class Solution {
  public:
    void floydWarshall(vector<vector<int>> &dist) {
        int V = dist.size();
        
        for (int k=0; k<V; k++) {
            // one iteraiton = one coplete traversal of matrix
            for (int i=0; i<V; i++) {
                for (int j=0; j<V; j++) {
                    if(dist[i][k] < 1e8 && dist[k][j] < 1e8) {
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
                    }
                }
            }
        }
    }
};
```



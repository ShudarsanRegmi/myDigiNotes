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




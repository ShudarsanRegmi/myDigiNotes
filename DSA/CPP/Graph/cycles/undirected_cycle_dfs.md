<img width="1224" height="1285" alt="image" src="https://github.com/user-attachments/assets/d9987129-d27a-4060-a698-8a3d1af6d424" />



```cpp
class Solution {
  public:
  
    bool dfs(int i, vector<vector<int>> &adj, vector<bool> &visited, vector<int> &parent) {
        visited[i] = true;
        
        for (int nei : adj[i]) {
            if(visited[nei] && parent[i] != nei) {
                return true;
            }
            if(!visited[nei]) {
                parent[nei] = i;
                // return false || dfs(nei, adj, visited, parent);
                // the problem with above is, if false comes than also it has to return
                // BUt the idea here is return when true is there. 
                // But if false, has to serach further. 
                
                if(dfs(nei, adj, visited, parent)) {
                    return true;
                }
            }
        }
        
        return false;
    }
    bool isCycle(int V, vector<vector<int>>& edges) {
        vector<vector<int>> adj(V);
        
        for (auto &edge: edges) {
            int u = edge[0];
            int v = edge[1];
            
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
        
        vector<bool> visited(V, false);
        vector<int> parent(V, -1);
        
        
        for(int i=0; i<V; i++) {
            if(!visited[i]) {
                if(dfs(i, adj, visited, parent)) {
                    return true;
                }
            }
        }
        
        return false;
    }
};
```

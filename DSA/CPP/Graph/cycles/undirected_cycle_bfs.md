<img width="1224" height="1285" alt="image" src="https://github.com/user-attachments/assets/d42d78e9-67ad-40d9-85ee-8ba7713a9ffa" />



```cpp
class Solution {
  public:
    bool isCycle(int V, vector<vector<int>>& edges) {
        vector<vector<int>> adj(V);
        
        for (auto edge : edges) {
            int u = edge[0];
            int v = edge[1];
            if(u==v) return true; 
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
        
        vector<bool> visited(V, false);
        
        vector<int> parent(V, -1);
        
        for(int i=0; i<V; i++) {
            queue<int> Q;
            
            if(visited[i]) continue;
            
            Q.push(i);
            visited[i] = true;
            
            
            while(!Q.empty()) {
                int t = Q.front();
                Q.pop();
                
                // traverse its adjacency
                for (int nei : adj[t]) {
                    if(visited[nei]) {
                        if(parent[t] != nei) return true;
                    }else{
                        Q.push(nei);
                        visited[nei] = true;
                        parent[nei] = t;
                    }
                    
                }
            }
        }
        return false;
    }
};
```

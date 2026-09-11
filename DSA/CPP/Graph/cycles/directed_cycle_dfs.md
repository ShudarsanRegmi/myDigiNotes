<img width="1312" height="1199" alt="image" src="https://github.com/user-attachments/assets/f6caa559-6f20-4bcc-b74a-04b027fb37b2" />



```cpp
class Solution {
  public:
    bool dfs(vector<vector<int>> &adj, vector<int> &visit, int curr) {
        visit[curr] = 1; // curr is in stack
        
        for(int nei : adj[curr]) {
            if(visit[nei] == 1) { // already in stack, so cycle
                return true;   
            }else{
                if(visit[nei] == 0) { // unvisited
                    if(dfs(adj, visit, nei)) {
                        return true;
                    }
                }
            }
            
        }
        
        visit[curr] = 2;
        return false;
    }
    
    bool isCyclic(int V, vector<vector<int>> &edges) {
        stack<int> st;
        vector<int> visit(V, 0); // 0 indicates visited
        vector<vector<int>> adj(V);
        
        for(auto edge : edges) {
            int u = edge[0];
            int v = edge[1];
            
            adj[u].push_back(v);
        }
        

        for (int i=0; i<V; i++) {
            if(visit[i] == 0) {
                if(dfs(adj, visit, i)) {
                    return true;
                }
            }
        }
        
        return false;
        
        
    }
};
```

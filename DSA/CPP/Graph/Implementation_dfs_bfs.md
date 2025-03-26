# Graph Implementation DFS and BFS


```cpp
#include <iostream>
#include <vector>

using namespace std;

class Graph {
public:
    int numVertices;
    vector<vector<int>> adjList;
    Graph(int numVertices) : numVertices(numVertices) {
        adjList.resize(numVertices);
    }

    void addEdge(int s, int d) {
        adjList[s].push_back(d);
        adjList[d].push_back(s);
    }


    void dfs(int curr, vector<bool> &visited) {
        cout << curr << " ";
        visited[curr] = true;

        // traverse its adjacency
        for (int i : adjList[curr]) {
            if (!visited[i]) {
                dfs(curr, visited);
            }
        }
    }
    void traversedfs() {
        vector<bool> visited(numVertices, false);
        dfs(0, visited);
    }
};

int main() {
    Graph g(5);
    g.addEdge(0,1);
    g.addEdge(0,2);
    g.addEdge(0,4);
    g.addEdge(1,3);

    g.traversedfs();
}
```

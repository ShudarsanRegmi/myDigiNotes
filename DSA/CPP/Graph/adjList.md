# Adjacency List

```cpp
#include <iostream>
#include <vector>

using namespace std;

void addEdge(vector<int> adj[], int s, int d) {
    adj[s].push_back(d);
    adj[d].push_back(s);
}

void printGraph(vector<int> adj[], int V) {
    for (int d=0; d<V; d++) {
        cout << "\n Vertex " << d << ":";
        for (auto x : adj[d])
            cout << "-> " << x;
        cout << endl;
    }
}

int main() {
    int V=5;

    vector<int> adj[V]; // array of vectors
    addEdge(adj, 0, 1);
    addEdge(adj, 0, 2);
    addEdge(adj, 0, 3);
    addEdge(adj, 1, 2);
    printGraph(adj, V);

    return 0;
}
```

# Dijkistra Algorithm

### To find the shortest path to all nodes from a source node

#### Techdose Code
```cpp
#include <iostream>
#include <vector>
#include<climits>

using namespace std;

#define V 6

int selectMinVertex(vector<int>& value, vector<bool>& processed) {
    int minimum = INT_MAX;
    int vertex;
    for (int i=0; i<V; i++) {
        if (processed[i] == false && value[i] < minimum) {
            vertex = i;
            minimum = value[i];
        }
    }
    return vertex;
}


void dijkistra(int graph[V][V]) {
    int parent[V]; // stores shortest path structure
    vector<int> value (V, INT_MAX);
    vector<bool> processed(V, false);

    // Assuming Starting point as node - 0
    parent[0] = -1;
    value[0] = 0;

    // Include V-1 edges to cover all the vertices
    for (int i=0; i<V-1; i++) {
        // Select the vertex by applying greedy method
        int U = selectMinVertex(value, processed);
        processed[U] = true;

        // Relax adjacent vertices
        for (int j=0; j<V; j++) {
         // 3 conditions to realx
         // 1. Edge is present from U to V
         // 2. Vertex j is not included in the shortest path graph
         // 3. Edge weight is smaller than current edge weight
            if (graph[U][j] != 0 && processed[j] == false && value[U] != INT_MAX && value[U]+graph[U][j] < value[j]) {
                value[j] = value[U]+graph[U][j];
                parent[j] = U;
            }
        }
    }
    // Print the shortest path graph
    for (int i=1; i<V; i++) {
        cout<<"U->V: "<<parent[i]<<"->"<<i<<"  wt = "<<graph[parent[i]][i]<<"\n";
    }

}

int main() {
    // Graph Representation Using Adjacency Matrix
    int graph[V][V] = { {0, 1, 4, 0, 0, 0},
                        {1, 0, 4, 2, 7, 0},
                        {4, 4, 0, 3, 5, 0},
                        {0, 2, 3, 0, 4, 6},
                        {0, 7, 5, 4, 0, 7},
                        {0, 0, 0, 6, 7, 0} };
    dijkistra(graph);
    return 0;
}
```

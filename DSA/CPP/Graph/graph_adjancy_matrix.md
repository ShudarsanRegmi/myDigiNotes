# Graph Representation Using Adjacency Matrix


```cpp
#include <iostream>

using namespace std;

/*

 [&abcd, &1234, &1242] <-- Array of pointers
 &abcd : [false/true] <-- These address stores boolean values
 we need a pointer which points to the starting address of the above array of pointers
 that pointer is stored by the variable adjMatrix
 *adjMatrix decays to starting address of array
*/

class Graph {
private:
    bool **adjMatrix;
    int numVertices;
public:
    Graph(int numVertices) {
        this->numVertices = numVertices;
        adjMatrix = new bool*[numVertices]; // creates an array of bool*
        for (int i=0; i<numVertices;i++) {
            adjMatrix[i] = new bool[numVertices];
            for (int j=0; j<numVertices; j++) {
                adjMatrix[i][j] = false;
            }
        }
     }
    void addEdge(int i, int j) {
        adjMatrix[i][j] = true;
        adjMatrix[i][j] = true;
    }

    void removeEdge(int i, int j) {
        adjMatrix[i][j] = false;
        adjMatrix[i][j] = false;
    }

    // print the matrix
    void toString() {
        for (int i=0; i<numVertices; i++) {
            cout << i << " : ";
            for (int j=0; j<numVertices; j++)
                cout << adjMatrix[i][j] << " ";
            cout << "\n";
        }
    }
};

int main () {
    Graph g(4);
    g.addEdge(0,1);
    g.addEdge(0,2);
    g.addEdge(1,2);
    g.addEdge(2,0);
    g.addEdge(2,3);

    g.toString();
}

```

# Graph Representaton Using Adjancy List


![image](https://github.com/user-attachments/assets/c4d24436-d173-4369-a22a-d9f9c3393d37)


```c
#include <stdio.h>
#include <stdlib.h>

typedef struct node {
    int vertex;
    struct node *next;
} Node;

Node *createNode(int);

typedef struct Graph {
    int numVertices;
    Node **adjLists;
} Graph;

// create a node

Node *createNode(int v) {
    Node *newNode = (Node *)malloc(sizeof(Node));
    newNode->vertex = v;
    newNode->next = NULL;
    return newNode;
}


// create a graph
Graph *createAGraph(int vertices) {
    Graph *graph = (Graph *)malloc(sizeof(Graph));
    graph->numVertices = vertices;
    graph->adjLists = malloc(vertices * sizeof(Node *));

    int i;
    for (i = 0; i < vertices; i++)
        graph->adjLists[i] = NULL;

    return graph;

}

void addEdge(Graph *graph, int s, int d) {
    // ADd edge from s to d
    Node *newNode = createNode(d);
    newNode->next = graph->adjLists[s];
    graph->adjLists[s] = newNode;

    // Add hte edge from d to s
    newNode = createNode(s);
    newNode->next = graph->adjLists[d];
    graph->adjLists[d] = newNode;
}

void printGraph(Graph *graph) {
    int v;
    for (v = 0; v < graph->numVertices; v++) {
        Node *temp = graph->adjLists[v];
        printf("\n Vertex %d \n: ",v);

        while(temp) {
            printf("%d -> ", temp->vertex);
            temp = temp->next;
        }
        printf("\n");
    }
}

int main() {
    Graph *graph = createAGraph(4);
    addEdge(graph, 0, 1);
    addEdge(graph, 0, 2);
    addEdge(graph, 0, 3);
    addEdge(graph, 1, 2);

    printGraph(graph);

    return 0;

}
```

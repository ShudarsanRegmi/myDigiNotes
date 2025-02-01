# Union Find

### Basic Implementation of Union Find

```cpp
#include <iostream>
#include <vector>
using namespace std;

class UnionFind {
public:
    vector<int> parent;
    UnionFind(int size) {
        parent.resize(size);
        for (int i=0; i<size; i++) {
            parent[i] = i;
        }
    }

    int find(int i) {
        if (parent[i] == i) return i;
        return find(parent[i]);
    }

    void unite(int i, int j) {
        int irep = find(i);
        int jrep = find(j);

        parent[irep] = jrep;
    }


};

int main() {
    UnionFind uf(5);
    uf.unite(1,2);
    uf.unite(3,4);
    cout << "Parent of 1: " << uf.find(1) << endl;
    cout << "Parent of 2: " << uf.find(2) << endl;
    uf.unite(2,3);
    cout << "Parent of 1: " << uf.find(1) << endl;
    return 0;
}
```


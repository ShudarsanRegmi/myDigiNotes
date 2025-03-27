# SkipList Implementation


```cpp
#include <iostream>
#include <vector>
#include <cstdlib>

using namespace std;

struct Node {
    Node *right, *down;
    int val;
    Node(Node *right, Node *down, int val) : right(right), down(down), val(val) {}
};

class Skiplist {
    Node* head;
    vector<Node*> insertPoints;
    
public:
    Skiplist() { head = new Node(NULL, NULL, 0); }
    
    bool search(int num) {
        Node *p = head;
        while (p) {
            while (p->right && p->right->val < num) p = p->right;
            if (!p->right || p->right->val > num) p = p->down;
            else return true;
        }
        return false;
    }
    
    void add(int num) {
        insertPoints.clear();
        Node *p = head;
        while (p) {
            while (p->right && p->right->val < num) p = p->right;
            insertPoints.push_back(p);
            p = p->down;
        }
        
        Node* downNode = NULL;
        bool insertUp = true;
        while (insertUp && !insertPoints.empty()) {
            Node *ins = insertPoints.back();
            insertPoints.pop_back();
            ins->right = new Node(ins->right, downNode, num);
            downNode = ins->right;
            insertUp = (rand() & 1) == 0;
        }
        if (insertUp) {
            head = new Node(new Node(NULL, downNode, num), head, 0);
        }
    }
    
    bool erase(int num) {
        Node *p = head;
        bool seen = false;
        while (p) {
            while (p->right && p->right->val < num) p = p->right;
            if (!p->right || p->right->val > num) p = p->down;
            else {
                seen = true;
                p->right = p->right->right;
                p = p->down;
            }
        }
        return seen;
    }
};

int main() {
    Skiplist skiplist;
    int choice, num;
    
    do {
        cout << "\nChoose an operation:" << endl;
        cout << "1. Add a number" << endl;
        cout << "2. Search for a number" << endl;
        cout << "3. Erase a number" << endl;
        cout << "4. Exit" << endl;
        cout << "Enter your choice: ";
        cin >> choice;
        
        switch (choice) {
            case 1:
                cout << "Enter number to add: ";
                cin >> num;
                skiplist.add(num);
                cout << num << " added to the skip list." << endl;
                break;
            case 2:
                cout << "Enter number to search: ";
                cin >> num;
                if (skiplist.search(num)) cout << num << " found in the skip list." << endl;
                else cout << num << " not found in the skip list." << endl;
                break;
            case 3:
                cout << "Enter number to erase: ";
                cin >> num;
                if (skiplist.erase(num)) cout << num << " removed from the skip list." << endl;
                else cout << num << " not found in the skip list." << endl;
                break;
            case 4:
                cout << "Exiting program." << endl;
                break;
            default:
                cout << "Invalid choice. Please try again." << endl;
        }
    } while (choice != 4);
    
    return 0;
}
```

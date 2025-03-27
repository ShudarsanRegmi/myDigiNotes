
```cpp
#include <iostream>
#include <list>
#include <vector>

using namespace std;

class HashTable {
private:
    static const int capacity = 20;
    vector<list<pair<int, int>>> table;

    // Hash function
    int hashFunction(int key) const {
        return key % capacity;
    }

public:
    HashTable() : table(capacity) {}

    // Insert a key-value pair into the hash table
    void insert(int key, int value) {
        int hashIndex = hashFunction(key);
        for (auto& pair : table[hashIndex]) {
            if (pair.first == key) {  // Update value if key already exists
                pair.second = value;
                return;
            }
        }
        table[hashIndex].emplace_back(key, value);
    }


    // Remove a key from the hash table
    bool remove(int key) {
        int hashIndex = hashFunction(key);
        auto& chain = table[hashIndex];

        for (auto it = chain.begin(); it != chain.end(); ++it) {
            if (it->first == key) {
                chain.erase(it);
                return true;
            }
        }
        return false;
    }

    // Search for a key and return its value
    int find(int key) const {
        int hashIndex = hashFunction(key);
        for (const auto& pair : table[hashIndex]) {
            if (pair.first == key) {
                return pair.second;
            }
        }
        return -1; // Key not found
    }

    // Display the contents of the hash table
    void display() const {
        for (int i = 0; i < capacity; ++i) {
            cout << "Bucket " << i << ": ";
            for (const auto& pair : table[i]) {
                cout << "[" << pair.first << " -> " << pair.second << "] ";
            }
            cout << "\n";
        }
    }
};

// Driver code
int main() {
    HashTable ht;

    ht.insert(1, 5);
    ht.insert(2, 15);
    ht.insert(3, 20);
    ht.insert(4, 7);
    ht.insert(21, 25);  // Collision with key 1 (21 % 20 == 1)

    cout << "Value of Key 4: "
         << (ht.find(4) != -1 ? to_string(ht.find(4)) : "Key does not exist")
         << endl;

    if (ht.remove(4))
        cout << "Key 4 deleted successfully.\n";
    else
        cout << "Key 4 does not exist.\n";

    cout << "Value of Key 4 after deletion: "
         << (ht.find(4) != -1 ? to_string(ht.find(4)) : "Key does not exist")
         << endl;

    cout << "\nHash Table Content:\n";
    ht.display();

    return 0;
}
Thursday 27 March 2025 06:13:59 AM IST 
```

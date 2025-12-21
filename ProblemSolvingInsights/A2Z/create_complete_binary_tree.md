
## My Initial Basic Version

```cpp
#include <bits/stdc++.h>
using namespace std;

/* -----------------------------
   Node definition (given)
----------------------------- */
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;

    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

TreeNode* buildCompleteBinaryTree(const vector<int>& values) {
    int i=0;
    TreeNode *root = new TreeNode(values[i++]);
    queue<TreeNode*> Q;
    Q.push(root);
    
    int n = values.size();
    
    
    while(!Q.empty() && i < n) {
        int s = Q.size();
        
        while(s--) {
            TreeNode *top = Q.front();
            Q.pop();
            
            TreeNode *lnode = new TreeNode(values[i++]);
            top->left = lnode;
            Q.push(lnode);
            
            if(i>=n) return root;
            
            
            TreeNode *rnode = new TreeNode(values[i++]);
            top->right = rnode;
            Q.push(rnode);
            
        }
    }
    
    return root;
}

/* -----------------------------
   Utility: Level-order traversal
   (for validation only)
----------------------------- */
void printLevelOrder(TreeNode* root) {
    if (!root) return;

    queue<TreeNode*> q;
    q.push(root);

    while (!q.empty()) {
        int sz = q.size();
        while (sz--) {
            TreeNode* node = q.front();
            q.pop();

            cout << node->val << " ";

            if (node->left)  q.push(node->left);
            if (node->right) q.push(node->right);
        }
        cout << "\n";
    }
}

/* -----------------------------
   Driver code
----------------------------- */
int main() {
    vector<int> values = {1, 2, 3, 4, 5, 6, 7, 8};

    TreeNode* root = buildCompleteBinaryTree(values);

    // sanity check
    cout << "Level order traversal" << endl;
    printLevelOrder(root);

    return 0;
}

```

## The most idiomatic way 

```cpp
TreeNode* buildCompleteBinaryTree(const vector<int>& values) {
    if (values.empty()) return nullptr;

    TreeNode* root = new TreeNode(values[0]);
    queue<TreeNode*> q;
    q.push(root);

    int i = 1;
    while (i < values.size()) {
        TreeNode* parent = q.front();
        q.pop();

        parent->left = new TreeNode(values[i++]);
        q.push(parent->left);

        if (i < values.size()) {
            parent->right = new TreeNode(values[i++]);
            q.push(parent->right);
        }
    }

    return root;
}

```

# Merge Two Trees

- return node2 if node1 is null and return node1 if node2 is null
- create a node called sumRoot
- node.left = mergeNode(root1.left, root2.left)
- node.right = mergeNode(root2.left, root2.right)
- return sumroot

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:

    TreeNode* mergeTrees(TreeNode* root1, TreeNode* root2) {
        if (root1 == nullptr && root2 == nullptr) {
            return nullptr;
        }

        if (root1 == nullptr) {
            return root2;
        }

        if (root2 == nullptr) {
            return root1;
        }

        TreeNode* sumRoot = new TreeNode(root1->val + root2->val);
        sumRoot->left = mergeTrees(root1->left, root2->left);
        sumRoot->right = mergeTrees(root1->right, root2->right);

        return sumRoot;
    }
};
```
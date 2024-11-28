# InOrder Traversal


```cpp
#include <iostream>
#include <vector>
using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    vector<int> vec; // Store the result of inorder traversal
    vector<int> inorderTraversal(TreeNode* root) {
        if (root != nullptr) {
            inorderTraversal(root->left);
            vec.push_back(root->val);
            inorderTraversal(root->right);
        }
        return vec;
    }
};

int main() {
    // Constructing the complete binary tree
    TreeNode* node4 = new TreeNode(4);
    TreeNode* node5 = new TreeNode(5);
    TreeNode* node6 = new TreeNode(6);
    TreeNode* node7 = new TreeNode(7);
    TreeNode* node2 = new TreeNode(2, node4, node5);
    TreeNode* node3 = new TreeNode(3, node6, node7);
    TreeNode* root = new TreeNode(1, node2, node3);

    // Create a Solution object and perform inorder traversal
    Solution sol;
    vector<int> result = sol.inorderTraversal(root);

    // Output the result
    cout << "Inorder Traversal: ";
    for (int val : result) {
        cout << val << " ";
    }
    cout << endl;

    // Clean up allocated memory
    delete node4;
    delete node5;
    delete node6;
    delete node7;
    delete node2;
    delete node3;
    delete root;

    return 0;
}

```

### If we rewrite the logic to check if `root` is `nullptr` instead of checking if `root` is not `nullptr`, the code can look like this:

### Modified Code
```cpp
vector<int> inorderTraversal(TreeNode* root) {
    if (root == nullptr) { 
        return vec; 
    }
    inorderTraversal(root->left);
    vec.push_back(root->val);
    inorderTraversal(root->right);
    return vec;
}
```

---

### Key Differences Between the Two Approaches

| **Aspect**           | **Check `root != nullptr`**              | **Check `root == nullptr`**                |
|-----------------------|------------------------------------------|--------------------------------------------|
| **Logic flow**        | Executes the body only when `root` exists. | Exits early when `root` is null, preventing further processing. |
| **Readability**       | Indicates processing occurs when there is a valid node. | Highlights early termination for null nodes. |
| **Conciseness**       | Slightly more verbose, as the body includes the main logic. | Simpler logic flow due to early return. |
| **Default state handling** | Naturally aligns with the idea of processing only when valid. | Puts a focus on handling invalid states early. |
| **Error handling**    | Slightly less explicit about null checks. | Explicitly handles null as the first step, reducing ambiguity. |

---

### Pros and Cons

#### **Checking `root != nullptr` (Original Code)**

- **Pros**:
  1. Logical flow is centered on **what to do** when there is a valid node.
  2. May feel more natural when thinking about recursive traversal.
  3. Aligns better with how most recursive tree algorithms are written, improving familiarity for readers.

- **Cons**:
  1. Can be slightly harder to trace the exit condition at a glance.
  2. Requires processing logic to reside in the main body of the function, potentially leading to deeper nesting in more complex cases.

---

#### **Checking `root == nullptr` (Modified Code)**

- **Pros**:
  1. Clearly separates the base case (when `root` is `nullptr`) from the recursive logic.
  2. Simplifies function logic for recursive algorithms, often making debugging easier.
  3. By handling null pointers upfront, you reduce the need for checking in subsequent steps.

- **Cons**:
  1. Focus on null checks first may feel counterintuitive when the intent is to process valid nodes.
  2. Early returns can complicate understanding if there are multiple exit conditions in more complex logic.

---

### Which Approach is Better?

- **Preference** often depends on the context and team conventions:
  - For **clarity and simplicity**, handling `root == nullptr` first (early exit) is often preferred in recursive algorithms.
  - For **consistency** with broader codebases or algorithms, checking `root != nullptr` is more aligned with typical recursion patterns.

In this specific case, both approaches work equally well. If the goal is to make the base case explicit, the second approach (`root == nullptr`) may be more readable.

## 

## Returning the Shared Memory : return vec

### Short summary

In the `inorderTraversal` function, the vector `vec` is a member of the `Solution` class, which means it is shared across all instances of the class. During the recursive traversal, each call operates on the same `vec` instance, modifying it directly. This shared state allows the function to accumulate the traversal results across all recursive depths without the need to pass `vec` as a parameter in each call.

However, since `vec` is shared across all calls, it's essential to clear it at the beginning of each traversal to prevent residual data from previous traversals. This can be done by invoking `vec.clear()` at the start of the `inorderTraversal` function.

Additionally, while this approach simplifies the function signature by eliminating the need to pass `vec` explicitly, it's important to be cautious of potential issues related to state persistence and thread safety when using class members in this manner. 

### Detailed Explanation

You're absolutely correct that the `vec` is a member of the `Solution` class, and all recursive calls in the `inorderTraversal` function share the same instance of `vec`. This is why all the recursive calls work with the same memory for `vec`.


### Detailed Breakdown of How `vec` Works in Recursion

1. **Shared Memory**:
   - `vec` is a member variable of the `Solution` class, meaning it is shared across all function calls of `inorderTraversal` for the same `Solution` object.
   - During recursion, when `vec.push_back(root->val)` is called, all recursive calls are appending values to the same `vec`.

2. **Stack Frames and Shared State**:
   - Each recursive call creates a **new stack frame**. This frame contains its local variables (e.g., the `root` pointer passed in that call).
   - However, `vec` is **not local to the function**. Instead, it resides in the `Solution` object, which all recursive calls reference.
   - This is why `vec` behaves like a global variable for all recursion levels — it doesn't get reallocated or overwritten during recursion.

3. **How `return vec` Works**:
   - The `return vec` at each recursion depth does not create a new vector or copy the `vec`. Instead, it just passes the reference to the same `vec` up the recursive call stack.
   - The recursive calls don’t rely on the return value of `vec` for appending or modifying it; instead, they modify it directly by calling `vec.push_back`.

4. **Example Execution**:
   - Consider this tree:
     ```
         1
        / \
       2   3
     ```
   - The execution flow would look like this:

     | Function Call Stack | Action                        | `vec` State         |
     |---------------------|-------------------------------|---------------------|
     | `inorderTraversal(1)` | Calls `inorderTraversal(2)`   | `[]`                |
     | `inorderTraversal(2)` | Calls `inorderTraversal(nullptr)` | `[]`                |
     | Base case (`nullptr`) | Returns `vec` unchanged       | `[]`                |
     | Back to `inorderTraversal(2)` | Pushes `2` to `vec`           | `[2]`              |
     | Back to `inorderTraversal(1)` | Pushes `1` to `vec`           | `[2, 1]`           |
     | Calls `inorderTraversal(3)`   | Pushes `3` to `vec`           | `[2, 1, 3]`        |

   - Notice how `vec` is modified in-place as the recursion progresses.

---

### Why Use a Class Member for `vec`?

1. **Avoid Passing State Around**:
   - Without `vec` as a class member, you'd have to pass a `vector<int>&` parameter to every recursive call to maintain the state.

   ```cpp
   void inorderTraversal(TreeNode* root, vector<int>& vec) {
       if (root == nullptr) return;
       inorderTraversal(root->left, vec);
       vec.push_back(root->val);
       inorderTraversal(root->right, vec);
   }
   ```

   This works just as well, but using a class member eliminates the need to pass the vector explicitly.

2. **Cleaner Interface**:
   - By keeping `vec` in the class, the `inorderTraversal` function is easier to use since the caller doesn't need to initialize or manage the vector.

---

### Potential Pitfall of Using `vec` as a Class Member

1. **State Persistence**:
   - Since `vec` is shared across multiple calls to `inorderTraversal`, it must be cleared before starting a new traversal. Otherwise, it will contain values from previous traversals.
   - To avoid this issue, always clear `vec` at the start:

     ```cpp
     vector<int> inorderTraversal(TreeNode* root) {
         vec.clear();  // Ensure vec is empty for each new traversal
         if (root == nullptr) return vec;
         inorderTraversal(root->left);
         vec.push_back(root->val);
         inorderTraversal(root->right);
         return vec;
     }
     ```

2. **Thread Safety**:
   - If the `Solution` class is used in a multi-threaded environment, the shared state (`vec`) can lead to race conditions.

---

### Insight Summary
- **`vec` in recursion works because it's shared memory** within the `Solution` object.
- Each recursive depth modifies the same vector directly, making changes visible across all stack frames.
- Returning `vec` in each recursion depth is just passing the reference upwards, not creating a new copy.
- This approach avoids the need to pass `vec` explicitly as a parameter but requires careful handling to reset its state before new traversals.

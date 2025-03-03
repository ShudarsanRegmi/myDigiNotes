### **Advanced Case Study: Exploring Git's Merkle Tree Structure**  

This case study will guide you through **visualizing** the Merkle tree structure in Git, **observing changes**, and **experimenting with operations** that modify the tree.  

---

## **🌲 Step 1: Create a Git Repository and Add Files**  
```bash
mkdir git-merkle-exploration && cd git-merkle-exploration
git init
```
Now, create some files and directories:  
```bash
mkdir dir1
echo "File A contents" > fileA.txt
echo "File B contents" > dir1/fileB.txt
git add .
git commit -m "Initial commit with multiple files"
```
---

## **🌿 Step 2: Visualizing the Merkle Tree Structure**  
### **1️⃣ Show the Commit Tree**  
Find the latest commit hash:  
```bash
git log --pretty=format:'%h %s'
```
Get the **tree hash** associated with the commit:  
```bash
git cat-file -p <commit-hash>
```
Output:
```
tree <tree-hash>
author Your Name <email@example.com> 1709539200 +0530
committer Your Name <email@example.com> 1709539200 +0530

Initial commit
```
### **2️⃣ Show the Tree Object**  
```bash
git cat-file -p <tree-hash>
```
Example output:
```
100644 blob abc123 fileA.txt
040000 tree def456 dir1
```
This shows:
- `blob abc123 fileA.txt` → A file stored as a **blob**.
- `tree def456 dir1` → A **subdirectory** with its own tree hash.

Now, inspect the subdirectory tree:  
```bash
git cat-file -p def456
```
Output:
```
100644 blob xyz789 fileB.txt
```
This means:
- `fileB.txt` is stored as a **blob** under `dir1`, maintaining a hierarchical **Merkle tree structure**.

---

## **🔄 Step 3: Modify Files and Observe Tree Changes**  
Modify `fileA.txt` and `fileB.txt`:  
```bash
echo "Updated File A" > fileA.txt
echo "Updated File B" > dir1/fileB.txt
git add .
git commit -m "Updated files"
```
### **Compare Tree Changes**  
Find the new commit tree:  
```bash
git cat-file -p <new-commit-hash>
```
Observe how:
- The **tree hash** for the root has changed.
- The **tree hash** for `dir1` has changed.
- New **blob hashes** were generated for modified files.

Run:  
```bash
git diff --name-only HEAD~1 HEAD
```
This confirms which files changed.

---

## **🌳 Step 4: Explore More Git Operations and Their Impact on the Merkle Tree**
### **1️⃣ Add a New File and Observe Changes**
```bash
echo "New File C" > dir1/fileC.txt
git add .
git commit -m "Added fileC.txt"
```
Check the new tree structure:  
```bash
git cat-file -p HEAD^{tree}
```

### **2️⃣ Remove a File and Observe Tree Changes**
```bash
git rm fileA.txt
git commit -m "Removed fileA.txt"
```
Now, inspect the tree again. You'll see `fileA.txt` is no longer listed.

### **3️⃣ Create a Branch and Observe Tree Differences**
```bash
git checkout -b new-branch
echo "Branch-specific changes" > branchFile.txt
git add .
git commit -m "Added branchFile.txt"
```
Compare trees between branches:
```bash
git diff --name-status main new-branch
```

### **4️⃣ Merge and Observe How Trees Combine**
```bash
git checkout main
git merge new-branch
```
Run:  
```bash
git log --graph --pretty=format:'%h - %s' --abbrev-commit
```
This will show a **branching Merkle tree** in action.

---

## **🔍 Summary of Findings**
- Git **constructs a Merkle tree** where **commits reference tree objects**, which reference **blobs and subtrees**.
- **Modifications** create **new blob hashes**, affecting parent trees.
- **Deleting files** removes them from the **tree** but preserves history.
- **Branching and merging** can be observed via tree comparisons.


---

![image](https://github.com/user-attachments/assets/b60b8d89-c5ca-414d-8be4-eebb95c8168e)

![image](https://github.com/user-attachments/assets/19825d72-e07d-45ac-97cf-6e8bd71f99e0)

![image](https://github.com/user-attachments/assets/1f42130d-46fc-402c-8952-3837dca14bc9)

![image](https://github.com/user-attachments/assets/83623d06-a8a6-4dfa-8e99-828974854245)

![image](https://github.com/user-attachments/assets/652d9e2f-8a3d-4b28-8118-f64cfaea1481)

![image](https://github.com/user-attachments/assets/14b9a4d2-5af6-4454-8dde-df694ae1e99a)




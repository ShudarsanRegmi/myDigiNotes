# Getting Good At Git



## Collaborative Git

### Fetching a branch

```
git fetch 
```

Fetches all the branch in remote repository that your local branch is tracking. 

> Remote tracking branches in Git are references to the state of branches on a remote repository. When you clone a repository, Git sets up these remote tracking branches to keep track of the branches on the remote repository.

## Comparing the changes

```
git diff feature-branch..origin/feature-branch
```

Compare the local feature-branch with origin/feature-branch

```
git diff main..origin/main
```

This command compares the local main with origin/main



> After fetching we can either merge or rebase



## Merging

```
git merge <target>
git merge origin/main
```

Merges the fetched branch with the local



## Pulling

 `git pull` fetches changes for all branches from the remote but merges only the changes for the current branch into your local branch. It doesn't automatically merge changes from all branches into your current branch; it focuses on the branch you're currently working on or the tracked branch if specified.

```
git pull origin/main
```

Fetches and merges origin/main with local branch from which this command is executed. 

```
git pull 
```

### Which branch your local branch is tracking to ?

```
git branch -vv
```

### Changing the remote tracking branch for a local branch

```
git branch --set-upstream-to=origin/remote-feature-branch your-local-branch
```
### Edit last commit message (before any change has been made)
```bash
git commit --amend
```
### Changing all global configurations
```bash
git config --global --edit
```

## Viewing PR locally

```bash
git fetch origin pull/$ID/head:$BRANCHNAME
```
where $ID is the pull request id and $BRANCHNAME is the name of the new branch that you want to create. Once you have created the branch, then simply

```bash
git checkout $BRANCHNAME
```

```bash
# Example
git fetch origin pull/2/head:pr-x 
```

### Going back to main after working in feature branch without commiting in feature branch

```bash
git stash
git checkout main
```

### Going back and continuing in the feature branch
```bash
git stash apply
```

### Handling above scenario with WIP commits

```bash
# in feature-branch
git add <file1> <file2>
git commit -m "WIP: Work title"
git checkout main
git checkout feature-branch
# made some changes
git add <files>
git commit -m "WIP2: Work title"
# Creating file commit  message
git rebase -i HEAD~number_of_commits
```

### Unstage all tracked files before commit

```bash
git reset .
```

>Note: don't add relative path in .ignore. [This stmt is incomplete]

### Renaming a branch from master to main

```bash
# first checkout to master branch if you haven't already
git checkout master
git branch -m main
```

### Listing all fetches
```bash
git fetch
```

### When you've sth in git and also sth initiated separately in local 
```bash
git merge main --allow-unrelated-histories
```

### Testing a Flask APP
```bash
FLASK_APP=app.py FLASK_ENV=development flask run --host=0.0.0.0 --port=5001
```

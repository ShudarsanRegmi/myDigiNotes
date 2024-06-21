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


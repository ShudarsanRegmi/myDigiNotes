**Rephrased question:**

> *I want to switch to SSH-based authentication for GitHub and use different GitHub accounts for different projects. Can you teach me the complete setup, including SSH keys, SSH configuration, GitHub account configuration, and per-repository Git identity (`user.name` and `user.email`)?*

This is exactly the setup I recommend. Once configured, you won't have to paste PATs or repeatedly authenticate. Let's build it from scratch.

---

# The final architecture

Suppose you have:

| Purpose              | GitHub Account       |
| -------------------- | -------------------- |
| Personal projects    | `personal@gmail.com` |
| College/Organization | `college@gmail.com`  |

We'll create:

```
~/.ssh/

id_ed25519_personal
id_ed25519_personal.pub

id_ed25519_college
id_ed25519_college.pub

config
```

Then:

```
Personal Repo
      │
      ▼
github-personal
      │
SSH Key A
      │
GitHub Personal Account


College Repo
      │
      ▼
github-college
      │
SSH Key B
      │
GitHub College Account
```

Notice something important:

**The repository chooses which GitHub account to use.**

---

# Step 1. Generate SSH keys

I recommend **Ed25519** keys.

Personal account:

```bash
ssh-keygen -t ed25519 -C "personal@gmail.com" \
-f ~/.ssh/id_ed25519_personal
```

College account:

```bash
ssh-keygen -t ed25519 -C "college@gmail.com" \
-f ~/.ssh/id_ed25519_college
```

You'll see:

```
Enter passphrase:
```

You can:

* Leave it empty (convenient)
* Set one (more secure)

You'll now have

```
~/.ssh/

id_ed25519_personal
id_ed25519_personal.pub

id_ed25519_college
id_ed25519_college.pub
```

---

# Step 2. Start SSH Agent

Ubuntu:

```bash
eval "$(ssh-agent -s)"
```

Add keys:

```bash
ssh-add ~/.ssh/id_ed25519_personal

ssh-add ~/.ssh/id_ed25519_college
```

Verify:

```bash
ssh-add -l
```

Output:

```
256 SHA256:....
256 SHA256:....
```

---

# Step 3. Add keys to GitHub

Copy public key

```bash
cat ~/.ssh/id_ed25519_personal.pub
```

Copy everything.

Go to

```
GitHub

Settings

SSH and GPG Keys

New SSH Key
```

Paste it.

Repeat for the second account.

---

# Step 4. Configure SSH

Create

```bash
~/.ssh/config
```

Contents:

```text
Host github-personal
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_personal
    IdentitiesOnly yes

Host github-college
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_college
    IdentitiesOnly yes
```

This file is the magic.

Instead of saying

```
github.com
```

you'll say

```
github-personal
```

or

```
github-college
```

SSH automatically chooses the correct key.

---

# Step 5. Test connections

Personal

```bash
ssh -T git@github-personal
```

Expected

```
Hi Shudarsan!
You've successfully authenticated.
```

College

```bash
ssh -T git@github-college
```

Expected

```
Hi CollegeAccount!
You've successfully authenticated.
```

Now you're done with authentication forever.

---

# Step 6. Clone repositories correctly

Personal repository

Instead of

```bash
git@github.com:Shudarsan/project.git
```

use

```bash
git@github-personal:Shudarsan/project.git
```

Notice

```
github-personal
```

not

```
github.com
```

College repository

```
git@github-college:CollegeOrg/project.git
```

Again

```
github-college
```

This determines which SSH key is used.

---

# Step 7. Existing repositories

Already cloned?

Check:

```bash
git remote -v
```

Suppose it shows

```
origin

git@github.com:Shudarsan/project.git
```

Change it.

Personal:

```bash
git remote set-url origin \
git@github-personal:Shudarsan/project.git
```

College:

```bash
git remote set-url origin \
git@github-college:CollegeOrg/project.git
```

Done.

---

# Step 8. Configure commit identity

Now we configure the author.

Global default:

```bash
git config --global user.name "Shudarsan Regmi"

git config --global user.email "personal@gmail.com"
```

This becomes your fallback.

---

For a specific repository:

```
cd ProjectA
```

Set:

```bash
git config user.name "Shudarsan Regmi"

git config user.email "college@gmail.com"
```

Notice:

No `--global`.

These values go into

```
ProjectA/.git/config
```

and affect **only that repository**.

---

Verify:

```bash
git config user.name

git config user.email
```

or

```bash
git config --list
```

You'll see

```
user.name=...

user.email=...
```

---

# Step 9. Where are configs stored?

Global

```
~/.gitconfig
```

Repository

```
project/

    .git/

        config
```

Example

```
Personal Repo

user.email=personal@gmail.com


College Repo

user.email=college@gmail.com
```

Git automatically uses the repository-specific values when present.

---

# Step 10. Verify before committing

Useful command:

```bash
git config --show-origin --get user.email
```

Example

```
file:/home/shudarsan/.gitconfig

personal@gmail.com
```

or

```
file:.git/config

college@gmail.com
```

This tells you **exactly** where the value came from.

---

# Step 11. Check commit author

Before pushing:

```bash
git log -1
```

or

```bash
git show HEAD
```

You'll see:

```
Author:

Shudarsan Regmi <college@gmail.com>
```

Exactly what GitHub will display.

---

# Final workflow

Suppose tomorrow you create two repositories.

## Personal

```bash
git clone git@github-personal:Shudarsan/MyPortfolio.git

cd MyPortfolio

git config user.email "personal@gmail.com"
```

Push

```
git push
```

SSH Key:

```
Personal
```

Commit Author:

```
personal@gmail.com
```

---

## College

```bash
git clone git@github-college:AmritaGPT/backend.git

cd backend

git config user.email "college@gmail.com"
```

Push

```
git push
```

SSH Key:

```
College
```

Commit Author:

```
college@gmail.com
```

No prompts. No tokens. No switching accounts.

## A tip for the future

If you end up with many repositories, you can automate the per-repository identity using Git's `includeIf` feature, so repositories under directories like `~/Projects/personal/` and `~/Projects/college/` automatically pick the correct `user.name` and `user.email` without running `git config` in each repository. Once you're comfortable with the basics, I can show you that cleaner, scalable setup as well. It's what many experienced developers use.

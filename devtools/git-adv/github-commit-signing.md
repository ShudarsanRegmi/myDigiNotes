**Rephrased question:**

> *I've decided to use SSH commit signing instead of GPG. Can you teach me how to configure it from scratch, explain what each step does, and show me how to verify that it's working?*

Excellent choice. SSH signing is the modern approach, especially since you're already planning to authenticate with SSH. In many cases, you can even reuse the same SSH key.

---

# Before we begin

Remember the difference:

```text
SSH Authentication
──────────────────────────────
git push
      │
      ▼
GitHub verifies you're allowed to push.

SSH Commit Signing
──────────────────────────────
git commit
      │
      ▼
GitHub verifies you created the commit.
```

These are independent features.

---

# Step 1: Check your Git version

SSH signing requires Git 2.34 or newer.

```bash
git --version
```

Example:

```text
git version 2.48.1
```

Anything newer than 2.34 is fine.

---

# Step 2: Find the SSH key you want to sign with

List your SSH keys:

```bash
ls ~/.ssh
```

Example:

```text
id_ed25519_personal
id_ed25519_personal.pub

id_ed25519_college
id_ed25519_college.pub
```

Suppose you want to use

```text
~/.ssh/id_ed25519_personal
```

---

# Step 3: Tell Git to use SSH for signing

Run:

```bash
git config --global gpg.format ssh
```

This is slightly confusing because the option still contains `gpg`, but you're **not using GPG**.

It simply tells Git:

> "When I sign commits, use the SSH signing backend."

Verify:

```bash
git config --global --get gpg.format
```

Output:

```text
ssh
```

---

# Step 4: Tell Git which SSH key to sign with

```bash
git config --global user.signingkey ~/.ssh/id_ed25519_personal.pub
```

Notice:

**Use the `.pub` file**, not the private key.

Verify:

```bash
git config --global --get user.signingkey
```

Output:

```text
~/.ssh/id_ed25519_personal.pub
```

---

# Step 5: Enable automatic signing

Instead of remembering

```bash
git commit -S
```

every time,

enable it globally:

```bash
git config --global commit.gpgsign true
```

Now every commit is automatically signed.

Verify:

```bash
git config --global --get commit.gpgsign
```

Output:

```text
true
```

---

# Step 6: Tell GitHub about this signing key

This is different from the SSH key used for authentication.

Go to:

```text
GitHub

Settings

SSH and GPG Keys
```

You'll see two sections:

```text
SSH Keys
```

and

```text
Signing Keys
```

Click

```text
New SSH Key
```

or

```text
New SSH Signing Key
```

depending on the UI.

Copy:

```bash
cat ~/.ssh/id_ed25519_personal.pub
```

Paste it.

When GitHub asks:

```text
Authentication

or

Signing
```

Choose

```text
Signing
```

This tells GitHub:

> "This public key should verify my commit signatures."

---

# Step 7: Make a commit

```bash
git add .

git commit -m "Initial setup"
```

Since

```text
commit.gpgsign=true
```

Git automatically signs it.

---

# Step 8: Verify locally

Run

```bash
git log --show-signature
```

Example:

```text
Good "git" signature
```

or

```text
Good SSH signature
```

depending on your Git version.

---

# Step 9: Push

```bash
git push
```

Open GitHub.

You'll see

```text
Verified
```

next to the commit.

Success!

---

# What happened behind the scenes?

When you committed,

Git created something like this:

```text
Commit

Files
Message
Author
Parent
Tree

↓

Sign everything

↓

Signature
```

GitHub downloads your public signing key and verifies:

```
Does this signature match the uploaded key?

YES

↓

Verified
```

---

# Multiple GitHub accounts

Suppose:

```text
Personal
    ~/.ssh/id_ed25519_personal

College
    ~/.ssh/id_ed25519_college
```

You can even use different signing keys.

Global:

```bash
git config --global user.signingkey ~/.ssh/id_ed25519_personal.pub
```

Inside your college repository:

```bash
git config user.signingkey ~/.ssh/id_ed25519_college.pub
```

Notice there's **no `--global`**, so only that repository uses the college signing key.

The same applies to:

```bash
git config user.email "college@example.edu"

git config user.name "Shudarsan Regmi"
```

Now everything aligns:

| Setting            | Personal Repo  | College Repo  |
| ------------------ | -------------- | ------------- |
| SSH Authentication | Personal key   | College key   |
| Commit Signing     | Personal key   | College key   |
| `user.email`       | Personal email | College email |

---

# Inspect your configuration

These commands are very useful:

```bash
git config --show-origin --list
```

Shows where every setting comes from.

```bash
git config --get gpg.format
```

```bash
git config --get user.signingkey
```

```bash
git config --get commit.gpgsign
```

---

# One final clarification

A common misconception is:

> "I'm using the same SSH key for authentication and signing, so they're the same thing."

Not quite.

Even if you reuse the same key pair, Git performs **two separate cryptographic operations**:

```
git push
    │
    └── SSH protocol authenticates you to GitHub.

git commit
    │
    └── Git signs the commit object with your SSH key.
```

They happen at different times and serve different purposes. GitHub simply recognizes that the public key you uploaded is authorized both to authenticate your account and to verify your commit signatures.

This separation is why a commit can still be **Verified** even if someone else pushes it later, and why an authenticated push can still contain **unsigned** commits.

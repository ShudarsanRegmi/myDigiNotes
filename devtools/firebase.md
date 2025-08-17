#  Firebase Hosting + Firestore Deployment Workflow (Reference Note)

### 🔹 1. One-time setup

```bash
firebase login             # Log in to Firebase CLI
firebase init              # Initialize project (choose Hosting, Firestore, etc.)
firebase projects:list     # See all Firebase projects
firebase use <project_id>  # Set active project
```

---

### 🔹 2. Firestore Rules & Indexes

```bash
firebase deploy --only firestore:rules     # Deploy Firestore security rules
firebase deploy --only firestore:indexes   # Deploy Firestore indexes
```

---

### 🔹 3. Build Frontend

*(for React/Vue/Svelte/etc.)*

```bash
npm run build     # Builds app into 'dist' or 'build' directory
```

*(Ensure your `firebase.json` has `"public": "dist"` or `"build"` depending on framework.)*

---

### 🔹 4. Deploy Hosting

```bash
firebase deploy --only hosting   # Deploys website to Firebase Hosting
```

---

### 🔹 5. Full Project Deploy (all at once)

```bash
firebase deploy
```

---

✅ With this flow:

1. Initialize once (`firebase init`).
2. Every time you update code: `npm run build → firebase deploy --only hosting`.
3. Update rules/indexes separately if needed.

---

### Sample firestore.json

```js
{
  "hosting": {
    "public": "dist",                 // Folder containing your built app
    "ignore": [
      "firebase.json",
      "**/.*",
      "**/node_modules/**"
    ],
    "rewrites": [
      {
        "source": "**",
        "destination": "/index.html"   // Needed for SPAs (React, Vue, Svelte, etc.)
      }
    ]
  },
  "firestore": {
    "rules": "firestore.rules",
    "indexes": "firestore.indexes.json"
  }
}
```

```js
{
  "hosting": { ... },
  "firestore": { ... },
  "storage": { ... },
  "functions": { ... }
}
```
> `firebase deploy` will push everything

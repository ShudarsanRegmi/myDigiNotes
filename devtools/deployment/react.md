# Deploying React Applications



**Vite config**

```js
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import path from 'path'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  base:'/negces/negceslab/client/dist/',
  build: {
    outDir: 'dist'
  },
  resolve: {
    alias: {
      '@images': path.resolve(__dirname, 'src/assets/'),
      '@': '/src'
    }
  },
  server: {
    allowedHosts: 'all' // this is when you want to server yoru app over different url; can be useful when using port forwarding
  }
})
```

**Building**
```bash
npm run build
```


## Setting Up Base Directory in React router
```bash
import BrowserRouter as Router

<Router basename="/negces/negceslab/client/dist">
  <Routes>
    <Route path='/login' element={<MainLayout> <Login /> <MainLayout />} />
  </Routes>
<Router>
```

## Setting up `base` parameter in vite config

```js
base:'/negces/negceslab/client/dist/',
```

### **React Router `basename` vs Vite `base`**

#### 1. **Vite `base` (vite.config.ts)**

* **What it does**: Tells Vite where your app will be served in the URL, so it generates correct links for JS, CSS, and assets.
* **Needed when**: Your app is **not hosted at domain root** (e.g. `intranet.edu/myapp/` instead of `intranet.edu/`).
* **Example**:

  ```ts
  export default defineConfig({
    base: '/negces/negceslab/client/dist/',
  })
  ```
* Without it: asset requests break (`/assets/...` → 404).

---

#### 2. **React Router `basename`**

* **What it does**: Tells React Router that your routes live under a URL prefix.
* **Needed when**: Your SPA is served from a subpath, and you want routing to resolve correctly.
* **Example**:

  ```tsx
  <BrowserRouter basename="/negces/negceslab/client/dist">
    <App />
  </BrowserRouter>
  ```
* Without it: routes like `/login` don’t work, because the app thinks `/login` is at the domain root.

---

#### 3. **Do they need to match?**

* ✅ Yes — they should both reflect the **public URL path** where the app is deployed.
* `vite.config.ts → base` handles **asset URLs**.
* `BrowserRouter → basename` handles **React routes**.
* If they don’t match, assets may load but routes break (or vice versa).

---

#### 4. **Quick scenarios**

* **Hosted at root** (`https://mydomain.com/`):

  * `vite.config.ts`: `base: '/'` (default)
  * `BrowserRouter`: no `basename` needed.

* **Hosted at subpath** (`https://mydomain.com/app/`):

  * `vite.config.ts`: `base: '/app/'`
  * `BrowserRouter`: `basename="/app"`

---

👉 Rule of thumb:

* Vite `base` = make assets load from the right place.
* React Router `basename` = make SPA routes resolve from the right place.
* Both are needed if app is **not at domain root**.





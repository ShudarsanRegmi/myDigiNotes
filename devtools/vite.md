# Vite

### Exposing vite to outside network
```bash
npm run dev -- --host
```

### Using environment variables in vite

- Vite automatically loads environment variables from .env files. (no need to load any extra package like dotenv)
- These variables are exposed to your frontend code only if they are prefixed with VITE_.
- Example: VITE_API_URL=https://example.com.

**File naming conventions**

You can create multiple .env files depending on the mode:

- .env → loaded in all cases.
- .env.development → loaded only in development mode.
- .env.production → loaded only in production builds.
- .env.local → loaded but not committed (good for secrets).

```
console.log(import.meta.env.VITE_API_URL);
```

**Other built-in variables Vite provides:**

- `import.meta.env.MODE → current mode (development, production, etc.)`
- `import.meta.env.DEV → true in dev mode`
- `import.meta.env.PROD → true in prod mode`

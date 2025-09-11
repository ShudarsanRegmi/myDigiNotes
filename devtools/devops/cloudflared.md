# Cloudflared

> This tool can be used to expose port to outside

## Steps:

**Download cloudflared binary**
```bash
wget https://github.com/cloudflare/cloudflared/releases/download/2025.8.1/cloudflared-linux-amd64
```

**Expose the service to outside**
```bash
./cloudflared tunnel --url http://localhost:5173
```

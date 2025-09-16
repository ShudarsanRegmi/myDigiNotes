# Certbot for enabling HTTPs


```bash
sudo apt update && sudo apt install -y certbot python3-certbot-nginx
```

```bash
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com
```

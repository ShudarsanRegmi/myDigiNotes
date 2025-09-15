## Gcloud Notes


**Add firewall rules**
```
# Check if default-allow-http exists
gcloud compute firewall-rules list --filter="name:default-allow-http"

# If it doesn't exist, create it
gcloud compute firewall-rules create default-allow-http \
    --allow tcp:80 \
    --source-ranges 0.0.0.0/0 \
    --target-tags http-server

```

> Debug  using python http.server

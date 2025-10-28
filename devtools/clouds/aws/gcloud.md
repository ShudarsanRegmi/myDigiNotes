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

### Setting up ssh connection from local device
- This command creates user, sets up ssh connection, generate keypairs and transports the private key to the server(authorized_keys)
  
```bash
gcloud compute ssh instance-20251015-154727 --project=acnctf --zone=us-central1-f
```

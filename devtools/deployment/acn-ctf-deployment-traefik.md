# Web6 CTF Challenge - Complete Deployment Guide

## 🏗️ **Infrastructure Overview**

**Architecture**: Single GCP VM running multiple Docker containers with Traefik reverse proxy
**Domain**: `amritacybernation.com` with versioned subdomains
**Challenge**: Multi-version website with hidden flag fragments

---

## 🌐 **1. Domain Configuration**

### **DNS Records Setup**
```
Record Type: A
Name: @
Value: 34.93.134.151
TTL: Automatic

Record Type: A  
Name: a7f3d2e1b9c8456789abcdef0123456789abcdef0123456789abcde.v1
Value: 34.93.134.151
TTL: Automatic

Record Type: A
Name: a7f3d2e1b9c8456789abcdef0123456789abcdef0123456789abcde.v2  
Value: 34.93.134.151
TTL: Automatic

Record Type: A
Name: a7f3d2e1b9c8456789abcdef0123456789abcdef0123456789abcde.v3
Value: 34.93.134.151
TTL: Automatic

Record Type: A
Name: a7f3d2e1b9c8456789abcdef0123456789abcdef0123456789abcde.v4
Value: 34.93.134.151
TTL: Automatic
```

### **Challenge URLs**
- **Main Site**: `http://amritacybernation.com`
- **Version 1**: `http://a7f3d2e1b9c8456789abcdef0123456789abcdef0123456789abcde.v1.amritacybernation.com`
- **Version 2**: `http://a7f3d2e1b9c8456789abcdef0123456789abcdef0123456789abcde.v2.amritacybernation.com`
- **Version 3**: `http://a7f3d2e1b9c8456789abcdef0123456789abcdef0123456789abcde.v3.amritacybernation.com`
- **Version 4**: `http://a7f3d2e1b9c8456789abcdef0123456789abcdef0123456789abcde.v4.amritacybernation.com`

---

## 🔥 **2. GCP Firewall Configuration**

### **Firewall Rules Created**
```bash
# Primary rule allowing HTTP/HTTPS traffic
Rule Name: web6-traffic
Direction: Ingress
Targets: Apply to all instances
Source IP ranges: 0.0.0.0/0
Protocols and ports: tcp:80, tcp:443, tcp:8080
Action: Allow
Priority: 1000
Network: default
```

### **Commands Used**
```bash
# Create firewall rule
gcloud compute firewall-rules create web6-traffic \
    --allow tcp:80,tcp:443,tcp:8080 \
    --source-ranges 0.0.0.0/0 \
    --description "Allow HTTP/HTTPS for Web6 CTF"

# Update to apply to all VMs
gcloud compute firewall-rules update web6-traffic \
    --target-tags=""
```

### **VM Instance Tags**
```bash
# Add HTTP server tags to VM
gcloud compute instances add-tags instance-20250915-030152 \
    --zone=asia-south1-c \
    --tags=http-server,https-server

# Verify tags
gcloud compute instances describe instance-20250915-030152 \
    --zone=asia-south1-c \
    --format="value(tags.items)"
# Output: http-server;https-server
```

---

## 🖥️ **3. Server Configuration**

### **VM Details**
- **Instance**: `instance-20250915-030152`
- **Zone**: `asia-south1-c`
- **Machine Type**: `e2-medium`
- **External IP**: `34.93.134.151`
- **Internal IP**: `10.160.0.2`
- **Project**: `acnctf`

### **Server Hosts File** (hosts)
```bash
# Added entries for local testing
127.0.0.1 amritacybernation.com
127.0.0.1 a7f3d2e1b9c8456789abcdef0123456789abcdef0123456789abcde.v1.amritacybernation.com
127.0.0.1 a7f3d2e1b9c8456789abcdef0123456789abcdef0123456789abcde.v2.amritacybernation.com
127.0.0.1 a7f3d2e1b9c8456789abcdef0123456789abcdef0123456789abcde.v3.amritacybernation.com
127.0.0.1 a7f3d2e1b9c8456789abcdef0123456789abcdef0123456789abcde.v4.amritacybernation.com
```

### **Command to Add Hosts**
```bash
cat << 'EOF' | sudo tee -a /etc/hosts
127.0.0.1 amritacybernation.com
127.0.0.1 a7f3d2e1b9c8456789abcdef0123456789abcdef0123456789abcde.v1.amritacybernation.com
127.0.0.1 a7f3d2e1b9c8456789abcdef0123456789abcdef0123456789abcde.v2.amritacybernation.com
127.0.0.1 a7f3d2e1b9c8456789abcdef0123456789abcdef0123456789abcde.v3.amritacybernation.com
127.0.0.1 a7f3d2e1b9c8456789abcdef0123456789abcdef0123456789abcde.v4.amritacybernation.com
EOF
```

---

## 🐳 **4. Docker Configuration**

### **Network Setup**
```yaml
networks:
  web6-network:
    driver: bridge
```

### **Port Mappings**
- **Port 80**: HTTP traffic → Traefik → Backend containers
- **Port 443**: HTTPS traffic → Traefik → Backend containers  
- **Port 8080**: Traefik dashboard (internal use)

### **Container Architecture**
```
Internet (Port 80/443) → Traefik Proxy → Internal Docker Network → Backend Containers
                                      ↓
                              Host-based routing by domain
```

---

## 🔀 **5. Traefik Reverse Proxy Configuration**

### **Traefik Settings**
```yaml
traefik:
  image: traefik:v2.10
  command:
    - "--api.insecure=true"
    - "--providers.docker=true"
    - "--providers.docker.exposedbydefault=false"
    - "--entrypoints.web.address=:80"
    - "--entrypoints.websecure.address=:443"
    - "--log.level=DEBUG"
  ports:
    - "80:80"
    - "443:443"
    - "8080:8080"
```

### **Routing Rules**
Each service uses Host-based routing:
```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.SERVICE.rule=Host(`DOMAIN`)"
  - "traefik.http.routers.SERVICE.entrypoints=web"
  - "traefik.http.services.SERVICE.loadbalancer.server.port=80"
```

---

## 🚀 **6. Deployment Process**

### **Step 1: Build and Deploy**
```bash
cd ~/web6
sudo docker-compose build
sudo docker-compose up -d
```

### **Step 2: Verify Containers**
```bash
sudo docker-compose ps
sudo docker-compose logs traefik
```

### **Step 3: Test Connectivity**
```bash
# Local testing
curl http://localhost:8080  # Traefik dashboard
curl http://amritacybernation.com

# External testing
curl http://34.93.134.151
telnet 34.93.134.151 80
```

---

## 🔍 **7. Troubleshooting Commands**

### **Network Debugging**
```bash
# Check listening ports
sudo ss -tlnp | grep :80

# Check firewall rules
gcloud compute firewall-rules list --filter="direction:INGRESS AND allowed.ports:80"

# Test external connectivity
curl -v http://34.93.134.151
```

### **Docker Debugging**
```bash
# Container logs
sudo docker-compose logs [service_name]

# Network inspection
sudo docker network ls
sudo docker network inspect web6_web6-network

# Port bindings
sudo docker port web6-traefik
```

### **Traefik Debugging**
```bash
# Check registered routes
curl http://localhost:8080/api/http/routers

# Check services
curl http://localhost:8080/api/http/services

# Test with Host headers
curl -H "Host: amritacybernation.com" http://localhost
```

---

## 🎯 **8. CTF Challenge Details**

### **Flag Distribution**
- **Version 1**: `flag{time_` (HTML comment)
- **Version 2**: `capsule_` (robots.txt)
- **Version 3**: `web_` (oldpage.html)
- **Version 4**: `trail}` (CSS comment)
- **Complete Flag**: `flag{time_capsule_web_trail}`

### **Player Journey**
1. Discover main site → Find hint to archived versions
2. Enumerate versioned subdomains with long UUID-like prefixes
3. Extract flag fragments from each version
4. Combine fragments to complete the flag

---

## 📋 **9. Security Considerations**

### **Production Hardening**
- Disable Traefik dashboard (`--api.insecure=false`)
- Implement SSL/TLS certificates
- Restrict firewall rules to specific source IPs
- Use Docker secrets for sensitive data
- Enable container resource limits

### **Monitoring**
- Monitor Traefik access logs
- Set up container health checks
- Monitor resource usage
- Implement log aggregation

---

## 🔧 **10. Maintenance Commands**

### **Service Management**
```bash
# Restart services
sudo docker-compose restart

# Update containers
sudo docker-compose down
sudo docker-compose build --no-cache
sudo docker-compose up -d

# Clean up
sudo docker system prune -f
```

### **Backup**
```bash
# Backup configuration
tar -czf web6-backup.tar.gz ~/web6/

# Export container images
sudo docker save web6_web6-v1 | gzip > web6-v1-backup.tar.gz
```

---

```Dockerfile
FROM nginx:alpine

# Remove default nginx website
RUN rm -rf /usr/share/nginx/html/*

# Copy version directories
COPY v1/ /usr/share/nginx/html/v1/
COPY v2/ /usr/share/nginx/html/v2/
COPY v3/ /usr/share/nginx/html/v3/
COPY v4/ /usr/share/nginx/html/v4/

# Create a simple navigation index page
RUN echo '<!DOCTYPE html>\n\
<html lang="en">\n\
<head>\n\
    <meta charset="UTF-8">\n\
    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n\
    <title>Website Versions - Alex Rodriguez Archive</title>\n\
    <style>\n\
        body { font-family: Arial, sans-serif; max-width: 900px; margin: 50px auto; padding: 20px; background: #f8f9fa; }\n\
        .container { background: white; padding: 40px; border-radius: 15px; box-shadow: 0 4px 20px rgba(0,0,0,0.1); }\n\
        h1 { color: #333; text-align: center; margin-bottom: 10px; }\n\
        .subtitle { text-align: center; color: #666; margin-bottom: 30px; font-style: italic; }\n\
        .archive-note { background: #e7f3ff; padding: 15px; border-left: 4px solid #007bff; margin-bottom: 30px; }\n\
        .version-list { list-style: none; padding: 0; }\n\
        .version-item { margin: 20px 0; padding: 25px; border: 2px solid #ddd; border-radius: 12px; transition: all 0.3s ease; }\n\
        .version-item:hover { border-color: #007bff; background-color: #f8f9fa; transform: translateY(-2px); }\n\
        .version-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; }\n\
        .version-link { text-decoration: none; color: #007bff; font-size: 18px; font-weight: bold; }\n\
        .version-date { color: #999; font-size: 14px; }\n\
        .version-description { color: #666; margin: 10px 0; }\n\
        .access-methods { margin-top: 15px; }\n\
        .access-label { font-weight: bold; color: #333; font-size: 14px; }\n\
        .access-links { margin-top: 5px; }\n\
        .access-link { display: inline-block; margin-right: 15px; padding: 5px 12px; background: #e9ecef; text-decoration: none; color: #495057; border-radius: 5px; font-size: 13px; transition: background 0.3s; }\n\
        .access-link:hover { background: #007bff; color: white; }\n\
    </style>\n\
</head>\n\
<body>\n\
    <div class="container">\n\
        <h1>Alex Rodriguez - Project Evolution Archive</h1>\n\
        <p class="subtitle">Website snapshots captured over time</p>\n\
        \n\
        <div class="archive-note">\n\
            <strong>💡 Archive Access:</strong> This site supports both subdomain and path-based access methods.\n\
            Use subdomains like <code>*.v1.site.com</code> or paths like <code>/v1/</code> to access different versions.\n\
        </div>\n\
        \n\
        <ul class="version-list">\n\
            <li class="version-item">\n\
                <div class="version-header">\n\
                    <a href="/v1/" class="version-link">Version 1 - Initial Launch</a>\n\
                    <span class="version-date">2023-01-15</span>\n\
                </div>\n\
                <p class="version-description">The original website launch with basic portfolio content and clean design.</p>\n\
                <div class="access-methods">\n\
                    <div class="access-label">Access Methods:</div>\n\
                    <div class="access-links">\n\
                        <a href="/v1/" class="access-link">Path: /v1/</a>\n\
                        <span class="access-link" style="background: #fff3cd; color: #856404;">Subdomain: *.v1.site.com</span>\n\
                    </div>\n\
                </div>\n\
            </li>\n\
            \n\
            <li class="version-item">\n\
                <div class="version-header">\n\
                    <a href="/v2/" class="version-link">Version 2 - SEO Updates</a>\n\
                    <span class="version-date">2023-03-22</span>\n\
                </div>\n\
                <p class="version-description">Added search engine optimization improvements and robots.txt for better crawling.</p>\n\
                <div class="access-methods">\n\
                    <div class="access-label">Access Methods:</div>\n\
                    <div class="access-links">\n\
                        <a href="/v2/" class="access-link">Path: /v2/</a>\n\
                        <span class="access-link" style="background: #fff3cd; color: #856404;">Subdomain: *.v2.site.com</span>\n\
                    </div>\n\
                </div>\n\
            </li>\n\
            \n\
            <li class="version-item">\n\
                <div class="version-header">\n\
                    <a href="/v3/" class="version-link">Version 3 - Content Addition</a>\n\
                    <span class="version-date">2023-07-08</span>\n\
                </div>\n\
                <p class="version-description">Temporarily added some extra content pages and draft materials.</p>\n\
                <div class="access-methods">\n\
                    <div class="access-label">Access Methods:</div>\n\
                    <div class="access-links">\n\
                        <a href="/v3/" class="access-link">Path: /v3/</a>\n\
                        <span class="access-link" style="background: #fff3cd; color: #856404;">Subdomain: *.v3.site.com</span>\n\
                    </div>\n\
                </div>\n\
            </li>\n\
            \n\
            <li class="version-item">\n\
                <div class="version-header">\n\
                    <a href="/v4/" class="version-link">Version 4 - Style Refresh</a>\n\
                    <span class="version-date">2023-11-14</span>\n\
                </div>\n\
                <p class="version-description">Updated styling, improved animations, and cleaned up the overall design.</p>\n\
                <div class="access-methods">\n\
                    <div class="access-label">Access Methods:</div>\n\
                    <div class="access-links">\n\
                        <a href="/v4/" class="access-link">Path: /v4/</a>\n\
                        <span class="access-link" style="background: #fff3cd; color: #856404;">Subdomain: *.v4.site.com</span>\n\
                    </div>\n\
                </div>\n\
            </li>\n\
        </ul>\n\
    </div>\n\
</body>\n\
</html>' > /usr/share/nginx/html/index.html

# Copy custom nginx configuration
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose port 80
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
```

**Docker compose**

```yml
# Docker Compose for Web6 CTF Challenge
# Multi-container setup with Traefik reverse proxy

networks:
  web6-network:
    driver: bridge

services:
  # Traefik Reverse Proxy
  traefik:
    image: traefik:v2.10
    container_name: web6-traefik
    command:
      - "--api.insecure=true"
      - "--providers.docker=true"
      - "--providers.docker.exposedbydefault=false"
      - "--entrypoints.web.address=:80"
      - "--entrypoints.websecure.address=:443"
      - "--log.level=DEBUG"
    ports:
      - "80:80"
      - "443:443"
      - "8080:8080"
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock:ro
    networks:
      - web6-network
    restart: unless-stopped

  # Version 1 - Initial launch
  web6-v1:
    build:
      context: ./v1
      dockerfile: Dockerfile
    container_name: web6-v1
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.web6-v1.rule=Host(`a7f3d2e1b9c8456789abcdef0123456789abcdef0123456789abcde.v1.amritacybernation.com`)"
      - "traefik.http.routers.web6-v1.entrypoints=web"
      - "traefik.http.services.web6-v1.loadbalancer.server.port=80"
      - "traefik.http.routers.web6-v1.service=web6-v1"
    networks:
      - web6-network
    restart: unless-stopped

  # Version 2 - With robots.txt
  web6-v2:
    build:
      context: ./v2
      dockerfile: Dockerfile
    container_name: web6-v2
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.web6-v2.rule=Host(`a7f3d2e1b9c8456789abcdef0123456789abcdef0123456789abcde.v2.amritacybernation.com`)"
      - "traefik.http.routers.web6-v2.entrypoints=web"
      - "traefik.http.services.web6-v2.loadbalancer.server.port=80"
      - "traefik.http.routers.web6-v2.service=web6-v2"
    networks:
      - web6-network
    restart: unless-stopped

  # Version 3 - With temporary page
  web6-v3:
    build:
      context: ./v3
      dockerfile: Dockerfile
    container_name: web6-v3
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.web6-v3.rule=Host(`a7f3d2e1b9c8456789abcdef0123456789abcdef0123456789abcde.v3.amritacybernation.com`)"
      - "traefik.http.routers.web6-v3.entrypoints=web"
      - "traefik.http.services.web6-v3.loadbalancer.server.port=80"
      - "traefik.http.routers.web6-v3.service=web6-v3"
    networks:
      - web6-network
    restart: unless-stopped

  # Version 4 - Final version
  web6-v4:
    build:
      context: ./v4
      dockerfile: Dockerfile
    container_name: web6-v4
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.web6-v4.rule=Host(`a7f3d2e1b9c8456789abcdef0123456789abcdef0123456789abcde.v4.amritacybernation.com`)"
      - "traefik.http.routers.web6-v4.entrypoints=web"
      - "traefik.http.services.web6-v4.loadbalancer.server.port=80"
      - "traefik.http.routers.web6-v4.service=web6-v4"
    networks:
      - web6-network
    restart: unless-stopped

  # Main site (latest version)
  web6-main:
    build:
      context: ./v4
      dockerfile: Dockerfile
    container_name: web6-main
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.web6-main.rule=Host(`amritacybernation.com`)"
      - "traefik.http.routers.web6-main.entrypoints=web"
      - "traefik.http.services.web6-main.loadbalancer.server.port=80"
      - "traefik.http.routers.web6-main.service=web6-main"
    networks:
      - web6-network
    restart: unless-stopped
```

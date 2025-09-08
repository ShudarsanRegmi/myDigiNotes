# Podman commands


**Used to login**
```bash
podman login registery.lab.example.com --tls-verify=false
```


**List Images**
```bash
podman images
```


**Run and remove**
```bash
podman run --rm registry.lab.example.com/ubi9/ubi echo 'Hello redhat'
```

****
```bash

```

**Show running containers**
```bash
podman ps
```

**Passing environment variables**
```bash
podman run --rm -e GREET=Hello -e NAME='Red Hat registry.lab.example.com/ubi9/ubi printenv GREET NAME' 
```

**Pull an image from registery**
```bash
podman pull registry.lab.example.com/rhel9/httpd-24 --tls-verify=false
```

**Exposing Port Outside**
```bash
podman run --rm -p 8080:8080 registry.lab.example.com/rhel9/httpd-24
```

**Run as a daemon**
```bash
podman run --rm -d  -p 8080:8080 registry.lab.example.com/rhel9/httpd-24
```

**Spawning a shell**
```bash
podman run -it <image> /bin/bash
docker exec -it <container> /bin/bash
```

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

**Stop a container**
```bash
podman stop 1b982aeb75dd
```

**Stop all running containers**
```bash
podman stop --all
```

**Stopping containers forcefully**
```bash
podman kill httpd
```

**Pausing/UnPausing**
```bash
podman pause 4f2038c05b8c
podman unpause 4f2038c05b8c
```

**Restarting containers**
```bash
podman restart nginx
```

**Removing containers**
```bash
podman rm c58cfd4b90df
podman rm c58cfd4b90df --force
podman rm --all # removed all stopped containers
```


**Running already downloaded images**
```bash
podman run -it ubuntu /bin/bash
podman run -d --name web nginx
podman run -d -p 8080:80 -v /data:/var/www/html:Z httpd
```

## Storage Persistence

```bash
podman run -v /host/path:/cont/path image
```


## Attaching SELinux context
```bash
podman run -v /host/path:/cont/path:z image
```

## Start a containerized service at boot
As a regular user, you can create systemd unit files to manage your rootless containers. You can use this configuration to manage your container as a regular systemd service with the systemctl command.

**Generate a systemd unit file**
```bash
podman generate systemd --name web --files
output: /home/user/container-web.service
```

**Move the above fileto `.config/systemd/user`**
```bash
mv /home/user/container-web.service ~/.config/systemd/user
```

**Manage the containerized service**
```bash
systemctl --user [start, stop, status, enable, disable] container-web.service
```

When you use the --user option, by default, systemd starts the service when you log in, and stops it when you log out. You can start your enabled services at the operating system boot, and stop them on shutdown, by running the loginctl enable-linger command.

```bash
loginctl enable-linger
```





## Investigate the container by overriding the entry point

```bash
docker run -it --entrypoint /bin/bash backend:v15
```

## Investigate the file system of the failed container

```bash
docker run -it --name debug-container --entrypoint /bin/bash backend:v15
docker mount <container_id> # returns the path to host fs where container fs is mounted
docker umount <container_id> # unmount the container fs
```

## Docker Notes

### Setup docker

```
sudo apt update
sudo apt install docker.io -y

sudo systemctl start docker
sudo systemctl enable docker

sudo usermod -aG docker $USER # for running without sudo
```


### Images

- `docker pull <image>`

**Build an image from a container file**
`docker build -t <image_name>:<tag> .`


**Remove an image**
`docker rmi <image_id>`


## Running container

**Run container with image name**
`docker run --name conname -p sysport:conport image_name` 

**Run container in backround**
`docker run -d --name conname -p sysprot:conport image_name` 


## Pushing an image to docker hub

`docker login`
> Generte Pat from settings and put acess token

`docker tag localtag user/reponame:v1`
`docker push user/reponame:v1`


`docker pull user/reponame:v1`



## Cleanup 

```bash
podman system df            # check how much space podman is using
podman image prune -a       # remove unused images
podman container prune      # remove stopped containers
podman volume prune         # remove unused volumes
podman system reset --force # (⚠️ if safe, clears *all* podman data)

```

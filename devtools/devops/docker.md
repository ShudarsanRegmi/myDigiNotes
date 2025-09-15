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


## Important Commands to Cleanup Disk Space in Ubuntu

### Clean npm tarballs

```bash
npm cache clean --force
npm cache verify
```

### Clean all conda tarballs

```bash
conda clean --all
```

### Cleaning up pip cache

```bash
pip cache purge
```

### Cleanup all dangling docker images

``` bash
docker system prune -a
```

### Cleanup all apt cache
```bash
sudo apt autoremove
sudo apt autoclean
sudo apt clean
```

### Cleanup Journalctl logs
```bash
journalctl --disk-usage
sudo journalctl --vacuum-time=7d
```


### Check Language specific package managers and tools
- cargo, meaven, go

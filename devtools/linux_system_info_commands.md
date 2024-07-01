# Commands

### Checking memory usage
```bash
free -h
```

### Getting cpu information
```bash
lscpu
cat /proc/cpuinfo
```

### Getting all hardware information
```bash
lshw
```

### Getting usb devices info
```bash
lsusb
```

### Getting the size of folder including its subdirectories
```bsah
du -sh /path/to/folder
```

### Getting detailed information about folder including its subdirectories
```bash
du -ah /path/to/folder
```

### mentioning the depth
``bash
du -h --max-depth=1 /path/to/folder
```

### Sorting by size
```bash
du -ah /path/to/folder | sort -rh
```

### Using character based GUI tool
```bash
ncdu /path/to/folder
```

### GUI based disk usage analytics tool
```bash
baobab /path/to/folder
```

### Cusion Maps based representation

```bash
gdmap /path/to/directory
```

 GdMap is a tool which allows to visualize disk space. Ever wondered why your hard disk is full or what directory and files take up most of the space? With GdMap these questions can be answered quickly. To display directory structures cushion treemaps are used which visualize a complete folder or even the whole hard drive with one picture.

Cushion treemaps display directories and files in rectangular areas. The larger a file is the larger is the rectangle which represents it. All files in one directory are painted within the rectangle of that directory.



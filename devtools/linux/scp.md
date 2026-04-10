# SCP


## Generic Syntax

```bash
scp [source] [destination]
```

## Send 
```bash
scp a.txt user@server:/tmp/
```


## Receive
```bash
scp user@server:/tmp/b.txt .
```

## Copy entire directory
```bash
scp -r myfolder user@server:/path/
```

## Copy between two remote servers
```bash
scp user1@server1:/file user2@server2:/path/
```

## Send with compression
```bash
scp -C file.txt user@server:/path/
```


## Limit Speed in Kbps
```bash
scp -l 1000 file.txt user@server:/path/
```

## Preserve file attributes such as MAC timing
```bash
scp -p file.txt user@server:/path/
```



# Next
- Learn `rsync`

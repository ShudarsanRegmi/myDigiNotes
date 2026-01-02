### Find command Guide


**Basic Structure**
```bash
find <path> <conditions> <actions>
```
If you skip the action, find defaults to printing the matched paths.


**Search exactly for notes.txt**
```bash
find . -name notes.txt
find /home name notes.txt
find . iname notes.txt
```

**Search by type**
```bash
find . -type f
find . -type d
```


**Seraching by modified time**
```bash
find . -mtime -1 # Modified in the last 24 hours
find . -mtime +7 # Modified more than 7 days ago
```








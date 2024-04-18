# Handy Bash Scripts for CTFs


## Running a single binary with multiple parameters(stdin)

```
#!/bin/bash

# Define the list
pos_pw_list=("8799" "d3ab" "1ea2" "acaf" "2295" "a9de" "6f3d")

# Iterate through each item in the list
for item in "${pos_pw_list[@]}"; do
    # Pass the item as stdin to a binary file
    echo "$item" | ./your_binary_file
done
```

## Looking for a file having a particular keyword in a forest of files and directories

```
find /path/to/your/directory -type f -exec grep -l "pico" {} +
```



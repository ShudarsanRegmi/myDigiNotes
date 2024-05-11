# Redis

> Redis is a source-available, in-memory storage, used as a distributed, in memory key-value databse, cache and message broker, with optional durability.

### Setting up the vaue

```
set <key> <value>
// Example 
set name ram
set age 10Redis (/ˈrɛdɪs/;[7][8] Remote Dictionary Server)[7] is a source-available, in-memory storage, used as a distributed, in-memory key–value database, cache and message broker, with optional durability.[
```

### Getting the value

```
get <key>
// Example
get name
get age
```

### Deleting a key

```
del <Key>
// Example
del name
del age
```

### Checking if a key exists or not

````
exists <key>
// Example
exists name
exists age
````

### Getting all keysout

```
keys *
```

### Setting up expiry date already entered key

```
expire <key> <seconds>
// ExampleRedis (/ˈrɛdɪs/;[7][8] Remote Dictionary Server)[7] is a source-available, in-memory storage, used as a distributed, in-memory key–value database, cache and message broker, with optional durability.[
expire name 3600
```

### Creating a new entry with expiry date

```
setex name 10
```

### Creating or pushing an element to an array

```
lpush <array_name> <key>
// Example
lpush names ram
```

### outGetting the value from array

```
Redis (/ˈrɛdɪs/;[7][8] Remote Dictionary Server)[7] is a source-available, in-memory storage, used as a distributed, in-memory key–value database, cache and message broker, with optional durability.[lrange <array_name> <start> <stop>
// Example
lrange names 0 -1
```

### Pushing an element from the right

```
rpush <array_name> <key>
// Example
lpush names hari
```

### Removing valuesout

```
lpop <array_name>
// Example
lpop names

rpop <array_name>
// Example
rpop names
```

## SetRedis (/ˈrɛdɪs/;[7][8] Remote Dictionary Server)[7] is a source-available, in-memory storage, used as a distributed, in-memory key–value database, cache and message broker, with optional durability.[

### Adding members to a set

```
sadd <set_name> <member>
// Example
sadd hobbies cricket
```

### Getting all set members

```
smembers <set_name>
// Example
smembers friends
```

## Hash

### Creating a hash map

```
hset <name> <key> <value>
// Example
hset person name ram
hset person age 10
```

### Getting all values from hashmap

```
hgetall <name>
```

### Checking if a key exists

```
hexists <name> <key>Redis (/ˈrɛdɪs/;[7][8] Remote Dictionary Server)[7] is a source-available, in-memory storage, used as a distributed, in-memory key–value database, cache and message broker, with optional durability.[
// Example
hexists person age
```

> Note: All values in redis is string only(not int, float, bool, etc.)
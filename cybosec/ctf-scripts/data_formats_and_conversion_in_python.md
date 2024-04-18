# Quickly convert the data in different formats in Python


## Conversion: hex-int
```
0x12
```

## Conversion: int-hex
```
hex(10)
'0xab'
```

## Finding the ascii value of a char
```
ord('a')
> 97
```

## Getting the ascii character from ascii value
```
chr(97)
> a
```

## Conversion: hex(str)-int
```
int('ab',16)
```


## Conversion: Octal-int
```
int(123,8)
```

## Convert continuous hex bytes to character

```
x = '414243'
 ''.join([chr((int(x[i]+x[i+1],16))) for i in range(0,len(x),2)])
```

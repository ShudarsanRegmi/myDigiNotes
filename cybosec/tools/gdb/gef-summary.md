# GEF Summary

## Security Check
```
checksec
```

## Reading elf structure
```
elf
```

## Getting registers info

```
registers
```

## Comprehensive address space layout

```
vmmap
vmmap stack // print stack layout
```

## Breakpoints
```
info breakpoints

```

### Show the hexdump of stack. 

```
hexdump byte $rsp
hexdump byte $rbp
```

rbp-0x4
rbp-0x8
rbp-0x110


```
 run <<< $(python3 -c "import sys; sys.stdout.buffer.write(b'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaA' + b'\xca\xfe')")
```
## Mmap

```
(base) aparichit@SUSHANKYA:~/rough/os$ cat /proc/459385/maps 
5f2c84b9f000-5f2c84ba0000 r--p 00000000 103:02 8155465                   /home/aparichit/rough/os/exp2
5f2c84ba0000-5f2c84ba1000 r-xp 00001000 103:02 8155465                   /home/aparichit/rough/os/exp2
5f2c84ba1000-5f2c84ba2000 r--p 00002000 103:02 8155465                   /home/aparichit/rough/os/exp2
5f2c84ba2000-5f2c84ba3000 r--p 00002000 103:02 8155465                   /home/aparichit/rough/os/exp2
5f2c84ba3000-5f2c84ba4000 rw-p 00003000 103:02 8155465                   /home/aparichit/rough/os/exp2
5f2c87313000-5f2c87334000 rw-p 00000000 00:00 0                          [heap]
762d49e00000-762d69e00000 rw-p 00000000 00:00 0 
762d69e00000-762d69e28000 r--p 00000000 103:02 6820591                   /usr/lib/x86_64-linux-gnu/[libc.so](http://libc.so).6
762d69e28000-762d69fbd000 r-xp 00028000 103:02 6820591                   /usr/lib/x86_64-linux-gnu/[libc.so](http://libc.so).6
762d69fbd000-762d6a015000 r--p 001bd000 103:02 6820591                   /usr/lib/x86_64-linux-gnu/[libc.so](http://libc.so).6
762d6a015000-762d6a016000 ---p 00215000 103:02 6820591                   /usr/lib/x86_64-linux-gnu/[libc.so](http://libc.so).6
762d6a016000-762d6a01a000 r--p 00215000 103:02 6820591                   /usr/lib/x86_64-linux-gnu/[libc.so](http://libc.so).6
762d6a01a000-762d6a01c000 rw-p 00219000 103:02 6820591                   /usr/lib/x86_64-linux-gnu/[libc.so](http://libc.so).6
762d6a01c000-762d6a029000 rw-p 00000000 00:00 0 
762d6a1a3000-762d6a1a6000 rw-p 00000000 00:00 0 
762d6a1c4000-762d6a1c6000 rw-p 00000000 00:00 0 
762d6a1c6000-762d6a1c8000 r--p 00000000 103:02 6817800                   /usr/lib/x86_64-linux-gnu/[ld-linux-x86-64.so](http://ld-linux-x86-64.so).2
762d6a1c8000-762d6a1f2000 r-xp 00002000 103:02 6817800                   /usr/lib/x86_64-linux-gnu/[ld-linux-x86-64.so](http://ld-linux-x86-64.so).2
762d6a1f2000-762d6a1fd000 r--p 0002c000 103:02 6817800                   /usr/lib/x86_64-linux-gnu/[ld-linux-x86-64.so](http://ld-linux-x86-64.so).2
762d6a1fe000-762d6a200000 r--p 00037000 103:02 6817800                   /usr/lib/x86_64-linux-gnu/[ld-linux-x86-64.so](http://ld-linux-x86-64.so).2
762d6a200000-762d6a202000 rw-p 00039000 103:02 6817800                   /usr/lib/x86_64-linux-gnu/[ld-linux-x86-64.so](http://ld-linux-x86-64.so).2
7ffc00cc0000-7ffc00ce2000 rw-p 00000000 00:00 0                          [stack]
7ffc00d84000-7ffc00d88000 r--p 00000000 00:00 0                          [vvar]
7ffc00d88000-7ffc00d8a000 r-xp 00000000 00:00 0                          [vdso]
ffffffffff600000-ffffffffff601000 --xp 00000000 00:00 0                  [vsyscall]
```

<img width="575" height="659" alt="image" src="https://github.com/user-attachments/assets/dfe9afd4-b566-4331-b695-035efb203982" />

```
HIGH ADDRESSES
┌──────────────────────────────┐
│        [vsyscall]            │  ffffffffff600000
├──────────────────────────────┤
│           [vdso]             │
├──────────────────────────────┤
│           [vvar]             │
├──────────────────────────────┤
│           [stack]            │  7ffc00cc0000 - 7ffc00ce2000
│   (grows downward ↓)         │
├──────────────────────────────┤
│   Memory-mapped regions      │
│   (anonymous mmap)           │  762d49e00000 - 762d69e00000
├──────────────────────────────┤
│         libc (shared)        │
│   r-- | r-x | r-- | rw       │
│   (/usr/lib/.../libc.so.6)   │
├──────────────────────────────┤
│     Dynamic linker (ld)      │
│   (/usr/lib/.../ld-linux)    │
├──────────────────────────────┤
│           [heap]             │  5f2c87313000 - 5f2c87334000
│   (grows upward ↑)           │
├──────────────────────────────┤
│   Your program (exp2)        │
│   ┌──────────────────────┐   │
│   │ r--  (ELF header)    │   │
│   │ r-x  (code / text)   │   │
│   │ r--  (rodata)        │   │
│   │ rw-  (data/bss)      │   │
│   └──────────────────────┘   │
└──────────────────────────────┘
LOW ADDRESSES
```



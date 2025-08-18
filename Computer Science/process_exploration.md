


```c
#include <stdlib.h>
#include <unistd.h>

int main() {
    void *p = malloc(100 * 1024 * 1024); // allocate 100 MB
    sleep(30); // keep process alive
    return 0;
}

```




<img width="1296" height="453" alt="image" src="https://github.com/user-attachments/assets/c96b5abf-5ef7-4ca5-8f76-07095e151a66" />

<img width="631" height="479" alt="image" src="https://github.com/user-attachments/assets/9acd1efd-93c3-4d5c-9ac3-e439a5e7e30a" />




```
aparichit@SUSHANKYA:~/rough/os$ sudo cat /proc/iomem 
[sudo] password for aparichit: 
00000000-00000fff : Reserved
00001000-0009dfff : System RAM
0009e000-0009efff : Reserved
0009f000-0009ffff : System RAM
000a0000-000fffff : Reserved
  000a0000-000dffff : PCI Bus 0000:00
    000c0000-000dffff : 0000:00:02.0
  000f0000-000fffff : System ROM
00100000-3fffffff : System RAM
40000000-403fffff : Reserved
  40000000-403fffff : pnp 00:00
40400000-981da017 : System RAM
981da018-981e6857 : System RAM
981e6858-a1e15fff : System RAM
a1e16000-a1e16fff : ACPI Non-volatile Storage
a1e17000-a1e17fff : Reserved
a1e18000-a5ac4fff : System RAM
a5ac5000-a5b09fff : Reserved
a5b0a000-a9f24fff : System RAM
a9f25000-aa532fff : Reserved
aa533000-aa5affff : ACPI Tables
aa5b0000-aa678fff : ACPI Non-volatile Storage
aa679000-ab0fdfff : Reserved
ab0fe000-ab0fefff : System RAM
ab0ff000-af7fffff : Reserved
  ad800000-af7fffff : Graphics Stolen Memory
af800000-dfffffff : PCI Bus 0000:00
  af800000-af800fff : 0000:00:15.0
    af800000-af8001ff : lpss_dev
      af800000-af8001ff : i2c_designware.0 lpss_dev
    af800200-af8002ff : lpss_priv
    af800800-af800fff : idma64.0
      af800800-af800fff : idma64.0 idma64.0
  af801000-af801fff : 0000:00:15.1
    af801000-af8011ff : lpss_dev
      af801000-af8011ff : i2c_designware.1 lpss_dev
    af801200-af8012ff : lpss_priv
    af801800-af801fff : idma64.1
      af801800-af801fff : idma64.1 idma64.1
  af802000-af802fff : 0000:00:19.0
    af802000-af8021ff : lpss_dev
      af802000-af8021ff : i2c_designware.2 lpss_dev
    af802200-af8022ff : lpss_priv
  b0000000-bfffffff : 0000:00:02.0
  c0000000-c0ffffff : 0000:00:02.0
  c1000000-c11fffff : PCI Bus 0000:02
    c1000000-c11fffff : 0000:02:00.0
      c1000000-c11fffff : ath
  c1200000-c12fffff : 0000:00:1f.3
  c1300000-c13fffff : PCI Bus 0000:03
    c1300000-c1303fff : 0000:03:00.0
      c1300000-c1303fff : nvme
  c1400000-c14fffff : PCI Bus 0000:01
    c1400000-c1403fff : 0000:01:00.0
    c1404000-c1404fff : 0000:01:00.0
      c1404000-c1404fff : r8169
  c1500000-c150ffff : 0000:00:14.0
    c1500000-c150ffff : xhci-hcd
  c1510000-c1517fff : 0000:00:04.0
    c1510000-c1517fff : proc_thermal
  c1518000-c151bfff : 0000:00:1f.3
    c1518000-c151bfff : ICH HD audio
  c151c000-c151dfff : 0000:00:17.0
    c151c000-c151dfff : ahci
  c151e000-c151ffff : 0000:00:14.2
  c1520000-c15200ff : 0000:00:1f.4
  c1522000-c15227ff : 0000:00:17.0
    c1522000-c15227ff : ahci
  c1523000-c15230ff : 0000:00:17.0
    c1523000-c15230ff : ahci
  c1524000-c1524fff : 0000:00:16.0
    c1524000-c1524fff : mei_me
  c1527000-c1527fff : 0000:00:14.2
  c1528000-c1528fff : 0000:00:12.0
    c1528000-c1528fff : Intel PCH thermal driver
  c1529000-c1529fff : 0000:00:08.0
e0000000-efffffff : PCI ECAM 0000 [bus 00-ff]
  e0000000-efffffff : pnp 00:06
fc800000-fe7fffff : PCI Bus 0000:00
  fd000000-fd69ffff : pnp 00:07
  fd6a0000-fd6affff : INT34BB:00
    fd6a0000-fd6affff : INT34BB:00 INT34BB:00
  fd6b0000-fd6cffff : pnp 00:07
  fd6d0000-fd6dffff : INT34BB:00
    fd6d0000-fd6dffff : INT34BB:00 INT34BB:00
  fd6e0000-fd6effff : INT34BB:00
    fd6e0000-fd6effff : INT34BB:00 INT34BB:00
  fd6f0000-fdffffff : pnp 00:07
  fe000000-fe010fff : Reserved
    fe010000-fe010fff : 0000:00:1f.5
      fe010000-fe010fff : 0000:00:1f.5 0000:00:1f.5
  fe200000-fe7fffff : pnp 00:07
fec00000-fec00fff : Reserved
  fec00000-fec003ff : IOAPIC 0
fed00000-fed003ff : HPET 0
  fed00000-fed003ff : PNP0103:00
fed10000-fed17fff : pnp 00:06
fed18000-fed18fff : pnp 00:06
fed19000-fed19fff : pnp 00:06
fed20000-fed3ffff : pnp 00:06
fed40000-fed44fff : MSFT0101:00
  fed40000-fed44fff : MSFT0101:00
fed45000-fed8ffff : pnp 00:06
fed90000-fed90fff : dmar0
fed91000-fed91fff : dmar1
fee00000-fee00fff : Reserved
ff000000-ffffffff : pnp 00:07
100000000-44e7fffff : System RAM
  31d400000-31e9fffff : Kernel code
  31ea00000-31f7a1fff : Kernel rodata
  31f800000-31fc55b3f : Kernel data
  320164000-3205fffff : Kernel bss
44e800000-44fffffff : RAM buffer

```


<img width="443" height="304" alt="image" src="https://github.com/user-attachments/assets/45b68f87-e444-486f-9886-9d48ca0a12ca" />

<img width="973" height="677" alt="image" src="https://github.com/user-attachments/assets/4a417307-05ca-4e38-beef-9badf70ee673" />
<img width="531" height="621" alt="image" src="https://github.com/user-attachments/assets/8b5eb618-723b-46ab-978a-95b82f41a70b" />

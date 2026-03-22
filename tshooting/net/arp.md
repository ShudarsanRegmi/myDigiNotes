# ARP troubleshooting commands


## Checking if arp is working or not

```bash
sudo arping -I enp1s0 192.168.10.2
```


## Flushing arp entries
```bash
sudo ip neigh flush all
sudo ip neigh del 192.168.10.1 dev <interface> #flush specific interface
sudo arp -d 192.168.10.1 # for specific ip
```

## Setup tcpdump listener for arp requests
```bash
sudo tcpdump -i enp1s0 arp
```

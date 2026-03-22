# Setting up Peer To Peer Network Between Two devices

## Setting up Ip address

```bash
ip addr add 192.168.10.1/24 dev enp1s0
ip link set enp1s0 up
```

# Usnig nmcli
```bash
nmcli con mod enp1s0 ipv4.addresses 192.168.10.1/24
nmcli con mod enp1s0 ipv4.method manual
nmcli con up enp1s0
```

# Getting Ethernet link info
```bash
sudo ethtool enp1s0
```


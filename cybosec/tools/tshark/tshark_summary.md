# Using tshark for reading pcap files


## Reading a pcap file
```
tshark -r file.pcap
```

## Reading a pcap file without name resolution
```
tshark -nr file.pcap
```

# Using display filter
```
tshark -nr file.pcap -Y "frame contains pico"
```

# Linux Swap Space Inspection Commands

*A comprehensive reference for analyzing swap usage, processes, and system memory*

---

## 🔍 **Basic Swap Information**

### **Overall Memory & Swap Status**
```bash
# Quick memory and swap overview
free -h

# Detailed memory statistics
cat /proc/meminfo

# Memory info with specific swap details
cat /proc/meminfo | grep -E "(MemTotal|MemFree|MemAvailable|SwapTotal|SwapUsed|SwapFree)"
```

### **Swap Device Information**
```bash
# Show active swap devices and usage
swapon --show

# Alternative format
swapon -s

# More detailed swap information
cat /proc/swaps
```

---

## 📊 **Process-Level Swap Analysis**

### **Processes Using Swap (Most Important)**
```bash
# Find processes using swap with amounts
sudo grep -l '^VmSwap:' /proc/*/status 2>/dev/null | \
while read file; do 
    pid=$(echo $file | cut -d'/' -f3)
    comm=$(cat /proc/$pid/comm 2>/dev/null || echo "unknown")
    swap=$(grep '^VmSwap:' $file | awk '{print $2}')
    if [ "$swap" -gt 0 ] 2>/dev/null; then 
        echo "$pid $comm ${swap}kB"
    fi
done | sort -k3 -nr | head -20

# Alternative one-liner for top swap users
for file in /proc/*/status; do 
    if [ -r "$file" ]; then
        pid=$(basename $(dirname $file))
        name=$(grep '^Name:' $file | awk '{print $2}' 2>/dev/null)
        swap=$(grep '^VmSwap:' $file | awk '{print $2}' 2>/dev/null)
        if [ -n "$swap" ] && [ "$swap" -gt 0 ] 2>/dev/null; then
            printf "%s %s %d kB\n" $pid $name $swap
        fi
    fi
done | sort -k3 -nr | head -20
```

### **Memory Usage by Process**
```bash
# Processes sorted by memory usage
ps aux --sort=-%mem | head -20

# Processes with memory details
ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%mem | head -20

# Specific process memory details
ps -p <PID> -o pid,vsz,rss,pmem,comm

# Memory map for specific process
pmap -x <PID>
```

---

## 🎯 **Advanced Swap Analysis**

### **Per-Process Swap Details**
```bash
# Detailed memory info for specific process
cat /proc/<PID>/status | grep -E "(VmSize|VmRSS|VmSwap)"

# Memory maps showing swap
cat /proc/<PID>/smaps | grep -E "(Swap|Size|Rss)"

# Summary of process memory usage
cat /proc/<PID>/smaps_rollup
```

### **System-Wide Memory Pressure**
```bash
# Check memory pressure and OOM events
dmesg | grep -i "killed process"

# Current memory statistics
vmstat 1 5

# I/O statistics including swap
iostat -x 1 5

# System activity including swap
sar -r 1 5

# Memory and swap activity
sar -S 1 5
```

---

## ⚙️ **Swap Configuration Inspection**

### **Swap Settings**
```bash
# Swappiness setting (0-100, how aggressively to swap)
cat /proc/sys/vm/swappiness

# VFS cache pressure
cat /proc/sys/vm/vfs_cache_pressure

# Check all VM parameters
sysctl -a | grep vm

# Swap accounting (if enabled)
cat /sys/fs/cgroup/memory/memory.memsw.usage_in_bytes 2>/dev/null
```

### **Swap File/Partition Details**
```bash
# Swap file information
ls -lh /swapfile*

# Partition information
lsblk | grep SWAP

# Disk usage of swap files
du -h /swap*

# Swap file type and location
file /swapfile
```

---

## 🔧 **Interactive Monitoring Tools**

### **Real-time Monitoring**
```bash
# htop with memory/swap view (F6 to sort by memory)
htop

# top with memory focus
top -o %MEM

# Watch memory changes
watch -n 1 'free -h'

# Monitor specific process
watch -n 1 'ps -p <PID> -o pid,vsz,rss,pmem,comm'

# iotop for I/O including swap
sudo iotop -o

# System resource monitor
nmon
```

---

## 📈 **Swap Usage History & Trends**

### **Historical Data (if available)**
```bash
# System statistics (requires sysstat package)
sar -r -f /var/log/sysstat/saXX  # XX = day of month

# Swap activity history
sar -S -f /var/log/sysstat/saXX

# Memory pressure events
journalctl -u systemd-oomd

# System logs for memory issues
grep -i "swap\|memory\|oom" /var/log/syslog
```

---

## 🚀 **Quick Diagnostic Commands**

### **One-liners for Common Scenarios**
```bash
# Top 10 swap users with readable output
sudo awk '/^Pid/{pid=$2} /^VmSwap/ && $2>0 {printf "%s %s %d kB\n", pid, cmd, $2; cmd=""} /^Name/{cmd=$2}' /proc/*/status | sort -k3 -nr | head -10

# Memory hogs (RSS + Swap)
ps -eo pid,comm,rss --sort=-rss | head -20

# Quick swap status
echo "Swap: $(free -h | awk '/^Swap:/ {print $3"/"$2" ("int($3/$2*100)"%)"}') - Available RAM: $(free -h | awk '/^Mem:/ {print $7}')"

# Processes that could benefit from more RAM
ps -eo pid,comm,vsz,rss | awk '{if($3>$4*2) print $0}' | head -20
```

---

## 🎯 **Specific Use Cases**

### **Finding Memory Leaks**
```bash
# Monitor process memory over time
while true; do 
    echo "$(date): $(ps -p <PID> -o rss= 2>/dev/null || echo 'dead')" 
    sleep 60
done

# Watch for growing processes
ps -eo pid,comm,rss --sort=-rss | head -10 > /tmp/mem1
sleep 300
ps -eo pid,comm,rss --sort=-rss | head -10 > /tmp/mem2
diff /tmp/mem1 /tmp/mem2
```

### **Container/Cgroup Memory**
```bash
# Docker container memory (if applicable)
docker stats --no-stream

# Systemd service memory
systemctl status <service-name>

# Cgroup memory limits
cat /sys/fs/cgroup/memory/memory.limit_in_bytes
```

---

## ⚠️ **Important Notes**

### **Understanding Output**
- **VmSwap**: Virtual memory currently in swap
- **RSS**: Resident Set Size (physical memory)
- **VSZ**: Virtual Size (virtual memory)
- **%MEM**: Percentage of physical memory used

### **Permissions**
- Most swap inspection commands require `sudo` for detailed process info
- `/proc/*/status` and `/proc/*/smaps` may need elevated privileges

### **Performance Impact**
- Commands scanning all processes can be CPU-intensive
- Use sparingly on production systems under high load

---

## 📝 **Quick Reference Card**

| Purpose | Command |
|---------|---------|
| **Swap Overview** | `free -h` |
| **Swap Devices** | `swapon --show` |
| **Top Swap Users** | `sudo grep -l '^VmSwap:' /proc/*/status 2>/dev/null \| ...` |
| **Process Memory** | `ps aux --sort=-%mem \| head -20` |
| **Real-time Monitor** | `htop` |
| **Swappiness** | `cat /proc/sys/vm/swappiness` |
| **Memory Pressure** | `vmstat 1 5` |
| **Detailed Process** | `cat /proc/<PID>/status` |

---

*Save this reference for troubleshooting swap and memory issues on Linux systems*

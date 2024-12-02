Nmap (Network Mapper) is a powerful tool for network discovery and security auditing. It is widely used to identify live hosts, services, open ports, operating systems, and more on a network. Here's a breakdown of **Nmap basics to advanced usage**:

---

## **Basics**

### 1. **Installation**
- On Linux:  
  ```bash
  sudo apt install nmap   # For Debian/Ubuntu-based systems
  sudo yum install nmap   # For RHEL-based systems
  ```
- On Windows/Mac: Download from [nmap.org](https://nmap.org/download.html).

### 2. **Basic Scanning**
- **Ping Scan** (Identify live hosts):  
  ```bash
  nmap -sn <target>
  ```
  Example:  
  ```bash
  nmap -sn 192.168.1.0/24
  ```

- **Port Scan** (Scan specific ports):  
  ```bash
  nmap -p <port> <target>
  ```
  Example:  
  ```bash
  nmap -p 80 192.168.1.1
  ```

- **Scan all 65,535 ports**:  
  ```bash
  nmap -p- <target>
  ```

### 3. **Service and Version Detection**
Identify the services running on open ports and their versions:  
```bash
nmap -sV <target>
```

### 4. **Operating System Detection**
Discover the OS running on the target system:  
```bash
nmap -O <target>
```

### 5. **Combining Options**
Perform a comprehensive scan:  
```bash
nmap -A <target>
```
This includes OS detection, service version detection, script scanning, and traceroute.

---

## **Intermediate Usage**

### 6. **Scan Types**
- **TCP Connect Scan** (Default):  
  ```bash
  nmap -sT <target>
  ```
  Uses a full TCP connection.

- **SYN Scan** (Stealth Scan):  
  ```bash
  nmap -sS <target>
  ```
  Faster and less detectable.

- **UDP Scan**:  
  ```bash
  nmap -sU <target>
  ```
  Scans UDP ports (use with root privileges).

### 7. **Script Scanning**
Nmap has a scripting engine (NSE) for vulnerability detection, brute force attacks, etc.
- Use default scripts:  
  ```bash
  nmap -sC <target>
  ```
- Run a specific script:  
  ```bash
  nmap --script <script_name> <target>
  ```
  Example:  
  ```bash
  nmap --script http-enum 192.168.1.10
  ```

- Use script categories (e.g., `vuln`):  
  ```bash
  nmap --script=vuln <target>
  ```

### 8. **Timing Options**
Control the speed of your scan (1 is slowest, 5 is fastest):  
```bash
nmap -T<0-5> <target>
```
Example:  
```bash
nmap -T4 192.168.1.1
```

### 9. **Output Options**
Save results in different formats:
- Normal:  
  ```bash
  nmap -oN output.txt <target>
  ```
- XML:  
  ```bash
  nmap -oX output.xml <target>
  ```
- Grepable:  
  ```bash
  nmap -oG output.gnmap <target>
  ```

---

## **Advanced Usage**

### 10. **Firewall Evasion**
- Randomize scan order:  
  ```bash
  nmap --randomize-hosts <target>
  ```
- Spoof source IP:  
  ```bash
  nmap -S <fake_ip> <target>
  ```
- Use decoys:  
  ```bash
  nmap -D RND:10 <target>
  ```
  Creates multiple decoy IPs to confuse firewalls.

### 11. **Aggressive Scanning**
Aggressively detect services, OS, scripts, and traceroute:  
```bash
nmap -A -T4 <target>
```

### 12. **Vulnerability Scanning**
Run vulnerability checks using NSE scripts:  
```bash
nmap --script vuln <target>
```
Check for specific CVEs or vulnerabilities.

### 13. **IPv6 Scanning**
Scan IPv6 addresses:  
```bash
nmap -6 <target>
```

### 14. **Subnet Scanning**
Scan an entire subnet:  
```bash
nmap 192.168.1.0/24
```

### 15. **Exclude Hosts**
Exclude specific IPs or ranges from a scan:  
```bash
nmap --exclude <IP1>,<IP2> <target_range>
```

---

## **Practical Scenarios**

### 16. **Scanning a Range of IPs**
```bash
nmap 192.168.1.1-100
```

### 17. **Scanning the Top 100 Ports**
```bash
nmap --top-ports 100 <target>
```

### 18. **Discovering Open HTTP Services**
```bash
nmap -p 80 --open <target_range>
```

### 19. **Checking for SSL/TLS Configurations**
```bash
nmap --script ssl-enum-ciphers <target>
```

---

## **Tips and Tricks**

- Always ensure **permission** before scanning any network to avoid legal issues.
- Use `-v` or `-vv` for verbose output.
- Combine Nmap with other tools like Metasploit for penetration testing.
- Regularly update Nmap scripts for the latest vulnerabilities:  
  ```bash
  nmap --script-updatedb
  ```

---


Nmap is extremely useful in Capture The Flag (CTF) challenges, particularly in reconnaissance and information gathering. Here’s a curated list of **Nmap commands tailored for CTF scenarios**:

---

### **General Reconnaissance**
1. **Basic Port Scan**
   ```bash
   nmap -p- <target>
   ```
   - Scans all 65,535 ports to identify open ones.

2. **Service Version and OS Detection**
   ```bash
   nmap -sV -O <target>
   ```
   - Identifies running services, versions, and the target’s operating system.

3. **Aggressive Scan**
   ```bash
   nmap -A <target>
   ```
   - Combines OS detection, version detection, script scanning, and traceroute.

---

### **Common Scans in CTFs**
4. **Top 100 or 1000 Ports**
   ```bash
   nmap --top-ports 100 <target>
   ```
   - Scans the most commonly used 100 ports.

   ```bash
   nmap -F <target>
   ```
   - Scans the top 1000 ports faster.

5. **Find Open Ports**
   ```bash
   nmap --open <target>
   ```
   - Lists only open ports.

---

### **Scripting Engine (NSE)**
NSE scripts are particularly helpful for detecting vulnerabilities or gathering detailed information.

6. **Default Scripts**
   ```bash
   nmap -sC <target>
   ```
   - Runs default Nmap scripts for common services.

7. **Vulnerability Scanning**
   ```bash
   nmap --script vuln <target>
   ```
   - Checks for known vulnerabilities.

8. **SMB Enumeration**
   ```bash
   nmap --script smb-enum-shares,smb-enum-users -p 445 <target>
   ```
   - Useful for discovering shared files and user accounts on SMB.

9. **HTTP Enumeration**
   ```bash
   nmap --script http-title,http-methods,http-headers -p 80,443 <target>
   ```
   - Extracts HTTP service information like titles, headers, and allowed methods.

10. **FTP Enumeration**
    ```bash
    nmap --script ftp-anon,ftp-bounce -p 21 <target>
    ```
    - Detects anonymous login and FTP bounce vulnerability.

11. **DNS Zone Transfer**
    ```bash
    nmap --script dns-zone-transfer -p 53 <target>
    ```
    - Attempts a zone transfer to dump DNS records.

12. **SSL/TLS Vulnerabilities**
    ```bash
    nmap --script ssl-enum-ciphers -p 443 <target>
    ```
    - Checks for weak SSL/TLS configurations.

---

### **Bypassing Defenses**
13. **Use Decoys**
    ```bash
    nmap -D RND:5 <target>
    ```
    - Creates five random decoy IPs to mask your real source.

14. **Fragmented Packets**
    ```bash
    nmap -f <target>
    ```
    - Sends fragmented packets to evade simple packet-based firewalls.

15. **Spoof Source IP**
    ```bash
    nmap -S <fake_ip> <target>
    ```
    - Sends packets appearing to originate from a different IP.

16. **Randomize Port Scan Order**
    ```bash
    nmap --randomize-hosts <target>
    ```
    - Randomizes the scan sequence.

---

### **Specific Protocol Enumeration**
17. **Identify Open SSH**
    ```bash
    nmap -p 22 --script ssh2-enum-algos,ssh-hostkey <target>
    ```
    - Lists SSH algorithms and fingerprints.

18. **SNMP Enumeration**
    ```bash
    nmap --script snmp-brute,snmp-info -p 161 <target>
    ```
    - Enumerates SNMP information.

19. **MySQL Enumeration**
    ```bash
    nmap --script mysql-enum,mysql-databases -p 3306 <target>
    ```
    - Explores MySQL databases and user configurations.

20. **Enumerate RPC Services**
    ```bash
    nmap --script rpcinfo -p 111 <target>
    ```
    - Lists RPC services on the target.

---

### **Output Management**
21. **Save Results in Multiple Formats**
    ```bash
    nmap -oA output <target>
    ```
    - Saves in normal, XML, and Grepable formats (e.g., `output.nmap`, `output.xml`, `output.gnmap`).

22. **Readable Output**
    ```bash
    nmap -oN scan.txt <target>
    ```
    - Saves a human-readable summary in `scan.txt`.

---

### **Practical CTF Workflow**
1. Perform a quick scan to identify open ports:
   ```bash
   nmap -F --open <target>
   ```
2. Enumerate services with version detection:
   ```bash
   nmap -sV -p <ports> <target>
   ```
3. Run NSE scripts on detected services:
   ```bash
   nmap --script <script> -p <ports> <target>
   ```
4. Save detailed output for analysis:
   ```bash
   nmap -A -oN scan_results.txt <target>
   ```

---

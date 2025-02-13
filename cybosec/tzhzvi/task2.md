# Tasks 

1. **Domain -> Subdomains -> IP**  
   - Identify all subdomains of a given domain.  
   - Resolve each subdomain to its corresponding IP address.  

2. **For Each IP -> Ports**  
   - Perform a port scan on each resolved IP address to find open ports.  

3. **Domain -> SPF and DMARC Record**  
   - Check and analyze the SPF (Sender Policy Framework) record of the domain.  
   - Check and analyze the DMARC (Domain-based Message Authentication, Reporting & Conformance) record of the domain.  

---

### **Framing Problems Based on This Task**  

1. **Subdomain Enumeration & IP Resolution**  
   - Given a domain (e.g., `example.com`), list all subdomains associated with it.  
   - Resolve each subdomain to its respective IP address.  
   - Tools to explore: `subfinder`, `amass`, `crt.sh`, `dnsx`, `dig`, `host`, `nslookup`.  

2. **Port Scanning on Resolved IPs**  
   - Perform a port scan on all resolved IPs.  
   - Identify open services running on these ports.  
   - Tools to explore: `nmap`, `masscan`, `rustscan`.  

3. **SPF & DMARC Record Analysis**  
   - Retrieve and analyze the SPF record of a given domain.  
   - Retrieve and analyze the DMARC record of the domain.  
   - Understand how these records affect email security and spoofing prevention.  
   - Tools to explore: `dig`, `nslookup`, `mxtoolbox`, `spf-tools`, `dmarcian`.  

---

# Solutions

## Subdomain Enumeration

1. **Amass**
```bash
amass enum -d example.com
amass enum -d amrita.edu
```




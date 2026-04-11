## Random Practical Snapshots

**Checkig the SPF Record of gmail.com**
<img width="1220" height="443" alt="image" src="https://github.com/user-attachments/assets/c6fc1e8f-22ea-4b25-8277-e3a3252c4b9e" />

- found that gmail.com delegetaes spf records to different doamin `_spf.googel.com`

**Checking the txt record `_spf.google.com`**
<img width="1278" height="435" alt="image" src="https://github.com/user-attachments/assets/ec2316b4-7645-4d63-a73c-90b2af06eb9d" />
- found actual ip ranges which is allowed to send email from the behalf of gmail.com


**Checking the DMARC policy of gmail**
```bash
dig TXT _dmarc.gmail.com
```
![alt text](image.png)
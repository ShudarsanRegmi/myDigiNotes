# Static Analysis

## Lab - 1-1


### Questions

#### 1. Upload the files to http://www.VirusTotal.com/ and view the reports. Does either file match any existing antivirus signatures?

#### Answer
![image](https://github.com/user-attachments/assets/bc036828-a0bf-46c7-b506-e97560a48c7f)

> Yes, 58/73 vendors flagged .exe as malware
> Yes, 47/73 vendors flagged .dll as malware
 
---

#### 2. When were these files compiled

#### Answer
![image](https://github.com/user-attachments/assets/9ca62d2f-583e-4ac4-ad82-5eed46567150)
> Both of them were compiled on 19 December, 2010

---

#### 3. Is there any indicators that the files are packed of obfuscated?

#### Answer
![image](https://github.com/user-attachments/assets/1239a0ba-3018-4637-9ce7-b3c52b3aae6c)

> The file has well structured sections as well as standard imports. So, there is no sign of pack of obfuscation
---

#### 4. Do any imports hint at what this malware does? If so, which imports are they?

#### Answer
![image](https://github.com/user-attachments/assets/3acbc2c1-1b98-4b23-ae10-5d6629492aa3)
> The imports in kernel32 contains file operations realted functions. So, it must be looking scanning for files in the filesystem.
![image](https://github.com/user-attachments/assets/62d63889-0f63-4e4b-9dff-ccca33d0beca)
> The dll is likely to spawn a new process and sleep at some time
![image](https://github.com/user-attachments/assets/fe3cd348-374b-4b5f-8bbb-1322ef60b66b)
> The dll also ordinal imports, upon mapping they reveal functions from scoket programming showing that the malware is likely to make network connection
---

#### 1. Are there any other files or host-based indicators that you could look for on infected systems?

#### Answer
![image](https://github.com/user-attachments/assets/4582db61-be9e-4799-b600-7b37d1b9e7bb)
> because of this it is likely malicious and we are able to use this to search for infected systems.
---
#### 1. What network-based indicators could be used to find this malware on infected machines?

#### Answer
![image](https://github.com/user-attachments/assets/b3805c3e-409e-4d08-b8eb-6568380c1304)

> It must be connecting to the Command and Control Server

---
#### 7. What would you guess the purpose of these files

#### Answer

Based on everything we’ve enumerated above, we would guess that the executable is used to run the DLL which acts as a backdoor or remote access trojan (RAT). Based on the imports it’s possible the executable searches to see if C:\windows\system32\kerne132.dll exists, and if it doesn’t it may attempt to copy the malicious DLL to C:\windows\system32\kerne132.dll which is used for persistence. Upon executing the DLL, it likely contacts a C2 server at 127.26.152.13.

---

## Lab - 1-2

![image](https://github.com/user-attachments/assets/887ea115-33d7-4669-8b9d-8c87154797a7)

### Questions

#### 1. Upload the Lab01-02.exe file to http://www.VirusTotal.com/. Does it match any existing antivirus definitions?

#### Answer
![image](https://github.com/user-attachments/assets/6eabb091-762e-4925-ae71-4946afd84755)

> Yes, 60/73 vendors detects this file as malware

---

#### 2. Are there any indications that this file is packed or obfuscated? If so, what are these indicators? If the file is packed, unpack it if possible.

#### Answer
![image](https://github.com/user-attachments/assets/42179fbd-e899-4acd-891d-5e0ed09cb459)

> The file is not having standard sections like .text, .rdata, etc. Also sections like upx0, upx1, upx2, shows that the executable has been packed with UPX

**Unpacking it using upx tool**
![image](https://github.com/user-attachments/assets/1a3f5f99-c25a-4952-b889-e8260a15ff6b)
```
upx -d /path/to/packedfile -o unpackedfile.exe
```

---


#### 3. Do any imports hint at this program’s functionality? If so, which imports are they and what do they tell you?

#### Answer
![image](https://github.com/user-attachments/assets/502f4d24-ea49-4f4d-9611-77ee083d1d9f)

> InternetOpenA, InternetOpenUrlA connects to the internet and CreateServiceA creates a service
> It could be creating a process which will then be connecting to the internet. 

---

#### 4. What host- or network-based indicators could be used to identify this malware on infected machines?

#### Answer
![image](https://github.com/user-attachments/assets/37ec20f8-19b9-4c85-a6e4-978a0f2e36d4)

> Looking at the strings of this file shows 2 interesting elements, ‘malservice’ and ‘http://www.malwareanalysisbook.com’.
> Based on this we can assume that searching hosts for the scheduled service called ‘malservice’ and looking at any hosts connectiong to ‘http://www.malwareanalysisbook.com’ would serve as reliable host and network indicators.

---






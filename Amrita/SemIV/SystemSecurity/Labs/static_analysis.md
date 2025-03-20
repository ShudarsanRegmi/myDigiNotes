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




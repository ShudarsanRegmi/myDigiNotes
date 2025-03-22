![image](https://github.com/user-attachments/assets/d6a21f2a-9fe6-4f14-bd2d-aa3458e61928)# Static Analysis

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

## Lab 1-3

### Questions

#### 1. Upload the Lab01-03.exe file to http://www.VirusTotal.com/. Does it match any existing antivirus definitions?

#### Answer
![image](https://github.com/user-attachments/assets/2e67ee15-7700-492a-b001-0e79ff8e0eba)


> Yes, 67/73 vendors flagged the .exe as malware
 
---

#### 2. Are there any indications that this file is packed or obfuscated? If so, what are these indicators? If the file is packed, unpack it if possible.

#### Answer
![image](https://github.com/user-attachments/assets/e016f891-4671-4726-b5db-09c88809e247)
> PEStudio shows that the file has virtual size of 0x3000 but the raw size of 0x000. This is an indiciation of that the file might have been packed of obfuscated.

![image](https://github.com/user-attachments/assets/4373f725-4b0b-4f33-bd6c-b3e9e563b4d1)

> We can confirm it by using PEID tool which shows that the file is packed with FSG -> dulex/xt.  
 
---

#### 1. Upload the files to http://www.VirusTotal.com/ and view the reports. Does either file match any existing antivirus signatures?

#### Answer
![image](https://github.com/user-attachments/assets/cd33447c-f9d5-4fa9-a4bc-9311009e8140)


> At this point of time we can see only two functions being imported which is more coomon in packed file. For further information we've to unpack it.
 
---


## Lab 1-4

### Questions

![image](https://github.com/user-attachments/assets/c07608b7-b837-44be-9460-f48fa8885aa7)

#### 1. Upload the files to http://www.VirusTotal.com/ and view the reports. Does either file match any existing antivirus signatures?

#### Answer
![image](https://github.com/user-attachments/assets/c56b10c6-1227-433f-975b-98ce19e63411)


> Yes, 63/72 vendors flagged .exe as malware
 
---

#### 2. Are there any indications that this file is packed or obfuscated? If so, what are these indicators? If the file is packed, unpack it if possible.

#### Answer
![image](https://github.com/user-attachments/assets/0b155687-fe4c-4e85-8004-8aaa13258ac9)


> The file has cleary defined sections and headers. Also it has proper import table. This shows that the program is not packed or obfuscated.
 
---


#### 3. When was this program compiled?

#### Answer
![image](https://github.com/user-attachments/assets/db338dd8-38a9-422a-b8c6-a0545b7d7725)



> The compiled time as shown is: Aug 2019. But this might been faked too. 
 
---


#### 4. Do any imports hint about program functionality

#### Answer
![image](https://github.com/user-attachments/assets/86492ebf-54f7-4175-b2a8-6c277603872a)



> The files has imports for file operations but the imports like FindResourceA, LoadResourceA, winexec make it suspicious. Further imporing .exe from ResourceHacker makes it more suspicious. 

 ![image](https://github.com/user-attachments/assets/4d8376ab-f945-4a5d-9554-8d4f239a5b88)

 > The imports from Advapi32 indicate that this is attempting to modify or change the token assigned to the execution of this process, presumably to elevate privileges or give extended access rights.
---


#### 5. What host- or network-based indicators could be used to identify this malware on infected machines?

#### Answer
> Unexpectedly, the malware doesn't seem to have made any imports for network functions.

![image](https://github.com/user-attachments/assets/b25c9bbc-528e-4e64-ae4a-e5d5f9f47f00)
> But this resource is suspicous.

> If we  open the resource in resource hacker, we can find the executable. which was attached as a resource.

![image](https://github.com/user-attachments/assets/0b1a1eb0-7353-4d71-9098-5830ecc07fef)

> Also, the string tools also provides some network or host based indicuator
---


#### 6. This file has one resource in the resource section. Use Resource Hacker to examine that resource, and then use it to extract the resource. What can you learn from the resource?

#### Answer
![image](https://github.com/user-attachments/assets/59d84612-8a82-4e34-9e36-b9fdc6660795)

> The main executable had no imports for networking functions. All networking operations was being done by the attached resource. Also, the url in the strings suggests that the attached resource was downloading another malware for further exploitation.  
---

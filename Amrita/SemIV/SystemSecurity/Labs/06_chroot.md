# To create isolated environment in Linux using chroot 

## Task Level 1

### Create the directory setup
```bash
mkdir -p newroot/{bin,lib,lib64}
```

### Copy the required binaries
```bash
cp -v /bin/{bash,ls,cp} /newroot/bin
```

### Find the the dynamic dependencies for each of above binaries
```bash
ldd /bin/bash
ldd /bin/ls
ldd /bin/pwd
```
**Output**
```
ldd /bin/bash
	linux-vdso.so.1 (0x00007ffd8a7d8000) # no need to add this
	libtinfo.so.6 => /lib/x86_64-linux-gnu/libtinfo.so.6 (0x00007ec9dcddc000)
	libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007ec9dca00000)
	/lib64/ld-linux-x86-64.so.2 (0x00007ec9dcf8c000)

ldd /bin/ls
	linux-vdso.so.1 (0x00007ffe95355000)
	libselinux.so.1 => /lib/x86_64-linux-gnu/libselinux.so.1 (0x0000753a02ebd000)
	libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x0000753a02c00000)
	libpcre2-8.so.0 => /lib/x86_64-linux-gnu/libpcre2-8.so.0 (0x0000753a02b69000)
	/lib64/ld-linux-x86-64.so.2 (0x0000753a02f2a000)
```
![image](https://github.com/user-attachments/assets/394005db-f37c-4db7-81b9-77e465473db1)


### Copy all the respective files with proper directory structures
```bash
cp --parents  /lib/x86_64-linux-gnu/libselinux.so.1 newroot/
cp --parents /lib/x86_64-linux-gnu/libc.so.6 newroot/
# copy all the dependencies like this
```
![image](https://github.com/user-attachments/assets/53b6a109-a1f5-4b1d-996b-4bb3f7b9002c)

### Finally run the chroot command
```bash
sudo chroot newroot/ /bin/bash
```
**Output**
Gives the bash shell spawned
![image](https://github.com/user-attachments/assets/d29cf70b-3aad-4f60-82af-c1a6f7b2aa68)

## Task Level 2
---

## **🚀 Task: Create a Minimal Linux Environment with Networking inside `chroot`**
You will:
1. **Set up a `chroot` environment** (revision).
2. **Copy essential binaries and libraries** (revision).
3. **Enable networking inside `chroot`** using DNS resolution (new concept).
4. **Test internet access inside `chroot`** using `ping` or `curl`.

---

## **📌 Steps to Follow**
### **1️⃣ Create the `chroot` Environment**
```bash
mkdir -p newroot/{bin,lib,lib64,dev,proc,sys,etc}
```

### **2️⃣ Copy Essential Binaries**
Copy `bash`, `ls`, `rm`, `touch`, and also `ping` and `curl` (to test networking later):
```bash
cp /bin/bash newroot/bin/
cp /bin/ls newroot/bin/
cp /bin/rm newroot/bin/
cp /bin/touch newroot/bin/
cp /bin/ping newroot/bin/
cp /usr/bin/curl newroot/bin/
```

### **3️⃣ Copy Dependencies**
Find and copy dependencies for all binaries:
```bash
ldd /bin/bash /bin/ls /bin/rm /bin/touch /bin/ping /usr/bin/curl
```
For each required library, copy it to `newroot/lib/` or `newroot/lib64/`, for example:
```bash
cp --parents /lib/x86_64-linux-gnu/libc.so.6 newroot/
cp --parents /lib64/ld-linux-x86-64.so.2 newroot/
cp --parents /lib/x86_64-linux-gnu/libtinfo.so.6 newroot/
cp --parents /lib/x86_64-linux-gnu/libpcre2-8.so.0 newroot/
```
(Repeat this for all missing dependencies.)

### **4️⃣ Mount Required Filesystems**
These are required for networking and system stability inside `chroot`:
```bash
mount -o bind /dev newroot/dev
mount -o bind /proc newroot/proc
mount -o bind /sys newroot/sys
```

### **5️⃣ Enable DNS Resolution Inside `chroot`**
To access the internet from `chroot`, copy the system's `resolv.conf`:
```bash
cp /etc/resolv.conf newroot/etc/
```

### **6️⃣ Enter `chroot`**
Now, switch into the `chroot` environment:
```bash
sudo chroot newroot /bin/bash
```

### **7️⃣ Test Your Setup**
- Run:
  ```bash
  ls /
  ```
  You should only see `newroot` contents.
- Try networking:
  ```bash
  ping -c 4 google.com
  ```
  If it works, networking is enabled!
- Try `curl`:
  ```bash
  curl https://www.example.com
  ```
  If it works, DNS and internet access are functioning inside `chroot`.

### **8️⃣ Cleanup**
When you're done:
```bash
exit
umount newroot/dev
umount newroot/proc
umount newroot/sys
```

---

## **🎯 Expected Outcome**
1. You **revise `chroot`** setup.
2. You **understand networking inside `chroot`**.
3. You can **ping external servers** and fetch webpages inside `chroot`!

---

### **💡 Bonus Challenge**
- Try adding `apt` inside `chroot` and installing packages.
- Set up a user inside `chroot` and log in.

Would you like hints for the bonus challenge? 🚀

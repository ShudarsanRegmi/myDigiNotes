# Special permissions in Linux (SUID, SGID, sticky)


### **Understanding SUID, SGID, and the Sticky Bit in Linux**

In Linux, **file permissions** determine who can read, write, or execute a file or directory. However, there are three **special permission bits** that modify how execution or access is handled:  

1. **SUID (Set User ID)**
2. **SGID (Set Group ID)**
3. **Sticky Bit**  

These special bits are mainly used for **security and access control**. Let's dive into each in detail.

---

## **1. SUID (Set User ID)**
**SUID (Set User ID) is a special permission that allows a user to execute a file with the permissions of the file’s owner.**  
This is useful when a normal user needs to execute a program that requires **elevated privileges**, such as accessing hardware or modifying system files.

### **How It Works**
- Normally, when you execute a file, it runs with **your** privileges.
- If the **SUID bit** is set, the file runs with the **owner’s** privileges instead of the user’s.
- The owner is usually **root** for system binaries.

### **Example Use Case**
A classic example is the `/usr/bin/passwd` command, which allows users to change their passwords.

```bash
ls -l /usr/bin/passwd
```
Output:
```
-rwsr-xr-x 1 root root 54256 Feb  5  2024 /usr/bin/passwd
```
![image](https://github.com/user-attachments/assets/079a7a32-39ba-473d-a017-a7add4156160)


- The **`s`** in `rwsr-xr-x` means the SUID bit is set.
- The file is owned by **root**, but any user can execute it with **root privileges**.
- This allows non-root users to change their passwords, even though password files are system-protected.

### **Setting the SUID Bit**
You can set the **SUID** bit using the `chmod` command.

```bash
chmod u+s filename
```
Example:
```bash
chmod u+s myscript.sh
```
To remove it:
```bash
chmod u-s myscript.sh
```
![image](https://github.com/user-attachments/assets/45fe346b-1cdc-47e1-906e-cc4a7236f6bb)


### **Security Concerns**
- SUID can be a **security risk** if applied to insecure binaries.
- Attackers can exploit vulnerable SUID binaries to escalate privileges.

To find all SUID files on your system:
```bash
find / -perm -4000 -type f 2>/dev/null
```
![image](https://github.com/user-attachments/assets/90e82068-1cc1-419e-833e-4e03e3fc4b80)

---

## **2. SGID (Set Group ID)**
**SGID (Set Group ID) works similarly to SUID but for groups.**  
- When applied to **files**, it allows execution with the **group's** permissions.
- When applied to **directories**, it ensures that all newly created files **inherit the directory's group**.

### **SGID on Files**
Example: `/usr/bin/locate`
```bash
ls -l /usr/bin/locate
```
Output:
```
-rwx--s--x 1 root locate 43656 Feb  5  2024 /usr/bin/locate
```
- The **`s`** in `--s--x` indicates SGID is set.
- The file is owned by the **root** user but belongs to the `locate` group.
- Any user executing this file will run it with the **locate group’s** permissions.

### **Setting SGID on Files**
```bash
chmod g+s filename
```
Example:
```bash
chmod g+s myscript.sh
```
![image](https://github.com/user-attachments/assets/399aa636-e4ff-4531-a9bf-cf2966924d9c)

To remove it:
```bash
chmod g-s myscript.sh
```
![image](https://github.com/user-attachments/assets/7f0b3d36-f029-4bde-b5bf-32cae3332d8f)

### **SGID on Directories**
When SGID is set on a directory, **all new files created inside will inherit the directory's group**, rather than the creator's default group.

#### **Example Use Case**
A shared group directory where multiple users collaborate.

```bash
mkdir /shared
chmod 2775 /shared
chown :developers /shared
```
- The **2** in `2775` sets the **SGID bit**.
- Now, any file created in `/shared` will **inherit the group 'developers'**, ensuring consistent access.

### **Finding SGID Files**
```bash
find / -perm -2000 -type f 2>/dev/null
```

---

## **3. Sticky Bit**
The **Sticky Bit** is used **only on directories**.  
It ensures that **only the owner of a file (or root) can delete or modify it**, even if the directory is world-writable.

### **How It Works**
- Normally, in a world-writable directory (`/tmp`), **any user** can delete any file.
- If the **Sticky Bit** is set, only the file **owner** (or root) can delete it.

### **Example: `/tmp` Directory**
```bash
ls -ld /tmp
```
Output:
```
drwxrwxrwt 10 root root 4096 Feb  5  2024 /tmp
```
- The `t` in `rwxrwxrwt` indicates the **Sticky Bit is set**.
- This prevents users from deleting files that **they don’t own**.

### **Setting the Sticky Bit**
```bash
chmod +t directory_name
```
Example:
```bash
chmod +t /public
```
To remove it:
```bash
chmod -t /public
```
![image](https://github.com/user-attachments/assets/d4a84a8d-589c-4fae-bf86-54eba4c21ad5)


### **Finding Directories with Sticky Bit**
```bash
find / -perm -1000 -type d 2>/dev/null
```

---

## **Summary Table**

| Bit | Symbol | Applied To | Effect |
|------|--------|------------|--------|
| **SUID** | `s` (User) | Executable files | Runs with the **owner's** privileges instead of the user's. |
| **SGID** | `s` (Group) | Files & Directories | Files run with the **group's** permissions; directories inherit the group. |
| **Sticky Bit** | `t` | Directories | Prevents users from deleting files they don’t own. |

---

## **Practical Examples**

### **Example 1: Creating an SUID Program**
Let's create a simple **C program** that prints the `/etc/shadow` file (which stores encrypted passwords and is only readable by root).

#### **Step 1: Create the C File**
```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    system("cat /etc/shadow");
    return 0;
}
```

#### **Step 2: Compile and Set SUID**
```bash
gcc suid_example.c -o suid_example
chmod u+s suid_example
sudo chown root suid_example
```
Now, even if a **normal user** runs `./suid_example`, it will execute as **root**.

---

### **Example 2: Setting SGID on a Shared Directory**
If multiple users need access to a project folder:

```bash
sudo mkdir /project
sudo chown :developers /project
sudo chmod 2775 /project
```
- New files inside `/project` will inherit the **developers** group.

---

### **Example 3: Secure Temporary Directory with Sticky Bit**
To create a shared directory where users **cannot delete each other’s files**:

```bash
sudo mkdir /public
sudo chmod 1777 /public
```
Now, `/public` is writable by everyone, but users **can only delete their own files**.

---

## **Conclusion**
- **SUID** allows **privilege escalation** for executables (e.g., `passwd`).
- **SGID** is useful for **group collaboration** (e.g., shared directories).
- **Sticky Bit** is essential for **public directories** (e.g., `/tmp`).

Each of these **special permission bits** improves **security and usability** but must be **used carefully** to avoid security risks. Always audit **SUID/SGID binaries** and **restrict permissions** where necessary. 🚀

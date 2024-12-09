# Users and Group Management in Linux

Linux provides a variety of commands for managing users and groups. Below are the key commands categorized for better understanding:

---

### **User Management**

#### **1. Add a User**
- **Command:** `sudo adduser <username>`
- **Example:**  
  ```bash
  sudo adduser john
  ```
  Creates a user named `john` and sets up their home directory.

---

#### **2. Delete a User**
- **Command:** `sudo deluser <username>`
- **Example:**  
  ```bash
  sudo deluser john
  ```
  Deletes the user `john` but retains their home directory by default.

- To delete the user along with their home directory:
  ```bash
  sudo deluser --remove-home john
  ```

---

#### **3. Modify a User**
- **Command:** `sudo usermod [options] <username>`
- **Common Options:**
  - `-l <newname>`: Rename the user.
  - `-d <new_home>`: Change the home directory.
  - `-g <group>`: Change the user's primary group.
  - `-aG <group>`: Add the user to a secondary group.
  - `-s <shell>`: Change the login shell.
  
- **Example:**  
  ```bash
  sudo usermod -aG sudo john
  ```
  Adds `john` to the `sudo` group, granting administrative privileges.

---

#### **4. Lock/Unlock a User Account**
- **Lock Account:**  
  ```bash
  sudo passwd -l <username>
  ```
- **Unlock Account:**  
  ```bash
  sudo passwd -u <username>
  ```

---

### **Group Management**

#### **1. Add a Group**
- **Command:** `sudo addgroup <groupname>`
- **Example:**  
  ```bash
  sudo addgroup developers
  ```
  Creates a group named `developers`.

---

#### **2. Delete a Group**
- **Command:** `sudo delgroup <groupname>`
- **Example:**  
  ```bash
  sudo delgroup developers
  ```

---

#### **3. Add a User to a Group**
- **Command:** `sudo usermod -aG <group> <username>`
- **Example:**  
  ```bash
  sudo usermod -aG developers john
  ```
  Adds `john` to the `developers` group.

---

#### **4. List Groups**
- **Command:** `groups <username>`
- **Example:**  
  ```bash
  groups john
  ```
  Displays all groups `john` belongs to.

---

#### **5. List users associated with a particular group**
- **Command:** `getent group <groupname>`
- **Example:**  
  ```bash
  getent group sudo
  ```
Displays all users which belogs to `sudo` group

---

### **Password Management**

#### **1. Change Password**
- **Command:** `passwd <username>`
- **Example:**  
  ```bash
  sudo passwd john
  ```
  Changes the password for user `john`.

---

#### **2. Expire Password**
- Forces the user to change their password on next login.
- **Command:** `sudo passwd --expire <username>`
- **Example:**  
  ```bash
  sudo passwd --expire john
  ```

---

### **User Information**

#### **1. View User Details**
- **Command:** `id <username>`
- **Example:**  
  ```bash
  id john
  ```
  Displays the user ID (UID), group ID (GID), and associated groups.

---

#### **2. List All Users**
- **Command:**  
  ```bash
  cat /etc/passwd
  ```
  Displays all system and regular users.

---

#### **3. Check Currently Logged-in Users**
- **Command:** `who` or `w`
- **Example:**  
  ```bash
  who
  ```

---

### **System-wide Files to Know**
- **User Information:** `/etc/passwd`
- **Group Information:** `/etc/group`
- **User Passwords:** `/etc/shadow` (accessible only by root)

Let me know if you'd like explanations or examples for specific scenarios!

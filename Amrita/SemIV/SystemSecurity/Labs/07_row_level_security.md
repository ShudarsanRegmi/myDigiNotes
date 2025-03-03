Here is a **comprehensive tutorial** on implementing **Row-Level Security (RLS) in MySQL** from scratch. 🚀  

---

# **📌 Implementing Row-Level Security in MySQL**
## **🔍 Goal**
We want to store **all users' data in a single table** but **ensure that each user can only see, modify, or delete their own data**.  
To achieve this, we will:
- Use **a single `books` table** with an `owner` column.
- Restrict access using **MySQL Views**.
- Enforce ownership using **triggers**.

---

## **🛠 Step 1: Clean Up (If Needed)**
If you attempted this before, **delete any previous data**:
```sql
DROP DATABASE IF EXISTS rls_practice;
DROP USER IF EXISTS 'user1'@'localhost';
DROP USER IF EXISTS 'user2'@'localhost';
FLUSH PRIVILEGES;
```

---

## **📂 Step 2: Create a New Database**
```sql
CREATE DATABASE rls_practice;
USE rls_practice;
```

**Output**
![image](https://github.com/user-attachments/assets/020f7082-78ba-42fc-9bb6-6ec4d5d588d0)


---

## **📖 Step 3: Create the `books` Table**
This table stores all books **with an owner field** that records who inserted the book.
```sql
CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    owner VARCHAR(50) NOT NULL
);
```
**Output**
![image](https://github.com/user-attachments/assets/4c3ec69b-ada0-4c41-8b05-5306e04341ed)

---

## **🔑 Step 4: Create Users**
We will create **two users (`user1` and `user2`)**.

```sql
CREATE USER 'user1'@'localhost' IDENTIFIED BY 'password1';
CREATE USER 'user2'@'localhost' IDENTIFIED BY 'password2';
```
**Output**
![image](https://github.com/user-attachments/assets/9f5e167d-9917-46c7-b80c-eae4e1b679d6)

---

## **🎯 Step 5: Enforce Ownership Using a Trigger**
We create a **before-insert trigger** to **automatically store the username** when a book is inserted.

```sql
DELIMITER //
CREATE TRIGGER before_insert_books
BEFORE INSERT ON books
FOR EACH ROW
BEGIN
    SET NEW.owner = SESSION_USER(); -- Ensures the actual logged-in user is stored
END;
//
DELIMITER ;
```
```sql
DELIMITER ;
```

**Output**
![image](https://github.com/user-attachments/assets/efb8ab97-1c2d-40d0-9563-ed3866250e65)

```sql

DELIMITER //
CREATE TRIGGER before_update_books
BEFORE UPDATE ON books
FOR EACH ROW
BEGIN
    IF OLD.owner != CURRENT_USER() THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Unauthorized update!';
    END IF;
END;
//
DELIMITER ;
```
**Output**
![image](https://github.com/user-attachments/assets/1f83910e-0923-4487-ad43-416019145985)

---

## **🔍 Step 6: Create a View for Row-Level Security**
Since users should **only see their own books**, we create a **view** that filters by `owner`.

```sql
CREATE VIEW user_books AS
SELECT id, title, author FROM books WHERE owner = SESSION_USER();
```
**Output**
![image](https://github.com/user-attachments/assets/c4c38383-1dde-4716-a607-bf634b05fd4f)

---

## **🔐 Step 7: Grant Permissions to Users**
1. **Revoke direct table access** (so users cannot see everything).
```sql
REVOKE ALL PRIVILEGES ON books FROM 'user1'@'localhost';
REVOKE ALL PRIVILEGES ON books FROM 'user2'@'localhost';
```

2. **Grant access to the `user_books` view** (so they only see their data).
```sql
GRANT SELECT, INSERT, UPDATE, DELETE ON user_books TO 'user1'@'localhost';
GRANT SELECT, INSERT, UPDATE, DELETE ON user_books TO 'user2'@'localhost';
```
**Output**
![image](https://github.com/user-attachments/assets/0706b063-b427-4f1d-bf46-eabe6a5e86af)

3. **Allow inserting books** (users can insert, but ownership is handled by the trigger).
```sql
GRANT INSERT ON books TO 'user1'@'localhost';
GRANT INSERT ON books TO 'user2'@'localhost';
```
**Output**
![image](https://github.com/user-attachments/assets/d5fa2a52-3298-47ef-81f3-7efbd78b9685)

---

## **📌 Step 8: Testing**
### **Test as `user1`**
1️⃣ **Login as `user1`**  
```sh
mysql -u user1 -p
USE rls_practice;
```
2️⃣ **Insert a book**  
```sql
INSERT INTO books (title, author) VALUES ('User1 Book', 'Author A');
```
3️⃣ **Check books (should only see their own)**  
```sql
SELECT * FROM user_books;
```
✅ **Output should be:**
```
+----+------------+----------+
| id | title      | author   |
+----+------------+----------+
|  1 | User1 Book | Author A |
+----+------------+----------+
```

---

### **Test as `user2`**
1️⃣ **Login as `user2`**  
```sh
mysql -u user2 -p
USE rls_practice;
```
2️⃣ **Insert a book**  
```sql
INSERT INTO books (title, author) VALUES ('User2 Book', 'Author B');
```
3️⃣ **Check books (should only see their own)**  
```sql
SELECT * FROM user_books;
```
✅ **Output should be:**
```
+----+------------+----------+
| id | title      | author   |
+----+------------+----------+
|  2 | User2 Book | Author B |
+----+------------+----------+
```

---

## **🔎 Step 9: Verify Security**
Login as `user1` and try to access `user2`'s data:
```sql
SELECT * FROM books;
```
❌ **Access Denied!**  
✅ **Security is working!**

---

## **📌 Final Summary**
### **✅ What We Achieved**
✔ A **single table (`books`)** that stores all users' books.  
✔ Users **can only see their own data** (enforced via a `VIEW`).  
✔ **A trigger automatically assigns ownership** during insertion.  
✔ Users **cannot view/edit/delete books they do not own**.  

### **🚀 Next Steps**
- Try **more users** and see how the security holds up.  
- Expand to **multi-tenant applications**.  

Now, **row-level security in MySQL is fully implemented!** 🎯 🚀

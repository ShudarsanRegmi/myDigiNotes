# Elgamal Cryptosystem

# Key Generation


1. Step 1: Select a large prime number p <br>
2. Step 2: Select g = primitive root of p
3. Step 3: Calculate y = g^x mod p

Public Key = (p, g, y)

---

Encryption:
- Step 1: Select a random Integer `k`
- Step 2: c1 = y^k mod p
- Step 3: c2 = M.y^k mod p ( M  = message )

Cipher Text = (c1, c2)

--- 
Decryption:
Step 1: M = c2 / c1^x mod p ( M = decrypted )

--- 
Example:

![{1B024F58-0C5D-463E-863F-3E8E4A99DC4B}](https://github.com/user-attachments/assets/e2a16f10-b35d-4e9d-9c82-013c94eb5177)


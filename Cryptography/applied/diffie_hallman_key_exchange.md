# Diffie-Hellman KeyExchange

```python
# Example parameters (small values for simplicity, real values should be much larger)

def generator(g, x, p):
    return pow(g, x) % p

p = 23  # Prime number
g = 5   # Generator

# Alice's private key
a = 6
# Bob's private key
b = 15

# Alice's public key
A = generator(g, a, p)
# Bob's public key
B = generator(g, b, p)

# Shared secret key (computed by both parties independently)
shared_key_alice = generator(B, a, p)
shared_key_bob = generator(A, b, p)

print(shared_key_alice == shared_key_bob)  # Should be True

```
## How Diffie-Hellman Key Exchange is able to exchange keys over an insecure channel. 

### **Steps 1:** Agreeing on parameters
- Both parties agrees on large prime numbers p and a base g (also called as generator). The value need not be kept secret and can be known to anyone. 

### **Step 2:** Private Key Selection
 - Alice selects a private key 𝑎 a (a random number) which she keeps secret.
 - Bob selects a private key 𝑏 b (a random number) which he keeps secret.

### **Step 3:** Public Key Computation
 - Alice computes her public key A using the generator function: A = g^a mod p.
 - Bob computes his public key B using the generator function: B = g^b mod p. 

### **Step 4:** Public Key Exchange
 - Alice sends her public key A to Bob.
 - Bob sends his public key B to Alice.

**This Exchange can occur over an insecure channel because knowing the public keys A and B doesn't allow an attacker to easily determine the private keys a and b due to the hardness of discrete logarithm problem**

### **Step 5:** Shared Key Computation
- Alice receives Bob's public key B and computes the shared secret key s: s = B^a mod p
- Bob receives Alice's public key A and computes the shared secret key s: s = A^b mod p

  ![image](https://github.com/ShudarsanRegmi/myDigiNotes/assets/65646203/638b5087-e10f-4919-9c7c-0b23dc753198)

### Another Example

<img width="820" height="421" alt="image" src="https://github.com/user-attachments/assets/3dbe5454-ee2c-4f35-813d-d067093e1aee" />


### How it worked?
<img width="712" height="516" alt="image" src="https://github.com/user-attachments/assets/5c48749d-2343-4c19-b2ae-2d2f9ce7c090" />


# Some Important Functions Used in Cryptography

### dynamic_xor_encrypt(plain_text, key)
```python
def dynamic_xor_encrypt(plaintext, text_key):
    cipher_text = ""
    key_length = len(text_key)
    for i, char in enumerate(plaintext[::-1]): # reverse the flag and create a tuple with indexes 
        key_char = text_key[i % key_length]
        encrypted_char = chr(ord(char) ^ ord(key_char))
        cipher_text += encrypted_char
    return cipher_text
```
>The dynamic_xor_encrypt function encrypts a reversed plaintext string by applying a bitwise XOR operation between each character of the plaintext and the corresponding character of a repeating key.
```
plaintext = plain
key = key
cipher =  n^k + i^e + a^y + l^k + p^e
```

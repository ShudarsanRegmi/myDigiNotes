# DES (Data Encryption Standard)

## Fiestel Structure
![image](https://github.com/ShudarsanRegmi/myDigiNotes/assets/65646203/c05ccb13-6e44-41bf-903c-0fb492e787ec)

## Features of DES
- Symmetric Block Cipher
- Replaced by AES in early 2000s
- Input: 64 bits
- Output: 64 bits
- Main key: 64 bits
- Sub Key: 56 bits
- Round Key: 48 bits
- No. of rounds = 16 rounds

## Important Points
- Its short key length of 56 bits makes it too insecure for modern applicaitons, it has played a significant role in development of modern cryptography.
- Developed in the early 1970s at IBM and based on an earlier design by Horst Feistel

## Facts
- In January 1999, distributed.net and the Electronic Frontier Foundation collaborated to publicly break a DES key in 22 hours and 15 minutes
- The algorithm is believed to be practically secure in the form of Triple DES, although there are theoretical attacks.
- This cipher has been superseded by the Advanced Encryption Standard (AES). DES has been withdrawn as a standard by the National Institute of Standards and Technology.
- 
  ## Important points about its working
  - DES is the archetypal block cipher—an algorithm that takes a fixed-length string of plaintext bits and transforms it through a series of complicated operations into another ciphertext bitstring of the same length.
  - The key ostensibly consists of 64 bits; however, only 56 of these are actually used by the algorithm. Eight bits are used solely for checking parity, and are thereafter discarded. Hence the effective key length is 56 bits.
  - The key is nominally stored or transmitted as 8 bytes, each with odd parity.
  - One bit in each 8-bit byte of the KEY may be utilized for error detection in key generation, distribution, and storage. Bits 8, 16,..., 64 are for use in ensuring that each byte is of odd parity.
  - Like other block ciphers, DES by itself is not a secure means of encryption, but must instead be used in a mode of operation.
  - Decryption uses the same structure as encryption, but with the keys used in reverse order. (This has the advantage that the same hardware or software can be used in both directions.)
  - Sixteen 48-bit subkeys—one for each round—are derived from the main key using the key schedule
  -  The S-boxes provide the core of the security of DES—without them, the cipher would be linear, and trivially breakable.
  -  The alternation of substitution from the S-boxes, and permutation of bits from the P-box and E-expansion provides so-called "confusion and diffusion" respectively.

 ### Fiestatl Function
 ![image](https://github.com/ShudarsanRegmi/myDigiNotes/assets/65646203/893d1e1b-6e61-4e42-a756-194478ed015c)


![image](https://github.com/ShudarsanRegmi/myDigiNotes/assets/65646203/8c1084d7-a2ac-4559-b97b-5350ccd9f3b1)
![image](https://github.com/ShudarsanRegmi/myDigiNotes/assets/65646203/7804d2d3-3271-4f1f-a30e-834a0adf53b2)
![image](https://github.com/ShudarsanRegmi/myDigiNotes/assets/65646203/3c3fb42b-42d1-4d91-839e-43a1adb51110)
![image](https://github.com/ShudarsanRegmi/myDigiNotes/assets/65646203/62728df9-0e13-457f-a295-89270eff7a22)


### F functions
![image](https://github.com/ShudarsanRegmi/myDigiNotes/assets/65646203/8ed721f6-3114-4de4-91c1-6844a99e8351)

### S box
![image](https://github.com/ShudarsanRegmi/myDigiNotes/assets/65646203/152d906c-dbde-44bc-8014-52a2b77bb7ae)

 ### Permutation
 ![image](https://github.com/ShudarsanRegmi/myDigiNotes/assets/65646203/dad6e43a-b80d-403c-8b81-0317e20d024c)

### DES Decryption
![image](https://github.com/ShudarsanRegmi/myDigiNotes/assets/65646203/3d8858e7-722a-420b-85f5-1824ee7a5d54)

![image](https://github.com/ShudarsanRegmi/myDigiNotes/assets/65646203/7e801aaa-4835-48b8-8632-3e42e12fdd66)
![image](https://github.com/ShudarsanRegmi/myDigiNotes/assets/65646203/f9a78e29-32c0-40e6-b1f9-273f786091e7)
![image](https://github.com/ShudarsanRegmi/myDigiNotes/assets/65646203/1510da5b-a833-49b4-bd97-b822bc3b03e3)

### Security And Cryptanalysis
Although more information has been published on the cryptanalysis of DES than any other block cipher, the most practical attack to date is still a brute-force approach. Various minor cryptanalytic properties are known, and three theoretical attacks are possible which, while having a theoretical complexity less than a brute-force attack, require an unrealistic number of known or chosen plaintexts to carry out, and are not a concern in practice.


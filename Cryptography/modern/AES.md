# AES - Advance Encryption Standard

## Introduction

- The Advanced Encryption Standard (AES), also known by its original name Rijndael (Dutch pronunciation: [ˈrɛindaːl]) is a specification for the encryption of electronic data established by the U.S. National Institute of Standards and Technology (NIST) in 2001.
- The algorithm described by AES is a symmetric-key algorithm, meaning the same key is used for both encrypting and decrypting the data.
-  AES is a variant of Rijndael, with a fixed block size of 128 bits, and a key size of 128, 192, or 256 bits.

## Description of the cipher
- AES is based on a design principle known as a substitution–permutation network, and is efficient in both software and hardware.
- AES operates on a 4 × 4 column-major order array of 16 bytes b0, b1, ..., b15 termed the state.
- ![image](https://github.com/ShudarsanRegmi/myDigiNotes/assets/65646203/f7bff3fb-bf3c-49b8-9304-8317346a13e1)
- 
- The key size used for an AES cipher specifies the number of transformation rounds that convert the input, called the plaintext, into the final output, called the ciphertext. The number of rounds are as follows:
  - 10 rounds for 128-bit keys.
  - 12 rounds for 192-bit keys.
  - 14 rounds for 256-bit keys
- Each round consists of several processing steps, including one that depends on the encryption key itself. A set of reverse rounds are applied to transform ciphertext back into the original plaintext using the same encryption key.

## High level description of the algorithm
1. **KeyExpansion** – round keys are derived from the cipher key using the AES key schedule. AES requires a separate 128-bit round key block for each round plus one more.

2. **Initial round key addition:**
   1. **AddRoundKey** – each byte of the state is combined with a byte of the round key using bitwise XOR.

3. **9, 11 or 13 rounds:**
   1. **SubBytes** – a non-linear substitution step where each byte is replaced with another according to a lookup table.
   2. **ShiftRows** – a transposition step where the last three rows of the state are shifted cyclically a certain number of steps.
   3. **MixColumns** – a linear mixing operation which operates on the columns of the state, combining the four bytes in each column.
   4. **AddRoundKey**

4. **Final round (making 10, 12 or 14 rounds in total):**
   1. **SubBytes**
   2. **ShiftRows**
   3. **AddRoundKey**

## The sub bytes step
In the SubBytes step, each byte 𝑎 𝑖 , 𝑗 {\displaystyle a_{i,j}} in the state array is replaced with a SubByte 𝑆 ( 𝑎 𝑖 , 𝑗 ) {\displaystyle S(a_{i,j})} using an 8-bit substitution box.
![image](https://github.com/ShudarsanRegmi/myDigiNotes/assets/65646203/f7f649c9-8d1c-48f3-ad26-960d1355d96a)
o avoid attacks based on simple algebraic properties, the S-box is constructed by combining the inverse function with an invertible affine transformation.

## The Shift rows step
The ShiftRows step operates on the rows of the state; it cyclically shifts the bytes in each row by a certain offset. For AES, the first row is left unchanged. Each byte of the second row is shifted one to the left. Similarly, the third and fourth rows are shifted by offsets of two and three respectively. The importance of this step is to avoid the columns being encrypted independently, in which case AES would degenerate into four independent block ciphers.

![image](https://github.com/ShudarsanRegmi/myDigiNotes/assets/65646203/e6e53e2f-b0fd-4c2d-b8c6-59d6ce698e98)

## Mix Columns step
- In the MixColumns step, the four bytes of each column of the state are combined using an invertible linear transformation. The MixColumns function takes four bytes as input and outputs four bytes, where each input byte affects all four output bytes. Together with ShiftRows, MixColumns provides diffusion in the cipher.
- During this operation, each column is transformed using a fixed matrix (matrix left-multiplied by column gives new value of column in the state)

  ![image](https://github.com/ShudarsanRegmi/myDigiNotes/assets/65646203/1d291a8d-0484-4a1b-8818-f5c889f22139)
  ![image](https://github.com/ShudarsanRegmi/myDigiNotes/assets/65646203/ccdd08ac-e090-49d3-8705-601d6517d987)

## Add Round Key step
In the AddRoundKey step, the subkey is combined with the state. For each round, a subkey is derived from the main key using Rijndael's key schedule; each subkey is the same size as the state. The subkey is added by combining of the state with the corresponding byte of the subkey using bitwise XOR.
![image](https://github.com/ShudarsanRegmi/myDigiNotes/assets/65646203/0ed8c702-ef66-465e-85ec-777818716ce5)

## AES S-box
![image](https://github.com/ShudarsanRegmi/myDigiNotes/assets/65646203/a5fc0335-236c-44bf-bc5f-7c8c6a8123e3)

## Other reading materials
- https://braincoke.fr/blog/2020/08/the-aes-key-schedule-explained/#conclusion

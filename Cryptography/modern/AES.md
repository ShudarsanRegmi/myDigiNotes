# AES - Advance Encryption Standard

## Introduction

- The Advanced Encryption Standard (AES), also known by its original name Rijndael (Dutch pronunciation: [ˈrɛindaːl]) is a specification for the encryption of electronic data established by the U.S. National Institute of Standards and Technology (NIST) in 2001.
- The algorithm described by AES is a symmetric-key algorithm, meaning the same key is used for both encrypting and decrypting the data.
-  AES is a variant of Rijndael, with a fixed block size of 128 bits, and a key size of 128, 192, or 256 bits.

## Description of the cipher
- AES is based on a design principle known as a substitution–permutation network, and is efficient in both software and hardware.
- AES operates on a 4 × 4 column-major order array of 16 bytes b0, b1, ..., b15 termed the state.
  ![image](https://github.com/ShudarsanRegmi/myDigiNotes/assets/65646203/ba19b198-590c-4b4a-be7c-01ee32062a71)
The key size used for an AES cipher specifies the number of transformation rounds that convert the input, called the plaintext, into the final output, called the ciphertext. The number of rounds are as follows:
  - 10 rounds for 128-bit keys.
  - 12 rounds for 192-bit keys.
  - 14 rounds for 256-bit keys
- Each round consists of several processing steps, including one that depends on the encryption key itself. A set of reverse rounds are applied to transform ciphertext back into the original plaintext using the same encryption key.

## High level description of the algorithm

**1. KeyExpansion** – round keys are derived from the cipher key using the AES key schedule. AES requires a separate 128-bit round key block for each round plus one more.

**2. Initial round key addition:**
  1. **AddRoundKey** – each byte of the state is combined with a byte of the round key using bitwise xor.
**3. 9, 11 or 13 rounds:**
  **1. SubBytes** – a non-linear substitution step where each byte is replaced with another according to a lookup table.
  **2. ShiftRows** – a transposition step where the last three rows of the state are shifted cyclically a certain number of steps.
  **3. MixColumns** – a linear mixing operation which operates on the columns of the state, combining the four bytes in each column.
  4, **AddRoundKey**
**4. Final round (making 10, 12 or 14 rounds in total):**
  1. SubBytes
  2. ShiftRows
  3. AddRoundKey

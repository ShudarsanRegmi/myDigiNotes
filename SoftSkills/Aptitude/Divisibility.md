# Notes on divisibility

- for a number to be divisible by 2^n, last n digits of the dividend should be divisible by n
- for a number to be divisible by 3, the sum of its digit should be divisible by 3
- for 5, last digit should be 5 or 0
- for 6, the number should be divisible by 2 and 3
- for 7,  (digits preceding 1 - 2 * unit_digit) should be multiple of 7 or 0 (recursively)
- for 13, (digits preceding last digit + 4*last_digit) should be multiple of 13 (recursive)

# No. of Divisors = product of (degree+1) of each prime factors
Eg. = 1728 = (2^6)*3^3 
==> (6+1) * (3+1)

# Sum of Divisors 
E.g. 544 = 2^5 * 17
Sum. of Divisors = (2^0 + 2^1 + 2^2 + 2^3 + 2^4 + 2^5) * (17^0 + 17^1)
Formula = (P1^(n+1) -1) / (p1 - 1) * (P2^(n+1) -1) / (p2 - 1) * (Pn^(n+1) -1) / (pn - 1)


![{57E2A8D8-2D9C-4ED5-9E64-32BC15B5BAF8}](https://github.com/user-attachments/assets/232424e9-5ed7-4a3f-88e6-01ad4f4ab278)





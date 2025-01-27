# Web Exploitation Tools

- BurpSuite
- [Jwt Tools](https://jwt.io/#debugger-io)
- [Jwt Cracker](https://github.com/lmammino/jwt-cracker)


## Cracking Weak JWTs using jwt-cracker

**Bruteforcing with wordlist**
```bash
jwt-cracker -t <jwt_token> -d word_list.txt
```

**Bruteforcing with charset**
```bash
jwt-cracker -t <jwt_token> -a abcdefghijklmnopqrstuwxyz --max 6
```



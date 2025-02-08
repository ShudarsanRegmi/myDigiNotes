# Cracking Weak JWT tokens


```bash
jwt-cracker -t <token> [-a <alphabet>] [--max <maxLength>] [-d <dictionaryFilePath>] [-f]
```

### Brute forcing Using dictinoary
```bash
jwt-cracker -t eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWV9.TJVA95OrM7E2cBab30RMHrHDcEfxjoYZgeFONFh7HgQ -d darkweb2017-top10000.txt
```

### RS256 vs HS256
- Two most common algorithms used to sign JWTs are the asymmetrical RS256 algorithm and the symmetrical HS256.

- HS256 uses a single secret to both create and verify the signature
- RS256 uses a public/private key pair — private key for signing the token and the public key for verification.

>Note: Jwt uses base64 urlencode instead of base64

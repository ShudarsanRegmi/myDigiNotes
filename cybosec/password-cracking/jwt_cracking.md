# Cracking Weak JWT tokens


```bash
jwt-cracker -t <token> [-a <alphabet>] [--max <maxLength>] [-d <dictionaryFilePath>] [-f]
```

### Brute forcing Using dictinoary
```bash
jwt-cracker -t eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWV9.TJVA95OrM7E2cBab30RMHrHDcEfxjoYZgeFONFh7HgQ -d darkweb2017-top10000.txt
```

>Note: Jwt uses base64 urlencode instead of base64

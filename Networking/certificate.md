
<img width="934" height="472" alt="image" src="https://github.com/user-attachments/assets/7319d909-7f15-4ba5-9ff6-c52c3039e298" />

<img width="542" height="621" alt="image" src="https://github.com/user-attachments/assets/30999cca-4004-4279-83be-8c563eb93e8c" />

<img width="1225" height="199" alt="image" src="https://github.com/user-attachments/assets/bdeb5d76-697a-4683-a3c7-4a102e7ccb0d" />


Short answer:

* **Certificate fingerprint (SHA-256 of whole cert):**
  Used for human-readable identification, logging, or manual comparison of certificates. It is **not part of the TLS certificate validation process**.

* **Public key fingerprint (SPKI fingerprint):**
  Used in **certificate/key pinning** (e.g., HPKP, mobile apps, browsers) to bind trust directly to the key, even if the cert itself changes. This plays a role in **strengthening trust**, but again, it’s not required in the standard CA-based validation.

So: browsers show them for **diagnostics and pinning**, but **normal certificate validation doesn’t depend on them**.


## Read the binary pem certificae usign openssl
```bash
openssl x509 -in shudarsanregmi.com.np -text -noout
```

<img width="827" height="583" alt="image" src="https://github.com/user-attachments/assets/e3d1d11b-d8d3-457f-8d51-b49d8253f6ed" />

```
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number:
            72:83:d3:42:db:c0:94:e5:0e:62:2f:f9:a2:df:29:19
        Signature Algorithm: ecdsa-with-SHA256
        Issuer: C = US, O = Google Trust Services, CN = WE1
        Validity
            Not Before: Sep 23 11:36:05 2025 GMT
            Not After : Dec 22 12:33:12 2025 GMT
        Subject: CN = shudarsanregmi.com.np
        Subject Public Key Info:
            Public Key Algorithm: id-ecPublicKey
                Public-Key: (256 bit)
                pub:
                    04:18:81:f1:68:7d:11:b0:28:5a:01:f4:ab:b0:79:
                    62:90:39:fa:61:f2:e6:9c:f1:18:8b:13:c4:1d:63:
                    7e:d2:bc:0b:06:12:ea:48:b7:7d:45:ee:56:4d:40:
                    46:af:b5:61:ca:b6:89:c7:ff:dc:1d:56:f1:49:46:
                    c4:70:d6:b9:9f
                ASN1 OID: prime256v1
                NIST CURVE: P-256
        X509v3 extensions:
            X509v3 Key Usage: critical
                Digital Signature
            X509v3 Extended Key Usage: 
                TLS Web Server Authentication
            X509v3 Basic Constraints: critical
                CA:FALSE
            X509v3 Subject Key Identifier: 
                1C:1B:B1:F3:88:6B:76:82:C5:D7:15:2D:C5:38:E2:98:F1:B3:73:1B
            X509v3 Authority Key Identifier: 
                90:77:92:35:67:C4:FF:A8:CC:A9:E6:7B:D9:80:79:7B:CC:93:F9:38
            Authority Information Access: 
                OCSP - URI:http://o.pki.goog/s/we1/coM
                CA Issuers - URI:http://i.pki.goog/we1.crt
            X509v3 Subject Alternative Name: 
                DNS:shudarsanregmi.com.np, DNS:*.shudarsanregmi.com.np
            X509v3 Certificate Policies: 
                Policy: 2.23.140.1.2.1
            X509v3 CRL Distribution Points: 
                Full Name:
                  URI:http://c.pki.goog/we1/T58q3x0jyXI.crl
            CT Precertificate SCTs: 
                Signed Certificate Timestamp:
                    Version   : v1 (0x0)
                    Log ID    : CC:FB:0F:6A:85:71:09:65:FE:95:9B:53:CE:E9:B2:7C:
                                22:E9:85:5C:0D:97:8D:B6:A9:7E:54:C0:FE:4C:0D:B0
                    Timestamp : Sep 23 12:36:06.267 2025 GMT
                    Extensions: none
                    Signature : ecdsa-with-SHA256
                                30:46:02:21:00:F1:9D:2D:93:E6:55:E6:F1:07:81:A2:
                                FF:3E:65:EC:54:6E:06:D0:BF:8F:E4:B5:F5:23:DA:FB:
                                DF:BF:2D:3B:FF:02:21:00:95:6B:EB:27:AF:D1:90:6B:
                                A1:DC:E8:DF:FD:05:81:88:C7:29:15:7F:37:93:2C:11:
                                98:4E:C1:2D:86:D6:D8:B6
                Signed Certificate Timestamp:
                    Version   : v1 (0x0)
                    Log ID    : DD:DC:CA:34:95:D7:E1:16:05:E7:95:32:FA:C7:9F:F8:
                                3D:1C:50:DF:DB:00:3A:14:12:76:0A:2C:AC:BB:C8:2A
                    Timestamp : Sep 23 12:36:06.081 2025 GMT
                    Extensions: none
                    Signature : ecdsa-with-SHA256
                                30:45:02:20:2B:E7:A1:7B:11:52:4F:1E:8D:45:27:03:
                                ED:2D:3E:A9:25:B5:D2:AA:9F:12:99:E6:EF:EA:E1:5D:
                                EB:61:FB:1E:02:21:00:F4:BC:03:4D:79:EF:49:E2:E2:
                                7E:0D:80:0F:9E:D6:5D:33:1E:82:35:1B:52:F0:6D:07:
                                1B:F2:89:8F:18:5A:34
    Signature Algorithm: ecdsa-with-SHA256
    Signature Value:
        30:45:02:20:2d:51:cb:10:87:12:b7:e1:6b:72:fb:59:de:2e:
        0c:19:fa:f1:48:ae:f9:98:70:d7:ef:e4:b9:33:a3:e7:a9:8e:
        02:21:00:e5:80:cc:f2:1b:5b:f3:5a:ab:4d:8c:2f:34:57:48:
        1f:d4:7e:31:3e:ce:9f:d6:ab:30:92:a4:fa:cf:93:db:39

```

**Generate Certificate Fingerprint**
```bash
openssl x509 -in cert.pem -noout -fingerprint -sha256
```

**Generate the fingerprint of public key**
```bash
# Extract public key
openssl x509 -in cert.pem -pubkey -noout > pubkey.pem

# Hash it (SHA-256)
openssl pkey -pubin -in pubkey.pem -outform DER | openssl dgst -sha256
```

### Validation

<img width="544" height="320" alt="image" src="https://github.com/user-attachments/assets/f6e8bfb2-d531-4e24-8eff-dd1f73ebd6fa" />


## Capture the http traffic
```
TARGET=example.com; SPORT=56001; OUT=curl.pcap; sudo tcpdump -i any -w "$OUT" "tcp and port $SPORT" & TPID=$!; sleep 0.2; curl --local-port "$SPORT" -v "http://$TARGET"; sleep 0.5; sudo kill "$TPID" || true; echo "saved: $OUT"
```
<img width="1515" height="245" alt="image" src="https://github.com/user-attachments/assets/9ccb8e28-03c9-4d8c-9d63-5b22c690b47e" />

1. **SYN** → Client starts TCP handshake.
2. **SYN, ACK** ← Server replies.
3. **ACK** → Client completes handshake.
4. **HTTP GET /** → Client requests page.
5. **ACK (pure)** ← Server acknowledges GET.
6. **ACK + HTTP/1.1 200 OK + data** ← Server acknowledges GET and piggybacks the first chunk of response (headers + body, ~1520 bytes).
7. **ACK (pure)** → Client acknowledges receipt of server’s first response segment.
8. **ACK + HTTP/1.1 200 OK (continued data)** ← Server sends remaining HTTP response payload (the tail end of the HTML).
9. **ACK (pure)** → Client acknowledges the final HTTP response bytes.
10. **FIN, ACK** → Client closes the connection.

**6th Packet**
<img width="1057" height="575" alt="image" src="https://github.com/user-attachments/assets/b6b7c8c1-7b37-4ef2-a753-a7cfe9fdd83e" />

**8th Packet**
<img width="1086" height="612" alt="image" src="https://github.com/user-attachments/assets/f9468cd8-5bb2-4ee6-9a8e-4a0a4aaac02f" />


## Capture the https traffic to example.com

```
TARGET=example.com; SPORT=56000; OUT=curl.pcap; sudo tcpdump -i any -w "$OUT" "tcp and port $SPORT" & TPID=$!; sleep 0.2; curl --local-port "$SPORT" -v "http://$TARGET"; sleep 0.5; sudo kill "$TPID" || true; echo "saved: $OUT"
```

<img width="1961" height="248" alt="image" src="https://github.com/user-attachments/assets/c53fdec9-4f7b-40b5-94f6-bce1de797d86" />


**TLS Client Hello**
<img width="971" height="751" alt="image" src="https://github.com/user-attachments/assets/f33fb528-e250-4495-abfd-98021d3fe3e6" />


```
Linux cooked capture v2
Internet Protocol Version 4, Src: 11.12.78.143, Dst: 23.192.228.80
Transmission Control Protocol, Src Port: 56003, Dst Port: 443, Seq: 1, Ack: 1, Len: 517
Transport Layer Security
    TLSv1.3 Record Layer: Handshake Protocol: Client Hello
        Content Type: Handshake (22)
        Version: TLS 1.0 (0x0301)
        Length: 512
        Handshake Protocol: Client Hello
            Handshake Type: Client Hello (1)
            Length: 508
            Version: TLS 1.2 (0x0303)
            Random: 27b0fc3a3299752bb48c00a64885daa3fe5acf47827a1fbc153f6808debfaa4f
            Session ID Length: 32
            Session ID: c3ffb3a947bd29cb6b837a07d6b2854f3cdfc865cc184032aa5c9f25e1208aa8
            Cipher Suites Length: 62
            Cipher Suites (31 suites)
            Compression Methods Length: 1
            Compression Methods (1 method)
            Extensions Length: 373
            Extension: server_name (len=16)
            Extension: ec_point_formats (len=4)
            Extension: supported_groups (len=22)
            Extension: next_protocol_negotiation (len=0)
            Extension: application_layer_protocol_negotiation (len=14)
            Extension: encrypt_then_mac (len=0)
            Extension: extended_master_secret (len=0)
            Extension: post_handshake_auth (len=0)
            Extension: signature_algorithms (len=42)
                Type: signature_algorithms (13)
                Length: 42
                Signature Hash Algorithms Length: 40
                Signature Hash Algorithms (20 algorithms)
                    Signature Algorithm: ecdsa_secp256r1_sha256 (0x0403)
                    Signature Algorithm: ecdsa_secp384r1_sha384 (0x0503)
                    Signature Algorithm: ecdsa_secp521r1_sha512 (0x0603)
                    Signature Algorithm: ed25519 (0x0807)
                    Signature Algorithm: ed448 (0x0808)
                    Signature Algorithm: rsa_pss_pss_sha256 (0x0809)
                    Signature Algorithm: rsa_pss_pss_sha384 (0x080a)
                    Signature Algorithm: rsa_pss_pss_sha512 (0x080b)
                    Signature Algorithm: rsa_pss_rsae_sha256 (0x0804)
                    Signature Algorithm: rsa_pss_rsae_sha384 (0x0805)
                    Signature Algorithm: rsa_pss_rsae_sha512 (0x0806)
                    Signature Algorithm: rsa_pkcs1_sha256 (0x0401)
                    Signature Algorithm: rsa_pkcs1_sha384 (0x0501)
                    Signature Algorithm: rsa_pkcs1_sha512 (0x0601)
                    Signature Algorithm: SHA224 ECDSA (0x0303)
                    Signature Algorithm: SHA224 RSA (0x0301)
                    Signature Algorithm: SHA224 DSA (0x0302)
                    Signature Algorithm: SHA256 DSA (0x0402)
                    Signature Algorithm: SHA384 DSA (0x0502)
                    Signature Algorithm: SHA512 DSA (0x0602)
            Extension: supported_versions (len=5)
            Extension: psk_key_exchange_modes (len=2)
            Extension: key_share (len=38)
            Extension: padding (len=178)
            [JA3 Fullstring [truncated]: 771,4866-4867-4865-49196-49200-159-52393-52392-52394-49195-49199-158-49188-49192-107-49187-49191-103-49162-49172-57-49161-49171-51-157-156-61-60-53-47-255,0-11-10-13172-16-22-23-49-13-43-45-51-21,29-23-30-25-24]
            [JA3: 4ea056e63b7910cbf543f0c095064dfe]
```

<img width="988" height="497" alt="image" src="https://github.com/user-attachments/assets/7ff6b426-ba69-4a2f-ae8f-348994370921" />

**Server Hello Msg**

```
Frame 5: 2802 bytes on wire (22416 bits), 2802 bytes captured (22416 bits)
Linux cooked capture v2
Internet Protocol Version 4, Src: 23.192.228.80, Dst: 11.12.78.143
Transmission Control Protocol, Src Port: 443, Dst Port: 56003, Seq: 1, Ack: 518, Len: 2730
Transport Layer Security
    TLSv1.3 Record Layer: Handshake Protocol: Server Hello
        Content Type: Handshake (22)
        Version: TLS 1.2 (0x0303)
        Length: 122
        Handshake Protocol: Server Hello
            Handshake Type: Server Hello (2)
            Length: 118
            Version: TLS 1.2 (0x0303)
            Random: 72f19d08ebd63dcccaaa0dd3efb25ab8a0f43951ad4912e9c1a5deb15f25e6ef
            Session ID Length: 32
            Session ID: c3ffb3a947bd29cb6b837a07d6b2854f3cdfc865cc184032aa5c9f25e1208aa8
            Cipher Suite: **TLS_AES_256_GCM_SHA384 (0x1302)**
            Compression Method: null (0)
            Extensions Length: 46
            Extension: supported_versions (len=2)
            Extension: key_share (len=36)
            [JA3S Fullstring: 771,4866,43-51]
            [JA3S: 15af977ce25de452b96affa2addb1036]
    TLSv1.3 Record Layer: Change Cipher Spec Protocol: Change Cipher Spec
        Content Type: Change Cipher Spec (20)
        Version: TLS 1.2 (0x0303)
        Length: 1
        Change Cipher Spec Message
    TLSv1.3 Record Layer: Application Data Protocol: http-over-tls
        Opaque Type: Application Data (23)
        Version: TLS 1.2 (0x0303)
        Length: 46
        Encrypted Application Data: 27782107b77ab086081c42ffd076ceac5a60072a3379aaba50429bc9389c3757ac71cce3…
        [Application Data Protocol: http-over-tls]
    TLSv1.3 Record Layer: Application Data Protocol: http-over-tls
        Opaque Type: Application Data (23)
        Version: TLS 1.2 (0x0303)
        Length: 2367
        Encrypted Application Data: 9c6deebe75304fb11957c7113c425441d45c1606719478592534fc1baaba15a5f2fb5d95…
        [Application Data Protocol: http-over-tls]
    TLSv1.3 Record Layer: Application Data Protocol: http-over-tls
        Opaque Type: Application Data (23)
        Version: TLS 1.2 (0x0303)
        Length: 95
        Encrypted Application Data: 905a343724c79a1b265d6b63f1644b949fed92c8503dcf0399d596acb1904cf2c708d9fc…
        [Application Data Protocol: http-over-tls]
    TLSv1.3 Record Layer: Application Data Protocol: http-over-tls
        Opaque Type: Application Data (23)
        Version: TLS 1.2 (0x0303)
        Length: 69
        Encrypted Application Data: 7d9a9c4fc41391cbc8d6c31d63cd2535d2fcc52d3014953082a0bd2e7a541e4e2ecfab0b…
        [Application Data Protocol: http-over-tls]
```

<img width="805" height="350" alt="image" src="https://github.com/user-attachments/assets/5cd72c1c-2813-48ef-b75b-7e5512608e1c" />

<img width="1304" height="463" alt="image" src="https://github.com/user-attachments/assets/270baf1e-b995-4282-a6cc-2d49e3f7f91b" />

**Change Cipher Spec**
- The client (your machine) is now saying: "I'm about to send encrypted data."
- But in TLS 1.3, this announcement is meaningless — encryption already started after the Server Hello and key exchange.
- It's just here to avoid confusing any legacy systems.

### Doing the capture ans saving the tls secrets
```bash
TARGET=example.com; SPORT=56000; OUT=curl.pcap; KEYFILE="$PWD/sslkeys.log"; sudo tcpdump -i any -w "$OUT" "tcp and (port $SPORT or port 443)" & TPID=$!; sleep 0.2; SSLKEYLOGFILE="$KEYFILE" curl --local-port "$SPORT" -v "https://$TARGET"; sleep 0.5; sudo kill "$TPID" >/dev/null 2>&1 || true; echo "saved: $OUT"; if [ -s "$KEYFILE" ]; then echo "keys: $KEYFILE"; else echo "warning: $KEYFILE is empty — curl may not support key logging or the client didn't write keys"; fi
```

### Decrypting tls packets by capturing tls session keys

**Secret Key File**
```
aparichit@SUSHANKYA:~/rough/https$ cat sslkeys.log 
SERVER_HANDSHAKE_TRAFFIC_SECRET 3d9972646e67c2b6b39c859b4ba96786aaf2c6f3c755d578d36583c0fb0d2624 b482bcd5eb966f54530c2d78d524e7db7492e7e02f038a6e221e00a71f53eb92e5682b0dd7450fafab548024b8ad454e
EXPORTER_SECRET 3d9972646e67c2b6b39c859b4ba96786aaf2c6f3c755d578d36583c0fb0d2624 91a529e72d1f256aaf69e1343a6eb848cc17ebdf32d21eedcea1f8bfb7e02f470cd1b120b836892ba226a4672c8e4218
SERVER_TRAFFIC_SECRET_0 3d9972646e67c2b6b39c859b4ba96786aaf2c6f3c755d578d36583c0fb0d2624 9a539f04476e14900e1607062281a6033cbd907a233bb0268fd6a10b0941e2578f18247a3ff2a277f3a5a1fdea6f0461
CLIENT_HANDSHAKE_TRAFFIC_SECRET 3d9972646e67c2b6b39c859b4ba96786aaf2c6f3c755d578d36583c0fb0d2624 e743c6f9d6110e3896383e404b0bf01fe4e84115e1bc491fec17d0f88514dc2a157a11db6b772ed6b2417ba3956b4158
CLIENT_TRAFFIC_SECRET_0 3d9972646e67c2b6b39c859b4ba96786aaf2c6f3c755d578d36583c0fb0d2624 ce3ef00e0b66ac39a73d7997d0f3e373b88578cee1f67d051311e1c8ec29fdf6b0a8dd4812c7781685d0b0b434b7b36f
SERVER_HANDSHAKE_TRAFFIC_SECRET 8b7835e0c0fc3ee8865cc7bab0b5216205b36b53add840eb9d12ff19d8e847e6 fc8c59fa1a311fe16ee88e2413e0d66a66da3c398ed7e13d911a87a7b424443ddc5b55b40087d639b1d1b9d42c9d602e
EXPORTER_SECRET 8b7835e0c0fc3ee8865cc7bab0b5216205b36b53add840eb9d12ff19d8e847e6 13a8c7a5631286773bf9256c111423cfd3f569e29e7cdaac55edccf10aaedfff4251d5dd4193e09638bbc493c27a4f88
SERVER_TRAFFIC_SECRET_0 8b7835e0c0fc3ee8865cc7bab0b5216205b36b53add840eb9d12ff19d8e847e6 255817ac031ed97041d0636621a856a5bd9ba29e5aeb64a60cd5d6138d0b9c8f898a30a0b9f561607118cf309227acba
CLIENT_HANDSHAKE_TRAFFIC_SECRET 8b7835e0c0fc3ee8865cc7bab0b5216205b36b53add840eb9d12ff19d8e847e6 b0bef9f1304adb1c7ee0572ab1d1c89578d9018d30b9eb5122659b3c7db16c8b289898b9ff9c3d81d17f5a7529f12713
CLIENT_TRAFFIC_SECRET_0 8b7835e0c0fc3ee8865cc7bab0b5216205b36b53add840eb9d12ff19d8e847e6 c7883936db574abfa567c2452bdb2118d2fd35bd3131c1da1d4ed86a385032f624c2a9ccbd6180ca4519711f58554619

```
<img width="1353" height="278" alt="image" src="https://github.com/user-attachments/assets/4aa4ed06-cbc4-466a-8c19-1f88ce82a590" />


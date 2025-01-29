# Stegonagraphy CTF Tools

- [ApriSolve](https://www.aperisolve.com/) - Aperi'Solve is an online platform which performs layer analysis on image. The platform also uses zsteg, steghide, outguess, exiftool, binwalk, foremost and strings for deeper steganography analysis. The platform supports the following images format: .png, .jpg, .gif, .bmp, .jpeg, .jfif, .jpe, .tiff



# Audio Steganography
- [Stegonaut](https://www.stegonaut.com/) -> Extract message from an audio file

## Brute forcing stegno
- [Stegseek](https://github.com/RickdeJager/stegseek?tab=readme-ov-file)


```bash
stegseek --crack image.jpg wordlsit.txt
```
 >Stegseek can also be used to detect and extract any unencrypted (meta) data from a steghide image. This exploits the fact that the random number generator used in steghide only has 2^32 possible seeds, which can be bruteforced in a matter of minutes.

```bash
stegseek --seed [stegofile.jpg]
```

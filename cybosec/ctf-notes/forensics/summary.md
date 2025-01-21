# Forensics Exploitation Notes


- Check file type (file command)
- Check file siguatre with hex exitors like xxd

>Different types of files have different metadata. The metadata on a photo could include dates, camera information, GPS location, comments, etc. For music, it could include the title, author, track number and album. CTF challenges often have you looking for specific clues in the metadata of a file (especially media files).

**Time Stamps**
- Timestamps are data that indicate the time of certain events (MAC): - Modification – when a file was modified - Access – when a file or entries were read or accessed - Creation – when files or entries were created

### LSB Steganography
![image](https://github.com/user-attachments/assets/5f944cd3-4c64-4109-80eb-9a4dd195ebac)

- LSB Steganography or Least Significant Bit Steganography is a method of Steganography where data is recorded in the lowest bit of a byte.

- Decoding LSB steganography is exactly the same as encoding, but in reverse. For each byte, grab the LSB and add it to your decoded message. Once you’ve gone through each byte, convert all the LSBs you grabbed into text or a file. (You can use your file signature knowledge here!)


## Disk Imaging

- A forensic image is an electronic copy of a drive (e.g. a hard drive, USB, etc.). It’s a bit-by-­bit or bitstream file that’s an exact, unaltered copy of the media being duplicated.

**Why image a disk?**
- Prevents tampering with the original data­ evidence
- Allows you to play around with the copy, without worrying about messing up the original

## Tools for memory dump forensics
- volatile

## Tips for Memory Forensics
- Run strings for clues
- Identify the image profile (which OS, version, etc.)
- Dump processes and look for suspicious processes
- Dump data related interesting processes
- View data in a format relating to the process (Word: .docx, Notepad: .txt, Photoshop: .psd, etc.)

## Important Volatile Commands
```
python vol.py -f ~/image.raw --profile=Win7SP0x64 memdump -p 2019 -D dump/
```
```
python vol.py -f IMAGE --profile=PROFILE connections
```
```
python vol.py -f IMAGE --profile=PROFILE cmdscan
```


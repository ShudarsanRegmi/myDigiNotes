## RTSP with Media MTX

**Start the mediamtx server**
```
snap start mediamtx
```

```bash
 docker run -it --rm   -p 8554:8554   -p 1935:1935   -p 8888:8888   bluenviron/mediamtx # Faced some issue with docker container 
```


**Push the video to rtsp server**
```bash
ffmpeg -f v4l2 -i /dev/video1 -f rtsp rtsp://localhost:8554/live
```

**Display the video over rtsp**
```bash
ffplay rtsp://localhost:8554/live
```

**Packet Analysis**
```
rtsp
```
<img width="1280" height="720" alt="image" src="https://github.com/user-attachments/assets/2e42aa44-b05d-43eb-9159-96aee6764dcb" />


**Video Stream Packets**
<img width="1280" height="679" alt="image" src="https://github.com/user-attachments/assets/9ff6983b-c064-4e24-aa8f-1b4a6e61faa5" />
<img width="1278" height="720" alt="image" src="https://github.com/user-attachments/assets/3cf27034-3d64-4a8d-b634-c4f1a7ad45df" />




**Streamed Camera**
<img width="1217" height="720" alt="image" src="https://github.com/user-attachments/assets/7f4eb9eb-1206-463b-8f63-5c56ac58a0da" />

# KF Sensor

### Initial Setup Info
```
Linux Host machine IP: 1i.12.17.62
Windows VM IP : 11.12.2.44
Connected via bridged interface
```

## Pinging each other
![image](https://github.com/user-attachments/assets/51663b21-c6e0-4bc6-a291-8f8217acdd68)
> Both the devices are connected to each other


## Initial port status of windows
![image](https://github.com/user-attachments/assets/949cd1a4-fcad-48f3-9969-3f2274827e42)
> Basic windows services are open as the windows sytem firewall was turned off

## After Starting KF-Sensor

![image](https://github.com/user-attachments/assets/bc62386f-2d7f-4089-b978-c1224807e614)

> AFter starting KFSensor we can see a lots of services open. This is exactly what a honey pot does.

## Logged nmap scan in Kfsensor
![image](https://github.com/user-attachments/assets/b67c00de-d1c0-44a1-82d5-ac12773f386e)


## Capturing dos attack using hping3
```bash
sudo hping3 -S -p 80 -c 100 11.12.2.44
```
![image](https://github.com/user-attachments/assets/0baa265b-061c-4dd3-8502-e40bbc37575b)

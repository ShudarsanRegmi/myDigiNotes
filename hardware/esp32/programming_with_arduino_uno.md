![{07F44A21-0AB1-4B70-94C7-C07F29030C42}](https://github.com/user-attachments/assets/5e3b6f75-fb29-4928-8ddc-8c6ca958f75b)# Programming ESP32 board with Arduino UNO

![image](https://github.com/user-attachments/assets/96bbf817-de6d-498d-ab90-8517ece57e86)

![{07F44A21-0AB1-4B70-94C7-C07F29030C42}](https://github.com/user-attachments/assets/19478cbf-375c-4aec-8548-be3e6af01028)


Before uploading the code to ESP32-CAM module, please check the following setting:

Update the Preferences –> Aditional boards Manager URLs: https://dl.espressif.com/dl/package_esp32_index.json <br> http://arduino.esp8266.com/stable/package_esp8266com_index.json
Board Settings: <br>
Board: “ESP32 Wrover Module” <br>
Flash Mode: “QIO” <br>
Partition Scheme: “Hue APP (3MB No OTA/1MB SPIFFS)” <br>
Flash Frequency: “40MHz” <br>
Upload Speed: “115200” <br>
Core Debug Level: “None” <br>
Programmer: “AVR ISP” <br>
COM Port: Depends On Your System <br>
GPIO 0 must be connected to GND pin while uploading the sketch <br>
After connecting GPIO 0 to GND pin, press ESP32 CAM on-board RESET button to put the board in the flashing mode <br>
After uploading the code disconnect the GPIO-0 pin from GND pin. <br>

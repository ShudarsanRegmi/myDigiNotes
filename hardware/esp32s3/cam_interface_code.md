# Esp32 : attempt to interface cam

## Connections

| Camera Pin | Connect to ESP32-S3                |
| ---------- | ---------------------------------- |
| 3.3V       | 3.3V                               |
| GND        | GND                                |
| SCL        | GPIO40                             |
| SDA        | GPIO39                             |
| VS         | GPIO12                             |
| HS         | GPIO13                             |
| PCLK       | GPIO11                             |
| MCLK       | GPIO10                             |
| D0         | GPIO4                              |
| D1         | GPIO5                              |
| D2         | GPIO6                              |
| D3         | GPIO7                              |
| D4         | GPIO15                             |
| D5         | GPIO16                             |
| D6         | GPIO17                             |
| D7         | GPIO18                             |
| RST        | 3.3V (or GPIO if you want control) |
| PWDN       | GND                                |

## Code

```c
#include <WiFi.h>
#include "esp_camera.h"

// ===== WIFI =====
const char* ssid = "Amrita_CHN";
const char* password = "amrita@321";

// ===== CAMERA PINS (same as before) =====
#define PWDN_GPIO_NUM     -1
#define RESET_GPIO_NUM    -1
#define XCLK_GPIO_NUM     10

#define SIOD_GPIO_NUM     39
#define SIOC_GPIO_NUM     40

#define Y9_GPIO_NUM       18
#define Y8_GPIO_NUM       17
#define Y7_GPIO_NUM       16
#define Y6_GPIO_NUM       15
#define Y5_GPIO_NUM       7
#define Y4_GPIO_NUM       6
#define Y3_GPIO_NUM       5
#define Y2_GPIO_NUM       4

#define VSYNC_GPIO_NUM    12
#define HREF_GPIO_NUM     13
#define PCLK_GPIO_NUM     11

WiFiServer server(80);

// ===== BMP HEADER HELPER =====
void sendBMP(WiFiClient client, uint8_t *buf, int w, int h) {
  int filesize = 54 + w * h * 3;

  uint8_t bmpHeader[54] = {
    'B','M',
    filesize, filesize>>8, filesize>>16, filesize>>24,
    0,0,0,0,
    54,0,0,0,
    40,0,0,0,
    w,0,0,0,
    h,0,0,0,
    1,0,
    24,0
  };

  client.write(bmpHeader, 54);

  // Convert RGB565 → RGB888
  for (int i = 0; i < w * h; i++) {
    uint16_t pixel = ((uint16_t*)buf)[i];

    uint8_t r = ((pixel >> 11) & 0x1F) << 3;
    uint8_t g = ((pixel >> 5) & 0x3F) << 2;
    uint8_t b = (pixel & 0x1F) << 3;

    uint8_t rgb[3] = {b, g, r}; // BMP uses BGR
    client.write(rgb, 3);
  }
}

void setup() {
  Serial.begin(115200);

  // ===== WIFI CONNECT =====
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nWiFi connected");
  Serial.println(WiFi.localIP());

  // ===== CAMERA CONFIG =====
  camera_config_t config;
  config.ledc_channel = LEDC_CHANNEL_0;
  config.ledc_timer   = LEDC_TIMER_0;

  config.pin_d0 = Y2_GPIO_NUM;
  config.pin_d1 = Y3_GPIO_NUM;
  config.pin_d2 = Y4_GPIO_NUM;
  config.pin_d3 = Y5_GPIO_NUM;
  config.pin_d4 = Y6_GPIO_NUM;
  config.pin_d5 = Y7_GPIO_NUM;
  config.pin_d6 = Y8_GPIO_NUM;
  config.pin_d7 = Y9_GPIO_NUM;

  config.pin_xclk = XCLK_GPIO_NUM;
  config.pin_pclk = PCLK_GPIO_NUM;
  config.pin_vsync = VSYNC_GPIO_NUM;
  config.pin_href = HREF_GPIO_NUM;

  config.pin_sccb_sda = SIOD_GPIO_NUM;
  config.pin_sccb_scl = SIOC_GPIO_NUM;

  config.pin_pwdn  = PWDN_GPIO_NUM;
  config.pin_reset = RESET_GPIO_NUM;

  config.xclk_freq_hz = 20000000;
  config.pixel_format = PIXFORMAT_RGB565;

  config.frame_size = FRAMESIZE_QQVGA; // 160x120
  config.fb_count = 1;

  if (esp_camera_init(&config) != ESP_OK) {
    Serial.println("Camera init failed");
    return;
  }

  server.begin();
  Serial.println("Server started");
}

void loop() {
  WiFiClient client = server.available();

  if (client) {
    Serial.println("Client connected");

    while (client.connected() && !client.available()) delay(1);

    String req = client.readStringUntil('\r');
    client.flush();

    if (req.indexOf("GET /") >= 0) {

      camera_fb_t *fb = esp_camera_fb_get();
      if (!fb) {
        client.println("HTTP/1.1 500 Internal Server Error");
        client.stop();
        return;
      }

      client.println("HTTP/1.1 200 OK");
      client.println("Content-Type: image/bmp");
      client.println();

      sendBMP(client, fb->buf, 160, 120);

      esp_camera_fb_return(fb);
    }

    client.stop();
    Serial.println("Client disconnected");
  }
}

```

<img width="679" height="308" alt="image" src="https://github.com/user-attachments/assets/49719666-950a-48e8-9ee1-6fa2fbc4e235" />





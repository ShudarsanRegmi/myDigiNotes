# Capturing Video with OpenCV Python

```python
import cv2

# open the camera
cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()
    # ret is a boolean that indicates of the frame was captured successfully
    # frame = actual image captured from the camera
    if not ret:
        print("Failed to grab frame")
        break

    cv2.imshow('WebCam', frame)
    # this function displays an image in a window


    # this line causes a delay of 1ms and looks if user pressed 'q` or not
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# releaes the video capture object and any resources associated with it
cap.release()

# closes all the openCV windows
cv2.destroyAllWindows()
```

## Getting the camera FPS

```python
# Get and print the actual FPS to see if it was applied
fps = cap.get(cv2.CAP_PROP_FPS)
print(f"Actual FPS: {fps}")
```

## Setting the FPS
```python
# Attempt to set the FPS to 1
cap.set(cv2.CAP_PROP_FPS, 1)
```

>Note: Setting the FPS to some custom value may not be suuported by the hardware


## Simulating low FPS (even if it is not supported by HardWare)

```python
import cv2
import time

# Open the camera
cap = cv2.VideoCapture(0)

# Simulate 1 FPS by delaying each frame
while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    cv2.imshow('Webcam', frame)

    # Simulate 1 frame per second (delay for 1 second)
    time.sleep(1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

>Note: This works for lower fps then the hardware can capture in maximum

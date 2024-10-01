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

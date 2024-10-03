# Hand Tracking


```python
import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        print("frame was not captured")
        break

    # converting the frame from BGR TO RGB

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame to detect hands
    results = hands.process(frame_rgb)

    

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Show the frame with hand landmarks
    cv2.imshow('Hand Tracking', frame)

    # Break the loop when q is pressed

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
```

- hands.process will return an object which we will be calling as result. Following are the imporant properties of the result object: 'count', 'index', 'multi_hand_landmarks', 'multi_hand_world_landmarks', 'multi_handedness'

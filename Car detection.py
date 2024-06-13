import cv2
import time
import numpy as np
# Create our body classifier
car_classifier = cv2.CascadeClassifier(r'C:\Users\User\Downloads\Harcascade\haarcascade_cars.xml')
# Initiate video capture for video filecap
cap=cv2.VideoCapture(r'C:\Users\User\Downloads\Harcascade\cars2.mp4')
# Loop once video is successfully loaded
while cap.isOpened():
    time.sleep(0.05)
    # Read first frame
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# Pass frame to our car classifierb
    cars = car_classifier.detectMultiScale(gray, 1.4, 2)
    # Extract bounding boxes for any bodies identified
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
        cv2.imshow('Cars', frame)

    if cv2.waitKey(1) == 13:  # 13 is the Enter Key
        break

cap.release()
cv2.destroyAllWindows()





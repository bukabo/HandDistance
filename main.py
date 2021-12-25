import cv2
from cvzone.HandTrackingModule import HandDetector

# webcam
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

# Hand detector
detect = HandDetector(detectionCon=0.8, maxHands=1)

# loop
while True:
    success, img = cap.read()
    hands, img = detect.findHands(img)
    cv2.imshow('image', img)
    cv2.waitKey(1)

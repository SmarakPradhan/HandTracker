import cv2 
import mediapipe as mp
import time

#using Mediapipe Solutions module
mpHands = mp.solutions.hands
hands = mp.solutions.hands.Hands()
#for drawing ponts and connectins btw points on  hands
mpdraw = mp.solutions.drawing_utils
#For video capturing using webcam
cam = cv2.VideoCapture(0)


while True :
    success,img = cam.read()
    h, w, c = img.shape
    #MediaPipe only uses RGB images but Opencv here gives us BGR images so we convert it to RGB images
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    output = hands.process(imgRGB)


    cv2.imshow("Image", img)
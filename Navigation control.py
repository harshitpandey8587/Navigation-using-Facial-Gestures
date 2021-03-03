
import cv2
#import numpy as np
from pynput.keyboard import Key, Controller

keyboard = Controller()
flag= -1
x1,y1=260,200
x2,y2=x1+40,y1+40

#importing haarcascade frontal face detection file,used to detect frontal face
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap=cv2.VideoCapture(0)
while cap.isOpened():
    ret,frame = cap.read()

    # Flipping the frame to get correct sense of direction(Left to Right,Right to Left )

    frame = cv2.flip(frame, 1)  # We have kept 1 to flip around y axis

    if ret == True:
        gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        face_list = faceCascade.detectMultiScale(gray_frame, 1.1, 4)
        # detectMultiScale() is used to Detect objects of different sizes in the input image

        for (x,y,w,h) in face_list:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255, 255, 0), 2)
            center = [int((x + x+w)/2),int((y + y+h)/2)] #We can also use x+w/2 and y+h/2
        #Drawing control region.
        cv2.rectangle(frame,(x1,y1),(x2,y2),(0,0,255),1)
        #Drawing navigation dot
        cv2.circle(frame,(center[0],center[1]),0,(0, 0, 255), 5)
#Code Author: Harshit Pandey ()
        if center[0]>x1 and center[0]<x2 and center[1]>y1 and center[1]<y2:
            flag = 0

        if flag == 0:
            if center[0] > x2:
                keyboard.press(Key.right)
                keyboard.release(Key.right)
                print("Right")
                flag = 1

            if center[0] < x1:
                keyboard.press(Key.left)
                keyboard.release(Key.left)
                print("Left")
                flag = 1

            if center[1] < y1:
                keyboard.press(Key.up)
                keyboard.release(Key.up)
                print("Up")
                flag = 1

            if center[1] > y2:
                keyboard.press(Key.down)
                keyboard.release(Key.down)
                print("Down")
                flag = 1

        # Display the resulting frame
        cv2.imshow('Face', frame)

        # Press Q on keyboard to  exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Break the loop
    else:
        break
cap.release()
# Closes all the frames
cv2.destroyAllWindows()
import cv2
import numpy as np

framewidth = 640
frameheight = 480
cap = cv2.VideoCapture(0)
cap.set(3,framewidth)
cap.set(4,frameheight)
cap.set(10,150)

mycolors = [[110,50,50,130,255,255],[0,50,50,10,255,255],27,79,0,100,255,255]
#mycolorsValues = [[255,0,0],[0,0,255],[0,255,0]]

def findcolor(img,mycolors):
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    for color in  mycolors:
        lower  = np.array(mycolors[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV,lower,upper)
        imgResult = cv2.bitwise_and(img,img,mask=mask)
    return imgResult

while True:
    success, img = cap.read()
    imgResult = findcolor(img,mycolors)
    
    cv2.imshow("Result",imgResult)
    cv2.imshow("mask",mask)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

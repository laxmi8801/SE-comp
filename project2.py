import cv2
import numpy as np
widthimg = 640
heightimg = 480
cap = cv2.VideoCapture(0)
cap.set(3,widthimg)
cap.set(4,heightimg)
cap.set(10,150)

def preprocess(img):
    imggray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgblur = cv2.GaussianBlur(imggray,(5,5,),3)
    imgcanny = cv2.Canny(imgblur,200,200)
    kernel = np.ones((5,5))
    imgdelitae = cv2.dilate(imgcanny,kernel,iterations= 2)
    imgthres = cv2.erode(imgdelitae,kernel,iterations=1)

    return imgthres

def getcontours(img):
    biggest = np.array([])
    maxarea = 0
    contours,hierarcy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in  contours:
        area = cv2.contourArea(cnt)
        #print(area)
        
        if area>5000:
            #cv2.drawContours(imgcontour,cnt,-1,(255,0,0),3)
            peri = cv2.arcLength(cnt,True)
            #print(peri)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            if area>maxarea and len(approx) == 4:
                biggest = approx
                maxarea = area

    cv2.drawContours(imgcontour,biggest,-1,(255,0,0),3)
    return biggest

def reorder(mypoints):
    mypoints = mypoints.reshape((4,2))
    mypointsnew = np.zeros((4,1,2),np.int32)
    add = mypoints.sum(1)
    #print("add ",add)

    mypointsnew[0] = mypoints[np.argmin(add)]
    mypointsnew[0] = mypoints[np.argmax(add)]
    
    diff = np.diff(mypoints,axis=1)
    mypointsnew[1] = mypoints[np.argmin(diff)]
    mypointsnew[1] = mypoints[np.argmax(diff)]
    #print("NewPoints",mypointsnew)
    return mypointsnew

def getwrap(img,biggest):
    biggest = reorder(biggest)
    #print(biggest)
    pts1  = np.float32(biggest)
    pts2 = np.float32([[0,0],[widthimg,0],[0,heightimg],[widthimg,heightimg]])
    matrix = cv2.getPerspectiveTransform(pts1,pts2)
    imgout = cv2.warpPerspective(img,matrix,(widthimg,heightimg))

    imgcropped = imgout[20:imgout.shape[0]-20,20:imgout.shape[1]-20]
    return imgout
    

while True:
    success, img = cap.read()
    cv2.resize(img,(widthimg,heightimg))
    imgcontour =  img.copy()
    imgthres = preprocess(img)
    biggest = getcontours(imgthres)
    print(biggest)

    imgwraped = getwrap(img,biggest)
    cv2.imshow("Result",imgwraped)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
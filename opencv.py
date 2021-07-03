import cv2
import numpy as np
#def empty(a):
    # pass

# def getcontours(img):
#     contours,hierarcy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
#     for cnt in  contours:
#         area = cv2.contourArea(cnt)
#         #print(area)
        
#         if area>500:
#             cv2.drawContours(imgcontour,cnt,-1,(255,0,0),3)
#             peri = cv2.arcLength(cnt,True)
#             #print(peri)
#             approx = cv2.approxPolyDP(cnt,0.02*peri,True)
#             print(len(approx))
#             objcor = len(approx)
#             x , y,w,h =cv2.boundingRect(approx)

#             if objcor ==3 : objectType = "Tri"
#             elif objcor ==4: 
#                 aspratio = w/float(h)
#                 if (aspratio>0.95 and aspratio<1.05):
#                     objectType = "square"
#                 else:
#                     objectType = "rect"
#             elif objcor>4: objectType = "circle "
#             else: objectType ="None"

#             cv2.rectangle(imgcontour,(x,y),(x+w,y+h),(0,255,0),2)
#             cv2.putText(imgcontour,objectType,(x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),1)



faceCascade = cv2.CascadeClassifier("C:\\Users\Prayog\\Desktop\\SE COMP\\haarcascade_frontalface_default_files")
path = "C:\\Users\\Prayog\\Desktop\\SE COMP\\resources\\action4.jpg"
img = cv2.imread(path)

# imgcontour = img.copy()
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(imgray,1.1,4)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
# imgblur = cv2.GaussianBlur(imgray,(7,7),1)
# imgcanny = cv2.Canny(imgblur,50,50)
# getcontours(imgcanny)
# imgBlank = np.zeros_like(img)
# cv2.imshow("original",img)   
#cv2.imshow("gray",imgray)  
#cv2.imshow("blur",imgblur)   
# cv2.imshow("canny",imgcanny) 
# cv2.imshow("blank",imgBlank) 
# cv2.imshow("contour",imgcontour) 
cv2.waitKey(0)


# cv2.namedWindow("trackbars")
# cv2.resizeWindow("trackbars",640,240)
# cv2.createTrackbar("hue min","trackbars",0,179,empty)
# cv2.createTrackbar("hue max","trackbars",31,179,empty)
# cv2.createTrackbar("sat min","trackbars",103,255,empty)
# cv2.createTrackbar("sat max","trackbars",240,255,empty)
# cv2.createTrackbar("val min","trackbars",153,255,empty)
# cv2.createTrackbar("val max","trackbars",255,255,empty)

# while True:
#     img = cv2.imread(path)
#     imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#     h_min = cv2.getTrackbarPos("hue min","trackbars")
#     h_max = cv2.getTrackbarPos("hue max","trackbars")
#     s_min = cv2.getTrackbarPos("sat min","trackbars")
#     s_max = cv2.getTrackbarPos("sat max","trackbars")
#     v_min = cv2.getTrackbarPos("val min","trackbars")
#     v_max = cv2.getTrackbarPos("val max","trackbars")
#     print(h_min,h_max,s_min,s_min,v_min,v_max)
#     lower = np.array([h_min,s_min,v_min])
#     upper = np.array([h_max,s_max,v_max])
#     mask = cv2.inRange(imgHSV,lower,upper)
#     imgresult = cv2.bitwise_and(img,img,mask=mask)
#     cv2.imshow("hsv",imgHSV)

#     cv2.imshow("mask",mask)
#     cv2.imshow("result",imgresult)


def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver


#imghor = np.hstack((img,img))
#imgver = np.vstack((img,img))
# width,height = 150,250
# pts1  = np.float32([[75,95],[126,54],[180,84],[127,143]])
# pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
# matrix = cv2.getPerspectiveTransform(pts1,pts2)
# imgout = cv2.warpPerspective(img,matrix,(width,height))
#img = np.zeros((512,512,3),np.uint8)
#print(img)
#img[:] = 255,0,0
# cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)
# cv2.rectangle(img,(0,0),(250,350),(0,0,255),2)
# cv2.circle(img,(300,300),30,(255,255,0),5)
# cv2.putText(img," OPENCV ",(400,300),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,255,255),1)
# img = cv2.imread("C:\\Users\\Prayog\\Desktop\\SE COMP\\resources\\action4.jpg")
# imgresize = cv2.resize(img,(500,300))
# print(img.shape)
# imgcrop = img[0:100,10:150]

#cv2.imshow("image hor",imghor)
#cv2.imshow("image ver",imgver)
#cv2.imshow("output",imgout)
# #cv2.imshow("image resize",imgresize)
# cv2.imshow("image crop",imgcrop)
 
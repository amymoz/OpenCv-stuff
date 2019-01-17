import numpy as np
import cv2

img = np.zeros((480,640,3), np.uint8)
cap = cv2.VideoCapture(0)

while(True):
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_green = np.array([68,42,0])
    upper_green = np.array([88,255,255])

    mask = cv2.inRange(hsv, lower_green, upper_green)
    
    madian = cv2.medianBlur(mask, 15)

    im2, contours, hierarchy = cv2.findContours(madian,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)    

    res = cv2.bitwise_and(frame,frame, mask= mask)
    #try:
        #cnt = contours[0]
        #area = cv2.contourArea(cnt)    
    if len(contours) > 0:
        cnt = max(contours, key = cv2.contourArea)
        (x1,y1), radius=cv2.minEnclosingCircle(cnt)
        center = (int(x1),int(y1))
        radius = int(radius)
        x,y,w,h = cv2.boundingRect(cnt)
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.circle(frame,center,radius,(0,0,255),2)
        cv2.circle(frame,center,2,(255,0,0),4)
        print(center)
    #except:
        print ('Wait ...')



    #print(area)

    #cv2.drawContours(frame, contours, -1, (0,255,0), 3)

    cv2.imshow('frame',frame)
    cv2.imshow('im2',im2)
    #cv2.imshow('RES',res)

    a = cv2.waitKey(5)
    if (a==ord("q")):
        break

cv2.destroyAllWindows()

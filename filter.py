###############################################
import numpy as np
import cv2 as cv
###############################################
thing = cv.VideoCapture(0)
while True:
    _,frame = thing.read()
    hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    minb= np.array([110,50,50])
    maxb= np.array([130,255,255])
    #minr = np.array([50, 50, 50])
    #maxr = np.array([255, 255, 255])
    bluep = cv.inRange(hsv,minb,maxb)
    #redp = cv.inRange(hsv, minr, maxr)
    bluepic = cv.bitwise_and(frame,frame,mask = bluep)
    #redpic = cv.bitwise_and(frame, frame, mask = redp)
    #realpic = cv.bitwise_and(redpic, bluepic, mask=bluep)
    cv.imshow('rand',frame)
    cv.imshow('smt',hsv)
    a = cv.waitKey(1)
###############################################   
    if ord("q") == a:
        break
cv.destroyAllWindows()
###############################################

#in code tamame dastoraee has ke ostad ta alan darbareye opencv gofte va ...
#in code ejraee nis faghat ye list az inja copy knin baray rahati 
#by Mohsen ^_^

import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)
_, frame = cap.read()
aks1 = cv.imread('dot.png')
print(type(aks1))
plt.imshow(aks1)
plt.show()
revclr = cv.cvtColor(aks1,cv.COLOR_BGR2RGB)
cv.namedWindow('picture',cv.WINDOW_NORMAL)
cv.imshow('picture',revclr)
cv.waitKey(0)
cv.destroyAllWindows()
cv.destroyWindow('picture')
ord("")
mask = cv.inRange(pic,minimum,maximum)
minbl= np.array([110,50,50])
maxbl= np.array([130,255,255])
RES = cd.bitwise_and(frame,frame,mask = mask)

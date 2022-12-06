import cv2
import numpy as np

#Shapping

#img = np.zeros((500,500))    #Black image
img = np.zeros((500,500,3),np.uint8)
img[200:300,100:300] = 255,0,0

#Create Line
cv2.line(img,(0,20),(200,20),(0,255,0),3)

#rectangle
cv2.rectangle(img,(20,100),(300,150),(0,0,255),cv2.FILLED)

#circle
cv2.circle(img,(220,50),30,(255,255,0),5)

#Put Text
cv2.putText(img,"Welcome",(130,250),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,255),2)

cv2.imshow("Image",img)
cv2.waitKey(0)
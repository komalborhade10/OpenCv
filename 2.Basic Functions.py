import cv2
import numpy as np

img =cv2.imread("resourcea/img.png")
kernel = np.ones((5,5),np.uint8)

# Convert into grayscle
imggray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#BLUR
imgblur = cv2.GaussianBlur(imggray,(7,7),0)

#edge detect
imgCany = cv2.Canny(img,150,200)  #threshold value

imgDialation = cv2.dilate(imgCany,kernel,iterations=1)

imgEroded = cv2.erode(imgDialation,kernel,iterations=1)

cv2.imshow("gray",imggray)
cv2.imshow("blur",imgblur)
cv2.imshow("canny",imgCany)
cv2.imshow("Dialation",imgDialation)
cv2.imshow("eroded",imgEroded)

cv2.waitKey(0)
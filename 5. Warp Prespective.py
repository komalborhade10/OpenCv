import cv2
import numpy as np

img = cv2.imread("resourcea/flowers.jpeg")

width,height = 560,869
pts = np.float32([[17,387],[438,387],[17,831],[438,831]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix = cv2.getPerspectiveTransform(pts,pts2)
imgoutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Flower",img)
cv2.imshow("output",imgoutput)
cv2.waitKey(0)
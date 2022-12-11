import cv2
import numpy as np
img = cv2.imread('resourcea/sunflower.jpg')

hor = np.hstack((img,img))
ver = np.vstack((img,img))
cv2.imshow("Horizaontal",hor)
cv2.imshow("Vertical",ver)
cv2.waitKey(0)
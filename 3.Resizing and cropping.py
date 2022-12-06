import cv2
import numpy

img = cv2.imread("resourcea/img.png")   #put image path
print(img.shape)
cv2.imshow("Image",img)

# Resizing Image
imgresize = cv2.resize(img,(800,700))   #W,H
#cv2.imshow("Image Resize",imgresize)


# Croping Image
imgcropped = img[0:200,200:500]  #H,W
cv2.imshow("cropped image",imgcropped)

cv2.waitKey(0)


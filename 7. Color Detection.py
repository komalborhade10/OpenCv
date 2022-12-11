import cv2
import numpy as np
def empty(a):
    pass

path = "resourcea/sunflower.jpg"

cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",500,300)
cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)
cv2.createTrackbar("Hue Max","TrackBars",19,179,empty)
cv2.createTrackbar("sat Min","TrackBars",110,255,empty)
cv2.createTrackbar("sat Max","TrackBars",240,255,empty)
cv2.createTrackbar("value Min","TrackBars",153,255,empty)
cv2.createTrackbar("value Max","TrackBars",255,255,empty)

while True:
    img = cv2.imread(path)

    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min","TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("value Min", "TrackBars")
    v_max = cv2.getTrackbarPos("value Max", "TrackBars")

    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max]
                     )
    mask = cv2.inRange(imgHSV,lower,upper)
    imgResult = cv2.bitwise_and(img,img,mask=mask)
    cv2.imshow("image",img)
    cv2.imshow("HSV",imgHSV)
    cv2.imshow("mask",mask)
    cv2.imshow("result", imgResult)
    cv2.waitKey(0)
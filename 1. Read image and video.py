import cv2
print("Package Imported")
'''''
# Read image

img = cv2.imread("resourcea\img.png")
cv2.imshow('Image',img)
cv2.waitKey(0)


# Read Video
video1 = cv2.VideoCapture("resourcea/pedestrians.mp4")

while True:
    success,img = video1.read()
    cv2.imshow('Video',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
'''''
#read video from camera

video1 = cv2.VideoCapture(0)
video1.set(3,640)
video1.set(4,480)
video1.set(10,100)

while True:
    success,img = video1.read()
    cv2.imshow('Video',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
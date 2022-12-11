import cv2
# We point OpenCV's CascadeClassifier function to where our classifier (XML file format) is stored
faceCascade = cv2.CascadeClassifier("resourcea/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("resourcea/haarcascade_eye.xml")

img = cv2.imread("resourcea/download (2).jpg")
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray,1.1,4)

# We iterate through our faces array and draw a rectangle over each face in faces
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

    roi_gray = imgGray[x:x + w, y:y + w]
    roi_color = img[x:x + h, y:y + w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

        cv2.imshow("Image",img)
        cv2.waitKey(0)


import cv2

img=cv2.imread("face.png")

eye_cascade=cv2.CascadeClassifier("eye.xml")
face_cascade=cv2.CascadeClassifier("frontalface.xml")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces=face_cascade.detectMultiScale(gray,1.3,5)


for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)


img2=img[y:y+h,x:x+w]
gray2=gray[y:y+h,x:x+w]


eyes=eye_cascade.detectMultiScale(gray2)

for (x2,y2,w2,h2) in eyes:
    cv2.rectangle(img2,(x2,y2),(x2+w2,y2+h2),(166,110,0),2)

cv2.imshow("Pencere",img)

cv2.waitKey(0)
cv2.destroyAllWindows()

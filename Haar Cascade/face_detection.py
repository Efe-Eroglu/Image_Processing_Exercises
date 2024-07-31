import cv2
import numpy as np



img=cv2.imread("face.png")

face_cascade=cv2.CascadeClassifier("frontalface.xml")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(gray,1.3,6)


#ilk parametre ölçeklendirme resmi ne kadar küçülteceği 
# ikinci parametre kaç adet bulacağı

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow("Pencere",img)

cv2.waitKey(0)
cv2.destroyAllWindows()






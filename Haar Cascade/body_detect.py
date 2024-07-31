import cv2 

img=cv2.imread("body.jpg")

body_cascade=cv2.CascadeClassifier("fullbody.xml")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

bodys=body_cascade.detectMultiScale(gray,1.2,1)

for (x,y,w,h) in bodys:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)



cv2.imshow("Pencere",img)


cv2.waitKey(0)
cv2.destroyAllWindows()
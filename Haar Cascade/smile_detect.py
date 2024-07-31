import cv2 

img=cv2.imread("C:\\Users\\Efe\\Desktop\\Okul\\Genel Programlama Dersleri\\Python_Library\\OpenCv\\images\\smile.jpg")

smile_cascade=cv2.CascadeClassifier("C:\\Users\\Efe\\Desktop\\Okul\\Genel Programlama Dersleri\\Python_Library\\OpenCv\\Xml_Dosyalari\\smile.xml")
face_cascade=cv2.CascadeClassifier("C:\\Users\\Efe\\Desktop\\Okul\\Genel Programlama Dersleri\\Python_Library\\OpenCv\\Xml_Dosyalari\\frontalface.xml")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces=face_cascade.detectMultiScale(gray,1.3,4)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(1,255,1),2)

    img2=img[y:y+h,x:x+w]
    gray2=gray[y:y+h,x:x+w]

    smile=smile_cascade.detectMultiScale(gray2,2,22)

    for (x2,y2,w2,h2) in smile:
        cv2.rectangle(img2,(x2,y2,),(x2+w2,y2+h2),(255,23,33),2)



cv2.imshow("Pencere",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
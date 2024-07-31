import cv2

cap=cv2.VideoCapture("faces.mp4")
face_cascade=cv2.CascadeClassifier("frontalface.xml")


while 1:
    ret,frame=cap.read()

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces=face_cascade.detectMultiScale(gray,1.1,3)


    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),1)
    

    if ret==0:
        break


    cv2.imshow("Cap",frame)


    if cv2.waitKey(10) & 0xFF==ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
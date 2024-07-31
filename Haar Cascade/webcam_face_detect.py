import cv2

cap=cv2.VideoCapture(0)

face_casade=cv2.CascadeClassifier("frontalface.xml")

while 1:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    face=face_casade.detectMultiScale(gray,1.4,5)

    for (x,y,w,h) in face:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)


    if ret==0:
        break

    cv2.imshow("Pencere",frame)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
    
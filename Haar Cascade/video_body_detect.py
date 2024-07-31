import cv2 

cap=cv2.VideoCapture("body.mp4")

body_cascade=cv2.CascadeClassifier("fullbody.xml")


while 1:
    ret,frame=cap.read()

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    bodyes=body_cascade.detectMultiScale(gray,1.1,2)

    for (x,y,w,h) in bodyes:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(222,222,22),2)

    cv2.imshow("Pencere",frame)

    if cv2.waitKey(5) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


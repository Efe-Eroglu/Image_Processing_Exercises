import cv2 

cap=cv2.VideoCapture(0)

smile_cascade=cv2.CascadeClassifier("smile.xml")
face_cascade=cv2.CascadeClassifier("frontalface.xml")

while 1:
    ret,frame=cap.read()

    frame=cv2.flip(frame,1)
    frame=cv2.resize(frame,(640,480))
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces=face_cascade.detectMultiScale(gray,1.3,5)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,22,222),2)

        frame_roi=frame[y:y+h,x:x+w]
        gray_roi=gray[y:y+h,x:x+w]

        smile=smile_cascade.detectMultiScale(gray_roi,1.6,7)

        for (x2,y2,w2,h2) in smile:
            cv2.rectangle(frame_roi,(x2,y2),(x2+w2,y2+h2),(21,212,2),2)

    
    cv2.imshow("Pencere",frame)

    if cv2.waitKey(12) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


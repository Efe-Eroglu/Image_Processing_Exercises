import cv2

cap=cv2.VideoCapture("eye.mp4")

face_cascade=cv2.CascadeClassifier("frontalface.xml")
eye_cascade=cv2.CascadeClassifier("eye.xml")

while 1:
    ret,frame=cap.read()

    if ret==0:
        break
    
    frame=cv2.resize(frame,(480,360))

    frame=cv2.flip(frame,1)

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces=face_cascade.detectMultiScale(gray,1.3,5)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(155,0,0),2)


        frame2=frame[y:y+h,x:x+w]
        gray2=gray[y:y+h,x:x+w]

        eyes=eye_cascade.detectMultiScale(gray2)

        for (x2,y2,w2,h2) in eyes:
            cv2.rectangle(frame2,(x2,y2),(x2+w2,y2+h2),(0,50,255),2)


    cv2.imshow("Pencere",frame)    


    if cv2.waitKey(5) & 0xFF==ord('q'):
        break



cap.release()
cv2.destroyAllWindows()
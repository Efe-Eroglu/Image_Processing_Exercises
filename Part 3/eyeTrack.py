import cv2
import numpy as np

cap=cv2.VideoCapture("C:\\Users\\Efe\\Desktop\\Okul\\Genel Programlama Dersleri\\Python_Library\\OpenCv\\images\\eye_motion.mp4")



while 1:
    ret,frame=cap.read()

    if ret==0:
        break

    roi=frame[80:210,230:450]
    row,col,channel=roi.shape

    gray=cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)

    _,thresh=cv2.threshold(gray,3,255,cv2.THRESH_BINARY_INV)

    contours,_=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    contours=sorted(contours,key=lambda x:cv2.contourArea(x),reverse=True)
    
    for cnt in contours:
        x,y,w,h=cv2.boundingRect(cnt)
        cv2.rectangle(roi,(x,y),(x+w,y+h),(0,255,0),2)

        cv2.line(roi,(int(x+w/2),0),(int(x+w/2),row),(255,255,222),2)
        cv2.line(roi,(0,int(y+h/2)),(col,int(y+h/2)),(255,222,222),2)
        break

    cv2.imshow("Pencere",roi)
    cv2.imshow("thre",thresh)


    if cv2.waitKey(80) & 0xFF==ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
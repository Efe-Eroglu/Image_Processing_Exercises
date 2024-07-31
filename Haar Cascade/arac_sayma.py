import numpy as np
import cv2

cap=cv2.VideoCapture("traffic.avi")

backsub=cv2.createBackgroundSubtractorMOG2()
sayac=0


while 1:
    ret,frame=cap.read()

    if ret:
        fgmask=backsub.apply(frame)
        
        cv2.line(frame,(50,0),(50,300),(255,255,0),1)
        cv2.line(frame,(70,0),(70,300),(255,255,0),1)
        
        contours,hierarchy=cv2.findContours(fgmask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

        try: hierarchy=hierarchy[0]
        except: hierarchy=[]

        for contour,hier in zip(contours,hierarchy):        
            (x,y,w,h)=cv2.boundingRect(contour)
            if w>40 and h>40 :
                cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
                if x>50 and x<70:
                    sayac+=1

        cv2.putText(frame,"Car : " + str(sayac),(90,100),cv2.FONT_HERSHEY_PLAIN,2,(0,0,155),2,cv2.LINE_AA)


        cv2.imshow("Sayac : " , frame)
        cv2.imshow("Video",fgmask)


        if cv2.waitKey(20) &0xFF==ord('q'):
            break


cap.release()
cv2.destroyAllWindows()





import cv2
import numpy as np

def nothing():
    pass


font=cv2.FONT_HERSHEY_SIMPLEX

cap=cv2.VideoCapture(0)

cv2.namedWindow("Ayarlar")

cv2.createTrackbar("Low-H","Ayarlar",0,180,nothing)
cv2.createTrackbar("Low-S","Ayarlar",0,255,nothing)
cv2.createTrackbar("Low-V","Ayarlar",0,255,nothing)

cv2.createTrackbar("Up-H","Ayarlar",0,180,nothing)
cv2.createTrackbar("Up-S","Ayarlar",0,255,nothing)
cv2.createTrackbar("Up-V","Ayarlar",0,255,nothing)

cv2.setTrackbarPos("Up-H","Ayarlar",180)
cv2.setTrackbarPos("Up-S","Ayarlar",255)
cv2.setTrackbarPos("Up-V","Ayarlar",255)




while 1:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lh=cv2.getTrackbarPos("Low-H","Ayarlar")
    ls=cv2.getTrackbarPos("Low-S","Ayarlar")
    lv=cv2.getTrackbarPos("Low-V","Ayarlar")


    uh=cv2.getTrackbarPos("Up-H","Ayarlar")
    us=cv2.getTrackbarPos("Up-S","Ayarlar")
    uv=cv2.getTrackbarPos("Up-V","Ayarlar")


    low_color=np.array([lh,ls,lv])
    up_color=np.array([uh,us,uv])

    mask=cv2.inRange(hsv,low_color,up_color)
    kernel=np.ones((5,5),dtype=np.uint8)
    mask=cv2.erode(mask,kernel)

    contours,_=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)



    for cnt in contours:
        area=cv2.contourArea(cnt)
        epsilon=(0.02)*cv2.arcLength(cnt,True)

        approx=cv2.approxPolyDP(cnt,epsilon,True)

        x=approx.ravel()[0]
        y=approx.ravel()[1]
        
        if area > 400 :
            cv2.drawContours(frame,[approx],0,(0,0,0),5)
            if len(approx)==3:
                cv2.putText(frame,"Triangle",(x,y),font,1,(0,0,0))

            elif len(approx)==4:
                cv2.putText(frame,"Rectangle",(x,y),font,1,(0,0,0))

            elif len(approx)==5:
                cv2.putText(frame,"pentagon",(x,y),font,1,(0,0,0))

            elif len(approx)==6:
                cv2.putText(frame,"hexagon",(x,y),font,1,(0,0,0))
            else:
                cv2.putText(frame,"Cokgen",(x,y),font,1,(0,0,0))


    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)



    if cv2.waitKey(5) & 0xFF==ord('q'):
        break



cap.release()
cv2.destroyAllWindows()
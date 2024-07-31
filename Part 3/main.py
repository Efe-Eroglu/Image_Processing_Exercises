import cv2
import numpy as np


def nothing():
    pass



cap=cv2.VideoCapture(0)

cv2.namedWindow("Ayarlar")
cv2.createTrackbar("Low-H","Ayarlar",0,179,nothing)
cv2.createTrackbar("Low-S","Ayarlar",0,255,nothing)
cv2.createTrackbar("Low-V","Ayarlar",0,255,nothing)

cv2.createTrackbar("Up-H","Ayarlar",0,179,nothing)
cv2.createTrackbar("Up-S","Ayarlar",0,255,nothing)
cv2.createTrackbar("Up-V","Ayarlar",0,255,nothing)

cv2.setTrackbarPos("Up-H","Ayarlar",185)
cv2.setTrackbarPos("Up-S","Ayarlar",255)
cv2.setTrackbarPos("Up-V","Ayarlar",255)


while 1:

    ret,frame=cap.read()

    frame=cv2.flip(frame,1)

    frame=cv2.resize(frame,(500,300))
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

    bitwise=cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow("Mask",mask)
    cv2.imshow("Normal",frame)
    cv2.imshow("hsv",hsv)
    cv2.imshow("Bitwise",bitwise)


    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows
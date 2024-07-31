import cv2
import numpy as np

cap=cv2.VideoCapture(0)

def findMaxContours(contours):
    max_i=0
    max_area=0

    for i in range(len(contours)):
        area_face=cv2.contourArea(contours[i])

        if max_area<area_face:
            max_area=area_face
            max_i=i
        try:
            c=contours[max_i]

        except:
            contours=[0]
            c=contours[0]
    return c



while 1 :

    ret,frame=cap.read()
    frame=cv2.flip(frame,1)

    roi=frame[100:550,150:600]#y1,y2 - x1,x2
    cv2.rectangle(frame,(150,100),(600,550),(255,115,12),0)

    hsv=cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)

    low_color=np.array([5,45,79],dtype=np.uint8)
    up_color=np.array([17,255,255],dtype=np.uint8)

    mask=cv2.inRange(hsv,low_color,up_color)



    kernel=np.ones((5,5),dtype=np.uint8)
    mask=cv2.dilate(mask,kernel,iterations=1)

    mask=cv2.medianBlur(mask,9)

    contours,_=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)


    if len(contours)>0:
        try:
            c=findMaxContours(contours)

            ext_left=tuple(c[c[:,:,0].argmin()][0])
            ext_right=tuple(c[c[:,:,0].argmax()][0])
            ext_top=tuple(c[c[:,:,1].argmin()][0])
            
            cv2.circle(roi,ext_left,5,(0,255,0),2)
            cv2.circle(roi,ext_right,5,(0,255,0),2)
            cv2.circle(roi,ext_top,5,(0,255,0),2)
            
            cv2.line(roi,ext_left,ext_top,(255,0,2),1)
            cv2.line(roi,ext_top,ext_right,(255,0,2),1)
            cv2.line(roi,ext_right,ext_left,(255,0,2),1)
            
            
        except: 
            pass
    else:
        pass


    cv2.imshow("pencere",frame)
    cv2.imshow("roi",roi)
    cv2.imshow("hsv",mask)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

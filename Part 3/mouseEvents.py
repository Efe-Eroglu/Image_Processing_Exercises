import cv2
import numpy as np

cap=cv2.VideoCapture(0)


circles=[]
def mouse(event,x,y,flags,params):
    
    if event==cv2.EVENT_LBUTTONDOWN:
        circles.append((x,y))


cv2.namedWindow("MouseCallBack")


cv2.setMouseCallback("MouseCallBack",mouse)


while 1:

    ret,frame=cap.read()
    frame=cv2.flip(frame,1)

    for center in circles:
        cv2.circle(frame,center,20,(0,255,0),-1)

    cv2.imshow("MouseCallBack",frame)   

    key=cv2.waitKey(1)

    if key==ord('c'):
        circles=[]

    elif key==ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
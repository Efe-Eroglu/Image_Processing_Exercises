import cv2
import numpy as np

cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()

    frame=cv2.flip(frame,1)
    if ret==0:
        break

        
    edges=cv2.Canny(frame,100,200)

    cv2.imshow("Kamera",frame)
    cv2.imshow("Kenar",edges)


    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
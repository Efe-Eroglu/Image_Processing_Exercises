import cv2

cv2.namedWindow("Deneme")

cap=cv2.VideoCapture(0)

cap.set(3,1280)
cap.set(4,720)

while 1:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    if ret==0:
        break


    cv2.imshow("Deneme",frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break 

cap.release()
cv2.destroyAllWindows()
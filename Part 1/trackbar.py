import cv2
import numpy as np

def nothing():
    pass


canvas=np.zeros((512,512,3),dtype=np.uint8)
cv2.namedWindow("Pencere")


cv2.createTrackbar("R","Pencere",0,255,nothing)
cv2.createTrackbar("G","Pencere",0,255,nothing)
cv2.createTrackbar("B","Pencere",0,255,nothing)
switch="0:OFF 1:ON"
cv2.createTrackbar(switch,"Pencere",0,1,nothing)


while True:
    cv2.imshow("Pencere",canvas)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

    s=cv2.getTrackbarPos(switch,"Pencere")
    if s ==0:
        canvas[:]=[0,0,0]
    else:
        r=cv2.getTrackbarPos("R","Pencere")
        g=cv2.getTrackbarPos("G","Pencere")
        b=cv2.getTrackbarPos("B","Pencere")

        canvas[:]=[b,g,r]

cv2.destroyAllWindows()
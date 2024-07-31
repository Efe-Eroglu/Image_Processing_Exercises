import cv2
import numpy as np

img=cv2.imread("text.png")
img1=cv2.imread("contour.png")

gray=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)

corner=cv2.goodFeaturesToTrack(gray,110,0.01,10)
gray=np.float32(gray)


corner=np.int0(corner)


for corners in corner:
    x,y=corners.ravel()
    cv2.circle(img1,(x,y),3,(0,0,255),-1)


cv2.imshow("pencere",img1)





cv2.waitKey(0)
cv2.destroyAllWindows()
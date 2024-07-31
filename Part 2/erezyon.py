import cv2
import numpy as np

img=cv2.imread("img.jpeg",0)


kernel=np.ones((5,5),np.uint8)
erosion=cv2.erode(img,kernel,iterations=2)
dilation=cv2.dilate(img,kernel,iterations=4)
opening=cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)



cv2.imshow("kalın",dilation)
cv2.imshow("erozyon",erosion)
cv2.imshow("morp",opening)

cv2.waitKey(0)
cv2.destroyAllWindows()
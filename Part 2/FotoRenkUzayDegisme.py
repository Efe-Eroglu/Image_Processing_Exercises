import cv2
import numpy as np

img=cv2.imread("bak.jpeg")
img1=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)



cv2.imshow("Pencere BGR",img)
cv2.imshow("Pencere RGB",img1)
cv2.imshow("Pencere hsv",img_hsv)
cv2.imshow("Pencere gray",img_gray)

cv2.waitKey(0)
cv2.destroyAllWindows()

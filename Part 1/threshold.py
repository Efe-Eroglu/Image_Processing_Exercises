import cv2
import numpy as np


img=cv2.imread("img.jpeg",0)


ret,th=cv2.threshold(img,147,155,cv2.THRESH_BINARY)

th2=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,31,11)
th3=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,31,11)



cv2.imshow("win3",th3)
cv2.imshow("pencere",th2)
cv2.imshow("win2",th)
# kamera açıp orda trackbarlar ile threshold yap
cv2.waitKey(0)
cv2.destroyAllWindows()
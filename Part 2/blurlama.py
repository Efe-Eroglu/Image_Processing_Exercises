import numpy as np
import cv2


img=cv2.imread("img.jpeg")

blur=cv2.blur(img,(9,9))
blur2=cv2.GaussianBlur(img,(5,5),cv2.BORDER_DEFAULT)
blur3=cv2.medianBlur(img,5)
blur4=cv2.bilateralFilter(blur2,9,95,95)

cv2.imshow("Pencere1",blur)
cv2.imshow("Pencere3",blur3)
cv2.imshow("Pencere2",blur2)
cv2.imshow("Pencere 4",blur4)


cv2.waitKey(0)
cv2.destroyAllWindows()
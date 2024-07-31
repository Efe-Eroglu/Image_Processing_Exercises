import cv2
import numpy as np

img=cv2.imread("bak.jpeg",0)
row,col=img.shape

# M=np.float32([[1,0,5],[0,1,70]])
# dst=cv2.warpAffine(img,M,(row,col))

M=cv2.getRotationMatrix2D((row/2,col/2),90,1)
dst=cv2.warpAffine(img,M,(col,row))

cv2.imshow("Pencere",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
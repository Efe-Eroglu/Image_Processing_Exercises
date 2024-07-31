import cv2
import numpy as np

img=cv2.imread("bitwise_1.png")
img2=cv2.imread("bitwise_2.png")


bitwise=cv2.bitwise_and(img,img2)
bitwise2=cv2.bitwise_xor(img,img2)
bitwise3=cv2.bitwise_not(img,img2)
bit_or=cv2.bitwise_or(img,img2)

cv2.imshow("or",bit_or)
cv2.imshow("not",bitwise3)
cv2.imshow("and",bitwise)
cv2.imshow("xor",bitwise2)


cv2.imshow("a",img)
cv2.imshow("b",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
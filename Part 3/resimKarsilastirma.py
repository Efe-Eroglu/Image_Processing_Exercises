import cv2
import numpy as np


img1=cv2.imread("aircraft.jpg")
img2=cv2.imread("aircraft1Kopya.jpg")

img1=cv2.resize(img1,(700,480))
img2=cv2.resize(img2,(700,480))

img3=cv2.medianBlur(img1,7)



diff=cv2.subtract(img3,img2)



if img3.shape==img2.shape:
    print("same size")

else:
    print("Not same")


b,g,r=cv2.split(diff)
if cv2.countNonZero(b)==0 and cv2.countNonZero(g)==0 and cv2.countNonZero(r)==0:
    print("Resimler eşit")

else:
    print("Eşit değil")




cv2.imshow("Image",diff)
# cv2.imshow("Image2",img2)




cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2

img=cv2.imread("img.jpeg")

# dimension=img.shape[:2]
# print(dimension)

# 200 400 200 600

roi=img[100:300, 530:700]
cv2.imshow("Roi",roi)

cv2.imshow("Pencere",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
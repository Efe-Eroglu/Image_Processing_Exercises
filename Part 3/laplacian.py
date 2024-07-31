import cv2

img=cv2.imread("starwars.jpg")


blur=cv2.medianBlur(img,9)

laplacian=cv2.Laplacian(blur,cv2.CV_64F).var()

if laplacian<500:
    print(laplacian)
    print("Resim blurludur")

cv2.imshow("Pencere",img)
cv2.imshow("Pencere2",blur)



cv2.waitKey(0)
cv2.destroyAllWindows()
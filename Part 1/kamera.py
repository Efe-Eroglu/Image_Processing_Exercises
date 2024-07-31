import cv2


cam=cv2.VideoCapture(0)# Farklı bir kamera kullanılacaksa 1.2 sırayla denenir

print(cam.get(3))#Genişlik
print(cam.get(4))#Yükseklik

cam.set(3,1024)
cam.set(4,768)



if not cam.isOpened():
    print("KAMERA TANINMADI")
    exit()

while True:
    ret,frame=cam.read()

    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    if not ret:
        print("Kameradan görüntü okunamıyor")
        break

    cv2.imshow("Kamera",frame)
    
    if cv2.waitKey(1) & 0xFF==ord("q"):
        print("Kamera sonlandırıldı")
        break
fps=cam.get(5)#fps değerini döndürür
print(fps)


cam.release()
cv2.destroyAllWindows()
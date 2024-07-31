import cv2

cam=cv2.VideoCapture("deneme.mp4")


while cam.isOpened():

    ret,frame=cam.read()

    if not ret:
        print("Kameradan görüntü alınamıyor")
        break

    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    cv2.imshow("Video",frame)

    if cv2.waitKey(1) & 0xFF== ord("q"):
        print("Video kapanıyor")
        break

cam.release()
cv2.destroyAllWindows()
import cv2

cam=cv2.VideoCapture(0)

fourrc=cv2.VideoWriter_fourcc(*'xVID')

out=cv2.VideoWriter("yenic.avi",fourrc,30.0,(640,480))


while cam.isOpened():

    ret,frame=cam.read()

    if not ret:
        print("Görüntü yok")
        break

    out.write(frame)

    cv2.imshow("Kamera",frame)

    if cv2.waitKey(1) == ord("q"):
        print("Kamera kapanıyor")
        break

cam.release()
out.release()
cv2.destroyAllWindows()


# import cv2

# cap=cv2.VideoCapture(0)
# fourrc=cv2.VideoWriter_fourcc(*'xVID')
# codec=cv2.VideoWriter_fourcc("W","M","V","2")
# filename="C:\\Users\\Efe\\Desktop\\deneme.avi"
# #Ters slastan sonra u yazılmaz python bunu komut olarak algılar
# camFps=30.0
# resolution=(640,480)

# videoFileOutput = cv2.VideoWriter(filename,fourrc,camFps,resolution)


# while True:
#     ret,frame=cap.read()
#     frame=cv2.flip(frame,1)

#     videoFileOutput.write(frame)



#     cv2.imshow("webcam kayıt",frame)

#     if cv2.waitKey(1) & 0xFF==ord('q'):
#         break


# videoFileOutput.release()
# cap.release()
# cv2.destroyAllWindows()
import cv2
import numpy as np

cap=cv2.VideoCapture("car.mp4")

subtractor=cv2.createBackgroundSubtractorMOG2(history=100,varThreshold=120,detectShadows=True)





while 1:
    ret,frame=cap.read()
    frame=cv2.resize(frame,(640,480))

    mask=subtractor.apply(frame)

    cv2.imshow("Frame",frame)
    cv2.imshow("mask",mask)

    if cv2.waitKey(20) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()




                    ##İkinci Yol##
# cap=cv2.VideoCapture("C:\\Users\\Efe\\Desktop\\Okul\\Genel Programlama Dersleri\\Python_Library\\OpenCv\\images\\car.mp4")


# f_ret,f_frame=cap.read()
# f_frame=cv2.resize(f_frame,(640,480))


# f_gray=cv2.cvtColor(f_frame,cv2.COLOR_BGR2GRAY)

# f_gray=cv2.GaussianBlur(f_gray,(5,5),0)


# while 1 :
    
#     ret,frame=cap.read()
#     frame=cv2.resize(frame,(640,480))
    
#     gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#     gray=cv2.GaussianBlur(gray,(5,5),0)
    

#     diff =cv2.absdiff(f_gray,gray)

#     _,diff=cv2.threshold(diff,61,255,cv2.THRESH_BINARY)


#     cv2.imshow("Pencere",frame)
#     cv2.imshow("Fark",diff)
#     cv2.imshow("First",f_frame)


#     if cv2.waitKey(20) & 0xFF==ord('q'):
#         break



# cap.release()
# cv2.destroyAllWindows()
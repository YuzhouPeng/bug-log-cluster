import cv2
print(2)
vc=cv2.VideoCapture("C:\\Users\\admin\Desktop\demotest.mp4")
c=1
if vc.isOpened():
    rval,frame=vc.read()
else:
    rval=False
while rval:
    rval,frame=vc.read()
    cv2.imwrite('C:\\Users\\admin\Desktop\opencv_picture\\'+str(c)+'.jpg',frame)
    c=c+1
    cv2.waitKey(1)
vc.release()
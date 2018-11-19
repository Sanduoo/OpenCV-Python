import  cv2 as  cv
import  numpy as np


def extrace_object_demo():
    capture = cv.VideoCapture("C:/1/001.mp4")
    while (True):
        ret, frame = capture.read()
        if ret == False:
            break
        hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
        lower_hsv = np.array([156,43,46])
        upper_hsv = np.array([180,255,255])
        mask = cv.inRange(hsv,lower_hsv,upper_hsv)
        dest = cv.bitwise_and(frame,frame,mask=mask)
        cv.imshow('mask', dest)
        cv.imshow('video', frame)
        c = cv.waitKey(50)
        if (c == 27):
            break



def color_space_demo(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    cv.imshow("gray",gray)
    hsv = cv.cvtColor(image,cv.COLOR_BGR2HSV)
    cv.imshow("hsv",hsv)
    yuv = cv.cvtColor(image,cv.COLOR_BGR2YUV)
    cv.imshow("yuv",yuv)
    Ycrcb = cv.cvtColor(image,cv.COLOR_BGR2YCrCb)
    cv.imshow("Ycrcb",Ycrcb)


src = cv.imread("C:/1/1.jpg")
cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
cv.imshow('input_image', src)
#get_image_info(src)
t1 = cv.getTickCount()
# inverse(src)
# create_image()
# create_image()
# color_space_demo(src)
extrace_object_demo()
t2 = cv.getTickCount()
time = (t2-t1)/cv.getTickFrequency()
print("time : %s ms"%(time*1000))
# gray = cv.cvtColor(src,cv.COLOR_BGR2GRAY)
#
#
# g,b,r, = cv.split(src)
# cv.imshow("green",g)
# cv.imshow("blue",b)
# cv.imshow("red",r)
#
# src[:,:,2]=0
# src = cv.merge([r,g,b])
# cv.imshow("changed image",src)
# cv.imwrite("C:/1/111.jpg",gray)
cv.waitKey(0)
cv.destroyAllWindows()
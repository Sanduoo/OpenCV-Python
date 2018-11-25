import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# 圆检测


def detcet_circles_demo(image):
    # dst = cv.pyrMeanShiftFiltering(image,10,100)      均值迁移（边缘过度模糊）
    dst = cv.bilateralFilter(image,0,100,30)            #高斯双边模糊
    cimage = cv.cvtColor(dst,cv.COLOR_BGR2GRAY)
    circles = cv.HoughCircles(cimage,cv.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=0)
    circle = np.uint16(np.around(circles))
    for i in circle[0,:]:
        cv.circle(image,(i[0],i[1]),i[2],(0,0,255),2)
        cv.circle(image,(i[0],i[1]),2,(0,0,255),2)
    cv.imshow("circle",image)


src = cv.imread("C:/1/image/stuff.jpg")
cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
cv.imshow("input_image",src)

detcet_circles_demo(src)

cv.waitKey(0)
cv.destroyAllWindows()


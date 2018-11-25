import cv2 as cv
import numpy as np

#边缘保留滤波(EPF)

#高斯双边模糊（磨皮）
def bi_demo(image):
    dest = cv.bilateralFilter(image,0,100,15)
    cv.imshow("bi_demo",dest)


#均值迁移（边缘过度模糊）油画
def shfit_demo(image):
    dest = cv.pyrMeanShiftFiltering(image,0,10,50)
    cv.imshow("shfit_demo",dest)


src = cv.imread("C:/1/1.jpg")
cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
cv.imshow("input_image",src)

shfit_demo(src)

cv.waitKey(0)
cv.destroyAllWindows()


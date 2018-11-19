import cv2 as cv
import cv2
# import numpy as np

def image_processing(image):
    grey_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)      #灰度处理

    kernel_size = 5
    blur_gray = cv2.GaussianBlur(grey_image, (kernel_size,kernel_size), 0)      #高斯模糊

    low_threshold = 200
    hight_threshold = 300
    edges = cv2.Canny(blur_gray,low_threshold,hight_threshold)      #边缘检测
    cv.imshow("edges",edges)


src = cv.imread("C:/1/whiteCarLaneSwitch.jpg")
cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
cv.imshow('input_image', src)

image_processing(src)

cv.waitKey(0)
cv.destroyAllWindows()

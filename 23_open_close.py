import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# 图像形态学操作——开闭操作

def open_close_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    # kerned = cv.getStructuringElement(cv.MORPH_ELLIPSE, (15, 1))    提取水平直线
    # kerned = cv.getStructuringElement(cv.MORPH_ELLIPSE, (1, 15))    提取竖直直线
    open_image = cv.morphologyEx(binary,cv.MORPH_OPEN,kernel)         #去除小的干扰块
    close_image = cv.morphologyEx(binary,cv.MORPH_CLOSE,kernel)       #填充闭合区域
    cv.imshow("open_image",open_image)
    cv.imshow("close_image",close_image)



src = cv.imread("C:/1/1.jpg")
cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
cv.imshow("input_image",src)

open_close_demo(src)

cv.waitKey(0)
cv.destroyAllWindows()


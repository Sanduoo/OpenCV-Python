import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# 形态学操作——膨胀与腐蚀

def erode_dilate_demo(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    ret,binary = cv.threshold(gray,0,255,cv.THRESH_BINARY | cv.THRESH_OTSU)
    # cv.imshow("binary image",binary)
    kerned = cv.getStructuringElement(cv.MORPH_RECT,(15,15))
    # erode_image = cv.erode(binary,kerned)
    # dilate_image = cv.dilate(binary,kerned)
    erode_image = cv.erode(image, kerned)         #彩色图像也可以
    dilate_image = cv.dilate(image, kerned)
    cv.imshow("erode image",erode_image)
    cv.imshow("dilate image",dilate_image)





src = cv.imread("C:/1/1.jpg")
cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
cv.imshow("input_image",src)

erode_dilate_demo(src)

cv.waitKey(0)
cv.destroyAllWindows()


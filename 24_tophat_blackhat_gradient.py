import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# 其他形态学操作：顶帽tophat，黑帽blackhat，形态学梯度gradient

def tophat_blackhat_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    tophat = cv.morphologyEx(gray,cv.MORPH_TOPHAT,kernel)
    blackhat = cv.morphologyEx(gray,cv.MORPH_BLACKHAT,kernel)
    cimage = np.array(gray.shape,np.uint8)
    cimage = 100
    tophat = cv.add(tophat,cimage)
    blackhat = cv.add(blackhat,cimage)
    cv.imshow("blackhat",blackhat)
    cv.imshow("tophat",tophat)

def gradient_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    gradient = cv.morphologyEx(gray, cv.MORPH_GRADIENT, kernel)
    cv.imshow("gradient", gradient)


def gradient_demo2(image):
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    dm = cv.dilate(image,kernel)
    em = cv.erode(image,kernel)
    internal_gradient = cv.subtract(image,em)       #内梯度（轮廓变小）
    external_gradient = cv.subtract(dm,image)       #外梯度（轮廓变大）
    cv.imshow("internal_gradient", internal_gradient)
    cv.imshow("external_gradient", external_gradient)



src = cv.imread("C:/1/1.jpg")
cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
cv.imshow("input_image",src)

gradient_demo2(src)

cv.waitKey(0)
cv.destroyAllWindows()


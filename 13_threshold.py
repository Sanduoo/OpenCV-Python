import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

#图像二值化

def threshold_demo(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    ret,binary = cv.threshold(gray,0,255,cv.THRESH_BINARY|cv.THRESH_OTSU)
    print("threshold value is %s"%ret)
    cv.imshow("threshold_demo",binary)


def local_threshold(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    binary = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY_INV,25,10)
    cv.imshow("local_threshold",binary)


def custom_threshold(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    mean = gray.mean()
    ret, binary = cv.threshold(gray, mean, 255, cv.THRESH_BINARY)
    print("threshold value is %s" % ret)
    cv.imshow("custom_threshold", binary)


src = cv.imread("C:/1/1.jpg")
cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
cv.imshow("input_image",src)

custom_threshold(src)

cv.waitKey(0)
cv.destroyAllWindows()



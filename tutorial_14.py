import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def big_image_binary(image):
    print(image.shape)
    cw = 256
    ch = 256
    h,w = image.shape[:2]
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    for row in range(0,h,ch):
        for col in range(0,w,cw):
            roi = gray[row:row+ch,col:col+cw]
            ret,dst = cv.threshold(roi,0,255,cv.THRESH_BINARY|cv.THRESH_OTSU)
            gray[row:row + ch, col:col + cw] =dst
            print((np.std(dst)),np.mean(dst))
    cv.imwrite("C:/1/text.png",gray)


def big_image_binary2(image):
    print(image.shape)
    cw = 256
    ch = 256
    h,w = image.shape[:2]
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    for row in range(0,h,ch):
        for col in range(0,w,cw):
            roi = gray[row:row+ch,col:col+cw]
            dst = cv.adaptiveThreshold(roi,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,127,20)
            gray[row:row + ch, col:col + cw] =dst
            print((np.std(dst)),np.mean(dst))
    cv.imwrite("C:/1/text.png",gray)


def big_image_binary3(image):
    print(image.shape)
    cw = 256
    ch = 256
    h,w = image.shape[:2]
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    for row in range(0,h,ch):
        for col in range(0,w,cw):
            roi = gray[row:row+ch,col:col+cw]
            dev = np.std(roi)
            if dev < 15:
                gray[row:row + ch, col:col + cw] =255
            else:
                dst = cv.adaptiveThreshold(roi,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,127,20)
                gray[row:row + ch, col:col + cw] = dst
    cv.imwrite("C:/1/text.png",gray)


src = cv.imread("C:/1/1118.png")
cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
cv.imshow("input_image",src)

big_image_binary2(src)

cv.waitKey(0)
cv.destroyAllWindows()


import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


#Canny边缘提取

def edge_demo(image):
    blarred = cv.GaussianBlur(image,(3,3),0)
    gray = cv.cvtColor(blarred,cv.COLOR_BGR2GRAY)
    # # X Gradient
    # gray_x = cv.Sobel(gray,cv.CV_16SC1,1,0)
    # # Y Gradient
    # gray_y = cv.Sobel(gray,cv.CV_16SC1,0,1)
    # Edge
    # edge_output = cv.Canny(gray_x,gray_y,50,150)
    edge_output = cv.Canny(gray,50,150)
    return  edge_output

# 轮廓发现

def contours_demo(image):

    """""
    dst = cv.GaussianBlur(image,(3,3),0)
    gray = cv.cvtColor(dst,cv.COLOR_BGR2GRAY)
    ret,binary = cv.threshold(gray,0,255,cv.THRESH_BINARY | cv.THRESH_OTSU)
    """""
    binary = edge_demo(image)

    cv.imshow("binary image",binary)

    # cloneImage,contours,heriachy = cv.findContours(binary,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
    cloneImage,contours,heriachy = cv.findContours(binary,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    for i,contour in enumerate(contours):
        cv.drawContours(image,contours,i,(0,0,255),2)
        # cv.drawContours(image,contours,i,(0,0,255),-1)
        print(i)
    cv.imshow("detect contours",image)




src = cv.imread("C:/1/image/stuff.jpg")
cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
cv.imshow("input_image",src)

contours_demo(src)

cv.waitKey(0)
cv.destroyAllWindows()


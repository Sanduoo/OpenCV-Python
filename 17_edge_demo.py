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
    cv.imshow("edge_output",edge_output)




src = cv.imread("C:/1/1.jpg")
cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
cv.imshow("input_image",src)

edge_demo(src)

cv.waitKey(0)
cv.destroyAllWindows()


import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

#直线检测-伙夫直线变换


def line_detection(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    edges = cv.Canny(gray,50,150,apertureSize=3)
    lines = cv.HoughLines(edges,1,np.pi/180,150)
    for line in lines:
        rho,theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0= a*rho
        y0= b*rho
        x1= int(x0+1000*(-b))
        y1= int(y0+1000*(a))
        x2= int(x0-1000*(-b))
        y2= int(y0-1000*(a))
        cv.line(image,(x1,y1),(x2,y2),(0,0,255),2)
    cv.imshow("image_line",image)


def line_detect_possible(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    edges = cv.Canny(gray, 50, 150, apertureSize=3)
    lines = cv.HoughLinesP(edges, 1, np.pi / 180, 100,minLineLength=50,maxLineGap=10)
    for line in lines:
        x1,y1,x2,y2 = line[0]
        cv.line(image,(x1,y1),(x2,y2),(0,0,255),2)
    cv.imshow("image_line",image)


src = cv.imread("C:/1/image/sudoku.png")
cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
cv.imshow("input_image",src)

line_detect_possible(src)

cv.waitKey(0)
cv.destroyAllWindows()


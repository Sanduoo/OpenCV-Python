import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

#图像梯度

def sobel_demo(image):
    grad_x = cv.Sobel(image,cv.CV_32F,0,1)
    grad_y = cv.Sobel(image,cv.CV_32F,1,0)
    gradx = cv.convertScaleAbs(grad_x)
    grady = cv.convertScaleAbs(grad_y)
    cv.imshow("gradx",gradx)
    cv.imshow("grady",grady)
    gradxy = cv.addWeighted(gradx,0.5,grady,0.5,0)
    cv.imshow("gradxy",gradxy)


def scharr_demo(image):
    grad_x = cv.Scharr(image,cv.CV_32F,0,1)
    grad_y = cv.Scharr(image,cv.CV_32F,1,0)
    gradx = cv.convertScaleAbs(grad_x)
    grady = cv.convertScaleAbs(grad_y)
    cv.imshow("gradx",gradx)
    cv.imshow("grady",grady)
    gradxy = cv.addWeighted(gradx,0.5,grady,0.5,0)
    cv.imshow("gradxy",gradxy)


def laplacian_demo(image):
    # dst = cv.Laplacian(image,cv.CV_32F)
    # lpls = cv.convertScaleAbs(dst)
    # 自定义算子
    kernel = np.array([[1,1,1],[1,-8,1],[1,1,1]])
    lpls = cv.filter2D(image,cv.CV_32F,kernel=kernel)
    cv.imshow("laplacian",lpls)


src = cv.imread("C:/1/1.jpg")
cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
cv.imshow("input_image",src)

scharr_demo(src)

cv.waitKey(0)
cv.destroyAllWindows()


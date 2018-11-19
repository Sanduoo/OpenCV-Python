import cv2 as cv
import numpy as np


# 均值模糊：去掉随机噪声
def blue_demo(image):
    dest = cv.blur(image,(5,5))
    cv.imshow("blue_demo",dest)

# 中值模糊：去掉椒盐噪声
def median_blue_demo(image):
    dest = cv.medianBlur(image,5)
    cv.imshow("median_blue_demo",dest)

# 自定义模糊锐化
def custom_blue_demo(image):
    # kernel = np.ones([5,5],np.float32)/25
    kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
    dest = cv.filter2D(image,-1,kernel=kernel)
    cv.imshow("custom_blue_demo",dest)


src = cv.imread("C:/1/1.jpg")
cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)

# median_blue_demo(src)
# blue_demo(src)
custom_blue_demo(src)

cv.waitKey(0)
cv.destroyAllWindows()


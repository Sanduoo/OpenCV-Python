import cv2 as cv
import numpy as np

#ROI与泛洪填充

def fill_color_demo(image):
    copyImg = image.copy()
    h,w = image.shape[:2]
    mask = np.zeros([h+2,w+2],np.uint8)
    cv.floodFill(copyImg,mask,(30,30),(0,255,255),(100,100,100),(50,50,50),cv.FLOODFILL_FIXED_RANGE)
    #floodFill(1.操作的图像,2.掩模,3.起始像素值,4.填充的颜色,5.填充颜色的低值,6.填充颜色的高值,7.填充的方法)
    cv.imshow("fill_color_demo",copyImg)


def fill_binary_demo(image):
    image = np.zeros([400,400,3],np.uint8)
    image[100:300,100:300,:] = 255
    cv.imshow("fill_binary",image)
    mask = np.ones([402,402,1],np.uint8)
    mask[101:301,101:301] = 0
    cv.floodFill(image,mask,(200,200),(0,255,255),cv.FLOODFILL_MASK_ONLY)
    cv.imshow("fill_color_demo",image)


src = cv.imread("C:/1/image/lena.jpg")
cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
cv.imshow('input_image', src)

"""
face = src[200:400,200:400]
gray = cv.cvtColor(face,cv.COLOR_BGR2GRAY)
backface = cv.cvtColor(gray,cv.COLOR_GRAY2BGR)
src[200:400,200:400] = backface
cv.imshow("face",src)
"""

# fill_color_demo(src)
fill_binary_demo(src)


cv.waitKey(0)
cv.destroyAllWindows()

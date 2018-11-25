import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

#图像直方图(histogram)

def plot_demo(image):
    plt.hist(image.ravel(),256,[0,256])
    plt.show()

def image_plot_demo(image):
    color = ('blue','green','red')
    for i,color in enumerate(color):
        hist = cv.calcHist([image],[i],None,[256],[0,256])
        plt.plot(hist,color=color)
        plt.xlim([0,256])
    plt.show()


src = cv.imread("C:/1/1.jpg")
cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
cv.imshow("input_image",src)

image_plot_demo(src)

cv.waitKey(0)
cv.destroyAllWindows()

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# 圆检测




src = cv.imread("C:/1/1.jpg")
cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
cv.imshow("input_image",src)



cv.waitKey(0)
cv.destroyAllWindows()


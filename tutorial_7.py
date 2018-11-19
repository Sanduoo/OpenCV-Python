import cv2 as cv
import numpy as np


def clam(pv):
    if pv>255:
        return 255
    if pv<0:
        return 0
    else:
        return pv


def gaussian_noise(image):
    w,h,c = image.shape
    for row in range(h):
        for col in range(w):
            s = np.random.normal(0,20,3)    #0均值，20标准差，3size
            b = image[row,col,0]    #blue
            g = image[row,col,1]    #green
            r = image[row,col,2]    #red
            image[row,col,0] = clam(b+s[0])
            image[row,col,1] = clam(g+s[1])
            image[row,col,2] = clam(r+s[2])
    cv.imshow("gaussian_noise",image)


src = cv.imread("C:/1/1.jpg")
cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
cv.imshow("input_image",src)

# gaussian_noise(src)

dest = cv.GaussianBlur(src,(5,5),0)
cv.imshow("GaussianBlur",dest)

cv.waitKey(0)
cv.destroyAllWindows()


import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# 分水岭算法  距离变换(Distance Transform)

def watershed_demo(image):

    #remove noise if any
    blue = cv.pyrMeanShiftFiltering(image,10,100)
    print(image.shape)
    
    #gray/binary image
    gray = cv.cvtColor(blue,cv.COLOR_BGR2GRAY)
    ret,binary = cv.threshold(gray,0,255,cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow("binary",binary)

    # marphology operation
    kernel = cv.getStructuringElement(cv.MORPH_RECT,(1,1))
    mb = cv.morphologyEx(binary,cv.MORPH_OPEN,kernel,iterations=2)
    sure_bg = cv.dilate(mb,kernel,iterations=3)
    cv.imshow("sure_bg",sure_bg)

    #distance transfore  曼哈顿（棋盘格）距离和欧几里德距离
    dist = cv.distanceTransform(mb,cv.DIST_L2,3)
    dist_out = cv.normalize(dist,0,1.0,cv.NORM_MINMAX)
    cv.imshow("distanceTransform",dist_out)
    ret,surface = cv.threshold(dist,dist.max()*0.6,255,cv.THRESH_BINARY)
    cv.imshow("surface-binary",surface)
    surface_fg = np.uint8(surface)
    unknown = np.subtract(sure_bg,surface_fg)
    ret,markers = cv.connectedComponents(surface_fg)
    print(ret)

    #watersheld transform
    markers = markers +1
    markers[unknown == 255] = 0
    markers = cv.watershed(image,markers=markers)
    image[markers==-1] = [0,0,255]
    cv.imshow("result",image)








src = cv.imread("C:/1/coin.jpg")
cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
cv.imshow("input_image",src)

watershed_demo(src)

cv.waitKey(0)
cv.destroyAllWindows()


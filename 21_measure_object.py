import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# 对象检测

def measure_object(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    ret,binary = cv.threshold(gray,0,255,cv.THRESH_BINARY | cv.THRESH_OTSU)     #二值图
    print('threshold value %s'%ret)
    cv.imshow("binary image",binary)
    dst = cv.cvtColor(binary,cv.COLOR_GRAY2BGR)
    # 找到轮廓
    outImage,contours,hireachy = cv.findContours(binary,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    for i,contour in enumerate(contours):
        area = cv.contourArea(contour)          #每个轮廓的面积
        x,y,w,h = cv.boundingRect(contour)      #轮廓的外接矩形
        mm = cv.moments(contour)
        print(type(mm))
        cx = mm['m01']/mm['m00']
        cy = mm['m10']/mm['m00']
        cv.circle(dst,(np.int(cx),np.int(cy)),2,(0,255,255),-1)
        cv.rectangle(dst,(x,y),(x+w,x+h),(0,0,255),2)
        print('contour area %s'%area)
        approxCure = cv.approxPolyDP(contour,4,True)
        if approxCure.shape[0] > 6:
            cv.drawContours(dst,contours,i,(0,255,0),2)
        if approxCure.shape[0] == 4:
            cv.drawContours(dst,contours, i, (0, 0, 255), 2)
        if approxCure.shape[0] == 3:
            cv.drawContours(dst,contours,i,(255,0,0),2)
    cv.imshow("measure_contour",dst)






src = cv.imread("C:/1/image/detect_blob.png")
cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
cv.imshow("input_image",src)

measure_object(src)

cv.waitKey(0)
cv.destroyAllWindows()


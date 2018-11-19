import cv2 as cv
import numpy as np


#加减乘除
def add_demo(m1,m2):
    dest = cv.add(m1,m2)
    cv.imshow("add_demo",dest)

def subtract_demo(m1,m2):
    dest = cv.subtract(m1,m2)
    cv.imshow("subtract_demo", dest)

def multiply_demo(m1,m2):
    dest = cv.multiply(m1,m2)
    cv.imshow("multiply_demo", dest)

def divide_demo(m1,m2):
    dest = cv.divide(m1,m2)
    cv.imshow("divide_demo", dest)


#均值，方差
def others(m1,m2):
    # M1 = cv.mean(m1)          均值
    # M2 = cv.mean(m2)
    M1,dev1 = cv.meanStdDev(m1)         #均值，方差（对比度）
    M2,dev2 = cv.meanStdDev(m2)
    h,w = m1.shape[:2]

    print(M1)
    print(dev1)
    print(M2)
    print(dev2)

    img = np.zeros([h,w],np.uint8)
    m,dev = cv.meanStdDev(img)
    print(m)
    print(dev)


#逻辑操作
def logiv_demo(m1,m2):
    dest = cv.bitwise_xor(m1,m2)    #异或
    # dest = cv.bitwise_and(m1,m2)  与
    # dest = cv.bitwise_or(m1,m2)   或
    # dest = cv.bitwise_not(m1)     取反

    cv.imshow("logiv_demo", dest)




src1 = cv.imread("C:/1/LinuxLogo.jpg")
src2 = cv.imread("C:/1/WindowsLogo.jpg")
cv.namedWindow('image1', cv.WINDOW_AUTOSIZE)
cv.imshow('image1', src1)
cv.imshow('image2', src2)
print(src1.shape)
print(src2.shape)

# add_demo(src1,src2)
# subtract_demo(src1,src2)
# divide_demo(src1,src2)
# multiply_demo(src1,src2)

others(src1,src2)
logiv_demo(src1,src2)

# gray = cv.cvtColor(src,cv.COLOR_BGR2GRAY)
# cv.imwrite("C:/1/111.jpg",gray)
cv.waitKey(0)
cv.destroyAllWindows()

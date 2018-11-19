import cv2 as cv
import numpy as np      #Python科学技术np包


def video_demo():
    capture = cv.VideoCapture(0)
    while(True):
        ret,frame = capture.read()
        frame = cv.flip(frame,1)
        cv.imshow('video',frame)
        c = cv.waitKey(50)
        if(c == 27):
            break


def get_image_info(image):
    print(type(image))
    print(image.size)
    print(image.shape)
    print(image.dtype)
    print(np.array(image))      # 矩阵数组

src = cv.imread("C:/1/1.jpg")
cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
cv.imshow('input_image', src)
get_image_info(src)
gray = cv.cvtColor(src,cv.COLOR_BGR2GRAY)
cv.imwrite("C:/1/111.jpg",gray)
cv.waitKey(0)
cv.destroyAllWindows()

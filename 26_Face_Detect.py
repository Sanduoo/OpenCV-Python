import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# 人脸检测  HAAR（小数）-LBP（整数）

def face_detect_demo(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    face_detector = cv.CascadeClassifier("C:/1/haarcascade_frontalface_alt_tree.xml")
    faces = face_detector.detectMultiScale(gray,1.1,2)
    for x,y,w,h in faces:
        cv.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)
    cv.imshow("face_detector",image)

def video_face_detect():

    while(True):
        ret,frame = capture.read()
        frame = cv.flip(frame,1)
        face_detect_demo(frame)
        c = cv.waitKey(10)
        if c == 27:
            break


# src = cv.imread("C:/1/1.jpg")
# cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
# cv.namedWindow("")
# cv.imshow("input_image",src)
capture = cv.VideoCapture(0)
cv.namedWindow('face_detector', cv.WINDOW_AUTOSIZE)
video_face_detect()

cv.waitKey(0)
cv.destroyAllWindows()


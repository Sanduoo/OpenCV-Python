import cv2 as cv

src = cv.imread("C:/1/1.jpg")
#读取这个路径的图片，注意这里的路径必须全是英文，不能有中文
#但是分隔符\是随意的，还可以是/ \\ //形式的（在python3至少是这样）

cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
#namedWindow函数，用于创建一个窗口，默认值为WINDOW_AUTOSIZE
#所以一般情况下，这个函数我们填第一个变量就可以了。
# 其实这一行代码没有也可以正常显示的（下面imshow会显示）

cv.imshow('input_image', src)
#在指定的窗口中显示一幅图像

cv.waitKey(0)
#参数=0: （也可以是小于0的数值）一直显示，不会有返回值
#若在键盘上按下一个键即会消失，则会返回一个按键对应的ascii码值
#　　　 参数>0:显示多少毫秒        超过这个指定时间则返回-1

cv.destroyAllWindows()
#删除建立的全部窗口，释放资源

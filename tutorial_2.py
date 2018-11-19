import cv2 as cv
import numpy as np

def access_pixels(image):
    print(image.shape)      #图像的宽高的维t度
    height = image.shape[0]
    width =image.shape[1]
    channels = image.shape[2]       #三个色彩通道（blue、green、red）
    print("height:%s,width:%s,channels:%s"%(height,width,channels))
    for row in range(width):
        for col in range(height):
            for c in range(channels):
                pv = image[row,col,c]
                image[row,col,c] = 255-pv
    cv.imshow("pixels_demo",image)


def inverse(image):
    dst = cv.bitwise_not(image)
    cv.imshow("inverse demo",dst)


def create_image():

    # img = np.zeros([400,400,3],np.uint8)
    # img[:,:,0] = np.ones([400,400])*255
    # cv.imshow("new image",img)

    # img = np.zeros([400,400,1],np.uint8)
    # img[:,:,0] = np.ones([400,400])*127
    img = np.ones([400, 400, 1], np.uint8)
    img = img*127
    cv.imshow("new image",img)

    m1 = np.ones([3,3],np.float)
    m1.fill(233.3333333)
    print(m1)

    m2 = m1.reshape([1,9])
    print(m2)

    m3 = np.array([[1,2,3],[3,4,5],[5,6,7]],np.int32)
    m3.fill(9)
    print(m3)

src = cv.imread("C:/1/1.jpg")
# cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
# cv.imshow('input_image', src)
#get_image_info(src)
t1 = cv.getTickCount()
#inverse(src)
#create_image()
create_image()
t2 = cv.getTickCount()
time = (t2-t1)/cv.getTickFrequency()
print("time : %s ms"%(time*1000))
gray = cv.cvtColor(src,cv.COLOR_BGR2GRAY)
# cv.imwrite("C:/1/111.jpg",gray)
cv.waitKey(0)
cv.destroyAllWindows()
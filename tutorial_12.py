import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def template_demo():
    tpl = cv.imread("C:/1/image/small2.jpg")
    target = cv.imread("C:/1/image/big.jpg")
    cv.imshow("tpl", tpl)
    cv.imshow("target", target)

    methods = [cv.TM_CCOEFF_NORMED,cv.TM_CCORR_NORMED,cv.TM_SQDIFF_NORMED]#TM_SQDIFF_NORMED平方最准
    th,tw = tpl.shape[:2]
    for md in methods:
        result = cv.matchTemplate(target,tpl,md)
        min_val,max_val,min_col,max_col = cv.minMaxLoc(result)
        if md == cv.TM_SQDIFF_NORMED:
            tl = min_col
        else:
            tl = max_col
        br = (tl[0]+th,tl[1]+tw)
        cv.rectangle(target,tl,br,[0,0,255],2)
        cv.imshow("match-"+np.str(md),target)





src = cv.imread("C:/1/1.jpg")
cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
cv.imshow("input_image",src)

template_demo()

cv.waitKey(0)
cv.destroyAllWindows()


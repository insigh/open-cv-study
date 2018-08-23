import cv2 as cv
import numpy as np


def bi_lateral_blur(image):
    # 双边模糊 高斯双边
    dst = cv.bilateralFilter(src=image, d=5, sigmaColor=15, sigmaSpace=15)
    cv.imshow(winname="bi_lateral_blur image", mat= dst)


def shift_blur(image):
    # mean shift filter 均值迁移
    # 可以使图片变得更加平滑，不粗糙
    dst = cv.pyrMeanShiftFiltering(src=image, sp=5, sr=20, maxLevel=3)
    cv.imshow("shift demo", mat=dst)


print("=========hello python!==========")
src = cv.imread(filename="C:\\Users\zcj\Desktop\docum\photos\8776db91659bf1b9abada9bbc9d9f15d0b085642.jpg")
cv.namedWindow(winname="input image", flags=cv.WINDOW_AUTOSIZE)
cv.imshow(winname="input image", mat=src)
print("=========Functions start here!==========")
bi_lateral_blur(image=src)
shift_blur(image=src)
print("=========Functions end here!==========")
cv.waitKey(0)
cv.destroyAllWindows()


import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def threshold_demo(image):
    # global threshold
    gray = cv.cvtColor(src=image, code=cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(src=gray, thresh=0, maxval=255, type=cv.THRESH_OTSU)
    print("threshold value", ret)
    cv.imshow(winname="Binary Image", mat=binary)


def local_threshold(image):
    gray = cv.cvtColor(src=image, code=cv.COLOR_BGR2GRAY)
    dst = cv.adaptiveThreshold(src=gray, maxValue=255, adaptiveMethod=cv.ADAPTIVE_THRESH_GAUSSIAN_C, thresholdType=cv.THRESH_BINARY, blockSize=35, C=5)
    cv.imshow("Local Binary Image", mat=dst)


def custom_threshold(image):
    gray = cv.cvtColor(src=image, code=cv.COLOR_BGR2GRAY)
    h, w = gray.shape
    gray.reshape([1, h*w])
    mean = np.sum(gray)/(h*w)
    ret, binary = cv.threshold(src=gray, thresh=mean, maxval=255, type=cv.THRESH_BINARY)
    cv.imshow(winname="Custom Binary Threshold", mat=binary)


print("=========hello python!==========")
src = cv.imread(filename="C:\\Users\zcj\Desktop\docum\photos\8776db91659bf1b9abada9bbc9d9f15d0b085642.jpg")
# cv.namedWindow(winname="input image", flags=cv.WINDOW_AUTOSIZE)
# cv.imshow(winname="input image", mat=src)
print("=========Functions start here!==========")
# threshold_demo(image=src)
local_threshold(image=src)
custom_threshold(image=src)
print("=========Functions end here!==========")
cv.waitKey(0)
cv.destroyAllWindows()

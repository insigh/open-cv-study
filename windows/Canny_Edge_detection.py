import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def canny_demo(image):
    blurred = cv.GaussianBlur(src=image, ksize=(3, 3), sigmaX=10, sigmaY=10)
    gray = cv.cvtColor(src=blurred, code=cv.COLOR_BGR2GRAY)
    # gradient
    grad_x = cv.Sobel(src=gray, ddepth=cv.CV_16SC1, dx=1, dy=0)
    grad_y = cv.Sobel(src=gray, ddepth=cv.CV_16SC1, dx=0, dy=1)
    # canny
    # edge_output = cv.Canny(dx=grad_x, dy=grad_y, threshold1=50, threshold2=150)
    # 双阈值
    edge_output = cv.Canny(image=gray, threshold1=50, threshold2=100)
    cv.imshow(winname="canny edge detection:", mat=edge_output)


src = cv.imread(filename="C:\\Users\zcj\Desktop\docum\photos\8776db91659bf1b9abada9bbc9d9f15d0b085642.jpg")
canny_demo(image=src)
cv.waitKey(0)
cv.destroyAllWindows()
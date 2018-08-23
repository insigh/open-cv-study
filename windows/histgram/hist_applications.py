import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def global_equalize_hist(image):
    # global contrast adjustment
    gray = cv.cvtColor(src=image, code=cv.COLOR_BGR2GRAY)
    dst = cv.equalizeHist(src=gray)
    cv.imshow(winname="global_equalizeHist", mat=dst)


def clahe(image):
    # local contrast adjustment
    gray = cv.cvtColor(src=image, code=cv.COLOR_BGR2GRAY)
    clahe = cv.createCLAHE(clipLimit=5, tileGridSize=(8, 8))
    dst = clahe.apply(gray)
    cv.imshow(winname="clahe", mat=dst)


print("=========hello python!==========")
src = cv.imread(filename="C:\\Users\zcj\Desktop\docum\photos\8776db91659bf1b9abada9bbc9d9f15d0b085642.jpg")
cv.namedWindow(winname="input image", flags=cv.WINDOW_AUTOSIZE)
cv.imshow(winname="input image", mat=src)
print("=========Functions start here!==========")
global_equalize_hist(image=src)
print("=========Functions end here!==========")
cv.waitKey(0)
cv.destroyAllWindows()


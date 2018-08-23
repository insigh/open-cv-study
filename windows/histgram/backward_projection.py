import cv2 as cv
import numpy as np


def hist2d_demo(image):
    hsv = cv.cvtColor(src=image, code=cv.COLOR_BGR2HSV)
    hist = cv.calcHist(images=[hsv], channels=[0, 1], histSize=[100, 256], ranges=[0, 180, 0, 256], mask=None)



print("=========hello python!==========")
src = cv.imread(filename="C:\\Users\zcj\Desktop\docum\photos\8776db91659bf1b9abada9bbc9d9f15d0b085642.jpg")
cv.namedWindow(winname="input image", flags=cv.WINDOW_AUTOSIZE)
cv.imshow(winname="input image", mat=src)
print("=========Functions start here!==========")

print("=========Functions end here!==========")
cv.waitKey(0)
cv.destroyAllWindows()


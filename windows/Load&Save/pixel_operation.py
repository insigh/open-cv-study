import cv2 as cv
import numpy as np

# def




print("------------hello,python------------")
src = cv.imread("C:\\Users\zcj\Desktop\docum\photos\8776db91659bf1b9abada9bbc9d9f15d0b085642.jpg")
print(type(src))
cv.namedWindow(winname="input image", flags=cv.WINDOW_AUTOSIZE)
cv.imshow(winname="input image", mat=src)

cv.waitKey(0)
cv.destroyAllWindows()
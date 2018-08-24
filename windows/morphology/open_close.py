import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def open_operation(image):
    # erode + dilate
    # usage: delete small noise region
    # AND
    print(image.shape)
    gray = cv.cvtColor(src=image, code=cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(src=gray, thresh=0, maxval=256, type=cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow(winname="binary", mat=binary)
    kernel = cv.getStructuringElement(shape=cv.MORPH_RECT, ksize=(5, 5))
    open_operated = cv.morphologyEx(src=binary, op=cv.MORPH_OPEN, kernel=kernel)
    cv.imshow(winname="open_operation", mat=open_operated)


def close_operation(image):
    # dilate + erode
    # usage: fulfill small closed region
    # AND
    gray = cv.cvtColor(src=image, code=cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(src=gray, thresh=0, maxval=256, type=cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow(winname="binary", mat=binary)
    kernel = cv.getStructuringElement(shape=cv.MORPH_RECT, ksize=(3, 3))
    close_operated = cv.morphologyEx(src=binary, op=cv.MORPH_CLOSE, kernel=kernel)
    cv.imshow(winname="close_operated", mat=close_operated)


src = cv.imread(filename=r"C:\Users\zcj\Desktop\videos\open_close.jpg")
cv.imshow(winname="input", mat=src)
close_operation(image=src)
cv.waitKey(0)
cv.destroyAllWindows()
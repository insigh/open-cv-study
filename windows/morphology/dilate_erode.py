import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def erode(image):
    gray = cv.cvtColor(src=image, code=cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(src=gray, thresh=0, maxval=256, type=cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    cv.imshow(winname="binary", mat=binary)
    kernel = cv.getStructuringElement(shape=cv.MORPH_RECT, ksize=(3, 3))
    dst = cv.erode(src=binary, kernel=kernel)
    cv.imshow(winname="eroded image", mat=dst)


def dilate(image):
    gray = cv.cvtColor(src=image, code=cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(src=gray, thresh=0, maxval=256, type=cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    cv.imshow(winname="binary", mat=binary)
    kernel = cv.getStructuringElement(shape=cv.MORPH_RECT, ksize=(5, 5))
    dst = cv.dilate(src=binary, kernel=kernel)
    cv.imshow(winname="dilated image", mat=dst)


src = cv.imread(filename=r"C:\Users\zcj\Desktop\videos\cat.jpg")
cv.imshow(winname="input", mat=src)
# dilate(image=src)
kernel = cv.getStructuringElement(shape=cv.MORPH_RECT, ksize=(3, 3))
dst = cv.erode(src=src, kernel=kernel)
cv.imshow(winname="dilated cat", mat=dst)
cv.waitKey(0)
cv.destroyAllWindows()
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def tophat_operation(image):
    # eroded - src
    gray = cv.cvtColor(src=image, code=cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(src=gray, thresh=0, maxval=256, type=cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow(winname="binary", mat=binary)
    kernel = cv.getStructuringElement(shape=cv.MORPH_RECT, ksize=(15, 15))
    dst = cv.morphologyEx(src=binary, op=cv.MORPH_TOPHAT, kernel=kernel)
    dst2 = np.ones(gray.shape, np.uint8)
    dst2 *= 200
    cv.add(src1=dst, src2=dst2)
    cv.imshow(winname="tophat_operated", mat=dst)




def blackhat_operation(image):
    # dilated - src
    gray = cv.cvtColor(src=image, code=cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(src=gray, thresh=0, maxval=256, type=cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow(winname="binary", mat=binary)
    kernel = cv.getStructuringElement(shape=cv.MORPH_RECT, ksize=(15, 15))
    dst = cv.morphologyEx(src=binary, op=cv.MORPH_BLACKHAT, kernel=kernel)
    cv.imshow(winname="blackhat_operated", mat=dst)


def morphology_gradient(image):
    # primry: dilated - eroded
    # inner : src - eroded
    # outer : dilated - src

    gray = cv.cvtColor(src=image, code=cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(src=gray, thresh=0, maxval=256, type=cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow(winname="binary", mat=binary)
    kernel = cv.getStructuringElement(shape=cv.MORPH_RECT, ksize=(5, 5))
    dst = cv.morphologyEx(src=binary, op=cv.MORPH_GRADIENT, kernel=kernel)
    cv.imshow(winname="morphology_gradient", mat=dst)


def inner_gradient(image):
    kernel = cv.getStructuringElement(shape=cv.MORPH_RECT, ksize=(5, 5))
    dm = cv.dilate(src=image, kernel=kernel)
    em = cv.erode(src=image, kernel=kernel)
    cv.imshow(winname="dilated image", mat=dm)
    cv.imshow(winname="eroded image", mat=em)
    dst1 = cv.subtract(src1=image, src2=em)  # inner gradient
    dst2 = cv.subtract(src1=dm, src2=image)  # outer gradient
    cv.imshow(winname="inner gradient", mat=dst1)
    cv.imshow(winname="outer gradient", mat=dst2)


src = cv.imread(filename=r"C:\Users\zcj\Desktop\videos\open_close.jpg")
cv.imshow(winname="input", mat=src)
inner_gradient(image=src)
cv.waitKey(0)
cv.destroyAllWindows()
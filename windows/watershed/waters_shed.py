import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def eater_shed(image):
    blurred = cv.pyrMeanShiftFiltering(src=image, sp=10, sr=100)
    gray = cv.cvtColor(src=blurred, code=cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(src=gray, thresh=0, maxval=256, type=cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow(winname="binary", mat=binary)

    # morphology
    kernel = cv.getStructuringElement(shape=cv.MORPH_RECT, ksize=(3, 3))
    mb = cv.morphologyEx(src=binary, op=cv.MORPH_OPEN, kernel=kernel, iterations=2)
    cv.morphologyEx(src=mb, op=cv.MORPH_OPEN, )


src = cv.imread(filename=r"C:\Users\zcj\Desktop\videos\circles.jpg")
cv.imshow(winname="input", mat=src)
eater_shed(image=src)
cv.waitKey(0)
cv.destroyAllWindows()
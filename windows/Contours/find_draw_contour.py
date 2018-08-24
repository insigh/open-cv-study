import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def canny_edge_detection(image):
    blurred = cv.GaussianBlur(src=image, ksize=(3, 3), sigmaX=0)
    gray = cv.cvtColor(src=blurred, code=cv.COLOR_BGR2GRAY)
    edges = cv.Canny(image=gray, threshold1=30, threshold2=100)
    cv.imshow(winname="canny detected edges", mat=edges)
    return edges


def contour_demo(image):
    dst = cv.GaussianBlur(src=image, ksize=(5, 5), sigmaX=0)
    gray = cv.cvtColor(src=dst, code=cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(src=gray, thresh=0, maxval=255, type=cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow(winname="binary image", mat=binary)

    # edges = canny_edge_detection(image=image)

    cloneimage, contours, hierarchy = cv.findContours(image=binary, mode=cv.RETR_TREE, method=cv.CHAIN_APPROX_SIMPLE)
    for i, contour in enumerate(contours):
        cv.drawContours(image=image, contours=contours, contourIdx=i, color=(0, 0, 255), thickness=2)
    cv.imshow(winname="contours image", mat=image)


src = cv.imread(filename=r"C:\Users\zcj\Desktop\videos\contour_shape.png")
cv.imshow(winname="input image", mat=src)
contour_demo(image=src)
cv.waitKey(0)
cv.destroyAllWindows()
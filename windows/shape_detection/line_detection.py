import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def Hough_line_transform(image):
    # gray transformation
    blurred = cv.GaussianBlur(src=image, ksize=(3, 3), sigmaX=10, sigmaY=10)
    gray = cv.cvtColor(src=blurred, code=cv.COLOR_BGR2GRAY)
    edges = cv.Canny(image=gray, threshold1=50, threshold2=150, apertureSize=3)
    # hough transformation
    lines = cv.HoughLines(image=edges, rho=1, theta=np.pi/180, threshold=200)
    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = rho * a
        y0 = rho * b
        x1 = int(x0+1000*(-b))
        y1 = int(y0+1000*a)
        x2 = int(x0-1000*(-b))
        y2 = int(y0-1000*a)
        cv.line(image, (x1, y1), (x2, y2), color=(0, 0, 255), thickness=2)
    cv.imshow(winname="Hough lines image", mat=image)


def hough_lines_detection(image):
    blurred = cv.GaussianBlur(src=image, ksize=(3, 3), sigmaX=10, sigmaY=10)
    gray = cv.cvtColor(src=blurred, code=cv.COLOR_BGR2GRAY)
    edges = cv.Canny(image=gray, threshold1=50, threshold2=150, apertureSize=3)
    lines = cv.HoughLinesP(image=edges, rho=1, theta=np.pi/180, threshold=200, minLineLength=300, maxLineGap=5)
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv.line(img=image, pt1=(x1, y1), pt2=(x2, y2), color=(0, 0, 255), thickness=2)
    cv.imshow(winname="Hough lines detection", mat=image)


src = cv.imread(filename=r"C:\Users\zcj\Desktop\docum\photos\8776db91659bf1b9abada9bbc9d9f15d0b085642.jpg")
# cv.namedWindow(winname="input image", flags=cv.WINDOW_AUTOSIZE)
Hough_line_transform(src)
hough_lines_detection(src)
cv.waitKey(0)
cv.destroyAllWindows()
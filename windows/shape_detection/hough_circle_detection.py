import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def hough_circle_detection(image):

    # blurred = cv.GaussianBlur(src=image, ksize=(9, 9), sigmaX=0)
    dst = cv.pyrMeanShiftFiltering(src=image, sp=1, sr=150)
    cv.imshow(winname="EPF filter", mat=dst)
    gray = cv.cvtColor(src=dst, code=cv.COLOR_BGR2GRAY)

    # "param2" is important, which means the smallest votes number
    # "param1" is the higher threshold of Canny edge detection, the lower one is set twice smaller automatically
    circles = cv.HoughCircles(image=gray, method=cv.HOUGH_GRADIENT, dp=1, minDist=30, param1=80, param2=30, minRadius=1, maxRadius=100)
    circles = np.uint16(np.round(circles))
    for circle in circles[0]:
        print(circle)
        cv.circle(img=image, center=(circle[0], circle[1]), radius=circle[2], color=(0, 0, 255), thickness=2)
        cv.circle(img=image, center=(circle[0], circle[1]), radius=2, color=(255, 0, 0), thickness=2)
    cv.imshow(winname="hough_circle_detection", mat=image)


def hough_lines_detection(image):
    # sigmaX and sigmaY means the var in each dimension
    blurred = cv.GaussianBlur(src=image, ksize=(3, 3), sigmaX=40, sigmaY=60)
    gray = cv.cvtColor(src=blurred, code=cv.COLOR_BGR2GRAY)

    # two thresholds for the line detection, larger one for obvious, smaller one for connectivity
    edges = cv.Canny(image=gray, threshold1=60, threshold2=100, apertureSize=3)

    # here "threshold" means the votes number, "rho" is radius step
    # "theta" is angle step, "minLineLength" if for the shortest line
    lines = cv.HoughLinesP(image=edges, rho=1, theta=np.pi/180, threshold=60, minLineLength=10)

    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv.line(img=image, pt1=(x1, y1), pt2=(x2, y2), color=(0, 0, 255), thickness=2)
    cv.imshow(winname="Hough lines detection", mat=image)


src = cv.imread(filename=r"C:\Users\zcj\Desktop\videos\line_circle.png")
hough_circle_detection(image=src)
hough_lines_detection(image=src)
cv.waitKey(0)
cv.destroyAllWindows()

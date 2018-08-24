import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def measure_object(image):
    dst = cv.cvtColor(src=image, code=cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(src=dst, thresh=40, maxval=256, type=cv.THRESH_BINARY)
    # print(ret)
    cv.imshow(winname="binary image", mat=binary)

    out_image, contours, hierarchy = cv.findContours(image=binary, mode=cv.RETR_TREE, method=cv.CHAIN_APPROX_SIMPLE)
    print(len(contours))
    dst = cv.cvtColor(src=binary, code=cv.COLOR_GRAY2BGR)
    for i, contour in enumerate(contours):
        # print(type(contours))
        # cv.drawContours(image=image, contours=contours, contourIdx=i, color=(0, 255, 0), thickness=3)
        # cv.imshow(winname="contour", mat=image)
        # cv.waitKey(0)
        # cv.destroyAllWindows()
        area = cv.contourArea(contour=contour)
        x, y, w, h = cv.boundingRect(points=contour)
        mm = cv.moments(array=contour)
        # print(mm)
        # if mm['m00'] == 0.:
        #     continue
        cx = mm['m10']/mm['m00']
        cy = mm['m01'] / mm['m00']
        cv.circle(img=dst, center=(int(cx), int(cy)), radius=3, color=(0, 255, 255), thickness=-1)
        cv.rectangle(img=image, pt1=(x, y), pt2=(x+w, y+h), color=(0, 0, 255), thickness=3)
        print("area of the contour：{}".format(area))
        apprcurve = cv.approxPolyDP(curve=contour, epsilon=4, closed=True)
        print(apprcurve.shape)
        if apprcurve.shape[0] == 3 :
            cv.drawContours(image=dst, contours=contours, contourIdx=i, color=(0, 0, 255), thickness=3)
        if apprcurve.shape[0] == 4 :
            cv.drawContours(image=dst, contours=contours, contourIdx=i, color=(0, 255, 0), thickness=3)
        if apprcurve.shape[0] >= 5 :
            cv.drawContours(image=dst, contours=contours, contourIdx=i, color=(255, 0, 0), thickness=3)
    cv.imshow(winname="measure contours:", mat=dst)




src = cv.imread(filename=r"C:\Users\zcj\Desktop\videos\shape.jpg")
cv.imshow(winname="input", mat=src)
measure_object(image=src)
cv.waitKey(0)
cv.destroyAllWindows()
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def eater_shed(image):
    # remove noise if any
    blurred = cv.pyrMeanShiftFiltering(src=image, sp=10, sr=100)
    gray = cv.cvtColor(src=blurred, code=cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(src=gray, thresh=0, maxval=256, type=cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    cv.imshow(winname="binary", mat=binary)

    # morphology
    kernel = cv.getStructuringElement(shape=cv.MORPH_RECT, ksize=(3, 3))
    mb = cv.morphologyEx(src=binary, op=cv.MORPH_OPEN, kernel=kernel, iterations=2)
    sure_bg = cv.dilate(src=mb, kernel=kernel, iterations=3)
    cv.imshow(winname="mor-opt", mat=sure_bg*50)

    # distance transform
    dist = cv.distanceTransform(src=mb, distanceType=cv.DIST_L2, maskSize=3)
    ret, surface = cv.threshold(src=dist, thresh=dist.max()*0.4, maxval=255, type=cv.THRESH_BINARY)
    cv.normalize(src=dist, dst=dist, alpha=0, beta=1.0, norm_type=cv.NORM_MINMAX)
    cv.imshow(winname="distance-t", mat=dist)
    cv.imshow(winname="surface-bin", mat=surface)

    surface_fg = np.uint8(surface)
    unknown = cv.subtract(src1=sure_bg, src2=surface_fg)
    ret, markers = cv.connectedComponents(image=surface_fg)
    print(ret)

    # watershed transform
    markers = markers + 1
    markers[unknown == 255] = 0
    markers = cv.watershed(image=image, markers=markers)
    image[markers == -1] = [0, 0, 255]
    cv.imshow(winname="result", mat=image)


src = cv.imread(filename=r"C:\Users\zcj\Desktop\videos\shape.jpg")
cv.imshow(winname="input", mat=src)
eater_shed(image=src)
cv.waitKey(0)
cv.destroyAllWindows()
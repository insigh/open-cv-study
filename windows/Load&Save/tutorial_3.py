import cv2 as cv
import numpy as np

def extract_object_demo():
    file = "C:\\Users\zcj\Desktop\\a19007bb28b874aca95b3c7ec5b44db1.mp4"
    capture = cv.VideoCapture(file)
    while True:
        ret, frame = capture.read()
        if not ret:
            break
        hsv = cv.cvtColor(src=frame, code=cv.COLOR_BGR2HSV)
        lower_hsv = np.array([26, 43, 46])
        higher_hsv = np.array([34, 255, 255])
        mask = cv.inRange(src=hsv, lowerb=lower_hsv, upperb=higher_hsv)
        cv.imshow(winname="video", mat=mask)

        c = cv.waitKey(40)
        if c == 27:
            break


def color_space_deomo(image):
    gray = cv.cvtColor(src=image, code=cv.COLOR_RGB2GRAY)
    cv.imshow(winname="gray", mat=gray)

    hsv = cv.cvtColor(src=image, code=cv.COLOR_BGR2HSV)
    cv.imshow(winname="hsv", mat=hsv)

    yuv = cv.cvtColor(src=image, code=cv.COLOR_RGB2YUV)
    cv.imshow(winname="yuv", mat=yuv)

    ycrcb = cv.cvtColor(src=image, code=cv.COLOR_BGR2YCrCb)
    cv.imshow(winname="ycrcb", mat=ycrcb)

    hls = cv.cvtColor(src=image, code=cv.COLOR_BGR2HLS)
    cv.imshow(winname="hls", mat=hls)

    Lab = cv.cvtColor(src=image, code=cv.COLOR_BGR2Lab)
    cv.imshow(winname="Lab", mat=Lab)

    lab = cv.cvtColor(src=image, code=cv.COLOR_RGB2Lab)
    cv.imshow(winname="lab", mat=lab)

    lab_ = cv.cvtColor(src=image, code=cv.COLOR_Lab2BGR)
    cv.imshow(winname="Lab2BGR", mat=lab_)



print("------------hello,python------------")
# src = cv.imread("C:\\Users\zcj\Desktop\docum\photos\8776db91659bf1b9abada9bbc9d9f15d0b085642.jpg")
src = cv.imread("C:\\Users\zcj\Desktop\\20180821153704.jpg")

b, g, r = cv.split(m=src)
cv.imshow(winname='blue', mat=b)
cv.imshow(winname='green', mat=g)
cv.imshow(winname='red', mat=r)
merged = cv.merge([b, g, r])
cv.imshow(winname='merged image', mat=merged)

cv.namedWindow("My Image Shower", cv.WINDOW_AUTOSIZE)
cv.imshow("My Image Shower", src)

color_space_deomo(src)
extract_object_demo()

cv.cvtColor(src, code=cv.COLOR_RGB2YUV)

cv.waitKey(0)
cv.destroyAllWindows()
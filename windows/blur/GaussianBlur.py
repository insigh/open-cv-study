import cv2 as cv
import numpy as np


def clamp(pv):
    if pv > 255 :
        return 255
    if pv < 0:
        return 0
    else:
        return pv


def gaussian_noise(image):
    # add gaussian noise to image
    h, w, c = image.shape
    for row in range(h):
        for col in range(w):
            n = np.random.normal(0, 20, 3)
            image[row, col, 0] = clamp(n[0] + image[row, col, 0])
            image[row, col, 1] = clamp(n[1] + image[row, col, 1])
            image[row, col, 2] = clamp(n[2] + image[row, col, 2])
    cv.imshow("noise image", mat=image)


def gaussian_blur_demo(image):
    # remove some noise for a image
    dst = cv.GaussianBlur(src=image, ksize=(5, 5), sigmaX=10, sigmaY=15)
    cv.imshow(winname="gaussian blured image", mat=dst)

print("=========hello python!==========")
src = cv.imread(filename="C:\\Users\zcj\Desktop\docum\photos\8776db91659bf1b9abada9bbc9d9f15d0b085642.jpg")
cv.namedWindow(winname="input image", flags=cv.WINDOW_AUTOSIZE)
cv.imshow(winname="input image", mat=src)
print("=========Functions start here!==========")
t1 = cv.getTickCount()
gaussian_noise(image=src)
t2 = cv.getTickCount()
gaussian_blur_demo(image=src)
print("Time consumed:{} ms".format((t2 - t1)/cv.getTickFrequency()*1000) )
print("=========Functions end here!==========")
cv.waitKey(0)
cv.destroyAllWindows()


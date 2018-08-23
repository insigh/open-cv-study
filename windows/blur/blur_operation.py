import cv2 as cv
import numpy as np


def blur_mean_demo(image):
    # mean blur
    dst = cv.blur(src=image, ksize=(5, 5))
    cv.imshow(winname="blured)image", mat=dst)


def median_blur(image):
    # median blur
    dst = cv.medianBlur(src=image, ksize=7)
    cv.imshow(winname="median_blured_image", mat=dst)


def custom_blur_demo(image):
    # customed mean blur
    kernel = np.ones([5, 5], np.float32)/25
    dst = cv.filter2D(src=image,ddepth=-1, kernel=kernel)
    cv.imshow(winname="customed_mean_blur", mat=dst)


def custom_mean_blur_demo(image):
    # for sharp
    kernel = np.array([[0, -1, 0], [-1, 10, -1], [0, -1, 0]], dtype=np.float32)
    dst = cv.filter2D(src=image, ddepth=-1, kernel=kernel)
    cv.imshow(winname="customed_mean_blur2", mat=dst)


print("------------hello,python------------")
src = cv.imread("C:\\Users\zcj\Desktop\docum\photos\8776db91659bf1b9abada9bbc9d9f15d0b085642.jpg")
print(src.shape)
cv.namedWindow(winname="input image", flags=cv.WINDOW_AUTOSIZE)
cv.imshow(winname="input image", mat=src)
# median_blur(src)
# blur_mean_demo(image=src)
# custom_blur_demo(image=src)
custom_mean_blur_demo(image=src)
cv.waitKey(0)
cv.destroyAllWindows()
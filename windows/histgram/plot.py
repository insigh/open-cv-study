import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def plot_demo(image):
    plt.hist(x=image.ravel(), bins=256, range=[0, 256], rwidth=0.7, color='r')
    plt.show()


def image_hist(image):
    color = ["blue", "green", "red"]
    for i, color in enumerate(color):
        hist = cv.calcHist(images=[image], channels=[i], mask=None, histSize=[256], ranges=[0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])
    plt.show()


print("==========hello python!==========")
src = cv.imread(filename="C:\\Users\zcj\Desktop\docum\photos\8776db91659bf1b9abada9bbc9d9f15d0b085642.jpg")
cv.namedWindow(winname="input image", flags=cv.WINDOW_AUTOSIZE)
cv.imshow(winname="input image", mat=src)
print("=========Functions start here!==========")
# plot_demo(image=src)
image_hist(image=src)
print("=========Functions end here!==========")
cv.waitKey(0)
cv.destroyAllWindows()


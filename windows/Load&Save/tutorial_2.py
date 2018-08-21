import cv2 as cv
import numpy as np


def access_pixels(image):
    print(image.shape)
    height,width,channels = image.shape[0],image.shape[1],image.shape[2]
    print("height: {0},width:{1},channels:{2}".format(height, width, channels))
    for row in range(height):
        for column in range(width):
            for c in range(channels):
                pv = image[row, column, c]
                image[row, column, c] = 255 - pv
    cv.imshow("pixel_demo",image)


def inverse(image):
    dst = cv.bitwise_not(image)
    cv.imshow("incerse_demo", dst)



def create_image_demo():
    # img = np.zeros([400,400,3], np.uint8)
    # # img[:, :, 0] = np.ones([400, 400])*255
    # img[:, :, 2] = np.ones([400, 400])*255
    # cv.imshow("new_image", img)
    img = np.zeros([600, 400, 1], dtype=np.uint8)
    img[:, :, 0] = np.ones([600, 400])*127
    cv.imshow("new_img", img)

print("------------hello,python------------")

src = cv.imread("C:\\Users\zcj\Desktop\docum\photos\8776db91659bf1b9abada9bbc9d9f15d0b085642.jpg")
cv.namedWindow("My Image Shower", cv.WINDOW_AUTOSIZE)
cv.imshow("My Image Shower", src)

t1 = cv.getTickCount()
inverse(src)
create_image_demo()

t2 = cv.getTickCount()
print("Time consuming:{}".format((t2-t1)/cv.getTickFrequency()))
print("TickFrequency:", cv.getTickFrequency())





cv.waitKey(0)
cv.destroyAllWindows()


import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def big_image_binary_demo(image):
    print(image.shape)
    ch, cw = 256, 256
    h, w = image.shape[:2]
    gray = cv.cvtColor(src=image, code=cv.COLOR_BGR2GRAY)
    for row in range(0, h, ch):
        for col in range(0, w, cw):
            roi = gray[row:row+ch, col:col+cw]
            ret, dst = cv.threshold(src=roi, thresh=0, maxval=255, type=cv.THRESH_OTSU)
            gray[row:row+ch, col:col+cw] = dst
            print(np.std(dst), np.mean(dst))
    cv.imwrite(filename=".\\big.jpg", img=gray)



print("=========hello python!==========")
src = cv.imread(filename="C:\\Users\zcj\Desktop\docum\photos\8776db91659bf1b9abada9bbc9d9f15d0b085642.jpg")
cv.namedWindow(winname="input image", flags=cv.WINDOW_AUTOSIZE)
cv.imshow(winname="input image", mat=src)
print("=========Functions start here!==========")
big_image_binary_demo(image=src)
print("=========Functions end here!==========")
cv.waitKey(0)
cv.destroyAllWindows()


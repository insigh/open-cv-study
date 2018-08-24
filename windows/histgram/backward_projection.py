import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def hist2d_demo(image):
    hsv = cv.cvtColor(src=image, code=cv.COLOR_BGR2HSV)
    hist = cv.calcHist(images=[hsv], channels=[0, 1], histSize=[8, 12], ranges=[0, 180, 0, 256], mask=None)
    # cv.imshow(winname="hist2d", mat=hist)
    plt.imshow(X=hist, interpolation="nearest")
    plt.title("2d histgram")
    plt.show()


def back_projection_demo(sample, target):
    roi_hsv = cv.cvtColor(src=sample, code=cv.COLOR_BGR2HSV)
    target_hsv = cv.cvtColor(src=target, code=cv.COLOR_BGR2HSV)

    roi_hist = cv.calcHist(images=[roi_hsv], channels=[0, 1], histSize=[8, 12], mask=None, ranges=[0, 180, 0, 256])
    cv.normalize(src=roi_hist, dst= roi_hist, alpha=0, beta=255, norm_type=cv.NORM_MINMAX)
    dst = cv.calcBackProject(images=[target_hsv], channels=[0, 1], hist=roi_hist, ranges=[0, 180, 0, 256], scale=1)
    cv.imshow(winname="back projection demo", mat=dst)
    cv.imwrite(filename="C:\\Users\zcj\Desktop\\res.jpg", img=dst)





print("=========hello python!==========")
target = cv.imread(filename="C:\\Users\zcj\Desktop\\videos\\20180821153704.jpg")
roi = cv.imread(filename="C:\\Users\zcj\Desktop\\videos\\20180823190802.png")
# cv.namedWindow(winname="input image", flags=cv.WINDOW_AUTOSIZE)
# cv.imshow(winname="roi", mat=roi)
# cv.imshow(winname="target", mat=target)
print("=========Functions start here!==========")
hist2d_demo(image=roi)
# back_projection_demo(sample=roi, target=target)
print("=========Functions end here!==========")
cv.waitKey(0)
cv.destroyAllWindows()


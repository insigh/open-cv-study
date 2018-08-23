import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def create_rgb_hist(image):
    h, w, c = image.shape
    rgb_hist = np.zeros(shape=[16*16*16, 1], dtype=np.float32)
    bsize = 256/16
    for row in range(h):
        for col in range(w):
            b = image[row, col, 0]
            g = image[row, col, 1]
            r = image[row, col, 2]
            index = (b//bsize)*16*16 + (g//bsize)*16 + r//bsize
            rgb_hist[int(index), 0] += 1
    return rgb_hist


def normalization(hist):
    mean = np.sum(hist)/hist.size
    var = np.sqrt(np.sum(np.square(hist - mean)))/hist.size
    return (hist - mean)/var




def hist_compare(image1, image2):
    hist1 = create_rgb_hist(image=image1)
    hist2 = create_rgb_hist(image=image2)
    corr1 = cv.compareHist(H1=hist1, H2=hist2, method=cv.HISTCMP_BHATTACHARYYA)
    corr2 = cv.compareHist(H1=hist1, H2=hist2, method=cv.HISTCMP_CHISQR)
    corr3 = cv.compareHist(H1=hist1, H2=hist2, method=cv.HISTCMP_CORREL)
    corr4 = cv.compareHist(H1=hist1, H2=hist2, method=cv.HISTCMP_INTERSECT)
    corr5 = cv.compareHist(H1=hist1, H2=hist2, method=cv.HISTCMP_KL_DIV)
    print("bath:{0},chisqr:{1},correl:{2},intersect:{3},KL_DIV:{4}".format(corr1, corr2, corr3, corr4, corr5))


print("=========hello python!==========")
src = cv.imread(filename="C:\\Users\zcj\Desktop\docum\photos\8776db91659bf1b9abada9bbc9d9f15d0b085642.jpg")
src2 = cv.imread(filename="C:\\Users\zcj\Desktop\\20180821153704.jpg")
src3 = cv.GaussianBlur(src=src, ksize=(5, 5), sigmaX=10)
cv.namedWindow(winname="input image", flags=cv.WINDOW_AUTOSIZE)
cv.imshow(winname="input image1", mat=src)
cv.imshow(winname="input image2", mat=src3)
print("=========Functions start here!==========")
hist_compare(image1=src3, image2=src)
print("=========Functions end here!==========")
cv.waitKey(0)
cv.destroyAllWindows()


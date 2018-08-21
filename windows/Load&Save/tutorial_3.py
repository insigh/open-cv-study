import cv2 as cv



print("------------hello,python------------")
src = cv.imread("C:\\Users\zcj\Desktop\docum\photos\8776db91659bf1b9abada9bbc9d9f15d0b085642.jpg")
cv.namedWindow("My Image Shower", cv.WINDOW_AUTOSIZE)
cv.imshow("My Image Shower", src)
cv.cvtColor(src, code=cv.COLOR_RGB2YUV)
cv.waitKey(0)
cv.destroyAllWindows()
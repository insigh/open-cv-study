import cv2 as cv

src = cv.imread("/home/zcj/Pictures/8776db91659bf1b9abada9bbc9d9f15d0b085642.jpg")
cv.namedWindow("input-image",cv.WINDOW_AUTOSIZE)
cv.imshow("input-image",src)
cv.waitKey(0)
cv.destroyAllWindows()

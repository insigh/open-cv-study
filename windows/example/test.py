import cv2 as cv

src = cv.imread("C:\\Users\zcj\Desktop\docum\photos\8776db91659bf1b9abada9bbc9d9f15d0b085642.jpg")
print(src.shape)
cv.namedWindow("input-image",cv.WINDOW_AUTOSIZE)
cv.imshow("input-image",src)
cv.waitKey(0)
cv.destroyAllWindows()




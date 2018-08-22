import cv2 as cv
import numpy as np


def flood_fill_color(image):
    cv.imshow(winname="src_image", mat=image)
    h,w = image.shape[:2]
    mask = np.zeros([h+2, w+2], np.uint8)
    cv.floodFill(image=image, mask=mask, seedPoint=(483,111), newVal=(0, 0, 255), loDiff=(100, 100, 100), upDiff=(50, 50, 50), flags=cv.FLOODFILL_FIXED_RANGE)
    cv.imshow(winname="filled image", mat=image)


def flood_fill_binary():
    image = np.zeros([400, 400], np.uint8)
    image[100:300, 100:300] = 255
    cv.imshow(winname="src_image", mat=image)
    mask = np.ones([402, 402], np.uint8)
    mask[101:301, 101:301] = 0
    cv.floodFill(image=image, mask=mask, seedPoint=(200, 200), newVal=(120), flags=cv.FLOODFILL_FIXED_RANGE)
    # cv.floodFill(image=image, mask=mask, seedPoint=(200, 200), newVal=(120), flags=cv.FLOODFILL_MASK_ONLY)
    cv.imshow(winname="filled_binary", mat=image)
    print(mask.all())
    cv.imshow(winname="mask", mat=mask)



print("------------hello,python------------")
src = cv.imread("C:\\Users\zcj\Desktop\docum\photos\8776db91659bf1b9abada9bbc9d9f15d0b085642.jpg")
print(type(src))
# cv.namedWindow(winname="input image", flags=cv.WINDOW_AUTOSIZE)
# cv.imshow(winname="input image", mat=src)

flood_fill_binary()
# flood_fill_color(src)

cv.waitKey(0)
cv.destroyAllWindows()
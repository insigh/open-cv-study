import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def template_demo():
    tpl = cv.imread(filename="C:\\Users\zcj\Desktop\\videos\\roi.png")
    target = cv.imread(filename="C:\\Users\zcj\Desktop\\videos\\all_stars.jpg")
    cv.imshow(winname="template", mat=tpl)
    cv.imshow(winname="target", mat=target)
    methods = [cv.TM_CCOEFF_NORMED, cv.TM_CCORR_NORMED, cv.TM_SQDIFF_NORMED]
    h, w = tpl.shape[:2]
    for method in methods:
        print(method)
        result = cv.matchTemplate(image=target, templ=tpl, method=method)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(src=result)
        if method == cv.TM_SQDIFF_NORMED:
            tl = min_loc
        else:
            tl = max_loc
        br = (tl[0] + h, tl[1] + w)
        cv.rectangle(img=target, pt1=tl, pt2=br, color=(0, 0, 255), thickness=2)
        # cv.imshow(winname="match"+str(method), mat=target)
        cv.imshow(winname="result"+np.str(method), mat=result)


print("=========hello python!==========")
# src = cv.imread(filename="C:\\Users\zcj\Desktop\docum\photos\8776db91659bf1b9abada9bbc9d9f15d0b085642.jpg")
# cv.namedWindow(winname="input image", flags=cv.WINDOW_AUTOSIZE)
# cv.imshow(winname="input image", mat=src)
print("=========Functions start here!==========")
template_demo()
print("=========Functions end here!==========")
cv.waitKey(0)
cv.destroyAllWindows()


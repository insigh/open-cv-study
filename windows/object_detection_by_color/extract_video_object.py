import cv2 as cv
import numpy as np


def extract_object_demo():
    """
    :parameter@red:    low[0, 0, 221],   high[180, 30, 255] or low[156, 43, 46], high[180, 255, 255]
    :parameter@black   low[0, 0, 0],     high[180, 255, 46]
    :parameter@gray    low[0, 0, 46],    high[180, 43, 220]
    :parameter@orange  low[11, 43, 46],  high[25, 255, 255]
    :parameter@yellow  low[26, 43, 46],  high[34, 255, 255]
    :parameter@green   low[35, 43, 46],  high[77, 255, 255]
    :parameter@grass   low[78, 43, 46],  high[99, 255, 255]
    :parameter@blue    low[100, 43, 46], high[124, 255, 255]
    :param@purple  low[125, 43, 46], high[155, 255, 255]
    :return: the mask contains where the color appears
    
    """
    file = "C:\\Users\zcj\Desktop\\videos\\3da68f2d530fd303e4a6ed694d425119.mp4"
    capture = cv.VideoCapture(file)
    while True:
        ret, frame = capture.read()
        if not ret:
            break
        hsv = cv.cvtColor(src=frame, code=cv.COLOR_BGR2HSV)
        lower_hsv = np.array([0, 43, 46])
        higher_hsv = np.array([10, 255, 255])
        mask = cv.inRange(src=hsv, lowerb=lower_hsv, upperb=higher_hsv)
        cv.imshow(winname="video", mat=mask)

        c = cv.waitKey(40)
        if c == 27:
            break

print("=========hello python!==========")
src = cv.imread(filename="C:\\Users\zcj\Desktop\docum\photos\8776db91659bf1b9abada9bbc9d9f15d0b085642.jpg")
cv.namedWindow(winname="input image", flags=cv.WINDOW_AUTOSIZE)
cv.imshow(winname="input image", mat=src)
print("=========Functions start here!==========")
extract_object_demo()
print("=========Functions end here!==========")
cv.waitKey(0)
cv.destroyAllWindows()


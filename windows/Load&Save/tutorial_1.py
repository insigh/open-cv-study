import cv2 as cv


def get_image_info(image):
    print(type(image))
    print(image.shape)
    print(image.size)
    print(image.dtype)


def video_demo():
    capture = cv.VideoCapture(0)
    while True:
        ret, frame = capture.read()
        frame = cv.flip(frame, 1)
        cv.imshow("video", frame)
        c = cv.waitKey(10)
        if c == 27:
            break


print("------------hello,python------------")
src = cv.imread("C:\\Users\zcj\Desktop\docum\photos\8776db91659bf1b9abada9bbc9d9f15d0b085642.jpg")
cv.namedWindow("My Image Shower", cv.WINDOW_AUTOSIZE)
cv.imshow("My Image Shower", src)
video_demo()
cv.waitKey(0)
get_image_info(src)
grey = cv.cvtColor(src, code=cv.COLOR_RGB2GRAY)
cv.imwrite(".\\result.png", src)
cv.imwrite(".\\result0.jpg", grey)


cv.destroyAllWindows()

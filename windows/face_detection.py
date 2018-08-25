import cv2 as cv
import numpy as np


def face_detection_demo(image):

    gray = cv.cvtColor(src=image, code=cv.COLOR_BGR2GRAY)
    face_detector = cv.CascadeClassifier(r"D:\github\opencv-master\opencv-master\data\haarcascades\haarcascade_eye.xml")
    # face_detector = cv.CascadeClassifier(r"D:\github\opencv-master\opencv-master\data\lbpcascades\lbpcascade_frontalface_improved.xml")

    faces = face_detector.detectMultiScale(image=gray, scaleFactor=1.2, minNeighbors=12)
    for x, y, w, h in faces:
        cv.rectangle(img=image, pt1=(x, y), pt2=(x+w, y+h), color=(0, 255, 0), thickness=3)
    cv.imshow(winname="face detection result", mat=image)


def face_detection_capture():
    capture = cv.VideoCapture(0)
    while True:
        ret, frame = capture.read()
        frame = cv.flip(src=frame, flipCode=1)
        face_detection_demo(image=frame)
        c = cv.waitKey(10)
        if c == 27:
            break


src = cv.imread(filename=r"C:\Users\zcj\Desktop\videos\faces2.jpg")
src = cv.resize(src=src, dsize=(600, 800))
# cv.imshow(winname="picture", mat=src)
# face_detection_demo(image=src)
face_detection_capture()
cv.waitKey(0)
cv.destroyAllWindows()
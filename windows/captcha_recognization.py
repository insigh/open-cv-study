import cv2 as cv
import numpy as np
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"D:\Programs\Tesseract-OCR\tesseract.exe"

def captcha_recognize(image):
    # get binary
    blurred = cv.pyrMeanShiftFiltering(src=image, sp=10, sr=100)
    gray = cv.cvtColor(src=blurred, code=cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(src=gray, thresh=0, maxval=255, type=cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    cv.imshow(winname="binary", mat=binary)

    # remove noise line
    kernel1 = cv.getStructuringElement(shape=cv.MORPH_RECT, ksize=(3, 3))
    kernel2 = cv.getStructuringElement(shape=cv.MORPH_RECT, ksize=(2, 2))

    open_operated = cv.morphologyEx(src=binary, op=cv.MORPH_OPEN, kernel=kernel1)
    open_operated = cv.morphologyEx(src=open_operated, op=cv.MORPH_OPEN, kernel=kernel2)
    cv.imshow(winname="open_operated", mat=open_operated)

    # recognize
    cv.bitwise_not(src=open_operated, mask=open_operated)
    text_image = Image.fromarray(obj=open_operated)
    text = pytesseract.image_to_string(image=text_image)
    print(text)


src = cv.imread(filename=r"C:\Users\zcj\Desktop\videos\captcha.jpeg")
cv.imshow(winname="input", mat=src)
captcha_recognize(image=src)
cv.waitKey(0)
cv.destroyAllWindows()
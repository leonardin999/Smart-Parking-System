import cv2
import os
import re
import imutils
import numpy as np
import pytesseract
from pytesseract import Output
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

image_path = r"E:\Python Project\Parking Software Project\app\images\license_9.png"
print(os.path.exists(image_path))

img = cv2.imread(image_path)
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
# resize image to three times as large as original for better readability
gray = cv2.resize(gray, None, fx = 3, fy = 3, interpolation = cv2.INTER_CUBIC)
# perform gaussian blur to smoothen image
blur = cv2.GaussianBlur(gray, (5,5), 0)

# threshold the image using Otsus method to preprocess for tesseract
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

# create rectangular kernel for dilation
rect_kern = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
# apply dilation to make regions more clear
dilation = cv2.dilate(thresh, rect_kern, iterations = 1)

# find contours of regions of interest within license plate
try:
    contours, hierarchy = cv2.findContours(dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
except:
    ret_img, contours, hierarchy = cv2.findContours(dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# sort contours left-to-right
sorted_contours = sorted(contours, key=lambda ctr: cv2.boundingRect(ctr)[0])
# create copy of gray image
im2 = gray.copy()
# create blank string to hold license plate number
plate_num = ""
# loop through contours and find individual letters and numbers in license plate
for cnt in sorted_contours:
    x,y,w,h = cv2.boundingRect(cnt)
    height, width = im2.shape
    # if height of box is not tall enough relative to total height then skip
    if height / float(h) > 6: continue

    ratio = h / float(w)
    # if height to width ratio is less than 1.5 skip
    if ratio < 1.5: continue

    # if width is not wide enough relative to total width then skip
    if width / float(w) > 15: continue

    area = h * w
    # if area is less than 100 pixels skip
    if area < 100: continue

    # draw the rectangle
    rect = cv2.rectangle(im2, (x,y), (x+w, y+h), (0,255,0),2)
    # grab character region of image
    roi = thresh[y-5:y+h+5, x-5:x+w+5]
    # perfrom bitwise not to flip image to black text on white background
    roi = cv2.bitwise_not(roi)
    # perform another blur on character region
    roi = cv2.medianBlur(roi, 5)
    try:
        text = pytesseract.image_to_string(roi, config='--psm 11 --oem 3 -c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ-')
        # clean tesseract text by removing any unwanted blank spaces
        clean_text = re.sub('[\W_]+', '', text)
        plate_num += clean_text
    except:
        text = None
if plate_num != None:
    print("License Plate #: ", plate_num)
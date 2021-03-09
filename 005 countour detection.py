#required libraries
import cv2 as cv
import numpy as np

#reading and showing image
img = cv.imread('images/kitten.jpg')
cv.imshow('Cats', img)

#converting to gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#blur
blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)

#edge cascade
canny = cv.Canny(blur, 120, 180)
cv.imshow('Canny', canny)

#detecting contours
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(len(contours))

#creating blank image
blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

#drawing the contour on blank
cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('drawn contours', blank)

cv.waitKey(0)
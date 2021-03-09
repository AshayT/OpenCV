#required library
import cv2 as cv

#reading the image
img = cv.imread('images/kitten.jpg')
#showing the read image
cv.imshow('Kitten', img)

#converting to Grayscale
gray = cv.cvtColor(img.copy(), cv.COLOR_BGR2GRAY)
#cv.imshow('Kitten Gray', gray)

#Blur
blur = cv.GaussianBlur(img.copy(),(3,3), cv.BORDER_DEFAULT)
#cv.imshow('Blurred cat', blur)

#Edge cascade
canny = cv.Canny(img.copy(), 50, 90)
cv.imshow('canny kitten', canny)

#Dilating 
dilated = cv.dilate(canny, (7,7))
cv.imshow('Dilated', dilated)

#Erode
eroded = cv.erode(dilated, (7,7))
cv.imshow('Eroded', eroded)

#resizing
resized = cv.resize(img.copy(), (400,200))
cv.imshow('Resized', resized)

#cropping
cropped = img[200:600, 400:1000]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
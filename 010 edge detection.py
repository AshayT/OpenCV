#required libraries
import cv2 as cv
import numpy as np 

#reading the image
img = cv.imread('images/kitten.jpg')
cv.imshow('kitten', img)

#converting to gray scale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)


#laplacian edges
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Lap', lap)

#sobel gradient magnitude

sobelx = cv.Sobel(gray, cv.CV_64F, 1,0)
sobely = cv.Sobel(gray, cv.CV_64F, 0,1)

cv.imshow('sobelx', sobelx)
cv.imshow('sobely', sobely)

#combinig both
sobel = cv.bitwise_or(sobelx, sobely)
cv.imshow('sobel', sobel)


#canny edge 
canny = cv.Canny(gray, 80, 125)
cv.imshow('canny', canny)




cv.waitKey(0)
#required libraries
import cv2 as cv
import numpy as np 

#reading the image
img = cv.imread('images/kitten.jpg')
cv.imshow('kitten', img)

#converting to gray scale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)


#simple thresholding
threshold, thresholded = cv.threshold(gray, 120, 255, cv.THRESH_BINARY)
cv.imshow('thresholded', thresholded)

#inverse threshold
threshold_inv, thresholded_inv = cv.threshold(gray, 120, 255, cv.THRESH_BINARY_INV)
cv.imshow('thresholded_inv', thresholded_inv)

#adaptive thresholding
adapt_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 9, 6) #hyperparameter -> kernel size and value that needs to be subtracted from mean
cv.imshow('adapt_thresh', adapt_thresh)

cv.waitKey(0)
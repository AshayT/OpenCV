#required libraries
import cv2 as cv
import numpy as np 

#reading the image
img = cv.imread('images/kitten.jpg')
cv.imshow('kitten', img)

#creating blank image
blank = np.zeros(img.shape[:2], dtype = 'uint8')
cv.imshow('blank', blank)


mask = cv.rectangle(blank,(400,100), (800,500), 255, -1)
cv.imshow('rect_mask', mask)

masked_img = cv.bitwise_and(img, img, mask = mask)
cv.imshow('rect_mask_img', masked_img)

cv.waitKey(0)
#required libraries
import cv2 as cv
import numpy as np 

#creating blank image
blank = np.zeros((600,600), dtype = 'uint8')
cv.imshow('blank', blank)

rect = cv.rectangle(blank.copy(),(200,200), (400,400), 255, -1)
circ = cv.circle(blank.copy(), (300,300), 120, 255, -1)
cv.imshow('blank', blank)
cv.imshow('rect', rect)
cv.imshow('circ', circ)

#bitwise AND
bitwise_and = cv.bitwise_and(rect, circ)
cv.imshow('AND', bitwise_and)

#bitwise OR
bitwise_or = cv.bitwise_or(rect, circ)
cv.imshow('OR', bitwise_or)

#bitwise XOR
bitwise_xor = cv.bitwise_xor(rect, circ)
cv.imshow('XOR', bitwise_xor)

#bitwise NOT
bitwise_not = cv.bitwise_not(rect)
cv.imshow('rect_NOT', bitwise_not)


cv.waitKey(0)
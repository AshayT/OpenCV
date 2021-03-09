#required library
import cv2 as cv
import numpy as np

#reading the image
img = cv.imread('images/kitten.jpg')
#showing the read image
cv.imshow('Kitten', img)


#translation
def translate(img, x, y):
    dimensions = (img.shape[1], img.shape[0])
    transMat = np.float32([[1,0,x], [0,1,y]])
    return cv.warpAffine(img, transMat, dimensions)

translated = translate(img, 100,200)
cv.imshow('Translated', translated)
#+x --> right
#+y --> down
#-x --> left
#-y --> up

#rotation
def rotate(img, angle, center=None):
    (height, width) = img.shape[:2]
    if center is None:
        center = (width//2, height//2)
    dimensions = (width, height)
    rotMat = cv.getRotationMatrix2D(center, angle, 1.0)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img.copy(), 60)
cv.imshow('Rotated', rotated)
#angle --> negative for clockwise, positive for anticlockwise

#Flipping
flip = cv.flip(img.copy(), 1)
cv.imshow('Flipped', flip)
#0 for horizonal flip, 1 for vertical and -1 for both 


cv.waitKey(0)

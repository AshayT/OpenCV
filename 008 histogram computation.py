#required library
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

#reading the image
img = cv.imread('images/kitten.jpg')
cv.imshow('kitten', img)


#creating a circular mask
blank = np.zeros(img.shape[:2], dtype = 'uint8')
mask = cv.circle(blank, (650,250), 120, 255, thickness=-1)
cv.imshow('blank circle',mask )

#masked image
masked = cv.bitwise_and(img, img, mask = mask)
cv.imshow('masked image',masked )


#plotting color histogram for masked image
colors = ['b', 'g', 'r']
plt.figure()
plt.xlabel('Bins')
plt.ylabel('no. of pixels')
plt.title('Color histogram')
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], mask, [256], [0,256])
    plt.plot(hist, color=col)
plt.xlim([0,256])
plt.show()


cv.waitKey(0)
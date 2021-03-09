#required library
import cv2 as cv

#reading the image
img = cv.imread('images/kitten.jpg')
#showing the read image
cv.imshow('Kitten', img)

#drawing a rectangle
rect = cv.rectangle(img.copy(), (550,100), (850,400), (255,0,0), thickness=2)
cv.imshow('Kitten with rectangle', rect)

#drawing a cicle
circ = cv.circle(img.copy(), (700,250), 200, (0,0,255), thickness=2)
cv.imshow('Kitten with circle', circ)

#drawing a line
line = cv.line(img.copy(),(550,100), (850,400), (255,0,0), thickness=2)
cv.imshow('Kitten with line', line)

#writing text
text = cv.putText(img.copy(), "This is a kitten", (20,200), cv.FONT_HERSHEY_TRIPLEX,  5,(0,255,0) , 2)
cv.imshow('Kitten with text', text)

cv.waitKey(0)

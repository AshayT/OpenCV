#required library
import cv2 as cv

#reading a local image 
img = cv.imread('face.jpg') 

#showing the read image in a window
cv.imshow('face', img)

#converting to gray scale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#showing the converted gray image
cv.imshow('gray', gray)

#reading the face haar cascade file
face_haar = cv.CascadeClassifier('face_haar.xml')

#detecting the faces
face_rect = face_haar.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)

print(len(face_rect)) #this tells the number of faces detected


#drawing a rectangle for each detected face
for (x,y,w,h) in face_rect:

    cv.rectangle(img, (x,y), (x+w, y+h), (0, 255,0), thickness=1) #this draws a rectangle for two given points

#showing the image with detected face
cv.imshow('rec face', img)
cv.waitKey(0)



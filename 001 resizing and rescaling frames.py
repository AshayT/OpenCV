#required library
import cv2 as cv

#reading the image
img = cv.imread('images/kitten.jpg')

#defining a function that scales the frame
def frame_rescale(frame, scale = 0.7):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


#scaling the image
resized_img = frame_rescale(img)

#showing the read image
cv.imshow('Kitten', img)

#showing reszied image
cv.imshow('resized', resized_img)

#reading video
capture = cv.VideoCapture('videos/dog.mp4')

while True:
    isTrue, vid_frame = capture.read() #taking each frame at time
    scaled_frame = frame_rescale(vid_frame) #scaling the frame
    cv.imshow('dog1', scaled_frame) #showing rescaled video
    cv.imshow('dog2', vid_frame)    #showing original video

    if cv.waitKey(20) & 0xFF==ord('q'): #break the loop on pressing 'q' key
        break

capture.release()
cv.waitKey(0)
cv.destroyAllWindows()
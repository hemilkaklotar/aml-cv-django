#program1
#Read color image and converted into gray and binary code.

import cv2 

image = cv2.imread('Images/a2.jpg',1)
cv2.imshow('color image',image)
images = cv2.imread('Images/a2.jpg',0)
cv2.imshow('Gray image',images)
met,image3 = cv2.threshold(images,140,255,cv2.THRESH_BINARY)
cv2.imshow('Binary image',image3)
cv2.waitKey(0)
cv2.destroyAllWindows()

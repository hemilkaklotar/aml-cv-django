#Program 2
#Implement a Python program to complement (image negation) an image. (Assume binary or gray scale image as an input).

import cv2 # import open cv library

image1 = cv2.imread('Images/a2.jpg',1) #read image
cv2.imshow('color image',image1) #show color image
image2 = cv2.imread('Images/a2.jpg',0) #read gray scale image
cv2.imshow('gray image',image2) #show gray scale image
ret, image3 = cv2.threshold(image2, 160, 255, cv2.THRESH_BINARY) # read binary image
cv2.imshow('binary image',image3) # show binary image
image4 = 255 - image2 #read gray complement image
cv2.imshow('gray complement', image4) # show gray complement image
image5 = 255 - image3 # read binary complement image
cv2.imshow('binary complement', image5) #show binary complement image
cv2.waitKey(0)
cv2.destroyAllWindows()

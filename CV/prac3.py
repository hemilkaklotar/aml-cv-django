#180450116009 - Hemil Kaklotar
#Program 3
'''Implement a Python program for Canny edge detection.'''
import cv2 # import open cv library
image1 = cv2.imread('Images/a2.jpg',1) #read image
cv2.imshow('color image',image1) #show color image
image2 = cv2.imread('Images/a2.jpg',0) #read gray scale image
cv2.imshow('gray image',image2) #show gray scale image
ret, image3 = cv2.threshold(image2, 160, 255, cv2.THRESH_BINARY) # read binary image
cv2.imshow('binary image',image3) # show binary image
edge1 = cv2.Canny(image2,100,200) # edge for canny on gray image
cv2.imshow('canny on gray image',edge1) # show canny edge detection on gray image
edge2 = cv2.Canny(image3,100,200) # edge for canny on binary image
cv2.imshow('canny on binary image',edge2) # show canny edge detection on binary image
cv2.waitKey(0)
cv2.destroyAllWindows()

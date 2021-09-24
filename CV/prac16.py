#Program 16
#erosion and dilation morphological operations
import cv2
import numpy as np

img=cv2.imread('Images/a5.jpg',0)

kernel=np.ones((3,3), np.uint8)

img_erosion=cv2.erode(img,kernel,iterations=1)

img_dilation=cv2.dilate(img,kernel,iterations=1)

cv2.imshow('original image',img)
cv2.imshow('Erosion operation',img_erosion)
cv2.imshow('Dilation operation',img_dilation)

cv2.waitKey(0)
cv2.destroyAllWindows()
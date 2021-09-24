#Program 14
#corner detection using window mask

import cv2
import numpy as np

#Read image
img = cv2.imread('Images/a3.jpg',0)
cv2.imshow('Original', img)
# Obtain number of rows and columns 
# of the image
m,n = img.shape
corner = np.zeros([m,n])

for i in range(1,m-1):
    for j in range(1,n-1):
        corner[i,j] = (1*img[i-1, j-1])+(-2*img[i-1, j])+(1*img[i-1, j + 1])+(-2*img[i, j-1])+ (4*img[i, j])+(-2*img[i, j + 1])+(1*img[i + 1, j-1])+(-2*img[i + 1, j])+(1*img[i + 1, j + 1])
        corner[i,j] = corner[i,j]/4;

corner = corner.astype(np.uint8)

edges = cv2.Canny(img,100,200)
cv2.imshow('Corner detection with canny',corner)
cv2.imshow('Edges detection with canny',edges)
cv2.imshow('Corner + Edges detection',corner+edges)

cv2.waitKey(0)
cv2.destroyAllWindows()


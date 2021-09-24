#Program 13
#Horizontal and vertical line detection using sobel mask

import cv2
import numpy as np

#read image
img =cv2.imread('Images/a3.jpg',0)
cv2.imshow('Original',img)

# Obtain number of rows and columns 
# of the image
m,n = img.shape
hori = np.zeros([m,n])
verti = np.zeros([m,n])

for i in range(1,m-2):
    for j in range(1,n-2):
        hori[i,j] = (-1*img[i-1, j-1])+(-2*img[i-1, j])+(-1*img[i-1, j + 1])+(0*img[i, j-1])+ (0*img[i, j])+(0*img[i, j + 1])+(1*img[i + 1, j-1])+(2*img[i + 1, j])+(1*img[i + 1, j + 1])
        verti[i,j] = (-1*img[i-1, j-1])+(0*img[i-1, j])+(1*img[i-1, j + 1])+(-2*img[i, j-1])+ (0*img[i, j])+(2*img[i, j + 1])+(-1*img[i + 1, j-1])+(0*img[i + 1, j])+(1*img[i + 1, j + 1])
        
hori =hori.astype(np.uint8)
verti =verti.astype(np.uint8)

edges = cv2.Canny(img,100,200)
cv2.imshow('Horizontal lines',hori)
cv2.imshow('Vertical lines',verti)
cv2.imshow('Both lines',hori+verti)

cv2.waitKey(0)
cv2.destroyAllWindows()
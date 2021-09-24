#Program 5
#Implement a Python program for 2D geometric operations like translation, rotation and scaling (image resizing).

import cv2
import numpy as np

original = cv2.imread('Images/a2.jpg')
cv2.imshow('Original image', original)
#translation
M = np.float32([[1, 0, 100], [0, 1, 50]])
(rows, cols) = original.shape[:2]
res = cv2.warpAffine(original, M, (cols, rows))
cv2.imshow('translation', res)
#Rotation
#getRotationMatrix20 creates a matrix needed for transformation
#We want matrix for rotation w,r,t cebter to 45 degree without scaling
M = cv2.getRotationMatrix2D((cols /2, rows / 2), 90, 1)
res = cv2.warpAffine(original, M, (cols, rows))
cv2.imshow('rotation', res)
#Scaling
half = cv2.resize(original, (0, 0), fx = 0.5, fy=0.5)
double = cv2.resize(original, (0, 0), fx = 2, fy=2) 
cv2.imshow('half scaling', half)
cv2.imshow('double scaling', double)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Program 15
#Harris corner detection Method

import cv2
import numpy as np

img = cv2.imread('Images/a3.jpg',1)

#convert the input image into
#grayscale color space
OperatedImg = cv2.cvtColor(img,cv2.COLOR_BGRA2GRAY)

#modify the data type
#setting to 32-bit floating point 
OperatedImg = np.float32(OperatedImg)

#apply the cv2.cornerHarris method
#to detect the corners with appropriate 
#values as input parameters

dest = cv2.cornerHarris(OperatedImg,2,5,0.07)

#Results are marked through the dilated corners
dest = cv2.dilate(dest,None)

#Reverting back to the original image,
#with optimal threshold value
img[dest>0.01*dest.max()]=[0,0,255]

#the window showing output image with corners 
cv2.imshow('Image with Borders',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
#180450116009 – Hemil Kaklotar
#Program9
'''Implement a Python program for Max filter in spatial domain.'''
import cv2
import numpy as np
#Read the image
img_noisy1 = cv2.imread('Images/home1.tif',0)
cv2.imshow('original',img_noisy1)
#obtain the number of rows and column of the image 
m,n = img_noisy1.shape
#Traverse the image. For every 3x3 area,
# Find the median of the pixels and replace the center pixel by the median
img_new1 = np.zeros([m,n])
for i in range(1,m-2):
 for j in range(1,n-2):
  temp = [img_noisy1[i-1,j-1],img_noisy1[i-1,j],img_noisy1[i-1,j+1],img_noisy1[i,j-1],img_noisy1[i,j],img_noisy1[i,j+1],img_noisy1[i+1,j-1],img_noisy1[i+1,j],img_noisy1[i+1,j+1]]
  temp = sorted(temp)
  img_new1[i,j] = temp[8]

img_new1 = img_new1.astype(np.uint8)
cv2.imwrite('Images/new_median_filterd.png',img_new1)
cv2.imshow('Max filter',img_new1)

cv2.waitKey(0)
cv2.destroyAllWindows()
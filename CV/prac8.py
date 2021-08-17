#180450116009 – Hemil Kaklotar
#Progarm 8
'''Implement a Python program for Median filter in spatial domain.'''
import cv2
import numpy as np
#read the image
img_noisy1 = cv2.imread('Images/pollen.tif', 0)
cv2.imshow('original', img_noisy1)
#obtain the number of rows and columns of the image
m, n = img_noisy1.shape
#Traverse the image. For every 3*3 areas,
#Find the median of the pixels and
#Replace the center pixels by the median
img_new1 = np.zeros([m, n])
for i in range(1, m-2):
 for j in range(1, n-2):
    temp = [img_noisy1[i-1, j-1],img_noisy1[i-1, j],img_noisy1[i-1, j+1],img_noisy1[i, j-1],img_noisy1[i, j],img_noisy1[i, j+1],img_noisy1[i+1, j-1],img_noisy1[i+1, j],img_noisy1[i+1, j+1],]
    temp = sorted(temp)
    img_new1[i, j] = temp[4]
 
img_new1 = img_new1.astype(np.uint8)
cv2.imwrite('Images/new_median_filtered.png', img_new1)
cv2.imshow('median filter', img_new1)
cv2.waitKey()
cv2.destroyAllWindows()

#program 12
#high pass filter(spatial domain)

import cv2
import numpy as np

#read image
img_noisy1=cv2.imread('Images/a3.jpg',0)
cv2.imshow('original',img_noisy1)
m, n=img_noisy1.shape   #no. of rows and coloumn of image


img_new1=np.zeros([m, n])

for i in range(1, m-1):
    for j in range(1, n-1):
        img_new1[i,j]=(8/9)*img_noisy1[i,j] - ((1/9)*(img_noisy1[i-1, j-1]+img_noisy1[i-1, j]+img_noisy1[i-1, j + 1]+img_noisy1[i, j-1]+img_noisy1[i, j + 1]+img_noisy1[i + 1, j-1]+img_noisy1[i + 1, j]+img_noisy1[i + 1, j + 1]))

img_new1=img_new1.astype(np.uint8)

cv2.imshow('high pass filters - spatial domain',img_new1)

cv2.waitKey(0)
cv2.destroyAllWindows()
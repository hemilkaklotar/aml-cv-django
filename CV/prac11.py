#program 11
#sharpening filter 1st and 2nd derivative(spatial domain)

import cv2
import numpy as np

#read image
img=cv2.imread('Images/a2.jpg',0)
cv2.imshow('original',img)
m, n=img.shape   #no. of rows and coloumn of image

#developing averaging filter(3,3)mask
mask=np.ones([3,3], dtype=int)
mask=mask/9

img_new=np.zeros([m, n])

for i in range(1, m-2):
    for j in range(1, n-2):
        temp = img[i-1, j-1]/9+img[i-1, j]/9+img[i-1, j + 1]/9+img[i, j-1]/9+ img[i, j]/9+img[i, j + 1]/9+img[i + 1, j-1]/9+img[i + 1, j]/9+img[i + 1, j + 1]/9
        
        img_new[i,j]=temp
img_new=img_new.astype(np.uint8)
cv2.imwrite('Images/blurred.png',img_new)
img_noisy1=cv2.imread('Images/blurred.png',0)


m, n=img_noisy1.shape

img_new1=np.zeros([m,n])
img_new2=np.zeros([m,n])

for i in range(1, m-2):
    for j in range(1, n-2):   
        img_new2[i, j]= img_noisy1[i-1,j-1]+ img_noisy1[i+1,j+1] - (2 *img_noisy1[i,j])
        img_new1[i, j]=img_noisy1[i+1,j+1]+img_noisy1[i,j]
img_new1=img_new1.astype(np.uint8)
img_new2=img_new2.astype(np.uint8)

cv2.imshow('sharpening 1st derivative',img_new1)
cv2.imshow('sharpening 2nd derivative',img_new2)

cv2.waitKey(0)
cv2.destroyAllWindows()
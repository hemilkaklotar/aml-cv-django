#practical 16
#opening and closing morphological operations

import cv2
import numpy as np

img=cv2.imread('Images/a5.jpg',0)

#taking a matrix of size 5 as the kernel
kernel=np.ones((5,5), np.uint8)

opening=cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
closing=cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)

cv2.imshow('original image',img)
cv2.imshow('opening operation',opening)
cv2.imshow('closing operation',closing)

cv2.waitKey(0)
cv2.destroyAllWindows()
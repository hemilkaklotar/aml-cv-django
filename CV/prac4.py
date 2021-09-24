#program 4
#Implement a Python program for contrast stretching. New = (255 )*((current – m1)/(m2 - m1))

import cv2
import numpy as np

image1=cv2.imread('Images/top2.tif', 0)
cv2.imshow('before contrast stretching', image1)
width = image1.shape[1]
height = image1.shape[0]
cimage = np.zeros((image1.shape[0], image1.shape[1]), dtype= 'uint8')
n1 = np.min(image1)
n2 = np.max(image1)
cimage = 255 * (((image1 - n1)/(n2-n1)))
cv2.imwrite('Images/after.png', cimage)
after = cv2.imread('Images/after.png', 0)
cv2.imshow('after', after)
cv2.waitKey(0)
cv2.destroyAllWindows()
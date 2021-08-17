#180450116009 – Hemil Kaklotar
#Program 6
'''Implement a Python program to display histogram for a given image and also
display its equalizedhistogram.'''
import cv2
import matplotlib.pyplot as plt
img = cv2.imread('Images/top4.tif', 0)
cv2.imshow('image', img)
histr = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.plot(histr)
plt.title('original')
plt.xlabel('intensity value')
plt.ylabel('number of pixels')
plt.show()
'''plt.hist(img.reval(), 256, [0, 256]) #another way to plot histogram
plt.show()'''
'''histogram of color image
color = ('b', 'g', 'r')
for i in col in enumerate(color):
 histr = cv2.colHist([img], [i], None, [256], [0, 256])
 plt.plot(histr, color = col)
 plt.xlim([0, 256])
plt.show()'''
#histogram equalization
'''equ = cv2.calcHist(img)
cv2.imshow('equalized', equ)
histr = cv2.calcHist([equ], [0], None, [256], [0, 256])
plt.plot(histr)
plt.title('histogram equalization')
plt.xlabel('intensity value')
plt.ylabel('number of pixels')
plt.show()'''
'''plt.hist(equ.ravel(), 256, [0, 256]) #another way to plot histogram
plt.show()'''
cv2.waitKey(0)
cv2.destroyAllWindows()

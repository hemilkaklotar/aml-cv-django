#practical 18
#find contours
import cv2


image=cv2.imread('Images/a3.jpg')

#converting RGB image to binary
gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(gray_image,100,230,0)
cv2.imshow('thresh',thresh)

#calculate contours from binary image
contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
with_contours=cv2.drawContours(image,contours,-1,(0,255,0),3)
cv2.imshow('contours',with_contours)


cv2.waitKey(0)
cv2.destroyAllWindows()
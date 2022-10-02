#import the library
import cv2 as cv
import numpy as np

img = cv.imread('input.jpg') #input the color image
cv.imwrite('C.jpg', img) #output the color image

gray_img = [] 
for i in img : 
	row = []
	for j in i : 
		avg = int(np.sum(j)/3) 
		row.append([avg]) #I = (R+G+B)/3
	gray_img.append(row)
gray_img = np.array(gray_img, dtype = "uint8")
# transform the color image C into a grayscale image

cv.imwrite('I.jpg', gray_img) #output the gray image

cv.imshow('grayscale image I', gray_img) #show the grayscale image I
cv.waitKey(0)
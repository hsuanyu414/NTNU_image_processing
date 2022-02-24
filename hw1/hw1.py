import cv2 as cv
import numpy as np
img = cv.imread('input.jpg')

for i in img :
	for j in i :
		print(i.index(j))

# print(img)

# cv.imshow('Cats', img)
# cv.waitKey(0)
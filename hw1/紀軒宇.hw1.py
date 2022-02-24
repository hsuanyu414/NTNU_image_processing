import cv2 as cv
import numpy as np

img = cv.imread('input.jpg')

gray_img = [] # use a list to store the gray image
for i in img : # for each row
	row = []
	for j in i : # for each pixel
		avg = int(np.average(j)) #calculate the average of one pixel
		row.append([avg, avg, avg]) #I = (R+G+B)/3
	gray_img.append(row)
gray_img = np.array(gray_img, dtype = "uint8")

cv.imwrite('output_c.jpg', img)
cv.imwrite('output_g.jpg', gray_img)

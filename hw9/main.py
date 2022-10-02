#import the library
import cv2 
import numpy as np
import math

img = cv2.imread("input.jpg") 
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
ret, img = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
struct_element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))

output = np.zeros(img.shape, dtype="uint8")

while(1):
	open_img = cv2.morphologyEx(img, cv2.MORPH_OPEN, struct_element)
	if cv2.countNonZero(open_img)==0:
		break
	diff = cv2.subtract(img, open_img)
	output = cv2.bitwise_or(output, diff)
	img = cv2.erode(open_img, struct_element)

cv2.imshow('ske', output)
cv2.waitKey(0)
cv2.imwrite('ske3x3.jpg', output)
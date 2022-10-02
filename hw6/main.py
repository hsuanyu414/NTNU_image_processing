#import the library
import cv2 
import numpy as np
import math
import matplotlib.pyplot as plt

img = cv2.imread("01.jpg") 
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
y, x = img.shape
his_data_p = np.bincount(img.flatten(), minlength=256)/(x*y)
mean = 0
for i in range(256):
	mean += i*his_data_p[i]
t = 0
max_out = 0
for i in range(256-1):
	pa = np.sum(his_data_p[:i+1])
	pb = np.sum(his_data_p[i+1:255])
	if(pa*pb==0):
		continue
	mean_a = 0
	for j in range (i+1):
		mean_a += j*his_data_p[j]
	mean_times_at = mean*pa
	out = ((mean_a-mean_times_at)**2)/(pa*pb)
	if(out>max_out):
		max_out = out 
		t = i	

ret1, out1 = cv2.threshold(img, t, 255, cv2.THRESH_BINARY)
ret2, out2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imwrite("out1.jpg", out1)
cv2.imwrite("out2.jpg", out2)
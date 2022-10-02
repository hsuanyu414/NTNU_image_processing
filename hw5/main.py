#import the library
import cv2 
import numpy as np
import math
import matplotlib.pyplot as plt

img = 100*np.ones([400, 600], dtype='uint8') 
cv2.imwrite("g(x,y).jpg", img)

y, x = img.shape
mean = 0
sd = math.sqrt(15)
for i in range(y):
	for j in range(0,x,2):
		r, p = np.random.uniform(0, 1, 2)
		z1 = round(sd*math.cos(2*math.pi*p)*math.sqrt(-2*math.log(r)))
		z2 = round(sd*math.sin(2*math.pi*p)*math.sqrt(-2*math.log(r)))
		img[i][j]   += z1
		img[i][j+1] += z2
img = np.clip(img, 0, 255)

cv2.imwrite("f(x,y).jpg", img)

plt.hist(img.flatten(), bins=255, range=(0, 255))
plt.savefig("h(i).jpg")
plt.close()
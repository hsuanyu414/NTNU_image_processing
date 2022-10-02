#import the library
import cv2 
import numpy as np
import colorsys

def histo_equalization_HSV(img):
	H, S, V = cv2.split(img)
	n_img = np.clip(np.round(V*255), 0, 255).astype('uint8')
	h_img = n_img.copy()
	y, x = n_img.shape
	level = list(range(256))
	img_1dim = n_img.flatten()
	his_data = np.bincount(img_1dim, minlength=256)
	acc_data = np.cumsum(his_data)
	acc_prob = acc_data/(x*y)
	roundvalue = np.rint(acc_prob*255).astype('uint8')
	for i in range(y):
		for j in range(x):
			h_img[i][j] = roundvalue[h_img[i][j]]
	output = n_img*(np.divide(h_img, n_img, where=n_img!=0))
	output = np.clip(output, 0, 255)/255
	output = cv2.merge([H, S, output])
	return output
img = cv2.imread("machi.jpg") 
img_norm = img/255
y, x, c = img.shape
for i in range(y):
	for j in range(x):
		B, G, R = img_norm[i][j]
		img_norm[i][j] = colorsys.rgb_to_hsv(R, G, B)
hsv_ = histo_equalization_HSV(img_norm)	
new = np.zeros(img.shape, dtype='uint8')
for i in range(y):
	for j in range(x):
		H, S, V = hsv_[i][j]
		r, g, b = colorsys.hsv_to_rgb(H, S, V)
		new[i][j] = b*255, g*255, r*255
cv2.imshow('output', new)
cv2.waitKey(0)
cv2.imwrite('output.jpg', new)
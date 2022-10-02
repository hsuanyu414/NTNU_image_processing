#import the library
import cv2 
import numpy as np
import math
import matplotlib.pyplot as plt

def histo_equalization(img_name):
	img = cv2.imread(img_name) 
	gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
	h_gray_img = gray_img.copy()
	y, x = gray_img.shape
	level = list(range(256))
	plt.hist(gray_img.flatten(), bins=255)
	plt.savefig(img_name[0]+"__hist.jpg")
	plt.close()
	img_1dim = gray_img.flatten()
	his_data = np.bincount(img_1dim, minlength=256)
	acc_data = np.cumsum(his_data)
	acc_prob = acc_data/(x*y)
	roundvalue = np.rint(acc_prob*255).astype('uint8')
	for i in range(y):
		for j in range(x):
			h_gray_img[i][j] = roundvalue[h_gray_img[i][j]]
	output = img*(np.tile(np.reshape(np.divide(h_gray_img, gray_img, where=gray_img!=0), (y, x, 1)), (1, 1, 3)))
	output = np.clip(output, 0, 255).astype('uint8')
	plt.hist(h_gray_img.flatten(), bins=255)
	plt.savefig(img_name[0]+"H__hist.jpg")
	plt.close()
	cv2.imwrite(img_name[0]+"H.jpg", output)
	return
histo_equalization("G.jpg")
histo_equalization("C.jpg")

img = cv2.imread("C.jpg")
b, g, r = cv2.split(img)
plt.hist(b.flatten(), bins=255, color="#0000FF")
plt.savefig("C_b_hist.jpg")
plt.close()
plt.hist(g.flatten(), bins=255, color="#00FF00")
plt.savefig("C_g_hist.jpg")
plt.close()
plt.hist(r.flatten(), bins=255, color="#FF0000")
plt.savefig("C_r_hist.jpg")
plt.close()

img = cv2.imread("CH.jpg")
b, g, r = cv2.split(img)
plt.hist(b.flatten(), bins=255, color="#0000FF")
plt.savefig("CH_b_hist.jpg")
plt.close()
plt.hist(g.flatten(), bins=255, color="#00FF00")
plt.savefig("CH_g_hist.jpg")
plt.close()
plt.hist(r.flatten(), bins=255, color="#FF0000")
plt.savefig("CH_r_hist.jpg")
plt.close()
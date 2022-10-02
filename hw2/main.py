#import the library
import cv2 
import numpy as np
import math

img = cv2.imread('I.jpg', cv2.IMREAD_GRAYSCALE) 
y, x = img.shape
# read the image and get the image's shape

# (A)
d2 = np.array([ [  0, 128,  32, 160,],  
				[192,  64, 224,  95,], 
				[ 48, 176,  16, 144,],  
				[240, 112, 208,  80 ] ])
rx = math.ceil(x/4)
ry = math.ceil(y/4)
d = np.tile(d2, (ry, rx))
# use the dithering matrix d2 to generate an array d of image size by repeating              

img_ext = np.zeros([ry*4, rx*4], dtype='uint8')
img_ext[0:y, 0:x] = img.copy()

out = (img_ext>d)[0:y, 0:x]*255 
# threshold image I

cv2.imwrite('A.jpg', out) #output the gray image

# (B)
d1 = np.array([ [ 0, 56], 
				[84, 28] ])
rx = math.ceil(x/2)
ry = math.ceil(y/2)
d = np.tile(d1, (ry, rx))
# use the dithering matrix d2 to generate an array d of image size by repeating 

img_ext = np.zeros([ry*2, rx*2], dtype='uint8')
img_ext[0:y, 0:x] = img.copy()
q = (img_ext//85)
out = (q+(img_ext-85*q>d))*85
# scale values of so that its values are in [0, 255] for displaying

cv2.imwrite('B.jpg', out) #output the gray image
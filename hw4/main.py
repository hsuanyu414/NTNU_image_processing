#import the library
import cv2 
import numpy as np

img = cv2.imread("cat.jpg") 

kernel_size = 3
k = 0.7

img_avg = cv2.blur(img, (kernel_size, kernel_size))
img_avg = img-img_avg*k
img_avg = np.clip((img_avg /(1-k)), 0, 255).astype('uint8')
showdata = np.hstack([img, img_avg])
cv2.imshow(str(k)+"avg.jpg", showdata)
cv2.waitKey(0)

img_med = cv2.medianBlur(img, kernel_size)
img_med = img - img_med*k
img_med = np.clip((img_med /(1-k)), 0, 255).astype('uint8')
showdata = np.hstack([img, img_med])
cv2.imshow(str(k)+"med.jpg", showdata)
cv2.waitKey(0)

cv2.imwrite(str(k)+"avg.jpg", img_avg)
cv2.imwrite(str(k)+"med.jpg", img_med)
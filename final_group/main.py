import cv2
import numpy as np
import matplotlib.pyplot as plt
# 選擇第二隻攝影機
# cap = cv2.VideoCapture(0)
frame = cv2.imread("C2.jpg")
frame_rgb = frame
frame_rgb=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
# plt.imshow(frame_rgb)
# plt.show()
rect = (675, 190, 1050, 918)

mask = np.zeros(frame_rgb.shape[:2], dtype=np.uint8)
bgmod = np.zeros((1, 65), np.float64)
fgmod = np.zeros((1, 65), np.float64)
cv2.grabCut(frame_rgb, mask, rect, bgmod, fgmod, 50, cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0), 0, 1).astype('uint8')
frame_rgb = frame_rgb*mask2[:, :, np.newaxis]

# 顯示圖片

plt.imshow(frame_rgb)
plt.show()
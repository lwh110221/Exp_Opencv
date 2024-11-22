import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取图片
image = cv2.imread('pic/yaosg.png')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

median_3x3 = cv2.medianBlur(image_rgb, 3)

# 5x5 中值滤波
median_5x5 = cv2.medianBlur(image_rgb, 5)

# 7x7 中值滤波
median_7x7 = cv2.medianBlur(image_rgb, 7)

# 显示处理后的图片
plt.figure(figsize=(15, 5))

plt.subplot(1, 4, 1)
plt.title("原图")
plt.imshow(image_rgb)
plt.axis('off')

plt.subplot(1, 4, 2)
plt.title("中值 3x3")
plt.imshow(median_3x3)
plt.axis('off')

plt.subplot(1, 4, 3)
plt.title("中值 5x5")
plt.imshow(median_5x5)
plt.axis('off')

plt.subplot(1, 4, 4)
plt.title("中值 7x7")
plt.imshow(median_7x7)
plt.axis('off')

plt.show()

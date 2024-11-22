import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取图片
image = cv2.imread('pic/yaosg.png')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# 设置邻域大小
kernel_size = 3
kernel = np.ones((kernel_size, kernel_size), np.float32) / (kernel_size ** 2)

# 应用邻域平均法
smoothed_image = cv2.filter2D(image_rgb, -1, kernel)

# 显示原图和处理后的图片
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(image_rgb)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Averaging Filter")
plt.imshow(smoothed_image)
plt.axis('off')

plt.show()

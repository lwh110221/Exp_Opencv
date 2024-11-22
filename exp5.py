import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取图片
image = cv2.imread('pic/BMW.jpg')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# 定义削波函数
def clip_image(img, a, b):
    clipped_img = np.clip(img, a, b)  # 将像素值限制在[a, b]之间
    return clipped_img

# 对每个通道进行削波处理
a, b = 0, 210
r, g, b = cv2.split(image_rgb)
r_clipped = clip_image(r, a, b)
g_clipped = clip_image(g, a, b)
b_clipped = clip_image(b, a, b)

# 合并通道
clipped_image = cv2.merge([r_clipped, g_clipped, b_clipped])

# 显示原图和削波处理后的图像
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(image_rgb)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Clipped Image")
plt.imshow(clipped_image)
plt.axis('off')

plt.show()

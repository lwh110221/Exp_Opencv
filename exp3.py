import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取图片
image = cv2.imread('pic/BMW.jpg')  # 替换为你的图片路径
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# 全域线性变换函数
def linear_transform(channel, a, b, c, d):
    result = ((channel - a) * (d - c) / (b - a) + c).clip(0, 255).astype(np.uint8)
    return result

r, g, b = cv2.split(image_rgb)
r_transformed = linear_transform(r, 0, 255, 50, 150)
g_transformed = linear_transform(g, 0, 255, 50, 150)
b_transformed = linear_transform(b, 0, 255, 50, 150)

transformed_image = cv2.merge([r_transformed, g_transformed, b_transformed])

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(image_rgb)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Global Linear Transformation")
plt.imshow(transformed_image)
plt.axis('off')

plt.show()



# 分段线性变换函数
def piecewise_linear_transform(channel, a1, b1, c1, d1, a2, b2, c2, d2, a3, b3, c3, d3):
    result = np.zeros_like(channel)
    # 区间 [0, a1]
    mask1 = (channel >= 0) & (channel <= a1)
    result[mask1] = ((channel[mask1] - 0) * (c1 - 0) / (a1 - 0) + 0).astype(np.uint8)

    # 区间 [a1, b1]
    mask2 = (channel > a1) & (channel <= b1)
    result[mask2] = ((channel[mask2] - a1) * (d1 - c1) / (b1 - a1) + c1).astype(np.uint8)

    # 区间 [b1, 255]
    mask3 = (channel > b1) & (channel <= 255)
    result[mask3] = ((channel[mask3] - b1) * (d3 - c2) / (255 - b1) + c2).astype(np.uint8)

    return result

# 对每一个基色通道进行分段线性变换
r_piecewise = piecewise_linear_transform(r, 0, 145, 0, 175, 145, 220, 175, 210, 220, 255, 210, 255)
g_piecewise = piecewise_linear_transform(g, 0, 145, 0, 175, 145, 220, 175, 210, 220, 255, 210, 255)
b_piecewise = piecewise_linear_transform(b, 0, 145, 0, 175, 145, 220, 175, 210, 220, 255, 210, 255)

# 合并通道
piecewise_image = cv2.merge([r_piecewise, g_piecewise, b_piecewise])

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(image_rgb)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Piecewise Linear Transformation")
plt.imshow(piecewise_image)
plt.axis('off')

plt.show()

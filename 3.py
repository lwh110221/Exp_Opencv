import cv2
import numpy as np

# 读取图片文件
img = cv2.imread('pic/mm.jpg', 1)

# 获取图片的高度、宽度和通道数
height, width, channels = img.shape

# 创建一个与原图大小相同的空白图像，用于存储灰度化后的图片
gray_img = np.zeros((height, width), dtype=np.uint8)

# 遍历图片的每个像素点，计算灰度值并赋值给新图像
for i in range(height):
    for j in range(width):
        b, g, r = img[i, j]
        gray = (int(b) + int(g) + int(r)) // 3
        gray_img[i, j] = gray

# 显示原始彩色图片
cv2.imshow('Original Image', img)

# 显示灰度化后的图片
cv2.imshow('Grayscale Image', gray_img)

# 等待按键事件，关闭窗口
cv2.waitKey(0)
cv2.destroyAllWindows()

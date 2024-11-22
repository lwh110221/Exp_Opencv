import cv2  # 导入OpenCV库，这是一个用于处理图像和视频的开源计算机视觉库

img = cv2.imread('pic/mm.jpg',0)  # 使用cv2.imread()函数读取名为'BMW.jpg'的图片文件，参数0表示以灰度模式读取图片
print(type(img))  # 打印img的数据类型，通常是一个numpy数组
cv2.imshow('image',img)  # 使用cv2.imshow()函数显示名为'image'的窗口，并将读取到的图片作为窗口的内容
cv2.waitKey(0)  # 使用cv2.waitKey()函数等待用户按键，参数0表示无限等待直到用户按下任意键


import cv2

img = cv2.imread('pic/mm.jpg')  # 读取彩色图片
gray_img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 浮点算法：Gray=R0.3+G0.59+B0.11

# 阈值化处理
threshold_value = 150  # 阈值
ret, binary_img = cv2.threshold(gray_img1, threshold_value, 255, cv2.THRESH_BINARY)

cv2.imshow('binary image', binary_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

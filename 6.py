import cv2

img = cv2.imread('pic/BMW.jpg')  # 读取彩色图片

inverted_img = cv2.bitwise_not(img)
cv2.imshow('image1', inverted_img)
cv2.waitKey(0)
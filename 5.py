import cv2

img = cv2.imread('pic/mm.jpg')  # 读取彩色图片
gray_img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 浮点算法：Gray=R0.3+G0.59+B0.11
# gray_img2 = (img[:,:,0] * 0.3 + img[:,:,1] * 0.59 + img[:,:,2] * 0.11).astype('uint8')  # 整数方法：Gray=(R30+G59+B11)/100
# gray_img3 = ((img[:,:,0] * 28 + img[:,:,1] * 151 + img[:,:,2] * 77) >> 8).astype('uint8')  # 移位方法：Gray=(R28+G151+B77)>>8;
# gray_img4 = (img[:,:,0] + img[:,:,1] + img[:,:,2]) // 3  # 平均值法：Gray=（R+G+B）/3;

# 反色显示
inverted_gray_img1 = cv2.bitwise_not(gray_img1)
# inverted_gray_img2 = cv2.bitwise_not(gray_img2)
# inverted_gray_img3 = cv2.bitwise_not(gray_img3)
# inverted_gray_img4 = cv2.bitwise_not(gray_img4)

cv2.imshow('image1', inverted_gray_img1)
# cv2.imshow('image2', inverted_gray_img2)
# cv2.imshow('image3', inverted_gray_img3)
# cv2.imshow('image4', inverted_gray_img4)
cv2.waitKey(0)

import cv2

img = cv2.imread('pic/mm.jpg', 1)  # 读取图片文件，参数1表示以彩色模式读取图片
sp = img.shape  # 获取图片的形状信息
print(sp)
sz1 = sp[0]  # 图片的高度（行数）
sz2 = sp[1]  # 图片的宽度（列数）
sz3 = sp[2]  # 像素值由三基色组成
print('width: %d height: %d number: %d' % (sz1, sz2, sz3))

# 输出像素(0,0)->(0,10)的11个像素的3基色RGB的灰度信息
for i in range(11):
    pixel = img[0, i]
    print("Pixel (0, %d): B: %d, G: %d, R: %d" % (i, pixel[0], pixel[1], pixel[2]))

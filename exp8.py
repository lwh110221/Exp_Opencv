from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


# 读取图片
def read_image(image_path):
    image = Image.open(image_path)
    image.show()  # 显示图片
    return image


# 将彩色图片转换为灰度图像
def convert_to_gray(image):
    gray_image = image.convert('L')
    return gray_image


# 统计灰度图像中各灰度级别的像素数量
def count_gray_levels(gray_image):
    gray_array = np.array(gray_image)
    histogram = np.zeros(256, dtype=int)
    rows, cols = gray_array.shape
    for i in range(rows):
        for j in range(cols):
            # 获取像素的灰度值，并将该灰度值的计数加 1
            histogram[gray_array[i, j]] += 1
    return histogram


# 绘制灰度直方图
def draw_histogram(histogram):
    plt.bar(range(len(histogram)), histogram)
    plt.title('Grayscale Histogram')
    plt.xlabel('Gray Level')
    plt.ylabel('Pixel Count')
    plt.show()


if __name__ == "__main__":
    image_path = 'pic/mm.jpg'
    image = read_image(image_path)
    gray_image = convert_to_gray(image)
    histogram = count_gray_levels(gray_image)
    draw_histogram(histogram)
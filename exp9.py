from PIL import Image
import numpy as np


# 读取图片
def read_image(image_path):
    image = Image.open(image_path)
    image.show()  # 显示图片
    return np.array(image)


# 平移矩阵
def translation_matrix(dx, dy):
    return np.array([[1, 0, dx], [0, 1, dy], [0, 0, 1]])


# 图像平移函数
def translate_image(image, dx, dy):
    rows, cols, channels = image.shape
    translated_image = np.zeros((rows + abs(dy), cols + abs(dx), channels), dtype=image.dtype)
    T = translation_matrix(dx, dy)
    for i in range(rows):
        for j in range(cols):
            # 齐次坐标
            point = np.array([i, j, 1]).reshape(3, 1)
            new_point = np.matmul(T, point)
            new_i, new_j, _ = new_point.flatten()
            # 确保新位置在平移后的图像范围内
            if 0 <= new_i < rows + abs(dy) and 0 <= new_j < cols + abs(dx):
                translated_image[int(new_i), int(new_j)] = image[i, j]
    return translated_image


if __name__ == "__main__":
    image_path = 'pic/mm.jpg'
    image = read_image(image_path)
    dx = 20
    dy = 5
    translated_image = translate_image(image, dx, dy)
    translated_image = Image.fromarray(translated_image.astype('uint8'))
    translated_image.show()
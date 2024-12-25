from PIL import Image
import numpy as np


# 读取图片
def read_image(image_path):
    image = Image.open(image_path)
    image.show()  # 显示图片
    return np.array(image)


# 缩放矩阵
def scaling_matrix(fx, fy):
    return np.array([[fx, 0, 0], [0, fy, 0], [0, 0, 1]])


# 图像缩放函数
def scale_image(image, fx, fy):
    rows, cols, channels = image.shape
    new_rows = int(rows * fx)
    new_cols = int(cols * fy)
    scaled_image = np.zeros((new_rows, new_cols, channels), dtype=image.dtype)
    S = scaling_matrix(fx, fy)
    for i in range(rows):
        for j in range(cols):
            # 齐次坐标
            point = np.array([i, j, 1]).reshape(3, 1)
            new_point = np.matmul(S, point)
            new_i, new_j, _ = new_point.flatten()
            # 确保新位置在缩放后的图像范围内
            if 0 <= new_i < new_rows and 0 <= new_j < new_cols:
                scaled_image[int(new_i), int(new_j)] = image[i, j]
    return scaled_image


if __name__ == "__main__":
    image_path = 'pic/BMW.jpg'
    image = read_image(image_path)
    fx = 2.0
    fy = 0.5
    scaled_image = scale_image(image, fx, fy)
    scaled_image = Image.fromarray(scaled_image.astype('uint8'))
    scaled_image.show()
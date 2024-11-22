from tkinter import LabelFrame, Scale, HORIZONTAL
from tkinter import Tk, Button, Label, filedialog, Frame
from PIL import Image, ImageTk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import ttk
import tkinter.font as tkFont


# 全局变量，用于存储当前打开的图片
current_image = None
# 全局变量，用于在界面上显示处理后的图像
image_label = None
# 全局变量，用于保存原始图片
original_image = None
# 全局变量，用于存储最大显示尺寸
MAX_DISPLAY_SIZE = (600, 400)


# 灰度变换算法函数

def global_linear_transformation():
    """全域线性变换函数"""
    def apply_transform(params):
        global current_image, image_label
        if current_image:
            try:
                img_array = np.array(current_image)
                a = params['斜率']
                b = params['偏移']
                img_array = np.clip(a * img_array + b, 0, 255).astype('uint8')
                processed_image = Image.fromarray(img_array)
                update_image_display(processed_image)
                print("执行全域线性变换算法成功")
            except Exception as e:
                print("执行全域线性变换算法出现错误:", e)
    
    params = [
        ('斜率', 0.1, 3.0, 1.0),
        ('偏移', -100, 100, 0)
    ]
    ParameterWindow("线性变换参数", apply_transform, params)


def color_to_gray():
    """彩色图像灰度化函数，此处需完善具体算法实现"""
    global current_image, image_label
    if current_image:
        try:
            processed_image = current_image.convert('L')
            update_image_display(processed_image)
            print("执行彩色图像灰度化算法成功")
        except Exception as e:
            print("执行彩色图像灰度化算法出现错误:", e)
    else:
        print("请先选择图片")


def inverse_color():
    """反色变换函数"""
    global current_image, image_label
    if current_image:
        try:
            img_array = np.array(current_image)
            if len(img_array.shape) == 3:  # RGB图像
                processed_image = Image.fromarray(255 - img_array)
            else:  # 灰度图像
                processed_image = Image.fromarray(255 - img_array)
            update_image_display(processed_image)
            print("执行反色变换算法成功")
        except Exception as e:
            print("执行反色变换算法出现错误:", e)
    else:
        print("请先选择图片")


def threshold_processing():
    """阈值化处理函数"""
    def apply_threshold(params):
        global current_image, image_label
        if current_image:
            try:
                threshold = params['阈值']
                width, height = current_image.size
                img_array = np.array(current_image)
                gray = np.dot(img_array[...,:3], [0.299, 0.587, 0.114])
                binary = np.where(gray > threshold, 255, 0)
                processed_image = Image.fromarray(binary.astype('uint8'))
                update_image_display(processed_image)
                print("执行阈值化处理算法成功")
            except Exception as e:
                print("执行阈值化处理算法出现错误:", e)
    
    params = [
        ('阈值', 0, 255, 128)
    ]
    ParameterWindow("阈值处理参数", apply_threshold, params)


def clipping_processing():
    """削波处理函数"""
    def apply_clipping(params):
        global current_image, image_label
        if current_image:
            try:
                lower_limit = params['下限']
                upper_limit = params['上限']
                
                img_array = np.array(current_image)
                if len(img_array.shape) == 3:
                    gray = np.dot(img_array[...,:3], [0.299, 0.587, 0.114])
                else:
                    gray = img_array
                    
                clipped = np.clip(gray, lower_limit, upper_limit)
                processed_image = Image.fromarray(clipped.astype('uint8'))
                update_image_display(processed_image)
                print("执行削波处理算法成功")
            except Exception as e:
                print("执行削波处理算法出现错误:", e)
    
    params = [
        ('下限', 0, 255, 30),
        ('上限', 0, 255, 220)
    ]
    ParameterWindow("削波处理参数", apply_clipping, params)


# 图像平滑算法函数

def neighborhood_averaging():
    """邻域平均法函数，此处需完善具体算法实现"""
    global current_image, image_label
    if current_image:
        try:
            width, height = current_image.size
            img_array = np.array(current_image)
            # 简单示例3x3邻域，可按需调整
            kernel_size = 3
            pad = kernel_size // 2
            padded_img = np.pad(img_array, ((pad, pad), (pad, pad), (0, 0)), 'constant')
            processed_img = np.zeros_like(img_array)
            for y in range(height):
                for x in range(width):
                    neighborhood = padded_img[y:y + kernel_size, x:x + kernel_size]
                    average_value = np.mean(neighborhood, axis=(0, 1))
                    processed_img[y, x] = average_value
            processed_image = Image.fromarray(processed_img.astype('uint8'))
            update_image_display(processed_image)
            print("执行邻域平均法算法成功")
        except Exception as e:
            print("执行邻域平均法算法出现错误:", e)
    else:
        print("请先选择图片")


def median_filtering():
    """中值滤波函数"""
    def apply_median_filter(params):
        global current_image, image_label
        if current_image:
            try:
                kernel_size = int(params['窗口大小'])
                if kernel_size % 2 == 0:  # 确保窗口大小为奇数
                    kernel_size += 1
                    
                pad = kernel_size // 2
                img_array = np.array(current_image)
                
                if len(img_array.shape) == 3:  # RGB图像
                    height, width, channels = img_array.shape
                    padded_img = np.pad(img_array, ((pad, pad), (pad, pad), (0, 0)), mode='reflect')
                    result = np.zeros_like(img_array)
                    
                    for i in range(height):
                        for j in range(width):
                            for c in range(channels):
                                window = padded_img[i:i+kernel_size, j:j+kernel_size, c]
                                result[i, j, c] = np.median(window)
                else:  # 灰度图像
                    height, width = img_array.shape
                    padded_img = np.pad(img_array, ((pad, pad), (pad, pad)), mode='reflect')
                    result = np.zeros_like(img_array)
                    
                    for i in range(height):
                        for j in range(width):
                            window = padded_img[i:i+kernel_size, j:j+kernel_size]
                            result[i, j] = np.median(window)
                
                processed_image = Image.fromarray(result.astype('uint8'))
                update_image_display(processed_image)
                print("执行中值滤波算法成功")
            except Exception as e:
                print("执行中值滤波算法出现错误:", e)
    
    params = [
        ('窗口大小', 3, 9, 3)  # 最小值3，最大值9，默认值3
    ]
    ParameterWindow("中值滤波参数", apply_median_filter, params)


# 直方图相关函数

def draw_histogram():
    """绘制直方图函数"""
    global current_image
    if current_image:
        try:
            # 创建新窗口显示直方图
            hist_window = Tk()
            hist_window.title("图像直方图")
            
            # 创建图形
            fig, axs = plt.subplots(2, 2, figsize=(10, 8))
            fig.suptitle('图像直方图分析')
            
            # 获取图像数据
            img_array = np.array(current_image)
            
            # 绘制RGB直方图
            if len(img_array.shape) == 3:  # RGB图像
                colors = ['red', 'green', 'blue']
                for i, color in enumerate(colors):
                    axs[0, 0].hist(img_array[:,:,i].ravel(), bins=256, 
                                 range=(0, 256), color=color, alpha=0.5)
                axs[0, 0].set_title('RGB通道直方图')
                axs[0, 0].set_xlabel('像素值')
                axs[0, 0].set_ylabel('频率')
                
                # 分别绘制三个通道的直方图
                for i, (color, title) in enumerate(zip(colors, ['R通道', 'G通道', 'B通道'])):
                    row = (i+1) // 2
                    col = (i+1) % 2
                    axs[row, col].hist(img_array[:,:,i].ravel(), bins=256, 
                                     range=(0, 256), color=color)
                    axs[row, col].set_title(title)
                    axs[row, col].set_xlabel('像素值')
                    axs[row, col].set_ylabel('频率')
            else:  # 灰度图像
                axs[0, 0].hist(img_array.ravel(), bins=256, range=(0, 256), 
                             color='gray')
                axs[0, 0].set_title('灰度直方图')
                axs[0, 0].set_xlabel('像素值')
                axs[0, 0].set_ylabel('频率')
                
                # 隐藏多余的子图
                axs[0, 1].set_visible(False)
                axs[1, 0].set_visible(False)
                axs[1, 1].set_visible(False)
            
            plt.tight_layout()
            
            # 将matplotlib图形嵌入tkinter窗口
            canvas = FigureCanvasTkAgg(fig, master=hist_window)
            canvas.draw()
            canvas.get_tk_widget().pack(fill='both', expand=True)
            
            print("绘制直方图成功")
        except Exception as e:
            print("绘制直方图出错:", e)
    else:
        print("请先选择图片")


# 几何变换算法函数

def image_translation():
    """图像平移函数，此处需完善具体算法实现"""
    global current_image, image_label
    if current_image:
        try:
            # 示例平移量，可按需调整
            x_offset = 50
            y_offset = 30
            width, height = current_image.size
            img_array = np.array(current_image)
            translated_img = np.zeros((height + abs(y_offset), width + abs(x_offset), 3), dtype='uint8')
            if y_offset >= 0 and x_offset >= 0:
                translated_img[y_offset:, x_offset:] = img_array
            elif y_offset < 0 and x_offset >= 0:
                translated_img[:height + y_offset, x_offset:] = img_array[-y_offset:]
            elif y_offset >= 0 and x_offset < 0:
                translated_img[y_offset:, :width + x_offset] = img_array[:, -x_offset:]
            else:
                translated_img[:height + y_offset, :width + x_offset] = img_array[-y_offset:, -x_offset:]
            processed_image = Image.fromarray(translated_img)
            update_image_display(processed_image)
            print("执行图像平移算法成功")
        except Exception as e:
            print("执行图像平移算法出现错误:", e)
    else:
        print("请先选择图片")


def image_mirroring():
    """图像镜像函数，此处需完善具体算法实现"""
    global current_image, image_label
    if current_image:
        try:
            # 水平镜像示例
            processed_image = current_image.transpose(Image.FLIP_LEFT_RIGHT)
            update_image_display(processed_image)
            print("执行图像镜像算法成功")
        except Exception as e:
            print("执行图像镜像算法出现错误:", e)
    else:
        print("请先选择图片")


def image_zooming():
    """图像放大函数"""
    def apply_zoom(params):
        global current_image, image_label
        if current_image:
            try:
                zoom_factor = params['放大倍数']
                width, height = current_image.size
                new_width = int(width * zoom_factor)
                new_height = int(height * zoom_factor)
                # 使用高质量的重采样方法
                processed_image = current_image.resize((new_width, new_height), 
                                                     Image.Resampling.LANCZOS)
                current_image = processed_image  # 更新当前图像
                update_image_display(processed_image)
                print("执行图像放大算法成功")
            except Exception as e:
                print("执行图像放大算法出现错误:", e)
    
    params = [
        ('放大倍数', 0.5, 4.0, 1.0)
    ]
    ParameterWindow("图像放大参数", apply_zoom, params)


# 选择图片的函数
def select_image():
    global current_image, original_image, image_label
    file_path = filedialog.askopenfilename()
    if file_path:
        try:
            original_image = Image.open(file_path)
            current_image = original_image.copy()
            if image_label:
                image_label.destroy()
            image_label = Label(image_frame)  # 改为放在image_frame中
            image_label.pack(expand=True, padx=5, pady=5)
            update_image_display(current_image)
            print("已成功选择图片:", file_path)
        except Exception as e:
            print("选择图片出现错误:", e)
    else:
        print("未选择任何图片")


# 更新界面上显示图像的函数
def update_image_display(image):
    global image_label
    if image:
        # 计算调整后的尺寸
        display_size = get_display_size(image)
        # 调整图片大小
        display_image = image.copy()
        display_image.thumbnail(display_size, Image.Resampling.LANCZOS)
        
        tk_image = ImageTk.PhotoImage(display_image)
        image_label.configure(image=tk_image)
        image_label.image = tk_image  # 保持引用


# 计算显示尺寸的函数
def get_display_size(image):
    # 获取原始尺寸
    original_width, original_height = image.size
    
    # 计算缩放比例
    width_ratio = MAX_DISPLAY_SIZE[0] / original_width
    height_ratio = MAX_DISPLAY_SIZE[1] / original_height
    ratio = min(width_ratio, height_ratio)
    
    # 如果图片小于最大显示尺寸，则保持原始大小
    if ratio >= 1:
        return (original_width, original_height)
    
    # 计算新的尺寸
    new_width = int(original_width * ratio)
    new_height = int(original_height * ratio)
    return (new_width, new_height)


# 重置函数
def reset_image():
    global current_image, original_image
    if original_image:
        current_image = original_image.copy()
        update_image_display(current_image)
        print("图片已重置")
    else:
        print("没有可重置的图片")


class ParameterWindow:
    def __init__(self, title, callback, parameters):
        self.window = Tk()
        self.window.title(title)
        self.callback = callback
        self.values = {}
        
        for param in parameters:
            name, min_val, max_val, default = param
            self.values[name] = default
            Label(self.window, text=name).pack()
            scale = Scale(self.window, from_=min_val, to=max_val, 
                         orient=HORIZONTAL, resolution=0.1,
                         command=lambda v, n=name: self.update_value(n, v))
            scale.set(default)
            scale.pack()
        
        Button(self.window, text="应用", command=self.apply).pack()
        
    def update_value(self, name, value):
        self.values[name] = float(value)
        
    def apply(self):
        self.callback(self.values)
        self.window.destroy()


root = Tk()
root.title("数字图像处理工具")
root.geometry("800x600")  # 设置窗口大小

# 创建左侧控制面板
control_panel = LabelFrame(root, text="控制面板")
control_panel.pack(side='left', fill='y', padx=5, pady=5)

# 图片显示区域
image_frame = LabelFrame(root, text="图片显示")
image_frame.pack(side='right', fill='both', expand=True, padx=5, pady=5)

# 选择图片和重置按钮放在一起
button_frame = Frame(control_panel)
button_frame.pack(fill='x', padx=5, pady=5)
select_image_button = Button(button_frame, text="选择图片", command=select_image)
select_image_button.pack(side='left', padx=2)
reset_button = Button(button_frame, text="重置图片", command=reset_image)
reset_button.pack(side='left', padx=2)

# 灰度变换算法按钮
gray_trans_buttons_frame = LabelFrame(control_panel, text="灰度变换算法")
gray_trans_buttons_frame.pack()
Button(gray_trans_buttons_frame, text="全域线性变换", command=global_linear_transformation).pack()
Button(gray_trans_buttons_frame, text="彩色图像灰度化", command=color_to_gray).pack()
Button(gray_trans_buttons_frame, text="反色变换", command=inverse_color).pack()
Button(gray_trans_buttons_frame, text="阈值化处理", command=threshold_processing).pack()
Button(gray_trans_buttons_frame, text="削波处理", command=clipping_processing).pack()

# 图像平滑算法按钮
smooth_buttons_frame = LabelFrame(control_panel, text="图像平滑算法")
smooth_buttons_frame.pack()
Button(smooth_buttons_frame, text="邻域平均法", command=neighborhood_averaging).pack()
Button(smooth_buttons_frame, text="中值滤波", command=median_filtering).pack()

# 直方图按钮
histogram_button = Button(control_panel, text="绘制直方图", command=draw_histogram)
histogram_button.pack()

# 几何变换算法按钮
geo_trans_buttons_frame = LabelFrame(control_panel, text="几何变换算法")
geo_trans_buttons_frame.pack()
Button(geo_trans_buttons_frame, text="图像平移", command=image_translation).pack()
Button(geo_trans_buttons_frame, text="图像镜像", command=image_mirroring).pack()
Button(geo_trans_buttons_frame, text="图像放大", command=image_zooming).pack()

root.mainloop()
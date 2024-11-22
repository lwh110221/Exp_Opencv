import numpy as np
import scipy.fftpack
from matplotlib import pyplot as plt

# 创建信号
srate = 1000   # 采样率 (Hz)
time = np.arange(0., 2., 1 / srate)  # 时间序列
pnts = len(time)  # 时间点数

# 模拟信号：两个不同频率的正弦波叠加
signal = 2.5 * np.sin(2 * np.pi * 4 * time) + 1.5 * np.sin(2 * np.pi * 6.5 * time)

# 傅里叶变换准备
fourTime = np.array(range(0, pnts)) / pnts
fCoefs = np.zeros((len(signal)), dtype=complex)

# 计算傅里叶系数
for fi in range(0, pnts):
    csw = np.exp(-1j * 2 * np.pi * fi * fourTime)  # 复数正弦波
    fCoefs[fi] = np.sum(np.multiply(signal, csw)) / pnts  # 点积

# 计算幅度
ampls = 2 * np.abs(fCoefs)

# 频率矢量
hz = np.linspace(0, srate / 2, num=int(np.floor(pnts / 2) + 1))

# 绘制频域信号图像
plt.figure(figsize=(10, 5))
plt.stem(hz, ampls[range(0, len(hz))])
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.title('Frequency Domain Signal')
plt.xlim(0, 10)
plt.show()


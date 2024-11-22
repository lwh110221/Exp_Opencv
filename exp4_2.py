import numpy as np
import matplotlib.pyplot as plt

# 一般参数设置
srate = 500  # 采样率 (Hz)
time = np.arange(0., 2., 1. / srate)  # 时间序列

# 正弦波参数设置
freq = 5     # 频率 (Hz)
ampl = 2     # 振幅
phas = np.pi / 3  # 相位 (弧度)

csw = ampl * np.exp(1j * (2 * np.pi * freq * time + phas))

from mpl_toolkits.mplot3d import Axes3D

# 生成图形
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(time, np.real(csw), np.imag(csw))
ax.set_xlabel('Time (sec)')
ax.set_ylabel('Real Part')
ax.set_zlabel('Imaginary Part')
ax.set_title('Complex Sine Wave in 3D')
plt.show()


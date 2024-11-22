import numpy as np
import matplotlib.pyplot as plt

# 一般参数设置
srate = 500  # 采样率 (Hz)
time = np.arange(0., 2., 1. / srate)  # 时间序列

# 正弦波参数设置
freq = 5     # 频率 (Hz)
ampl = 2     # 振幅
phas = np.pi / 3  # 相位 (弧度)

# 生成复数正弦波
csw = ampl * np.exp(1j * (2 * np.pi * freq * time + phas))

plt.figure(figsize=(10, 4))
plt.plot(time, np.real(csw), label='Real Part')
plt.plot(time, np.imag(csw), label='Imaginary Part')
plt.xlabel('Time (sec.)')
plt.ylabel('Amplitude')
plt.title('Complex Sine Wave Projections')
plt.legend()
plt.show()

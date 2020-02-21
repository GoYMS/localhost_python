import wave
from matplotlib import pylab as pl
import numpy as np
# 打开WAV文档
f = wave.open("1.wav", "rb")
# open返回一个的是一个Wave_read类的实例，通过调用它的方法读取WAV文件的格式和数据：
# 读取格式信息
# getparams：一次性返回所有的WAV文件的格式信息，它返回的是一个元组(tuple)：声道数, 量化位数（byte单位）, 采样频率,
# 采样点数, 压缩类型的描述。wave模块只支持非压缩的数据，因此可以忽略最后1个信息：
# getnchannels, getsampwidth, getframerate, getnframes等方法可以单独返回WAV文件的特定的信息。
# ( nchannels音频通道数, sampwidth量化位数, framerate采样频率, nframes音频帧数, comptype, compname )
params = f.getparams()
nchannels, sampwidth, framerate, nframes = params[:4]
# 读取波形数据
# 创建一个字符串表示readframes返回的二进制数据
str_data = f.readframes(nframes)
f.close()

# 根据声道数和量化单位，将读取的二进制数据转换为一个可以计算的数组：
wave_data = np.frombuffer(str_data, dtype=np.short)
# wave_data是一个一维的short类型的数组，但音频文件为双声道，因此它由左右两个声道的取样交替构成
wave_data.shape = -1, 2
wave_data = wave_data.T
# 通过取样点数和取样频率计算出每个取样的时间：
time = np.arange(0, nframes) * (1.0 / framerate)
# 绘制波形
pl.subplot(211)
pl.plot(time, wave_data[0])
pl.subplot(212)
pl.plot(time, wave_data[1], c="g")
pl.xlabel("time (seconds)")
pl.show()
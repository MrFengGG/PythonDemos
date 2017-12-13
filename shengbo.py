import wave
import pylab as pl
import numpy as np

f = wave.open("C:/Users/JACK/Desktop/录音.wav","rb")

params = f.getparams()
nchannels,sampwidth,framerate,nframes = params[:4]

str_data = f.readframes(nframes)
f.close()

wave_data = np.fromstring(str_data,dtype=np.short)
wave_data.shape = -1,2
wave_data = wave_data.T

time = np.arange(0,nframes)*(1.0/framerate)
pl.subplot(211)
pl.plot(time,wave_data[0])
pl.subplot(211)
pl.plot(time,wave_data[1],c="g")
pl.xlabel("time(secounds)")
pl.show()

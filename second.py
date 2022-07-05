from time import time
import wave
import matplotlib.pyplot as plt
import numpy as np

obj= wave.open("Recording.wav","rb")
sample_freq= obj.getframerate()
n_samples= obj.getnframes()
signal_wav = obj.readframes(-1)
obj.close()

t_audio = n_samples/sample_freq
print(t_audio)

#creating a plot
signal_array=np.frombuffer(signal_wav, dtype=np.int16)
times= np.linspace(0,t_audio,num=n_samples)
plt.figure(figsize=(15,5))
plt.plot(times)
plt.title("Audio signal")
plt.ylabel("signal wave")
plt.xlabel("time")
plt.xlim(0,t_audio)
plt.show()

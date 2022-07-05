import wave
import pyaudio

FRAMES_PER_BUFFER = 3200
FORMAT = pyaudio.paInt16
channels = 1
rate = 16000

p = pyaudio.PyAudio()

stream = p.open(
    format=FORMAT,
    channels=channels,
    rate=rate,
    input=True,
    frames_per_buffer=FRAMES_PER_BUFFER

)

print("start recording")
seconds = 5
frames = []
for i in range(0, int(rate/FRAMES_PER_BUFFER * seconds)):
    data = stream.read(FRAMES_PER_BUFFER)
    frames.append(data)

stream.stop_stream()
stream.close()
p.terminate()

obj = wave.open("output.wav", "wb")
obj.setnchannels(channels)
obj.setframerate(rate)
obj.setsampwidth(p.get_sample_size(FORMAT))
obj.writeframes(b"".join(frames))
obj.close()

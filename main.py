# Audio file formats
# .mp3  - losely compressed audio file.
# .flac - less lossely compressed audio file.
# .wav  - uncompressed audio file.

from time import time
import wave

# audio signal parameters
# -number of channels.
# - sample width
# - framerate / sample rate 44,100Hz
# - number of frames
# - values of a frame

# load a wave file
obj = wave.open("Recording.wav", "rb")  # read binary
print("number of channels", obj.getnchannels())
print('sample width', obj.getsampwidth())
print('frame rate', obj.getframerate())
print('Number of frames', obj.getnframes())
print("Parameter", obj.getparams())

# calculate time of the audio
time_audio = obj.getnframes()/obj.getframerate()
print(time_audio)

frames = obj.readframes(-1)
print(type(frames), type(frames[0]))
print(len(frames)/2)
obj.close()
# writing a audio file

obj_new = wave.open("audio_new.wav", "wb")

obj_new.setnchannels(2)
obj_new.setsampwidth(2)
obj_new.setframerate(48000.0)

obj_new.writeframes(frames)
obj_new.close()

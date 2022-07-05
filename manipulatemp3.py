from re import A
from sqlite3 import adapt
from pydub import AudioSegment
audio = AudioSegment.from_wav("Recording.wav")

# increase the volume by 6Db

audio = audio+6
audio = audio*2
audio = audio.fade_in(2000)
audio.export("mashup.mp3", format="mp3")
audio2 = AudioSegment.from_mp3("mashup.mp3")
print("done")

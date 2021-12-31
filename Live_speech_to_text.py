import sounddevice as sd
import speech_recognition as sr

fs = sd.default.samplerate
sd.default.channels = 2 

duration = 10 # seconds
myrecording = sd.rec(int(duration * fs ), samplerate=fs, channels=2)

myrecording = sd.rec(int(duration * fs))

sd.wait()
myrecording = sd.rec(int(duration * fs), dtype='float64')
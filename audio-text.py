import speech_recognition as sr
import soundfile
data,samplerate=soundfile.read('sample.wav')
soundfile.write('new.wav',data,samplerate, subtype='PCM_16')

r=sr.Recognizer()
with sr.AudioFile("new.wav") as source:
    audio_data=r.record(source)
    text=r.recognize_google(audio_data)
    print(text)
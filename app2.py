import speech_recognition as sr
from os import path
from gtts import gTTS
from playsound import playsound

AUDIO = path.join(path.dirname(path.realpath(__file__)),'audio.wav')

r = sr.Recognizer() #inicializa o reconhecedor de audio
with sr.AudioFile(AUDIO) as source:
    audio = r.record(source) #le o audio
    texto = r.recognize_google(audio,language='pt-BR') #definindo a lingua
    print('Você disse: ',texto)

    tts = gTTS(f"{texto}",lang='pt')
    tts.save(f'{texto}.mp3')
    playsound(f'{texto}.mp3')
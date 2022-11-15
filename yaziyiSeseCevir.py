from gtts import gTTS

from playsound import playsound

audio = 'speech.mp3'
language = 'en'  #tr yazılır.

sp = gTTS(text = "Python Junior Developer", lang = language,slow=False)


sp.save(audio)
playsound(audio)
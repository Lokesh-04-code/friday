import pyttsx3
import datetime

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
  engine.say(audio)
  engine.runAndWait()

def WishMe():
  hour=int(datetime.datetime.now().hour)
  if hour>=0 and hour<12:
    speak("Good morning, sir")
  elif hour>=12 and hour<18:
    speak("Good Afternoon, sir")
  else:
    speak("goood evening,sir")
  speak("how can i help you ")
import requests
import json
import pyttsx3
from greet import *  # Import custom modules

from searchnow import *
from datetime import timedelta
import pywhatkit
strTime=int(datetime.datetime.now().strftime("%H"))
update=int((datetime.datetime.now()+timedelta(minutes=2)).strftime("%M"))
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
  engine.say(audio)
  engine.runAndWait()
def sendmesssage():
  speak("whomm do yo want to message")
  a=takeCommand()
  speak("whats the message")
  message=takeCommand()
  if a=="lokesh":
    
    pywhatkit.sendwhatmsg("+917382824195",message,time_hour=strTime,time_min=update)

  elif a=="ganesh":
    pywhatkit.sendwhatmsg("+917989828391",message,time_hour=strTime,time_min=update)
    
  elif a=="tarun":
    pywhatkit.sendwhatmsg("+919494070922",message,time_hour=strTime,time_min=update)
  elif a=="akhil":
    pywhatkit.sendwhatmsg("+919182069451",message,time_hour=strTime,time_min=update)

  elif a=="vijay":
    pywhatkit.sendwhatmsg("+919030146290",message,time_hour=strTime,time_min=update)


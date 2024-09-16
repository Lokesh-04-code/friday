import speech_recognition as sr
import  pyttsx3
import pywhatkit
import wikipedia
from greet import *
import webbrowser
from googlesearch import search
def takeCommand():
  r=sr.Recognizer()
  with sr.Microphone() as source:
    
    print("listening....")
    
    r.pause_threshold = 0.5  # Adjust the pause duration between words
    r.energy_threshold = 300  # Minimum energy level for speech detection
    r.dynamic_energy_threshold = True  # Dynamically adjust the threshold
    audio=r.listen(source)
  try: 
    print("recognizing...")
    query=r.recognize_google(audio,language='en-in')
    print(f"use said:{query}\n")
  except Exception as e:
  #  print(e)
    print("say that again pleaase...")
    
    return "none"
  return query

def searchGoogle(query):
  if "google" in query:
    query=query.replace('jarvis',"")
    query=query.replace("on google ","")
    query=query.replace("google","")
    query=query.replace("search","")
    query=query.replace("on","")
    speak("this is what i found on google")
    try:
      pywhatkit.search(query)
      search_results = search(query, num_results=5)
      speak(search_results)
    except Exception as e:
      print(e)
      

def searchYoutube(query):
  if'youtube' in query:
    speak("this is what i found for your search")
    query=query.replace("youtube search","")
    query=query.replace("youtube","")
    query=query.replace("jarvis","")
    web="https://www.youtube.com/results?search_query="+query
    webbrowser.open(web)
    pywhatkit.playonyt(query)
    speak("done sir")

def searchWikipedia(query):
  if "wikipedia" in query:
    speak("searching from wkipedia")
    query=query.replace("wikipedia","")
    query=query.replace("search wikipedia","")
    query=query.replace("jarvis","")
    results= wikipedia.summary(query,sentences=2)
    speak("according to wikipedia...")
    print(results)
    speak(results)


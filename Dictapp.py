import os
import pyautogui
import webbrowser
import pyttsx3
from time import sleep
from searchnow import *

dictapp = {
    "command prompt": "cmd",
    "paint": "mspaint",
    "word": "winword",
    "excel": "excel",
    "chrome": "chrome",
    "vs code": "code",
    "powerpoint": "powerpnt",
    "notepad": "notepad",
    "calculator": "calc",
    "file explorer": "explorer",
    "task manager": "taskmgr",
    "control panel": "control",
    "snipping tool": "SnippingTool",
    "edge": "msedge",
    "windows media player": "wmplayer",
    "outlook": "outlook",
    "skype": "skype",
    "whatsapp":"C:\\Users\\gemba\\OneDrive\\Desktop\\WhatsApp"
}

def opeappweb(query):
  speak("launching, sir")
  if ".com" in query or ".co.in" in query or ".org" in query:
    query=query.replace("open","")
    query=query.replace("jarvis","")
    query=query.replace("launch","")
    query=query.replace(" ","")
    webbrowser.open(f"https://www.{query}")

  else:
    keys=list(dictapp.keys())
    for app in keys:
      if app in query:
        os.system(f"start {dictapp[app]}")
  
def closeappweb(query):

  speak("closing, sir")
  if "one tab" in query or "1 tab" in query:
    print("1")
    pyautogui.hotkey("ctrl","w")

  elif "2 tab" in query or "two tab" in query:
    pyautogui.hotkey('ctrl','w')
    sleep(0.5)
    pyautogui.hotkey('ctrl',"w")
    print("2")
    speak("all tabs closed")

  elif "3 tab" in query or "three tab" in query:
    pyautogui.hotkey('ctrl','w')
    sleep(0.5)
    pyautogui.hotkey('ctrl',"w")
    sleep(0.5)
    pyautogui.hotkey('ctrl',"w")
    print("3")
    speak("all tabs closed")

  elif "4 tab" in query or "four tab" in query:
    pyautogui.hotkey('ctrl','w')
    sleep(0.5)
    pyautogui.hotkey('ctrl',"w")
    sleep(0.5)
    pyautogui.hotkey('ctrl',"w")
    sleep(0.5)
    pyautogui.hotkey('ctrl',"w")
    print("4")
    speak("all tabs closed")

  elif "5 tab" in query or "five tab" in query:
    pyautogui.hotkey('ctrl','w')
    sleep(0.5)
    pyautogui.hotkey('ctrl',"w")
    sleep(0.5)
    pyautogui.hotkey('ctrl',"w")
    sleep(0.5)
    pyautogui.hotkey('ctrl',"w")
    sleep(0.5)
    pyautogui.hotkey('ctrl',"w")
    print("5")
    speak("all tabs closed")

  else:
    keys=list(dictapp.keys())
    for app in keys:
      if app in query:
        os.system(f"taskkill /f /im {dictapp[app]}.exe")


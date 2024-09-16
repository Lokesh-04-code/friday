import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib 
from greet import *
from searchnow import *
from wikipedia.exceptions import DisambiguationError, PageError  
import requests
from bs4 import BeautifulSoup
import pyautogui
import smtplib
from email.message import EmailMessage
from Dictapp import *
import keyboard
from keyboard import *
from news import *
from whatsapp import *
from whatsapp import sendmesssage
def sendMail(to,content):
  server=smtplib.SMTP('smtp.gmail.com',587)
  server.ehlo()
  server.starttls()
  server.login('gembali.lokesh2004@gmail.com',"Lokesh@123")
  server.sendmail('gembali.lokesh2004@gmail.com',to,content)
  server.close()
schedule = {
    
    'tuesday': ['maths at 9:00 AM', 'data Structures and algorithms at 11:00 AM', 'softskills 12 PM'],
    'wednesday': ['entreprenuership 9:30 AM', 'c language 11:00 AM', 'dsa lab 1:00 PM'],
    'thursday': ['AI at 10:00 AM', 'data Structures and algorithms at 11:00 AM', 'java 12 PM'],
    'friday': ['entreprenuership lab 9:30 AM', 'introduction to programming 11:00 AM', 'dsa theory 1:00 PM'],
    'saturday': ['discrete maths at 9:00 AM', 'data Structures and algorithms at 11:00 AM', 'softskills 12 PM'],
    'monday': ['entreprenuership 9:30 AM', 'c language 11:00 AM', 'dsa lab 1:00 PM'],
  
}
def list_classes(day):
    
    day = day.lower()

    if day in schedule:
        
        classes = schedule[day]
        speak(f"Your classes on {day.capitalize()} are: ")
        for cls in classes:
            speak(cls)
    else:
        speak("You don't have any classes scheduled for this day.")

def sendEmail(subject, body, to_email):
    
    # Set your email and app-specific password
    sender_email = "gembali.lokesh2004@gmail.com"
    sender_password = "Lokesh@123"

    # Create the email message
    msg = EmailMessage()
    msg.set_content(body)  # Email body
    msg["Subject"] = subject  # Email subject
    msg["From"] = sender_email  # Sender's email
    msg["To"] = to_email  # Recipient's email
 
    try:
        # Connect to Gmail's SMTP server
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            # Login to the server
            smtp.login(sender_email, sender_password)

            # Send the email
            smtp.send_message(msg)
            print(f"Email sent to {to_email} successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
def alarm(query):
   timehere=open("Alarmtext.txt","a")
   timehere.write(query)
   timehere.close()
   os.startfile('alarm.py')
if __name__=="__main__":
  while True:
    query=takeCommand().lower()
    if 'akeup' or 'wake up' in query:
        WishMe()
    while True:
      query=takeCommand().lower()

      if 'wikipedia' in query:
         searchWikipedia(query)

      elif 'hello' in query:
         speak("hello sir, how are you")
      elif 'mini player' in query:
         pyautogui.press("i")
      elif 'pause' in query:
         pyautogui.press("k")

      elif 'play' in query:
         pyautogui.press("k")

      elif 'full screen' in query:
         print("full screen")
         pyautogui.press("f")

      elif 'theatre' in query:
         pyautogui.press("t")
    
      elif 'mute' in query:
         pyautogui.press("m")

      elif 'volume up'  in query or 'increase volume' in query:
         speak("turning volume up sir")
         volumeup()
      elif 'volume down' in query or 'decrease volume' in query:
         speak("turning volume down sir")
         volumedown()
      elif 'i am fine' in query:
         speak("that's great sir")
      elif 'how are you' in query:
         speak(" i am perfect sir")

      elif 'thank you' in query:
         speak("you are welcome sir")

      elif 'open youtube' in query: 
        webbrowser.open("youtube.com")

      elif 'open google' in query:
        webbrowser.open("google.com")

      elif "open whatsapp" in query:
         opeappweb(query)
      elif "open" in query:    
         opeappweb(query)

      elif "close" in query:
         closeappweb(query)
         

      elif "google" in query:
         searchGoogle(query)
      elif "youtube" in query:
         searchYoutube(query)
      elif "news" in query:
         latestnews()


      elif "whatsapp" in query: 
         from whatsapp import sendmesssage
         sendmesssage()
         

      elif 'play music' in query: 
        music_dir="C:\\Users\\gemba\\OneDrive\\Desktop\\songs"
        songs=os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir,songs[0]))
      elif "set an alarm" in query:
         print("input time example 10 and 10 and 10")
         speak("set the time")
         a=input('please tell the time')
         alarm(a)
         speak("done, sir")
      elif 'the time' in query:
        strTime=datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"time is {strTime}")
        
      elif 'open vs code' in query:
        os.startfile("C:\\Users\\gemba\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

      elif 'mail to lokesh' in query:
        
        try:
          
          speak("what should i say?")
          content=takeCommand()
          speak("what is the subject")
          subject=takeCommand()
          to="lokesh.23bce9813@vitapstudent.ac.in"
          sendMail(to,content)
          speak("Email has sent")

        except Exception as e:
          
          print(e)
          speak("sorry boss i a unable to send the Email due to network issue")

      elif 'open notepad' in query:
        
        os.startfile("C:\\Users\\gemba\\OneDrive\\Desktop\\Notepad.lnk")

      elif 'what are my class' in query:
                
                day = query.split()[-1]  # Get the day from the query (e.g., "Monday")
                list_classes(day)

      elif "to sleep"  in query:
        
        speak('ok boss you can call me anytime')
        break
  
      elif "finally sleep" in query:
         speak("going to sleep")
         exit()

      elif "remember that" in query:
         rememberMessage=query.replace("remember that","")
         rememberMessage=query.replace("jarvis","")
         speak("you told me to that"+rememberMessage)
         remember=open("Remember.txt","w")
         remember.write(rememberMessage)
         remember.close()

      elif "what do you remember" in query:
         remember=open("Remember.txt","r")
         speak("you told me that "+remember.read())

      elif "shut down" in query:
         speak("are you want to shut conform yes or no")
         check=takeCommand()
         if("yes"  in check or "s" in check):
            os.system("shutdown /s /t 1")
         else:
            break
      else :
         searchWikipedia(query)
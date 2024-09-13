import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib 

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
  speak("i am friday sir.how can i help you ")

def takeCommand():
  r=sr.Recognizer()
  with sr.Microphone() as source:
    
    print("listennig....")
    
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
import smtplib
from email.message import EmailMessage
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
    'thursday': ['maths at 9:00 AM', 'data Structures and algorithms at 11:00 AM', 'softskills 12 PM'],
    'friday': ['entreprenuership 9:30 AM', 'c language 11:00 AM', 'dsa lab 1:00 PM'],
    'saturday': ['maths at 9:00 AM', 'data Structures and algorithms at 11:00 AM', 'softskills 12 PM'],
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

  #it takes microphone input from the user and returns string output
if __name__=="__main__":
  WishMe()
  while True:
   query=takeCommand().lower()

   if('wikipedia' in query):
     speak('searching wikipedia...')
     query=query.replace("wikipedia","")
     results=wikipedia.summary(query,sentences=2)
     speak("According to wikipedia")
     speak(results)

   elif 'open youtube' in query:
     webbrowser.open("youtube.com")

   elif 'open google' in query:
     webbrowser.open("google.com")

   elif 'play music' in query:
     music_dir="C:\\Users\\gemba\\OneDrive\\Desktop\\songs"
     songs=os.listdir(music_dir)
     print(songs)
     os.startfile(os.path.join(music_dir,songs[0]))

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
   elif "exit"  in query:
     speak('have a nice day boss')
     break
  
   else:
      speak('searching')
      query=query.replace("wikipedia","")
      results=wikipedia.summary(query,sentences=1)
      speak("According to wikipedia")
      speak(results)

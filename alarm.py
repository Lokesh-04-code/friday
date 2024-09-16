from greet import *
import os
extractedtime=open("Alarmtext.txt","r")
time=extractedtime.read()
Time=str(time)
extractedtime.close()
deleteTime=open("Alarmtext.txt","r+")
deleteTime.truncate(0)
deleteTime.close()

def ring(time):
  timeset=str(time)
  timenow=timeset.replace("jarvis","")
  timenow=timeset.replace("set an alarm","")
  timenow=timeset.replace(" and ",":")
  AlarmTime=str(timenow)
  print(AlarmTime)
  while True:
    
    currentTime=datetime.datetime.now().strftime("%H:%M:%S")
    if(currentTime==AlarmTime):
      speak("alarm ringing, sir")
      os.startfile("music.mp3") 
      
    elif currentTime+"00:00:30"==AlarmTime:
      exit()
ring(time)
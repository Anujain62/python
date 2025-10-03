
from random import choices
import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import time


recognizer = sr.Recognizer()
# engine = pyttsx3.init()
engine = pyttsx3.init(driverName='sapi5')
newsapi = "3a79ec96030e4890aedcee302ece0ce3"

def speak(text):
 try:
  print("jarvis says :",text)
  engine.say(text)
  engine.runAndWait()
  time.sleep(0.1)
 except Exception as e:
  print(f"speak error : {e}") 


def processCommand(c):
 if 'open google' in c.lower():
  webbrowser.open("https://google.com")
 elif  'open facebook' in c.lower():
  webbrowser.open("https://facebook.com")
 elif  'open youtube' in c.lower():
  webbrowser.open("https://youtube.com")
 elif  'open linkedin' in c.lower():
  webbrowser.open("https://linkedin.com")  
 elif c.lower().startswith("play"):
  song = c.lower().split(" ")[1]
  link = musicLibrary.music[song] 
  webbrowser.open(link)



  # ????????
 # elif 'news' in c.lower():
 #  r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
 #  if r.status_code == 200:
 #   # parse the json response
 #   data = r.json()

 #   # extract the articles
 #   articles = data.get('articles',[])

 #   # print the headlines
 #   for article in articles[:5]:
 #    print("inside news")
 #    speak(article['title'])        #here why not speak this 





if __name__== "__main__":
 speak("Initializing Jarvis.....")
 while True:
  # listen for the wake word 'Jarvis'
  # obtain audio from the microphone
  r = sr.Recognizer()

  # recognize speech 
  try:
   with sr.Microphone() as source:
    print("Listening....")
    audio = r.listen(source, timeout=2, phrase_time_limit=1)
   word= r.recognize_google(audio)
   if(word.lower()=='jarvis'):
    speak("Yes")
    # listen for command
    with sr.Microphone() as source:
     print("Jarvis active..")
     audio = r.listen(source)
     command= r.recognize_google(audio)
     processCommand(command)


  except Exception as e: 
   print("Error; {0}".format(e))


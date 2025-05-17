import pyttsx3 as p
import speech_recognition as sr
from jokes import *
from wikipedia_automation import *
from youtube_automation import *
from news import *
import randfacts
from weather import *
import datetime as d

engine = p.init()
rates = engine.getProperty('rate')
engine.setProperty('rate',150)
#print(rates)
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voice',voices[1].id)



def speak(text):
    engine.say(text)
    engine.runAndWait()
    
todate= d.datetime.now()

r = sr.Recognizer()

def wishme():
    hour= int( d.datetime.now().hour)
    if hour>0 and hour<12:
        return("morning")
    elif hour>=12 and hour<18:
        return("afternoon")
    else :
        return("evening")
    
speak("hello sir, good" + wishme() + "I'm your assistant. Today is"+ todate.strftime("%d")+"of"+todate.strftime("%b")+"and its currently"+todate.strftime("%I")+"past"+todate.strftime("M")+"minutes" )
speak("Temperature today in hyderabad is"+str(temp())+"degree celcius and with" + str(des()))
speak("how are you doing sir?")
with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source,1.2)
    print("speak something")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)
    
if "what about you" in text:
       speak("I am already having a good day sir")
    
speak("what can I do for you sir?")

with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source,1.2)
    print("bolo")
    audio = r.listen(source)
    text2 = r.recognize_google(audio)
    
    
if "search" or "information"in text2:
    with sr.Microphone() as source:
         r.energy_threshold = 10000
         r.adjust_for_ambient_noise(source,1.2)
         print("bolo")
         audio = r.listen(source)
         infor = r.recognize_google(audio)
         
    speak("searching {} in wikipedia".format(infor))
    assist = Infow4()
    assist.get_info(infor)
    
elif "play" or "video" in text2:
    with sr.Microphone() as source:
         r.energy_threshold = 10000
         r.adjust_for_ambient_noise(source,1.2)
         print("bolo")
         audio = r.listen(source)
         vid = r.recognize_google(audio)
         
    speak("searching{} in youtube".format(vid))
    assist = Infow()
    assist.play(vid)
elif "news" in text2:
    print("sure sir, I will read news for you")
    speak("sure sir, I will read news for you")
    arr=news()
    for i in range(len(arr)):
       
       print(arr[i])
       speak(arr[i])
    

elif "facts" or "fact"in text2:
    facts=randfacts.getfact()
    print(facts)
    speak("did you know that"+facts)

elif"joke" or "jokes" in text2:
   jokes= joke()
   print()
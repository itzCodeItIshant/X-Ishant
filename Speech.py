import pyttsx3
import speech_recognition as sr 
import pyaudio
from internet import Weather
import random





class speech1():

    name = "Mister Sharma"


    def tts(say2):
      speaker = pyttsx3.init()
      speaker.say(say2)
      speaker.runAndWait()
       
    
    def stt():
      r = sr.Recognizer() 

      with sr.Microphone() as source:
        print("Please speak something : " )
        audio = r.listen(source) 

        try:
          text = r.recognize_google(audio)
          if text == 'weather':
            print(Weather.sorters(str(Weather.response.json())))
            cliche = ["There you go" + speech1.name , "This is the weather sir" + speech1.name, "Done!" + speech1.name]
            print(speech1.tts(random.choice(cliche)))
        
          else:
            touche = ["Didn't quite get that " + speech1.name, "Sorry can't hear you "+ speech1.name , "I think you're mic isn't working " + speech1.name]
            print(speech1.tts(random.choice(touche)))
         
        except:
          print("Something went wrong")

           


print(speech1.stt())  

print("Wanna change what I call you ? Try saying change my name ")
import os
import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import time
from google import genai
from google.genai import types

from dotenv import load_dotenv
load_dotenv()

#! Custom Module Imports

from geminiImage import generateImage

#? About the chatbot

name = "Jarvis"
role = "Personal Assistant Chatbot"
owner= "Jay"

#? Loading Apis

news_api_key = os.getenv("NEWS_API")
client = genai.Client(api_key=os.getenv("GEMINI_API"))

recogniser = sr.Recognizer()
ttsx = pyttsx3.init()

def speak(meassage):
    ttsx.say(meassage)
    ttsx.runAndWait()
      
      
      
#! Commands are processed from here
    
def proccessCommand(c):
    if "open google" in c.lower():
        speak("Sure thing!")
        webbrowser.open("https://google.com")
    elif "open instagram" in c.lower():
        speak("Sure thing!")
        webbrowser.open("https://instagram.com")
    elif "open linkedin" in c.lower():
        speak("Sure thing!")
        webbrowser.open("https://linkedin.com")
    elif "open youtube" in c.lower():
        speak("Sure thing!")
        webbrowser.open("https://youtube.com")
    elif "open udemy" in c.lower():
        speak("Sure thing!")
        webbrowser.open("https://udemy.com")
        
    #? Play Music from musicLibrary
    elif "play" in c.lower():
        song = " ".join(c.lower().split(" ")[1:])
        print(song)
        speak(f"Playing {song}")
        webbrowser.open(musicLibrary.music[song])
        
    #? Get some news
    
    elif "news" in c.lower():
        speak("Getting some news for you right now!")
        r = requests.get(f"https://newsapi.org/v2/top-headlines?apiKey={news_api_key}&pageSize=5&page=1&category=general")
        
        if r.status_code == 200:
            response = r.json()
            
            for article in response['articles']:
                speak(article['title'])
                time.sleep(2)
                
    #? Generate Image using Gemini
    
    elif "generate image" in c.lower():
        speak("How you want your image to be?")
        
        try:
            with sr.Microphone() as source:
                audio = recogniser.listen(source)
                command =recogniser.recognize_google(audio)
                generateImage(command)
                speak(f"Generating image of {command}")
        except Exception as e:
            print("Error: {0} ".format(e))
            
          
    #? Use gemini to handle other tasks      
    else: 
        print("Working with gemini")
        response = client.models.generate_content(config=types.GenerateContentConfig(
        system_instruction=f"You are {owner}'s {role}. Your name is {name}. Give short responses"),
        model="gemini-2.0-flash", contents=c
        )
        speak(response.text)
        
    
    
    
#! Main Prrocess starts from Here

if __name__ == "__main__":
    print("Working")
    speak("Initialising Jarvis")
    
    while True:
        #! Listen to the wake word Jarvis! 
        # Obtain audio from the microphone
        
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = recogniser.listen(source, timeout = 5, phrase_time_limit= 5)
                print("Recognizing")
            word = recogniser.recognize_google(audio)
            print(word)
            
            if ("jarvis" in word.lower()):
                print("Jarvis is Activated: ")
                speak("Yes sir")
                
                #? Listen for command Now
                
                try:
                    with sr.Microphone() as source:
                        audio = recogniser.listen(source)
                        command =recogniser.recognize_google(audio)
                        proccessCommand(command)
                except Exception as e:
                    print("Error: {0} ".format(e))
                
            else:
                print("No jarvis")
                
        except Exception as e:
            print(" error; {0} ".format(e))
    
    
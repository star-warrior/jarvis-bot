import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary

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
                    print("Error: {0} ".format(0))
                
            else:
                print("No jarvis")
                
        except Exception as e:
            print(" error; {0} ".format(e))
    
    
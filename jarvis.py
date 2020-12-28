import pyttsx3
import speech_recognition as sr
import datetime
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def greet():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>12 and hour<18:
        speak('Good afternoon!')
    else:
        speak("Good Evening!")
    speak("Welcome to this mini AI world, I am Jarvis , how can i help you?")
def takeCommand():
    # it takes microphone input from user & return string as output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...") 
        r.pause_threshold = 0.8
        audio = r.listen(source)
        try:
            print('Recognising...')
            query = r.recognize_google(audio,Language = 'en-in')
            print(f"User said : {query}\n")
        except Exception as e:
            print(e)
            print("I didn't got you, pardon please!")
            return "None"
        return query
if __name__ == "__main__":
     speak("my name is jarvis")
     greet()
     takeCommand()

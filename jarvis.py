import pyttsx3
import speech_recognition as sr
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

#this function converts the text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#this function convert voice into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning...")
        r.pause_threshold = 1
        audio = r.listen(source , timeout = 1, phrase_time_limit=5)
    
    try:
        print("Recogizing")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"User said:{query}")

    except Exception as e:
        speak("say that again please...")
        return "none"
    return query

#this function is supposed to wish the user
def wish():
    hour = (datetime.datetime.now().hour)

    if hour>= 0 and hour<=12:
        speak("good morning")
    elif hour>12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("i am jarvis sir , please tell me hoe can i help you.")





if __name__ == "__main__":
    wish()
    while True:

        query = takecommand().lower()

        #logic building for tasks

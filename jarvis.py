import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit 
import smtplib
import sys

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
        # audio = r.listen(source ,"timeout = 1, phrase_time_limit = 5")
        audio = r.listen(source ,phrase_time_limit = 5)
    
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

#this function is supposed to send email
def sendEmail(to , content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login('your email' , "password")
    server.sendmail("your email",to, content)
    server.close()


if __name__ == "__main__":
    wish()
    while True:
    # if 1:

        query = takecommand().lower()

        #logic building for tasks

        if "open notepad" in query:
            npath = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(npath)
        
        elif "open command prompt" in query:
            os.system("start cmd") 
        
        elif "play music" in query:
            music_dir = "C:\\Users\\HP\\OneDrive\\Desktop\\all code\\virtual asistiance\\songs"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))

        elif "ip address" in query:

            ip = get("https://api.ipify.org").text
            speak(f"your ip address is {ip}")

        elif "wikipedia" in query:
            speak("searching  wikipedia...")
            query = query.replace("wikipedia", "")
            results =wikipedia.summary(query , sentences = 1) 
            speak("according to wikipedia")
            speak(results)
        
        elif "open youtube" in query:
            webbrowser.open("www.Youtube.com")
     
        elif "open news" in query:
            webbrowser.open("www.indiatoday.in")

        elif "shopping" in query:
            webbrowser.open("www.amazon.in")

        elif "open google" in query:
            speak("sir what should i search on google.")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}") 

        elif "send message" in query:
            speak("sir what should i send.")
            message = takecommand().lower()
            kit.sendwhatmsg("+94046 44880", message, 15, 13)

        elif "play songs on youtube" in query:
            speak("sir which song would you like to play")
            song_name = takecommand().lower()
            kit.playonyt(song_name)
        
        elif "email to shreyas" in query:
            try:
                speak("what should i say")
                content = takecommand().lower()
                to = "keoteshreyas@gmail.com"
                sendEmail(to,content)
                speak("email has been send to avinish")
            
            except Exception as e:
                print(e)

        elif "no thanks" in query:
            speak("thanks for using me sir, have a good day")
            sys.exit()

        speak("sir , do you have any other work")

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[0].id)
print(voices[0].id + voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def hello(name):
    speak(f"Hello {name} Sir...")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("aakashgarg289@gmail.com", "A@k@$#@Gm@1!.")
    server.sendmail('aakashgarg289@gmail.com', to, content)
    server.close()

def wishme():
    hour = int(datetime.datetime.now().hour)
    # print(hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am your jarvis, How can I help you??")

def takeCommand():
    """This function takes microphone input from the user and return string object"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print("You said: ", query)

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

if __name__ == '__main__':
    name = input("Please tell me your name first??")
    hello(name)
    # speak("Aakash is a good boy!!")
    wishme()
    # Logic for executing task for query
    while True:
        query = takeCommand().lower()
        if 'wikipedia in hindi' in query:
            speak('Searching Wikipedia...')
            print("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            # print("Querryyyyy", query)
            wikipedia.set_lang("hi")
            results = wikipedia.summary(query, sentences=2)
            speak("According To Wikipedia...")
            print(results)
            speak(results)
        
        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            print("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            # print("Querryyyyy", query)
            results = wikipedia.summary(query, sentences=2)
            speak("According To Wikipedia...")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open github' in query:
            webbrowser.open("github.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

        elif 'play music' in query:
            musicdir = "C:\\Users\\Aakash Garg\\Documents\\Songs"
            songs = os.listdir(musicdir)
            print(songs)
            # os.startfile(os.path.join(musicdir, songs[0]))
            os.startfile(os.path.join(musicdir, songs[random.randint(0, len(songs) - 1)]))  #random.randint(0, len(songs) - 1 )

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The Time is {strTime}")

        elif 'open code' in query:
            codepath = "C:\\Users\\Aakash Garg\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        
        elif 'email to akash' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "aakashgarg289@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!!!")
            except Exception as e:
                print(e)
                speak("Sorry My friend Aakash, I am not able to sent email at this moment..")

        elif 'you do' in query:
            speak("Everything for you Sir!!")

        elif 'stupid' in query:
            speak("Thank you Sir for calling my pet names..")
        
        elif 'quit' in query:
            speak("I am quitting sir... I hope you will come again to talk to me...")
            quit()
        
        elif 'latest news' in query:
            import requests
            import json

            # def speak(str):
            #     from win32com.client import Dispatch
            #     speak = Dispatch("SAPI.SpVoice")
            #     speak.Speak(str)

            if __name__ == '__main__':
                # speak("Hi, Welcome To Listen All The News For Today")
                url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=a1a20bc8d8d049a49e54568159f96d26"
                r = requests.get(url).text
                print(r)
                news = json.loads(r)
                # for k,v in news.items():
                #     print(k, v)
                arts = news["articles"][0:5]
                for i in arts:
                    print(i['title'])
                    speak(i['title'])
                    speak("Moving To The Next..")
                speak("Thanks For Listening....")
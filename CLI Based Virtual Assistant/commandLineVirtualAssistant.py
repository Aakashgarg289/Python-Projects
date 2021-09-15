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
# print(voices)             ZIRA AND DAVID
engine.setProperty('voice', voices[0].id)
# print(voices[0].id + voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def greet(name):
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
    speak("I am your assistant sir, How can I help you??")
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
    greet(name)
    wishme()
    while True:
        query = takeCommand().lower()
        if 'wikipedia in hindi' in query:
            speak('Searching Wikipedia...')
            print("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
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
        elif 'meaning' in query:
            from PyDictionary import PyDictionary
            pydictionary = PyDictionary()
            speak("Tell me what is your word to search??")
            query = takeCommand().lower()
            print(pydictionary.meaning(query))
            speak(pydictionary.meaning(query))
            speak("I hope you get the right result...")
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
            musicdir = "C:\\Users\\Aakash Garg\\Desktop\\Github\\Songs"
            songs = os.listdir(musicdir)
            # print(songs)
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
                speak("Email has been sent sir!!!")
            except Exception as e:
                print(e)
                speak("Sorry Sir, I am not able to sent email at this moment..")
        elif 'you do' in query:
            speak("Everything for you Sir!!")
        elif 'stupid' in query:
            speak("Thank you Sir for calling my pet name...")
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
                    speak("Hi, I am your news teller. Welcome To Listen All The Latest News Of Today")
                    speak("Please Enter, What type of news you want to listen?? 1. Related to Technology, 2. Related to Sports, 3. Related to Science")
                    inp = input("Enter here: \n").lower()
                    if inp == "technology":
                        url = "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=a1a20bc8d8d049a49e54568159f96d26"
                        r = requests.get(url).text
                        print(r)
                        news = json.loads(r)
                        title = news["articles"][:5]
                        print(len(title))
                        j = 0
                        for i in title:
                            print(i['title'])
                            speak(i['title'])
                            if j<(len(title)-1):
                                speak("Moving to the next")
                                j += 1
                            else:
                                speak("Thanks for listening....")               
                    elif inp == "science":
                        url = "https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=a1a20bc8d8d049a49e54568159f96d26"
                        r = requests.get(url).text
                        print(r)
                        news = json.loads(r)
                        title = news["articles"][:5]
                        j=0
                        for i in title:
                            print(i['title'])
                            speak(i['title'])
                            if j<(len(title)-1):
                                speak("Moving to the next")
                                j += 1
                            else:
                                speak("Thanks for listening....")
                    elif inp == "sports":
                        url = "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=a1a20bc8d8d049a49e54568159f96d26"
                        r = requests.get(url).text
                        print(r)
                        news = json.loads(r)
                        title = news["articles"][:5]
                        j = 0
                        for i in title:
                            print(i['title'])
                            speak(i['title'])
                            if j<(len(title)-1):
                                speak("Moving to the next")
                                j += 1
                            else:
                                speak("Thanks for listening....")

                    elif inp == "quit":
                        quit()
                    else:
                        print("Please provide correct details...")
                        speak("Please provide correct details...")
    
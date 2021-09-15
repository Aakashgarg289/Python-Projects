# REAL TIME NEWS READER - BASED ON YOUR CHOICE
import requests
import json
def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

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
        j = 0
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
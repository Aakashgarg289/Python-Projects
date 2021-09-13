from plyer import notification
import requests
from bs4 import BeautifulSoup
import json

def getData(url):
    r = requests.get(url)
    return r.text

def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "C:\\Users\\Aakash Garg\\Desktop\\Covid Notifications\\icon.ico",
        timeout = 10
    )

if __name__== '__main__':
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=a1a20bc8d8d049a49e54568159f96d26"
    r = requests.get(url).text
    print(r)
    print(type(r))
    news = json.loads(r)
    # for k,v in news.items():
    #     print(k, v)
    arts = news["articles"][0:2]
    for i in arts:
        notifyMe(i['title'][:10], i['content'][:10])
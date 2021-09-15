from plyer.facades import notification
import requests
import json
from plyer import notification
import time

def notify(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "C:\\Users\\Aakash Garg\\Desktop\\Github\\Python Projects\\Covid-19 Cases Notificator\\favicon.ico",
        timeout = 2
    )
    time.sleep(5)

url = "https://data.covid19india.org/data.json"
r = requests.get(url).text
# print(r)
li = json.loads(r)
# print(li)
state = li["statewise"]
print(state)
for i in state[1:]:
    v1 = "State: " + i["state"] + " --- " + i["statecode"]
    v2 = "Confirmed Cases: " + i["confirmed"] + "\n" + "Deaths: " + i["deaths"] + "\n" + "Recovered Cases: " + i["recovered"] + "\n" + "Updated Till: " + i["lastupdatedtime"]
    notify(v1, v2)
    print(v1, v2)
    


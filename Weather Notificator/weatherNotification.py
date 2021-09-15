from plyer import notification
import requests
import json
def getData(url):
    r = requests.get(url)
    return r.text
def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "C:\\Users\\Aakash Garg\\Desktop\\Github\\Python Projects\\Weather Notificator\\icon.ico",
        timeout = 10
    )

def location1():
    url = "https://api.weatherapi.com/v1/current.json?key=363f9e9c204046afbea81022211409&q=Hapur&aqi=yes"
    weather = getData(url)
    print(weather)
    li = json.loads(weather)
    loc = li["location"]
    # print(loc)
    # print(loc["name"])
    val1 = loc["name"] + " - " + loc["region"]
    # print(val1)
    cu = li["current"]
    # print(cu["temp_c"])
    val2 = "Temperature: " + str(cu["temp_c"]) + " C" + "\n" + "Wind Speed: " + str(cu["wind_kph"]) + "\n" + "Humidity: " + str(cu["humidity"])
    notifyMe(val1, val2)
def location2():
    url = "https://api.weatherapi.com/v1/current.json?key=363f9e9c204046afbea81022211409&q=Noida&aqi=yes"
    weather = getData(url)
    print(weather)
    li = json.loads(weather)
    loc = li["location"]
    # print(loc)
    # print(loc["name"])
    val1 = loc["name"] + " - " + loc["region"]
    # print(val1)
    cu = li["current"]
    # print(cu["temp_c"])
    val2 = "Temperature: " + str(cu["temp_c"]) + " C" + "\n" + "Wind Speed: " + str(cu["wind_kph"]) + "\n" + "Humidity: " + str(cu["humidity"])
    notifyMe(val1, val2)

def location3():
    url = "https://api.weatherapi.com/v1/current.json?key=363f9e9c204046afbea81022211409&q=Ghaziabad&aqi=yes"
    weather = getData(url)
    print(weather)
    li = json.loads(weather)
    loc = li["location"]
    # print(loc)
    # print(loc["name"])
    val1 = loc["name"] + " - " + loc["region"]
    # print(val1)
    cu = li["current"]
    # print(cu["temp_c"])
    val2 = "Temperature: " + str(cu["temp_c"]) + " C" + "\n" + "Wind Speed: " + str(cu["wind_kph"]) + "\n" + "Humidity: " + str(cu["humidity"])
    notifyMe(val1, val2)

if __name__== '__main__':
    location1()
    location2()
    location3()
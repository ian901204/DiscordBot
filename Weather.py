import json
import requests
import time

def weatherGet():
    city = [["taipei","台北"],["keelung","基隆"],["Taitung","台東"],["Pingtung","屏東"],["Yilan","宜蘭"],["Tainan","台南"],["Kaohsiung","高雄"]]
    outputString=""
    for i in city:
        response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + i[0] + "&appid=###&lang=zh_tw&units=metric")#put your OpenWeather API key
        data = response.json()
        sunrise = time.localtime(int(data["sys"]["sunrise"]))
        sunset = time.localtime(int(data["sys"]["sunset"]))
        sunrise = str(sunrise.tm_mon) + "/" + str(sunrise.tm_mday) + "\t" + str(sunrise.tm_hour) + ":" + str(sunrise.tm_min)
        sunset = str(sunset.tm_mon) + "/" + str(sunset.tm_mday) + "\t" + str(sunset.tm_hour) + ":" + str(sunset.tm_min)
        outputString += "\n" + i[1] + "\t溫度: " + str(data["main"]["temp_min"]) + "～" + str(data["main"]["temp_max"]) + "C\t天氣狀況: " + str(data["weather"][0]["description"]) + "\t日出時間: " + str(sunrise) + "\t日落時間: " + str(sunset)+"\n\t"
    return outputString
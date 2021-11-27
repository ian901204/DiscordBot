import json
import requests
def newsGet():
    response = requests.get("http://newsapi.org/v2/top-headlines?country=tw&apiKey=###")#put your news API key
    data = response.json()
    return data["articles"]
import json
import requests
import getConfig
def newsGet():
    key = getConfig.getConfig().news_api_key
    response = requests.get(f"https://newsapi.org/v2/top-headlines?country=tw&apiKey={key}")#put your news API key
    data = response.json()
    return data["articles"]
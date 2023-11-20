import requests
from bs4 import BeautifulSoup

data = requests.get("https://graduate.ntut.edu.tw/")
data.encoding = 'utf-8'
soup = BeautifulSoup(data.text, 'html.parser')

data_1 = soup.select("body > div > div > div.col-sm-9 > div > div > div:nth-child(1) > table > tbody > tr")
print(data_1[0].text.strip())
import requests


from bs4 import BeautifulSoup

class CollegeNews:
    def __init__(self):
        self.centerNews = ""
        self.chungzhiNews = ""
        self.taipeiNews = ""
    
    async def getNews(self):
        self.centerNews = self.getCenterNews()
        self.chungzhiNews = self.getChungzhiNews()
        self.taipeiNews = self.getTaipeiNews()
    
    def getCenterNews(self):
        data = requests.get("https://www.csie.ncu.edu.tw/")
        data.encoding = 'utf-8'
        soup = BeautifulSoup(data.text, 'html.parser')

        data_1 = soup.select("body > div.container > div.content > div:nth-child(1) > div > div > div > div.col-xs-12.col-md-9 > div:nth-child(4) > a")
        return data_1[0].text.strip()

    def getChungzhiNews(self):
        data = requests.get("https://exams.ccu.edu.tw/p/404-1032-20287.php?Lang=zh-tw")
        data.encoding = 'utf-8'
        soup = BeautifulSoup(data.text, 'html.parser')

        data_1 = soup.select("#Dyn_2_3 > div > div > section > div:nth-child(2)")
        return (data_1[0].text.strip())
    
    def getTaipeiNews(self):
        data = requests.get("https://graduate.ntut.edu.tw/")
        data.encoding = 'utf-8'
        soup = BeautifulSoup(data.text, 'html.parser')

        data_1 = soup.select("body > div > div > div.col-sm-9 > div > div > div:nth-child(1) > table > tbody > tr")
        return (data_1[0].text.strip())
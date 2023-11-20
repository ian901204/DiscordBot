import discord
from discord.ext import commands, tasks
import asyncio
import time
import News
import os
import getConfig
import Weather
import traceback
from CollegeNews import CollegeNews
config = getConfig.getConfig()
intents = discord.Intents.all() # or .all() if you ticked all, that is easier
intents.members = True # If you ticked the SERVER MEMBERS INTENT
bot=commands.Bot(command_prefix='[', intents = intents)
news_channel = 802023446342664232
weather_channel = 798103577390219304

def timeshow():
    result = time.localtime(time.time())
    return  str(result.tm_mon) + "/" + str(result.tm_mday) + "\t" + str(result.tm_hour) + ":" + str(result.tm_min)

async def sendCollegesNews():
    try:
        taipei_channel = bot.get_channel(1176202306610540577)
        center_channel = bot.get_channel(1176117625135317022)
        chungzhi_channel = bot.get_channel(1176202227002646649)
        async for msg in taipei_channel.history(limit=10000):
            await msg.delete()
        async for msg in center_channel.history(limit=10000):
            await msg.delete()
        async for msg in chungzhi_channel.history(limit=10000): 
            await msg.delete()
        #取得最新公告
        collegeNews = CollegeNews()
        await collegeNews.getNews()
        await taipei_channel.send(collegeNews.taipeiNews)
        await center_channel.send(collegeNews.centerNews)
        await chungzhi_channel.send(collegeNews.chungzhiNews)
        print("send info success!" + time.ctime())
    except:
        traceback.print_exc()
    
async def sendTodayInfo(message_channel = None):
    try:
        discord_weather_channel = bot.get_channel(weather_channel)
        discord_news_channel = bot.get_channel(news_channel)
        async for msg in discord_news_channel.history(limit=10000):
            await msg.delete()
        async for msg in discord_weather_channel.history(limit=10000):
            await msg.delete()
        
        #取得天氣
        outputString = Weather.weatherGet(key=config.weather_api_key)
        await discord_weather_channel.send(outputString)
        await discord_weather_channel.send("\n最後更新時間:"+timeshow()+"\t請輸入[update來得到最新資訊!")
        
        #取得新聞
        outputString = News.newsGet(key=config.news_api_key)
        for i in outputString:
            await discord_news_channel.send(i["url"])
    except:
        traceback.print_exc()

@bot.event
async def on_message(message):
    message_channel = message.channel
    if message.content.startswith('[update'):
        await sendTodayInfo(message_channel)
    if message.content.startswith('[school'):
        await sendCollegesNews()

@tasks.loop(hours=1)
async def called_once_a_day():
    hourTime = time.strftime("%H")
    if (hourTime == "00" or hourTime == "12" or hourTime == "18"):
        await sendCollegesNews()
    
    if (time.strftime("%H") == "19"):
        await sendTodayInfo()
        print("send info success!" + time.ctime())

@called_once_a_day.before_loop
async def before():
    await bot.wait_until_ready()
    print("Finished waiting! right now the time is " + time.ctime())

async def main():
    async with bot:
        called_once_a_day.start()
        await bot.start(config.discord_token)

asyncio.run(main())

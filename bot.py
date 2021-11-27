import discord
from discord.ext import commands, tasks
import asyncio
import time
import News
import Weather
def timeshow():
    result = time.localtime(time.time())
    return  str(result.tm_mon) + "/" + str(result.tm_mday) + "\t" + str(result.tm_hour) + ":" + str(result.tm_min)

bot=commands.Bot(command_prefix='[')
news_channel = 792637087018778674
weather_channel = 798103577390219304
@tasks.loop(hours=1)
async def called_once_a_day():
    if (time.strftime("%H") == "18"):
        discord_weather_channel = bot.get_channel(weather_channel)
        discord_news_channel = bot.get_channel(news_channel)
        async for msg in discord_news_channel.history(limit=10000):
            await msg.delete()
        async for msg in discord_weather_channel.history(limit=10000):
            await msg.delete()
        
        #取得天氣
        outputString = Weather.weatherGet()
        await channelweather.send(discord_weather_channel)
        await discord_weather_channel.send("\n最後更新時間:"+timeshow()+"\t請輸入[update來得到最新資訊!")
        
        #取得新聞
        outputString = News.newsGet()
    
        for i in outputString:
            await discord_news_channel.send(i["url"])
        
@called_once_a_day.before_loop
async def before():
    await bot.wait_until_ready()
    print("Finished waiting")

called_once_a_day.start()
@bot.event
async def on_message(message):
    message_channel = message.channel
    if message.content.startswith('[update'):
        discord_weather_channel = bot.get_channel(weather_channel)
        discord_news_channel = bot.get_channel(news_channel)
        async for msg in discord_news_channel.history(limit=10000):
            await msg.delete()
        async for msg in discord_weather_channel.history(limit=10000):
            await msg.delete()
        
        #取得天氣
        outputString = Weather.weatherGet()
        await discord_weather_channel.send(outputString)
        await discord_weather_channel.send("\n最後更新時間:"+timeshow()+"\t請輸入[update來得到最新資訊!")
        
        #取得新聞
        outputString = News.newsGet()
        for i in outputString:
            await discord_news_channel.send(i["url"])
        
bot.run("your discord bot run key")

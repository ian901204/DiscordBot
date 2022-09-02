import discord
from discord.ext import commands, tasks
import asyncio
import time
import News
import os
import Weather
def timeshow():
    result = time.localtime(time.time())
    return  str(result.tm_mon) + "/" + str(result.tm_mday) + "\t" + str(result.tm_hour) + ":" + str(result.tm_min)
intents = discord.Intents.all() # or .all() if you ticked all, that is easier
intents.members = True # If you ticked the SERVER MEMBERS INTENT
bot=commands.Bot(command_prefix='[', intents = intents)
news_channel = 792637087018778674
weather_channel = 798103577390219304
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

@tasks.loop(hours=1)
async def called_once_a_day():
    if (time.strftime("%H") == "10"):
        discord_weather_channel = bot.get_channel(weather_channel)
        discord_news_channel = bot.get_channel(news_channel)
        async for msg in discord_news_channel.history(limit=10000):
            await msg.delete()
        async for msg in discord_weather_channel.history(limit=10000):
            await msg.delete()
        
        #取得天氣
        output_string = Weather.weatherGet()
        await discord_weather_channel.send(output_string)
        await discord_weather_channel.send("\n最後更新時間:"+timeshow()+"\t請輸入[update來得到最新資訊!")
        
        #取得新聞
        output_string = News.newsGet()
        for i in output_string:
            await discord_news_channel.send(i["url"])
        print("send info success!" + time.ctime())

@called_once_a_day.before_loop
async def before():
    await bot.wait_until_ready()
    print("Finished waiting! right now the time is " + time.ctime())

async def main():
    async with bot:
        called_once_a_day.start()
        await bot.start('your Discord botkey')

asyncio.run(main())

import discord
import time
from datetime import datetime
import json
import requests
from discord.ext import commands, tasks
import asyncio
bot=commands.Bot(command_prefix='[')
target_news_channel_id_list = []#put your news channel_Id
target_weather_channel_id_list = []#put your weather channel_Id
@tasks.loop(hours=1)
async def called_once_a_day():
    if (time.strftime("%H") == "10"):
        weather_channer = bot.get_channel("")#put your main channel_Id
        for target_channel_id in target_news_channel_id_list:
            message_channel = bot.get_channel(target_channel_id)
            async for msg in bot.get_channel(target_channel_id).history(limit=10000):
                await msg.delete()
            channel = bot.get_channel(target_channel_id)
            response = requests.get("http://localhost/discordbot/new_api.php")
            for i in response.json():
                await channel.send(i["url"])
            await channel.send("\nLast update time:" + i["updateTime"] + "\tPlease, Input [update to update the latest!")
            time.sleep(3)
        for target_channel_id in target_weather_channel_id_list:
            message_channel = bot.get_channel(target_channel_id)
            async for msg in bot.get_channel(target_channel_id).history(limit=10000):
                await msg.delete()
            response = requests.get("http://localhost/discordbot/weather_api.php")
            channelweather = bot.get_channel(target_channel_id)
            outputString = ""
            for i in response.json():
                if (i["updateTime"] == ""):
                    outputString += "\n" + i["name"] + "\ttemperature:" + i["mintemp"] + "~" + i["maxtemp"] + "C\tweather:" + i["des"] + "\tsun rise:" + i["sunrise"] + "\tsun set:" + i["sunset"] + "\n\t"
                else:
                    outputString += "\nLast update time:" + i["updateTime"] + "\tPlease, Input [update to update the latest!"
            await channelweather.send(outputString)
@called_once_a_day.before_loop
async def before():
    await bot.wait_until_ready()
    print("Finished waiting")

called_once_a_day.start()
@bot.event
async def on_message(message):
    message_channel = message.channel
    if message.content.startswith('[update'):
        for target_channel_id in target_news_channel_id_list:
            message_channel = bot.get_channel(target_channel_id)
            async for msg in bot.get_channel(target_channel_id).history(limit=10000):
                await msg.delete()
            channel = bot.get_channel(target_channel_id)
            response = requests.get("http://localhost/discordbot/new_api.php")
            for i in response.json():
                await channel.send(i["url"])
            await channel.send("\nLast update time:" + i["updateTime"] + "\tPlease, Input [update to update the latest!")
            time.sleep(3)
        for target_channel_id in target_weather_channel_id_list:
            message_channel = bot.get_channel(target_channel_id)
            async for msg in bot.get_channel(target_channel_id).history(limit=10000):
                await msg.delete()
            response = requests.get("http://localhost/discordbot/weather_api.php")
            channelweather = bot.get_channel(target_channel_id)
            outputString = ""
            for i in response.json():
                if (i["updateTime"] == ""):
                    outputString += "\n" + i["name"] + "\ttemperature:" + i["mintemp"] + "~" + i["maxtemp"] + "C\tweather:" + i["des"] + "\tsun rise:" + i["sunrise"] + "\tsun set:" + i["sunset"] + "\n\t"
                else:
                    outputString += "\nLast update time:" + i["updateTime"] + "\tPlease, Input [update to update the latest!"
            await channelweather.send(outputString)
bot.run("")#your bot key

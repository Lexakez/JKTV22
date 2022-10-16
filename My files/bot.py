import discord
from discord.ext import commands
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


config = {
    'token': 'MTAyOTc2MzU1MjQwMTE2MjMwMA.Gx6d7N.oAvkGOFgsd2QrD0QKbhn_zpvZMumCwjvlx4Tqk',
    'prefix': '!',
}

import discord

bot = commands.Bot(command_prefix=config['prefix'], intents = discord.Intents.all())

@bot.command()
async def расписание(ctx, *arg):   
    await ctx.send("https://tahvel.edu.ee/#/timetable/8/group/6516/592/6")

@bot.command()
async def рас(ctx, *arg):
    driver = webdriver.Chrome(ChromeDriverManager().install())
 
    driver.get('https://tahvel.edu.ee/#/timetable/8/group/6516/592/6')
    
    sleep(1)

    driver.save_screenshot('screenshot.png')
    
    driver.quit()
    await ctx.send(file=discord.File('screenshot.png'))
    
bot.run(config['token'])


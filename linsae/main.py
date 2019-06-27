import discord
from discord.ext import commands
import asyncio
import logging
import os

def read_token():
    with open("token/token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()
token = read_token()
prefix = '?'
bot = commands.Bot(command_prefix=prefix, description='Linsae is a good bot! yeey hack week is here!')
bot.remove_command('help')



async def change_status():
    while True:
        activity = discord.Activity(name='Yeey, Hack Week is here!', type=discord.ActivityType.streaming,
                                    url="https://twitch.tv/linsae")
        activity1 = discord.Activity(name='Made by Ɗrake#7418', type=discord.ActivityType.streaming,
                                    url="https://twitch.tv/linsae")
        activity2 = discord.Activity(name='?help for help' , type=discord.ActivityType.streaming,
                                     url="https://twitch.tv/linsae")
        await bot.change_presence(activity=activity)
        await asyncio.sleep(10)
        await bot.change_presence(activity=activity1)
        await asyncio.sleep(10)
        await bot.change_presence(activity=activity2)
        await asyncio.sleep(10)


@bot.event
async def on_ready():
    print('Bip bip linsae is ready to go')
    print(f'Hosting {len(bot.guilds)} guilds!')
    bot.loop.create_task(change_status())



for cog in os.listdir(".\\cogs"):
    if cog.endswith(".py") and not cog.startswith("_"):
        try:
            cog = f"cogs.{cog.replace('.py', '')}"
            bot.load_extension(cog)
        except Exception as e:
            print(f"{cog} cannot be loaded")
            raise e
bot.run(token, bot=True, reconnect=True)
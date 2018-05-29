import discord
import pyparsing
import claculators as calcer

from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
room=False

Client = discord.Client() #Initialise Client 
client = commands.Bot(command_prefix = "!") #Initialise client bot
nsp= calcer.NumericStringParser()

@client.event 
async def on_ready():
    print("Bot is online and connected to Discord") #This will be called when the bot connects to the server

@client.event
async def on_message(message):
    global room
    if room:
        room=False
        if "bedroom" in  message.content.lower():
            await client.send_message(message.channel, ":heart:")
            await client.send_message(message.channel, "hope U will get the answer soon\n bye bye\n---------------------\nSHUTDOWN")
            await client.close()
        else:
            await client.send_message(message.channel, "Nope ")

    elif message.content == "cookie":
        await client.send_message(message.channel, ":cookie:") #responds with Cookie emoji when someone says "cookie"

    elif message.content == "help":
        await client.send_message(message.channel, "just chat with me\n command:[what is this,calc <1+1 2*6 4/3 balๆ>, cookie]\n other commands are in progress")

    elif message.content == "what is this":
        await client.send_message(message.channel,"Just a game")

    elif message.content.startswith("calc"):
        try:

            await client.send_message(message.channel, nsp.eval(message.content[4:].strip()))
        except pyparsing.ParseException:
            await client.send_message(message.channel,"Wrong Format")

    elif message.content == "9412":
        await client.send_message(message.channel, "What is it?")
        room=True

    elif str(message.author) != "Stupid Bot#8243":
        await client.send_message(message.channel, "No. Don't understand")
client.run("NDUxMDQ4NDI0NjU4MTczOTUy.De8HWw.nLpc5VmYkpTNweRoLpyYcKRn7rE") #Replace token with your bots token

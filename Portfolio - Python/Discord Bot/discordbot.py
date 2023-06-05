#Import Discord.py, allows access to Discord API
#Imports other important imports
import discord
from discord.ext import commands
import requests
import aiohttp
import json

#Load Discord Token from dotenv
import os
from dotenv import load_dotenv
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
GIPHY_API_KEY = os.getenv("GIPHY_API_KEY")


#Gets client object from Discord.py, Client is synonymous with bot
embedColour = 0x00ff00
command_prefix = '$'
bot = commands.Bot(command_prefix='$')

limit = 10

#Tenor GIFS
def get_gif(searchTerm):
    response = requests.get("https://api.giphy.com/v1/gifs/search?api_key=%s&q=%s&limit=%s" % (GIPHY_API_KEY, searchTerm, limit))
    data = response.json()


    if 'data' in data and len(data['data']) > 0:
        return data['data'][0]['images']['original']['url']

    return None

#Event Listener for when the bot has switched from offline to online
@bot.event
async def on_ready():

    #Creates a counter to keep track of number of servers the bot is in 
      guild_count = 0

      #Loops through all the servers the bot is associated with
      for guild in bot.guilds:
        #Print the servers ID and name
        print(f'{guild.id} - (name: {guild.name})')
        #Increments the counter for the number of servers the bot is in
        guild_count = guild_count + 1
        #Prints how many servers the bot is in
        print(f'There are {guild_count} servers that Mashbot is in.')


#Event listener for when a new message is sent to a channel
@bot.event
async def on_message(message):
    #If the message is from the bot, do nothing
    if message.author == bot.user:
        return
    #If the message is sent equal to "Hello"
    if message.content == 'Hello':
        #Sends a message to the channel
        await message.channel.send('Hello!')

    if message.content.lower().startswith(f"{command_prefix}gif"):
        gif_url = get_gif(message.content.lower()[5:])

        if gif_url is not None:
            embed = discord.Embed()
            embed.set_image(url=gif_url)
        
            await message.channel.send(embed=embed)

        else:
            await message.channel.send("Sorry, I couldn't find a gif for that search term.")


#--- Main ---
#Executes bot with specified token
if DISCORD_TOKEN is not None:
    bot.run(DISCORD_TOKEN.strip())
else:
    print('No token provided')

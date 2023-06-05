#Import Discord.py, allows access to Discord API
import discord
from discord import Client, Intents
intents = discord.Intents.default()
client = Client(intents=intents)

#Load Discord Token from dotenv
import os
from dotenv import load_dotenv
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")


#Gets client object from Discord.py, Client is synonymous with bot
bot = discord.Client()

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

#Executes bot with specified token
if DISCORD_TOKEN is not None:
    bot.run(DISCORD_TOKEN.strip())
else:
    print('No token provided')

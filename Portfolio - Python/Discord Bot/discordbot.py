#Import Discord.py, allows access to Discord API
#Imports other important imports
import discord
from discord.ext import commands
import requests
import aiohttp
import json
import random
import secrets

#Load Discord and GIPHY Tokens from dotenv
import os
from dotenv import load_dotenv
load_dotenv()
DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")
GIPHY_API_KEY = os.environ.get("GIPHY_API_KEY")


#Gets client object from Discord.py, Client is synonymous with bot
embedColour = 0x00ff00
command_prefix = '$'
bot = commands.Bot(command_prefix='$')

limit = 10

#GIPHY GIFS
def get_gif(searchTerm):
    response = requests.get(f"https://api.giphy.com/v1/gifs/search?api_key={GIPHY_API_KEY}&q={searchTerm}&limit={limit}")
    data = response.json()


    if 'data' in data and len(data['data']) > 0:
        index = random.randint(0, min(9, len(data['data'])-1))
        return data['data'][index]['images']['original']['url']

    return ('')

#Event Listener for when the bot has switched from offline to online
@bot.event
async def on_ready():

    #Determines the number of servers/guilds the bot is in
    guild_count = len(bot.guilds)

    #Loops through all the servers the bot is associated with
    for guild in bot.guilds:
        #Print the servers ID and name
        print(f'{guild.id} - (name: {guild.name})')
            
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

    #Command to import GIF from GIPHY as an Embed
    if message.content.lower().startswith(f"{command_prefix}gif"):
        gif_url = get_gif(message.content.lower()[5:])

        if gif_url is not None:
            embed = discord.Embed()
            embed.set_image(url=gif_url)
        
            await message.channel.send(embed=embed)

        else:
            await message.channel.send("Sorry, I couldn't find a gif for that search term.")

    #Added a basic Coinflip command that works via $coinflip
    if message.content.lower().startswith(f"{command_prefix}coinflip"):
        result = random.randint(0, 1)
        if result == 0:
            result = 'heads'
        else:
            result = 'tails'
        response = f'{message.author.mention} flipped a coin and got {result}'

        await message.channel.send(response)

    #Added a basic d20 Dice roll command that works with $roll <number of rolls>d<limit>
    if message.content.lower().startswith(f"{command_prefix}roll"):
        try:
            dice = message.content.split()[1]
            rolls, limit = map(int, dice.split('d'))
        except Exception:
            await message.channel.send('Invalid syntax, use $roll <number of rolls>d<limit>')
            return
        results = [secrets.randbelow(limit) + 1 for _ in range(rolls)]
        total = sum(results)

        response = f'{message.author.mention} rolled {dice} and got {results}'
        if rolls > 1:
            response += f'\nTotal: {total}'

        await message.channel.send(response)  


# Event listener for when a member's attributes are updated
@bot.event
async def on_member_update(before, after):
    # Check if the roles list has changed
    if before.roles != after.roles:
        # Get the difference between the before and after roles lists
        added_roles = [role for role in after.roles if role not in before.roles]
        removed_roles = [role for role in before.roles if role not in after.roles]

        # Log the role changes to a separate channel
        if added_roles:
            role_names = [role.name for role in added_roles]
            role_colors = [role.color for role in added_roles]
            for i in range(len(role_names)):
                embed = discord.Embed(title=f"{after.name} was given the {role_names[i]} role", color=discord.Color.blue())
                if role_colors[i] != discord.Color.default():
                    embed.description = f" (color: {role_colors[i]})"
                channel = bot.get_channel(1014448478425993250)
                await channel.send(embed=embed)

        if removed_roles:
            role_names = [role.name for role in removed_roles]
            role_colors = [role.color for role in removed_roles]
            for i in range(len(role_names)):
                embed = discord.Embed(title=f"{after.name} was removed from the {role_names[i]} role", color=discord.Color.blue())
                if role_colors[i] != discord.Color.default():
                    embed.description = f" (color: {role_colors[i]})"
                channel = bot.get_channel(1014448478425993250)
                await channel.send(embed=embed)

    # Check if the role colors have changed
    for role in after.roles:
        if role in before.roles and role.color != before.roles[before.roles.index(role)].color:
            embed = discord.Embed(title=f"The {role.name} role color was updated for {after.name} (new color: {role.color})")
            channel = bot.get_channel(1014448478425993250)
            await channel.send(embed=embed)

# Event listener for when a member's voice state is updated
@bot.event
async def on_voice_state_update(member, before, after):
    if before.channel != after.channel:
        if before.channel:
            embed = discord.Embed(title="Voice Channel Leave", description=f"{member.name} left voice channel {before.channel.name}", color=discord.Color.red())
            channel = bot.get_channel(1014448478425993250)
            await channel.send(embed=embed)

        if after.channel:
            embed = discord.Embed(title="Voice Channel Join", description=f"{member.name} joined voice channel {after.channel.name}", color=discord.Color.green())
            channel = bot.get_channel(1014448478425993250)
            await channel.send(embed=embed)


#--- Main ---
#Executes bot with specified token
if DISCORD_TOKEN is not None:
    bot.run(DISCORD_TOKEN.strip())
else:
    print('No token provided')

# --- Setup ---

# Import Discord.py, allows access to Discord API
# Imports other important imports
import discord
from discord.ext import commands
import requests
import aiohttp
import json
import random
import secrets
import toml

# Load Discord and GIPHY tokens from .env
import os
from dotenv import load_dotenv
load_dotenv()
DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")
GIPHY_API_KEY = os.environ.get("GIPHY_API_KEY")


# Gets client object from discord.py, client is synonymous with bot
embedColour = 0x00ff00
command_prefix = "!"
bot = commands.Bot(command_prefix="!")

limit = 10

# Exports config.toml
config_data = {
    "information": {
    "name": "Mashbot",
    "authors": "Waylon Neal [<93296689+mashumelo@users.noreply.github.com>]",
    "version": "0.0.5",
    "description": "Mashumelo's personal Discord bot",
    "readme": "README.md",
    "website": "https://github.com/mashumelo/mashumelo",
    },              
    "config": {
        "embedColour": 0x00ff00,
        "command_prefix": "!",
        "limit": 10
    },
    "dependencies": {
        "discord.py": "1.7.2",
        "giphy_client": "3.0.0",
        "toml": "0.10.2"
    }
}

with open("config.toml", "w") as f:
    toml.dump(config_data, f)


# --- Main ---

# Pull GIFs from GIPHY GIFs


def get_gif(searchTerm):
    response = requests.get(
        f"https://api.giphy.com/v1/gifs/search?api_key={GIPHY_API_KEY}&q={searchTerm}&limit={limit}")
    data = response.json()

    if "data" in data and len(data["data"]) > 0:
        index = random.randint(0, min(9, len(data["data"])-1))
        return data["data"][index]["images"]["original"]["url"]

    return ("")

# Event listener for when the bot has switched from offline to online


@bot.event
async def on_ready():
    # Determines the number of servers/guilds the bot is in
    guild_count = len(bot.guilds)
    # Loops through all the servers/guilds the bot is associated with
    for guild in bot.guilds:
        # print the servers ID and name
        print(f"{guild.id} - (name: {guild.name})")
    # Print how many servers/guilds the bot is in
    print(f"There are {guild_count} servers that Mashbot is in.")

# Event listener for when a new message is sent to a channel


@bot.event
async def on_message(message):
    # If the message is from the bot, do nothing
    if message.author == bot.user:
        return
    # If the message is sent equal to "Hello"
    if message.content == ("Hello"):
        # Sends a message to the channel
        await message.channel.send(f"Hello, {mention.member} welcome to {guild.name}!")
    # Command to import GIF from GIPHY as an embed via $gif <searchTerm>
    if message.content.lower().startswith(f"{command_prefix}gif"):
        gif_url = get_gif(message.content.lower()[5:])
        if gif_url is not None:
            embed = discord.Embed()
            embed.set_image(url=gif_url)
            await message.channel.send(embed=embed)
        else:
            await message.channel.send("Sorry, I couldn't find a gif for that search term.")

    # Added a basic coinflip command that works via $coinflip
    if message.content.lower().startswith(f"{command_prefix}coinflip"):
        result = random.randint(0, 1)
        if result == 0:
            result = "heads"
        else:
            result = "tails"
        response = f"{message.author.mention} flipped a coin and got {result}!"
        embed = discord.Embed(
            title="Coin Flip", description=response, color=embedColour)
        await message.channel.send(embed=embed)

    # Added a basic d20 dice roll command that works with $roll <number of rolls>d<limit>
    if message.content.lower().startswith(f"{command_prefix}roll"):
        try:
            dice = message.content.split()[1]
            rolls, limit = map(int, dice.split("d"))
        # If the syntax is invalid, send an error message
        except Exception:
            embed = discord.Embed(
                title="Invalid syntax", description="Use !roll <number of rolls>d<limit>.", color=embedColour)
            await message.channel.send(embed=embed)
            return
        # Roll the dice
        results = [secrets.randbelow(limit) + 1 for _ in range(rolls)]
        total = sum(results)
        response = f"{message.author.mention} rolled {dice} and got {results}"
        if rolls > 1:
            response += f"\nTotal: {total}"
        embed = discord.Embed(
            title="Dice Roll", description=response, color=embedColour)
        await message.channel.send(embed=embed)

# Event listener for when a member joins the server/guild


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1014448478933483580)
    embed = discord.Embed(title=f"{member.mention} has joined the server!",
                          description=f"Welcome to the server, {member.mention}!", color=discord.color.green())
    await channel.send(embed=embed)
    # Adds a role to the member on join
    role = discord.utils.get(member.guild.roles, id="1014448477050253341")
    await member.add_roles(role)

# Event listener for when a member leaves the server/guild


@bot.event
async def on_member_leave(member):
    channel = bot.get_channel(1014448478933483580)
    embed = discord.Embed(title=f"{member.mention} has left the server!",
                          description=f"Goodbye, {member.mention}!", color=discord.color.red())
    await channel.send(embed=embed)

# Event listener for when a member is banned from the server/guild


@bot.event
async def on_member_ban(member):
    log_channel = bot.get_channel(1014448478933483580)
    embed = discord.Embed(
        title=f"{member.name} has been banned from {member.guild.name}!", color=discord.Color.red())
    await log_channel.send(embed=embed)

# Event listener for when a member is kicked from the server/guild


@bot.event
async def on_member_kick(member):
    log_channel = bot.get_channel(1014448478933483580)
    embed = discord.Embed(
        title=f"{member.name} has been kicked from {member.guild.name}!", color=discord.Color.red())
    await log_channel.send(embed=embed)

# Event listener for when a member's attributes are updated


@bot.event
async def on_member_update(before, after):
    # Check if the roles list has changed
    if before.roles != after.roles:

        # Get the difference between the before and after roles lists
        added_roles = [
            role for role in after.roles if role not in before.roles]
        removed_roles = [
            role for role in before.roles if role not in after.roles]

        # Log the role change for added roles
        if added_roles:
            role_names = [role.name for role in added_roles]
            role_colors = [role.color for role in added_roles]
            for i in range(len(role_names)):
                embed = discord.Embed(
                    title=f"{after.name} was given the {role_names[i]} role", color=role_colors[i])
                if role_colors[i] != discord.Color.default().value:
                    embed.description = f" (color: {role_colors[i]})"
                channel = bot.get_channel(1014448478425993250)
                await channel.send(embed=embed)

        # Log the role change for removed roles
        if removed_roles:
            role_names = [role.name for role in removed_roles]
            role_colors = [role.color for role in removed_roles]
            for i in range(len(role_names)):
                embed = discord.Embed(
                    title=f"{after.name} was removed from the {role_names[i]} role", color=role_colors[i])
                if role_colors[i] != discord.Color.default().value:
                    embed.description = f" (color: {role_colors[i]})"
                channel = bot.get_channel(1014448478425993250)
                await channel.send(embed=embed)

    # Check if the role colors have changed
    for role in after.roles:
        if role in before.roles and role.color != before.roles[before.roles.index(role)].color:
            embed = discord.Embed(
                title=f"The {role.name} role color was updated for {after.name} (new color: {role.color})")
            channel = bot.get_channel(1014448478425993250)
            await channel.send(embed=embed)

# Event listener for when a member's voice state is updated


@bot.event
async def on_voice_state_update(member, before, after):
    if before.channel != after.channel:

        # Log the leave
        if before.channel:
            embed = discord.Embed(
                title="Voice Channel Leave", description=f"{member.name} left voice channel {before.channel.name}", color=discord.Color.red())
            channel = bot.get_channel(1014448478425993250)
            await channel.send(embed=embed)

        # Log the join
        if after.channel:
            embed = discord.Embed(
                title="Voice Channel Join", description=f"{member.name} joined voice channel {after.channel.name}", color=discord.Color.green())
            channel = bot.get_channel(1014448478425993250)
            await channel.send(embed=embed)


# Executes bot with specified token
if DISCORD_TOKEN is not None:
    bot.run(DISCORD_TOKEN.strip())
# If no token is provided
else:
    print("No token provided")


config_data = {
    "information": {
    "name": "Mashbot",
    "authors": "Waylon Neal [<93296689+mashumelo@users.noreply.github.com>]",
    "version": "0.0.5",
    "description": "Mashumelo's personal Discord bot",
    "readme": "README.md",
    "website": "https://github.com/mashumelo/mashumelo",
    },              
    "config": {
        "embedColour": 0x00ff00,
        "command_prefix": "!",
        "limit": 10
    },
    "dependencies": {
        "discord.py": "1.7.2",
        "giphy_client": "3.0.0",
        "toml": "0.10.2"
    }
}

with open("config.toml", "w") as f:
    toml.dump(config_data, f)

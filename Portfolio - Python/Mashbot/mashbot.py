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

# Load Discord and GIPHY tokens from .env
import os
import toml
from dotenv import load_dotenv
load_dotenv()
DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")
GIPHY_API_KEY = os.environ.get("GIPHY_API_KEY")


# Gets client object from discord.py, client is synonymous with bot
embedColour = 0x00FF00
command_prefix = "!"
bot = commands.Bot(command_prefix="!")

limit = 10

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
    await bot.process_commands(message)


@bot.command(description="Usage: !gif <searchTerm> - Searches GIPHY and displays a random gif from a search term")
async def gif(ctx, *, search: str):
    # Command to import GIF from GIPHY as an embed via $gif <searchTerm>
    embed = discord.Embed()
    gif_url = await get_gif(search)
    if gif_url is not None:
        embed.set_image(url=gif_url)
        await ctx.send(embed=embed)
    else:
        await ctx.send("Sorry, I couldn't find a gif for that search term.")


@bot.command(description="Usage: !coinflip - Flips a coin")
async def coinflip(ctx):
    # Added a basic coinflip command that works via $coinflip
        result = random.choice(["heads", "tails"])
        response = f"{ctx.author.mention} flipped a coin and got {result}!"
        embed = discord.Embed(
            title="Coin Flip", description=response, color=embedColour)
        await ctx.send(embed=embed)


@bot.command(description="Usage: !roll <number of rolls>d<limit> - Rolls the dice")
async def roll(ctx, dice: str):
    # Added a basic d20 dice roll command that works with $roll <number of rolls>d<limit>
        try:
            rolls, limit = map(int, dice.split("d"))
        # If the syntax is invalid, send an error message
        except ValueError:
            embed = discord.Embed(
                title="Invalid syntax", description="Use !roll <number of rolls>d<limit>.", color=embedColour)
            await ctx.send(embed=embed)
            return
        # Roll the dice
        results = ", ".join(str(random.randint(1, limit))
                            for _ in range(rolls))
        if rolls > 1:
            total = sum(map(int, results.split(",")))
            results += f"\nTotal: {total}"
        response = f"{ctx.author.mention} rolled {dice} and got {results}"
        embed = discord.Embed(
            title="Dice Roll", description=response, color=embedColour)
        await ctx.send(embed=embed)
@bot.remove_command("help")
@bot.command(description="Displays a list of available commands")
async def help(ctx):
    """Displays a list of available commands"""
    embed = discord.Embed(title="Mashbot Command List", color=embedColour)
    command_list = [
        f"{command.name} - {command.description}" for command in bot.commands]
    help_message = "\n".join(command_list)
    embed.add_field(name="Commands", value=help_message, inline=False)
    await ctx.send(embed=embed)

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

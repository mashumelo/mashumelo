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
import asyncio

# Load Discord and GIPHY tokens from .env
import os
import toml
from dotenv import load_dotenv
load_dotenv()
DISCORD_TOKEN = os.environ.get('DISCORD_TOKEN')
GIPHY_API_KEY = os.environ.get('GIPHY_API_KEY')

# Gets client object from discord.py, client is synonymous with bot
embedColour = 0x00FF00
intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

limit = 10

# --- Main ---

# Pull GIFs from GIPHY GIFs


def get_gif(search):
    response = requests.get(
        f'https://api.giphy.com/v1/gifs/search?api_key={GIPHY_API_KEY}&q={search}&limit={limit}')
    data = response.json()

    if 'data' in data and len(data['data']) > 0:
        index = secrets.randbelow(min(9, len(data['data'])-1))
        return data['data'][index]['images']['original']['url']

    return ('')

# Prevents any users from seeing commands dictated for Admin/Moderator in !help command list


def has_any_role(*role_ids):
    def predicate(ctx):
        return any(role.id in ctx.author.roles for role in ctx.author.roles)
    return commands.check(predicate)

# Event listener for when the bot has switched from offline to online


@bot.event
async def on_ready():
    # Determines the number of servers/guilds the bot is in
    guild_count = len(bot.guilds)
    # Loops through all the servers/guilds the bot is associated with
    for guild in bot.guilds:
        # print the servers ID and name
        print(f'{guild.id} - (name: {guild.name})')
    # Print how many servers/guilds the bot is in
    print(f'There are {guild_count} servers that Mashbot is in.')

# Event listener for when a new message is sent to a channel


@bot.event
async def on_message(message):
    # If the message is from the bot, do nothing
    if message.author == bot.user:
        return
    # If the message is sent equal to 'Hello'
    if message.content == ('Hello'):
        # Sends a message to the channel
        await message.channel.send(f'Hello, {mention.member} welcome to {guild.name}!')
    await bot.process_commands(message)

for command in bot.commands:
    bot.remove_command('help')
    bot.remove_command('kick')
    bot.remove_command('ban')
    bot.remove_command('mute')

# --- Commands ---


@bot.command(description='Usage: !kick <member> [reason] - Kicks a member with an optional reason', category='Moderation')
@commands.has_permissions(kick_members=True)
@commands.has_any_role(1014448477083795559, 1014448477083795560, 1014448477083795561, 1115164855670935602)
async def kick(ctx, member: discord.Member, *, reason=None):
    # Command to kick a member
    if reason is None:
        reason = "No reason given"

    embed = discord.Embed(title='Member Kicked', color=0xff0000)
    embed.add_field(name='Member', value=f'{member.mention}', inline=False)
    embed.add_field(name='Reason', value=reason, inline=False)
    embed.set_author(name=ctx.author.display_name,
                     icon_url=ctx.author.avatar_url)

    await member.kick(reason=reason)
    await ctx.send(embed=embed)


@bot.command(description='Usage: !ban <member> [reason] - Bans a member with an optional reason', category='Moderation')
@commands.has_permissions(ban_members=True)
@commands.has_any_role(1014448477083795559, 1014448477083795560, 1014448477083795561, 1115164855670935602)
async def ban(ctx, member: discord.Member, *, reason=None):
    # Command to ban a member
    if reason is None:
        reason = "No reason given"

    embed = discord.Embed(title='Member Banned', color=0xff0000)
    embed.add_field(name='Member', value=f'{member.mention}', inline=False)
    embed.add_field(name='Reason', value=reason, inline=False)
    embed.set_author(name=ctx.author.display_name,
                     icon_url=ctx.author.avatar_url)

    await member.ban(reason=reason)
    await ctx.send(embed=embed)


@bot.command(description='Usage: !mute <member> [reason] - Mutes a member with an optional reason', category='Moderation')
@commands.has_permissions(manage_messages=True)
@commands.has_any_role(1014448477083795559, 1014448477083795560, 1014448477083795561, 1115164855670935602)
async def mute(ctx, member: discord.Member, *, reason=None, duration: int):
    # Command to mute a member
    if reason is None:
        reason = "No reason given"

    muted_role = discord.utils.get(ctx.guild.roles, id=1014448477083795558)
    await member.add_roles(muted_role)

    embed = discord.Embed(title='Member Muted', color=0xff0000)
    embed.add_field(name='Member', value=f'{member.mention}', inline=False)
    embed.add_field(name='Duration', value=f'{duration} seconds', inline=False)
    embed.add_field(name='Reason', value=reason, inline=False)
    embed.set_author(name=ctx.author.display_name,
                     icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed)

    await asyncio.sleep(300)

    await member.remove_roles(muted_role)

    embed = discord.Embed(title='Member Unmuted', color=0x00ff00)
    embed.add_field(name='Member', value=f'{member.mention}', inline=False)
    embed.add_field(name='Reason', value=reason, inline=False)
    embed.set_author(name=ctx.author.display_name,
                     icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed)


@bot.command(description='Usage: !gif <searchTerm> - Searches GIPHY and displays a random gif from a search term', category='Fun')
async def gif(ctx, *, search: str):
    # Command to import GIF from GIPHY as an embed via $gif <searchTerm>
    embed = discord.Embed()
    gif_url = get_gif(search)
    if gif_url:
        embed.set_image(url=gif_url)
        await ctx.send(embed=embed)
    else:
        await ctx.send("Sorry, I couldn't find a gif for that search term.")


@bot.command(description='Usage: !coinflip - Flips a coin', category='Fun')
async def coinflip(ctx):
    # Added a basic coinflip command that works via $coinflip
        result = random.choice(['heads', 'tails'])
        response = f'{ctx.author.mention} flipped a coin and got {result}!'
        embed = discord.Embed(
            title='Coin Flip', description=response, color=embedColour)
        await ctx.send(embed=embed)


@bot.command(description='Usage: !roll <number of rolls>d<limit> - Rolls the dice', category='Fun')
async def roll(ctx, dice: str):
    # Added a basic d20 dice roll command that works with $roll <number of rolls>d<limit>
        try:
            rolls, limit = map(int, dice.split('d'))
        # If the syntax is invalid, send an error message
        except ValueError:
            embed = discord.Embed(
                title='Invalid syntax', description='Use !roll <number of rolls>d<limit>.', color=embedColour)
            await ctx.send(embed=embed)
            return
        # Roll the dice
        results = ', '.join(str(random.randint(1, limit))
                            for _ in range(rolls))
        if rolls > 1:
            total = sum(map(int, results.split(',')))
            results += f'\nTotal: {total}'
        response = f'{ctx.author.mention} rolled {dice} and got {results}'
        embed = discord.Embed(
            title='Dice Roll', description=response, color=embedColour)
        await ctx.send(embed=embed)


@bot.command(description='Usage: !dog - Gives a random dog picture', category='Fun')
async def dog(ctx):
    # Command to get a random dog picture
    request = requests.get('https://dog.ceo/api/breeds/image/random')
    data = request.json()
    embed = discord.Embed(
        title='Random Dog', description='', color=embedColour)
    embed.set_image(url=data['message'])
    await ctx.send(embed=embed)


@bot.command(description='Usage: !help - Display a list of available commands')
async def help(ctx):
    # Displays a list of available commands
    embed = discord.Embed(title='Mashbot Command List', color=embedColour)
    mod_commands = [command for command in bot.commands if command.name in [
        'kick', 'ban', 'mute', 'help']]
    fun_commands = [command for command in bot.commands if command.name in [
        'gif', 'coinflip', 'roll', 'dog']]
    mod_list = [
        f'{chr(8226)} {command.name} - {command.description}' for command in mod_commands]
    fun_list = [
        f'{chr(8226)} {command.name} - {command.description}' for command in fun_commands]
    mod_message = '\n'.join(mod_list) if mod_list else 'No commands available.'
    fun_message = '\n'.join(fun_list) if fun_list else 'No commands available.'

    embed.add_field(name='Moderation', value=mod_message, inline=False)
    embed.add_field(name='Fun', value=fun_message, inline=False)

    await ctx.send(embed=embed)

# Event listener for when a member joins the server/guild


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1014448478933483580)
    embed = discord.Embed(title=f'{member.mention} has joined the server!',
                          description=f'Welcome to the server, {member.mention}!', color=discord.color.green())
    await channel.send(embed=embed)
    # Adds a role to the member on join
    role = discord.utils.get(member.guild.roles, id='1014448477050253341')
    await member.add_roles(role)

# Event listener for when a member leaves the server/guild


@bot.event
async def on_member_leave(member):
    channel = bot.get_channel(1014448478933483580)
    embed = discord.Embed(title=f'{member.mention} has left the server!',
                          description=f'Goodbye, {member.mention}!', color=discord.color.red())
    await channel.send(embed=embed)

# Event listener for when a member is banned from the server/guild


@bot.event
async def on_member_ban(member):
    log_channel = bot.get_channel(1014448478933483580)
    embed = discord.Embed(
        title=f'{member.name} has been banned from {member.guild.name}!', color=discord.Color.red())
    await log_channel.send(embed=embed)

# Event listener for when a member is kicked from the server/guild


@bot.event
async def on_member_kick(member):
    log_channel = bot.get_channel(1014448478933483580)
    embed = discord.Embed(
        title=f'{member.name} has been kicked from {member.guild.name}!', color=discord.Color.red())
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
                    title=f'{after.name} was given the {role_names[i]} role', color=role_colors[i])
                if role_colors[i] != discord.Color.default().value:
                    embed.description = f' (color: {role_colors[i]})'
                channel = bot.get_channel(1014448478425993250)
                await channel.send(embed=embed)

        # Log the role change for removed roles
        if removed_roles:
            role_names = [role.name for role in removed_roles]
            role_colors = [role.color for role in removed_roles]
            for i in range(len(role_names)):
                embed = discord.Embed(
                    title=f'{after.name} was removed from the {role_names[i]} role', color=role_colors[i])
                if role_colors[i] != discord.Color.default().value:
                    embed.description = f' (color: {role_colors[i]})'
                channel = bot.get_channel(1014448478425993250)
                await channel.send(embed=embed)

    # Check if the role colors have changed
    for role in after.roles:
        if role in before.roles and role.color != before.roles[before.roles.index(role)].color:
            embed = discord.Embed(
                title=f'The {role.name} role color was updated for {after.name} (new color: {role.color})')
            channel = bot.get_channel(1014448478425993250)
            await channel.send(embed=embed)

# Event listener for when a member's voice state is updated


@bot.event
async def on_voice_state_update(member, before, after):
    if before.channel != after.channel:

        # Log the leave
        if before.channel:
            embed = discord.Embed(
                title='Voice Channel Leave', description=f'{member.name} left voice channel {before.channel.name}', color=discord.Color.red())
            channel = bot.get_channel(1014448478425993250)
            await channel.send(embed=embed)

        # Log the join
        if after.channel:
            embed = discord.Embed(
                title='Voice Channel Join', description=f'{member.name} joined voice channel {after.channel.name}', color=discord.Color.green())
            channel = bot.get_channel(1014448478425993250)
            await channel.send(embed=embed)


# Executes bot with specified token
if DISCORD_TOKEN is not None:
    print("Starting bot...")
    bot.run(DISCORD_TOKEN.strip())
# If no token is provided
else:
    print('No token provided')

# Work with Python 3.6
# {0.author.mention} = mention author
import discord
import random
import time
import math
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
PREFIX = os.getenv('DISCORD_PREFIX')
OWNER = os.getenv('OWNER')
COMPILE_TIME = time.ctime()
random.seed(COMPILE_TIME)

bot = commands.Bot(command_prefix=PREFIX)

bot.load_extension('bot_owner')
bot.load_extension('bot_info')
bot.load_extension('bot_util')
bot.load_extension('bot_time')

@bot.event
async def on_ready():
    print("Logged in as " + str(bot.user.name) + " (ID: " + str(bot.user.id) + ")")
    #bot.activity = discord.Game(name='g')

@bot.command(name='hello', help='Are you sure you want to do this???')
async def greetings(ctx):
    msg = '***loud screeching noise***'
    await ctx.send(msg)
    print('Saying hi...')

@bot.command(name='reload', help='OWNER ONLY: Reloads commands',hidden = 1)
@commands.is_owner()
async def reload(ctx, extension):
    await ctx.send('Reloading ' + str(extension) + '...')
    print('Reloading ' + str(extension) + '...')
    await bot.reload_extension(extension)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You fool, your permissions are wrong. Now perish.')
        print('User tried to access a command with invalid permissions')

bot.run(TOKEN)
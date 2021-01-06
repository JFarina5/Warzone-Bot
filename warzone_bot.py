'''
Project: warzone_bot.py
'''
import os
import discord
import random
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='!')

# Test to ensure warzone bot has successfully connected to Discord
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

# Drop location method which will randomly display a location, based from the provided text file
@bot.command(name='wherewedropping', help='When in doubt, have Warzone Bot help you out; randomly chooses a drop point for you and/or your squad in Verdansk.')
async def drop_location(ctx):
    lines = open('verdansk_locations.txt').read().splitlines() # Opens txt document and reads eachline
    myline = random.choice(lines) # Randomizes the results in the 'lines' variable

    drop_response = [
        (myline + ' looks like a good place to drop.'), 
        (myline + '? Looks more like dubcity to me.'),
        ('I\'d reccomend dropping at ' + myline)
    ]

    response = random.choice(drop_response) # Used to randomize the response provided by the bot, based on the 'drop_response' variable

    await ctx.send(response)


# @bot.command(name='gulagchances', help='You never know what your chances of getting out of Gulag are, allow Warzone bot to help with that.')

# @bot.command(name='')

# @bot.command(name='')

# @bot.command(name='')


bot.run(TOKEN)

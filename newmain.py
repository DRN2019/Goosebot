from time import time
import discord
from discord.ext import commands
from discord.utils import get
import random
import time
import os
import pickle

"""
Programmed by Darren Wu
Created: December 2020
Last Updated: August 23 2022

Project: Discord Goosebot
"""

"""
Unique server toggle variables
    serverToggle[index][0] = serverID
    serverToggle[index][1] = Message actions toggled on
    serverToggle[index][2] = Message actions toggled off
    serverToggle[index][3] = Voice actions toggled on
    serverToggle[index][4] = Voice actiona toggled off
"""

"""
Improvements I want:

Add reactions to toggle commands
SQL server to store saved permissions
Add the top.gg advertisement

-- Optional -- 
Requires message intent
If ping goose or mentioned goose, then goose will honk over you every time you talk in vc and do something specific to the user
    It is possible to take their next message and replace it with honks sporadically



"""


# Constants
maxRand = 15        # How many messages for an action to occur
serverId = []       # List containing an id corresponding to each server
serverToggle = []   # Multi dimentional list containing each server's permissions

# Intents
intents = discord.Intents.default()

# Command Symbol
client = commands.Bot(command_prefix = '|', intents=intents)

# on_ready event -- Executed once bot is online
@client.event
async def on_ready():
    nServers = len(client.guilds)
    print(f"I'm in {nServers} servers!")

    with open('servers.data', 'rb') as f:
        serverId = pickle.load(f)
        print("Server IDs loaded")
    with open('toggle.data', 'rb') as filehandle:
        serverToggle = pickle.load(filehandle)
        print("Server toggled actions loaded!")
    
    print("Honks Incoming")

# Custom Help command
client.remove_command('help')
@client.command()
async def help(message):
    embed = discord.Embed(
        colour = discord.Colour.orange()
    )

    embed.set_author(name = 'Help')

    embed.add_field(name = '|help', value = 'Shows this message', inline = False)
    embed.add_field(name = '|toggle', value = 'Can toggle actions on and off', inline = False)
    embed.add_field(name = '|show', value = 'Shows actions that are toggled on and off', inline = False)


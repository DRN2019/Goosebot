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
    embed.add_field(name = '|toggle', value = 'Can toggle actions on and off. Can toggle using word commands or reactions', inline = False)
    embed.add_field(name = '|show', value = 'Shows actions that are toggled on and off', inline = False)
    embed.add_field(name='How the bot works', value = 'The bot has a random chance per message of performing a random action  ', inline=False)
    await message.channel.send(embed=embed)


# Shows what is toggled on and off
@client.command()
async def show(message):
    # Add server to server list if not present
    server = message.guild.id 
    if not(server in serverID):
        serverID.append(server)
        index = serverID.index(server)
        serverToggle.append([])
        serverToggle[index].append(server)
        for i in range(4):
            serverToggle[index].append([])
        serverToggle[index][1].append('MessageHonk')
        serverToggle[index][1].append('Memes')
        serverToggle[index][1].append('Reaction')
        serverToggle[index][1].append('Delete')
        serverToggle[index][1].append('MessageGoose')
        serverToggle[index][1].append('NoPeace')
        serverToggle[index][3].append('Disconnect')
        serverToggle[index][3].append('VoiceHonk')
    index = serverID.index(server)

    channel = message.channel
    string = "Message On:"

    for i in serverToggle[index][1]:
        string = string + " " + i
    await channel.send(string)
    string = "Message Off:"

    for i in serverToggle[index][2]:
        string = string + " " + i
    await channel.send(string)
    string = "Voice On:"

    for i in serverToggle[index][3]:
        string = string + " " + i
    await channel.send(string)
    string = "Voice Off:"

    for i in serverToggle[index][4]:
        string = string + " " + i
    await channel.send(string)


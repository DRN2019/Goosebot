import discord
from discord.ext import commands
from discord.utils import get
import random
import time
import os
import pickle
import asyncio
"""
Programmed by: Darren Wu 2020
Project: Discord GooseBot

"""

# Command symbol
client = commands.Bot(command_prefix = '|')
client.remove_command('help')
# How often the Goosebot activates
maxRand = 15

"""
Unique server toggle variables
    serverToggle[index][0] = serverID
    serverToggle[index][1] = Message actions toggled on
    serverToggle[index][2] = Message actions toggled off
    serverToggle[index][3] = Voice actions toggled on
    serverToggle[index][4] = Voice actiona toggled off
"""
serverID = []
serverToggle = []
with open('servers.data', 'rb') as filehandle:
        serverID = pickle.load(filehandle)
        print("Server IDs loaded!")
with open('toggle.data', 'rb') as filehandle:
    serverToggle = pickle.load(filehandle)
    print("Server toggled actions loaded!")


# Lets host know if bot is functional
@client.event
async def on_ready():
    print("I'm in " + str(len(client.guilds)) + " servers!")
    with open('servers.data', 'rb') as filehandle:
        serverID = pickle.load(filehandle)
        print("Server IDs loaded!")
    with open('toggle.data', 'rb') as filehandle:
        serverToggle = pickle.load(filehandle)
        print("Server toggled actions loaded!")
    print("Honks Incoming")


# Custom Help command
@client.command()
async def help(message):
    author = message.author
    embed = discord.Embed(
        colour = discord.Colour.orange()
    )
    embed.set_author(name= 'Help')
    embed.add_field(name='|help', value = 'Shows this message', inline=False)
    embed.add_field(name='|toggle', value = 'Can toggle certain actions on and off\nTakes \'MessageHonk\', \'Reaction\', \'Memes\', \'Delete\', \'Disconnect\', \'VoiceHonk\'', inline=False)
    embed.add_field(name='|show', value = 'Shows actions that are toggled on and off', inline=False)
    embed.add_field(name='How the bot works', value = 'The bot has a random chance per message of performing a random action  ', inline=False)
    await message.channel.send(embed=embed)

# Allows user to toggle certain actions on and off
@client.command()
async def toggle(channel):
    # Add server to server list if not present
    server = channel.guild.id 
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

    message = channel.message
    change = False
    if 'messagehonk' in message.content.lower():
        change = True
        if 'MessageHonk' in serverToggle[index][1]:
            serverToggle[index][1].remove('MessageHonk')
            serverToggle[index][2].append('MessageHonk')
            await message.channel.send('Message Honking is now Disabled')
        else:
            serverToggle[index][2].remove('MessageHonk')
            serverToggle[index][1].append('MessageHonk')
            await message.channel.send('Message Honking is now Enabled')
    if 'reaction' in message.content.lower():
        change = True
        if 'Reaction' in serverToggle[index][1]:
            serverToggle[index][1].remove('Reaction')
            serverToggle[index][2].append('Reaction')
            await message.channel.send('Message Reactions is now Disabled')
        else:
            serverToggle[index][2].remove('Reaction')
            serverToggle[index][1].append('Reaction')
            await message.channel.send('Message Reactions is now Enabled')
    if 'memes' in message.content.lower():
        change = True
        if 'Memes' in serverToggle[index][1]:
            serverToggle[index][1].remove('Memes')
            serverToggle[index][2].append('Memes')
            await message.channel.send('Memes is now Disabled')
        else:
            serverToggle[index][2].remove('Memes')
            serverToggle[index][1].append('Memes')
            await message.channel.send('Memes is now Enabled')
    if 'delete' in message.content.lower():
        change = True
        if 'Delete' in serverToggle[index][1]:
            serverToggle[index][1].remove('Delete')
            serverToggle[index][2].append('Delete')
            await message.channel.send('Message Deleting is now Disabled')
        else:
            serverToggle[index][2].remove('Delete')
            serverToggle[index][1].append('Delete')
            await message.channel.send('Message Deleting is now Enabled')
    if 'messagegoose' in message.content.lower():
        change = True
        if 'MessageGoose' in serverToggle[index][1]:
            serverToggle[index][1].remove('MessageGoose')
            serverToggle[index][2].append('MessageGoose')
            await message.channel.send('Message Goose is now Disabled')
        else:
            serverToggle[index][2].remove('MessageGoose')
            serverToggle[index][1].append('MessageGoose')
            await message.channel.send('Message Goose is now Enabled')
    if 'nopeace' in message.content.lower():
        change = True
        if 'NoPeace' in serverToggle[index][1]:
            serverToggle[index][1].remove('NoPeace')
            serverToggle[index][2].append('NoPeace')
            await message.channel.send('Peace is now an option')
        else:
            serverToggle[index][2].remove('NoPeace')
            serverToggle[index][1].append('NoPeace')
            await message.channel.send('Peace is now not an option')
    if 'disconnect' in message.content.lower():
        change = True
        if 'Disconnect' in serverToggle[index][3]:
            serverToggle[index][3].remove('Disconnect')
            serverToggle[index][4].append('Disconnect')
            await message.channel.send('Voice Disconnection is now Disabled')
        else:
            serverToggle[index][4].remove('Disconnect')
            serverToggle[index][3].append('Disconnect')
            await message.channel.send('Voice Disconnection is now Enabled')
    if 'voicehonk' in message.content.lower():
        change = True
        if 'VoiceHonk' in serverToggle[index][3]:
            serverToggle[index][3].remove('VoiceHonk')
            serverToggle[index][4].append('VoiceHonk')
            await message.channel.send('Voice Honking is now Disabled')
        else:
            serverToggle[index][4].remove('VoiceHonk')
            serverToggle[index][3].append('VoiceHonk')
            await message.channel.send('Voice Honking is now Enabled')
    if change == False:
        await message.channel.send("Setting not found, try \'MessageHonk\', \'Reaction\', \'Memes\', \'Delete\', \'MessageGoose\', \'NoPeace\' \'Disconnect\', \'VoiceHonk\'")

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


# On Message random actions
@client.event
async def on_message(message):
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
    await client.process_commands(message)
    if (len(serverToggle[index][1]) != 0 or len(serverToggle[index][3]) != 0) and message.author != client.user and (not message.content.startswith('|')):
        if type(message.author.voice) !=  type(None):
            actions = len(serverToggle[index][1]) + len(serverToggle[index][3])
            voicechannel = message.author.voice.channel
        else:
            actions = len(serverToggle[index][1])
        activation = random.randint(1, maxRand * actions)
        if activation <= actions:
            # Send "HONK!"
            inVoice = False
            if activation > len(serverToggle[index][1]):
                activation = activation - len(serverToggle[index][1])
                inVoice = True
            if inVoice:
                if serverToggle[index][3][activation-1] == 'Disconnect':
                    await message.author.move_to(None)
                
                if serverToggle[index][3][activation-1] == 'VoiceHonk':
                    voice = get(client.voice_clients, guild = message.guild)
                    if voice and voice.is_connected():
                        await voice.move_to(voicechannel)
                    else:
                        voice = await voicechannel.connect()

                    voice.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source = "GooseHonk.mp3"), after = lambda e: print("Honks away")  )
                    voice.source = discord.PCMVolumeTransformer(voice.source)
                    voice.source.volume = 1
                    await message.channel.send("Honks Away")
                    time.sleep(8)
                    await voice.disconnect()
            else:
                if serverToggle[index][1][activation-1] == "MessageHonk":
                    await channel.send('Honk!')
                if serverToggle[index][1][activation-1] == "Memes":
                    imageNum = random.randint(1,8)
                    if(imageNum == 1):
                        await channel.send(file=discord.File('Goose Images\Meme1.png'))
                    if(imageNum == 2):
                        await channel.send(file=discord.File('Goose Images\Meme2.png'))
                    if(imageNum == 3):
                        await channel.send(file=discord.File('Goose Images\Meme3.png'))
                    if(imageNum == 4):
                        await channel.send(file=discord.File('Goose Images\Meme4.png'))
                    if(imageNum == 5):
                        await channel.send(file=discord.File('Goose Images\Meme5.png'))
                    if(imageNum == 6):
                        await channel.send(file=discord.File('Goose Images\Meme6.png'))
                    if(imageNum == 7):
                        await channel.send(file=discord.File('Goose Images\Meme7.png'))
                    if(imageNum == 8):
                        await channel.send(file=discord.File('Goose Images\GooseDance.gif'))
                if serverToggle[index][1][activation-1] == "Delete":
                    await message.delete()
                    await message.channel.send(message.author.mention + " Your message got honked")
                if serverToggle[index][1][activation-1] == "Reaction":
                    react = random.randint(0,1)
                    if react == 0:
                        await message.add_reaction('\N{REGIONAL INDICATOR SYMBOL LETTER G}')
                        await message.add_reaction('\N{REGIONAL INDICATOR SYMBOL LETTER O}')
                        await message.add_reaction('\N{Negative Squared Latin Capital Letter O}')
                        await message.add_reaction('\N{REGIONAL INDICATOR SYMBOL LETTER S}')
                        await message.add_reaction('\N{REGIONAL INDICATOR SYMBOL LETTER E}')

                    if react == 1:
                        await message.add_reaction('\N{REGIONAL INDICATOR SYMBOL LETTER H}')
                        await message.add_reaction('\N{REGIONAL INDICATOR SYMBOL LETTER O}')
                        await message.add_reaction('\N{REGIONAL INDICATOR SYMBOL LETTER N}')
                        await message.add_reaction('\N{REGIONAL INDICATOR SYMBOL LETTER K}') 
                if serverToggle[index][1][activation-1] == "MessageGoose":
                    await channel.send('>o)\n  (_>')
                if serverToggle[index][1][activation-1] == "NoPeace":
                    await channel.send('Peace was never an option...\n  -the goose(me)')



client.run('NzYzODUzNTU0NjM2OTQ3NDU2.X39wDw.uTK3vGTfWsIbdGuGUGPhEkFgxjQ')


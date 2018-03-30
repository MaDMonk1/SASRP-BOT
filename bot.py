import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord.voice_client import VoiceClient

startup_extension = ["Music"]
Client = discord.Client()
client = commands.Bot(command_prefix = "?")

@client.event
async def on_ready():
    print("Bot Is Ready!")

class Main_Commands():
        def __init__(self, client):
         self.client = client
@client.event
async def on_message(message):
    if message.content.upper().startswith('?PING'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Pong!" % (userID))
    if message.content.upper().startswith('?FLIPCOIN'):
        userID = message.author.id
        randnum = random.randint(1,3)
        if randnum == 1:
          emb = (discord.Embed(description=None, colour=0x3DF270))
          emb.add_field(name="Coinflip", value="It landed on Heads!", inline=False)
          await client.send_message(message.channel, embed=emb)
        elif randnum == 2:
          emb = (discord.Embed(description=None, colour=0x3DF270))
          emb.add_field(name="Coinflip", value="It landed on Tails!", inline=False)
          await client.send_message(message.channel, embed=emb)
    if message.content.upper().startswith('?NP'):
        userID = message.author.id
        await client.send_message(message.channel, " @everyone Could we get some Cops, CIVS and SAFD online please!")
    if message.content.upper().startswith('?INFO'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> The Official Bot For SASRP Made By MaDMonk!" % (userID))

if __name__ == "__main__":
    for extension in startup_extension:
        try:
            client.load_extension(extension)
        except Exception as e:
            exc = "(): ()".format(type(E).__name__< e)
            print('Failed to load extension ()\n()'.format(extensiom, exc))

client.run(process.env.NDI5MzA2MTg5NDM2NjgyMjUw.DZ_w9Q.Ncwh0RuitRgEA9RIRnxewTP5GCU):


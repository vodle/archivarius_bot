import discord
from discord.ext import commands
import time
import asyncio
import requests
import urllib.request
import random
import sys

token = 'NjAzNzE1NDY4MTA4NDk2OTEy.XhDuJA.kS1z41nLgWUEJkvNFhri9Y9j32Y'


client = discord.Client()

@client.event
async def on_connect():
    print('connected')
    print('-----')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    author = message.author
    msgc = message.content
    msgg = message.channel

    if (str(msgg) == "science-fiction") and (msgc == "<!!dump!!>"):
        counter = 0
        _msg = await message.channel.fetch_message('663353270940598272')

        guild = "science-fiction"
        async for elem in message.channel.history(limit=1500, oldest_first=True, after=_msg):
            destination = 'F:\\code\\python\\bot\\pic\\' + 'pic' + str(random.randint(1, sys.maxsize)) + '.png'
            if (len(elem.attachments) > 0):

                for i in range(len(elem.attachments)):
                    _attachments = elem.attachments[i]
                    image = _attachments.url
                    print(image)



                    with open(destination, 'wb') as handle:
                        print(destination)
                        response = requests.get(image, stream=True)
                        if not response.ok:
                            print(response)
                        for block in response.iter_content(1024):
                            if not block:
                                    break
                            handle.write(block)
                    handle.close()
                counter += 1

client.run(token)
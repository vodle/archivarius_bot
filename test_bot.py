import discord
from discord.ext import commands
import time
import asyncio
import requests
import urllib.request

token = 'NjAzNzE1NDY4MTA4NDk2OTEy.Xg_mdg.0Y-7NOZEtnZxTkdJK4yXRXoZV5M'

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

    if (str(msgg) == "science-fiction") and (msgc == "hbdsaLDVJBV") :


        counter = 0
        async for elem in message.channel.history(oldest_first=True):
            destination = 'G:\\code\\python\\pic\\' + 'pic' + str(counter) + '.png'

            if (len(elem.attachments) > 0):

                _attachments = elem.attachments[0]
                image = _attachments.url
                print(image)
                for i in range(len(elem.attachments)):
                    with open(destination, 'wb') as handle:
                        response = requests.get(image, stream=True)
                        if not response.ok:
                            print(response)
                        for block in response.iter_content(1024):
                            if not block:
                                break
                            handle.write(block)

                    counter += 1
            if elem.author.bot:
                await elem.delete()

client.run(token)

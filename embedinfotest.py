import os
import asyncio
import time
import discord
from discord.ext import commands


#my_secret = os.environ['TOKEN']
client = discord.Client()

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    embeds = message.embeds # return list of embeds
    for embed in embeds:
        print(embed.to_dict())

client.run('OTM5OTk0MzAzOTY1NTkzNjAw.YgA76g.84EzRFftvFbWItN1yyN6OK3b5qo')
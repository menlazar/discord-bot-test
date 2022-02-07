import discord
import os

client = discord.Client()
huntTime = int(60)
eventValue = float(0.25)
donatorRole = float(0.35)
donorHunt = huntTime * donatorRole
eventHunt = huntTime - donorHunt * eventValue
totalTime = huntTime - donorHunt - eventHunt

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$test'):
        await message.channel.send('Hello!')
    if message.content.startswith('$time'):
        await message.channel.send('tiempo restante en hunt es: ' + str(totalTime) )

client.run(os.getenv('TOKEN'))
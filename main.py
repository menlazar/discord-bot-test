from distutils import command
import os
import asyncio
import discord
from discord.ext import commands

botcom = commands.bot(command_prefix = '.')

my_secret = os.environ['TOKEN']
client = discord.Client()
hunt = int(60)
eventValue = float(0.25)
donatorRole = float(0.35)

donatorTime = hunt * donatorRole
donatorhunt = hunt - donatorTime
eventTime = donatorhunt * eventValue
totalTime = donatorhunt - eventTime

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@botcom.command()
async def embed(ctx):
    embed = discord.Embed(title="Sample Embed", url="https://realdrewdata.medium.com/", description="This is an embed that will show how to build an embed and the different components", color=0xFF5733)

@client.event
async def on_message(message):
    
    if message.author == client.user:
        return

    embeds = message.embeds
    for embed in embeds:        
        for field in embed.fields: 
            if "STEALTH" in field.value:
                value_stealth = int(field.value.splitlines()[1].split("**STEALTH**: ")[1])
                value_energy = int(field.value.splitlines()[0].split("**ENERGY**: ")[1])
                if value_stealth >= 90:
                    if value_energy >= 1000:
                        await message.channel.send("I recommend to do a Guild **UPGRADE**")
                    elif value_energy < 1000:
                        await message.channel.send("I recommend to do a Guild **RAID**")
                elif value_stealth < 90:
                    await message.channel.send("Hi looking at the Stealth level i recommend **UPGRADE** ")
                else:
                    return


            await ctx.send(embed=embed)

    #if "rpg hunt t" in message.content:
    #    await asyncio.sleep(totalTime)
    #    await message.channel.send("Hunt T Ready")

client.run(my_secret)
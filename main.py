import os
import asyncio
import discord
from discord.ext import commands

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
                        embed=discord.Embed(title="Demon Slayrs Helper Bot",
                                            description="The recommendation looking at the stats is to do a Guild **UPGRADE**",
                                            color=0xFF5733)
                        await message.channel.send(embed=embed)
                    elif value_energy < 1000:
                        embed=discord.Embed(title="Demon Slayrs Helper Bot",
                                            description="The recommendation looking at the stats is to do a Guild **RAID**",
                                            color=0xFF5733)
                        await message.channel.send(embed=embed)
                elif value_stealth < 90:
                        embed=discord.Embed(title="Demon Slayrs Helper Bot",
                                            description="The recommendation looking at the stats is to do a Guild **UPGRADE**",
                                            color=0xFF5733)
                        await message.channel.send(embed=embed)
                else:
                    return



                #Guild action reminder

        for embed in embeds:
            for field in embed.fields:
                if "Your guild has already" in field.value:
                    await message.channel.send("already raided")
                else:
                    return


    #if "rpg hunt t" in message.content:
    #    await asyncio.sleep(totalTime)
    #    await message.channel.send("Hunt T Ready")

client.run(my_secret)
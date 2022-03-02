import os
import time
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
                value_rank = str(field.value.splitlines()[2].split("**RANK**: ")[1])
                if value_rank == "best 1%":
                    embed=discord.Embed(title="Demon Slayrs Helper Bot",
                                        description="The recommendation looking at the stats is to do a Guild **UPGRADE**",
                                        color=0xFF5733)
                    await message.channel.send(embed=embed)
                    return
                else:
                    embed=discord.Embed(title="Demon Slayrs Helper Bot",
                                        description="The recommendation looking at the stats is to do a Guild **RAID**",
                                        color=0xFF5733)
                    await message.channel.send(embed=embed)
                    return
                # if value_stealth == 90:
                #     if value_energy == 1000:
                #         embed=discord.Embed(title="Demon Slayrs Helper Bot",
                #                             description="The recommendation looking at the stats is to do a Guild **UPGRADE**",
                #                             color=0xFF5733)
                #         await message.channel.send(embed=embed)
                #     elif value_energy < 1000:
                #         embed=discord.Embed(title="Demon Slayrs Helper Bot",
                #                             description="The recommendation looking at the stats is to do a Guild **RAID**",
                #                             color=0xFF5733)
                #         await message.channel.send(embed=embed)
                #         return
                # elif value_stealth <= 90:
                #         embed=discord.Embed(title="Demon Slayrs Helper Bot",
                #                             description="The recommendation looking at the stats is to do a Guild **UPGRADE**",
                #                             color=0xFF5733)
                #         await message.channel.send(embed=embed)
                #         return
                # elif value_stealth == 100:
                #         embed=discord.Embed(title="Demon Slayrs Helper Bot",
                #                             description="The recommendation looking at the stats is to do a Guild **RAID**",
                #                             color=0xFF5733)
                #         await message.channel.send(embed=embed)
                #         return



                #Guild action reminder

        # for embed in embeds:
        #     for field in embed.fields:
        #         if "Your guild has already" in field.value:
        #             await message.channel.send("already raided")
        #         else:
        #             return



#-------------------------------------------------- RANDOM EVENTS -----------------------------------------------------------

    embeds = message.embeds
    for embed in embeds:
        if "**FISH**" in embed.fields[0].value:
            time.sleep(1)
            await message.channel.send("FISH @everyone")
        else:
            print("no event embed")
            return

    embeds = message.embeds
    for embed in embeds:
        if "**CHOP**" in embed.fields[0].value:
            time.sleep(1)
            await message.channel.send("CHOP @everyone")
        else:
            print("no event embed")
            return

    embeds = message.embeds
    for embed in embeds:
        if "**SUMMON*" in embed.fields[0].value:
            time.sleep(1)
            await message.channel.send("SUMMON @everyone")
        else:
            print("no event embed")
            return


    embeds = message.embeds
    for embed in embeds:
        if "**CATCH**" in embed.fields[0].value:
            time.sleep(1)
            await message.channel.send("CATCH @everyone")
        else:
            print("no event embed")
            return

    embeds = message.embeds
    for embed in embeds:
        if "**TIME TO FIGHT**" in embed.fields[0].value:
            time.sleep(1)
            await message.channel.send("TIME TO FIGHT @everyone")
        else:
            print("no event embed")
            return
#------------------------------------------------ END RANDOM EVENTS ---------------------------------------------------

    #if "rpg hunt t" in message.content:
    #    await asyncio.sleep(totalTime)
    #    await message.channel.send("Hunt T Ready")


# ---------------------------------------------- GET EMBED --------------------------------------------------------------


client.run(my_secret)
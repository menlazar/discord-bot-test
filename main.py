import os
import asyncio
import discord

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
    dcuser = message.author.name


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
                        await message.channel.send("I recommend to do a Guild Upgrade")
                    elif value_energy < 1000:
                        await message.channel.send("I recommend to do a Guild Raid")
                elif value_stealth < 90:
                    await message.channel.send("Hi looking at the Stealth level i recommend Upgrade " + dcuser)
                else:
                    # it will never get here/ true XD, lets test it out.  BEAUTIFUL XD yes if you need anything else only that for the moment! many thanks for helping me ;)
                    return
        # With F10 - StepOver - it will jump line 
        # f11 - StepIn - It will enter on the function if there is any on the line
        # StepOut - no its the oposite of stepin

        # lets see




    if "rpg hunt t" in message.content:
        await asyncio.sleep(totalTime)
        await message.channel.send("Hunt T Ready")




client.run(my_secret)
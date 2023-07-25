#Jamin's discord bot (monketech)

import discord
from discord.ext import commands
from discord import app_commands
import os
from keep_alive import keep_alive
import functions
import requests
import datetime, time
import functools

intents = discord.Intents.all()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

API_KEY = str(os.environ['uwutech'])


@client.event
async def on_ready():

    #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening ,name="^help"))
    await client.change_presence(activity=discord.Streaming(
        name="monke land", url="https://www.twitch.tv/monketech"))

    await tree.sync()

    print("nikhil sucks")


@tree.command(name="invite_bot",
              description="provides an invite link for the bot")
async def invite(interaction: discord.Interaction):

    await interaction.response.send_message(
        "https://discord.com/api/oauth2/authorize?client_id=903057763108814888&permissions=534723951680&scope=bot"
    )


#?"""
#@client.event
#async def on_message(message):
#  if str(message.author.name + "#" + message.author.discriminator) == "Doctor Blink#9922":
#    await message.channel.send("SHUT UP BLINKY POOOOPOOOO")

#  if str(message.author.name + "#" + message.author.discriminator) == "SteeeeeeeeevN#7902":
#   await message.channel.send("SHUT UP MOMMY STEVEN")

#"""


@tree.command(name="help")
async def help(interaction: discord.Interaction):
    helpEmbed = discord.Embed(title="**:weary: Commands :weary:**",
                              colour=0xFF7CEF)

    helpEmbed.add_field(
        name="GEXP GRABBER",
        value="`/getweekly <guild name>\n/getdaily <guild name>`",
        inline=True)
    helpEmbed.add_field(name="INVITE LINK", value="`/invite_bot`", inline=True)
    helpEmbed.set_thumbnail(
        url=
        'https://cdn.discordapp.com/attachments/898736814658035712/902975179456643092/uwutech.PNG'
    )

    numServers = len(client.guilds)
    helpEmbed.set_footer(text="I am in " + str(numServers) +
                         " servers. Made by monketech")

    await interaction.response.send_message(embed=helpEmbed)


@tree.command(name="getweekly")
async def getweekly(interaction: discord.Interaction, hypixelguild: str):
    whichday = ""
    sorter = []
    leaderboard = []

   # guildName = "+".join(hypixelguild)
    guildName = hypixelguild
    print(guildName)
    today = datetime.date.today()
    day1 = today - datetime.timedelta(days=7)
    day2 = today - datetime.timedelta(days=6)
    day3 = today - datetime.timedelta(days=5)
    day4 = today - datetime.timedelta(days=4)
    day5 = today - datetime.timedelta(days=3)
    day6 = today - datetime.timedelta(days=2)
    day7 = today - datetime.timedelta(days=1)
    day8 = today - datetime.timedelta(days=0)

    guildInfo = functions.get_guildInfo(guildName)
    try:
        memberList = guildInfo["guild"]["members"]
        guildName = guildInfo["guild"]["name"]
        estTime = functions.get_number_of_elements(memberList)
        guildSize = len(memberList)
        print(guildSize)
        await interaction.response.send_message("estimated time: " +str(int(estTime / 3)) + " seconds")

    except:
        await interaction.response.send_message("**" + guildName + "**" +
                                                " IS NOT A GUILD MONKE")

    counter = 0
    for member in memberList:
        lbFinal = []
        exp = 0
        memberUuid = member["uuid"]
        print(memberUuid)

        person = f"https://sessionserver.mojang.com/session/minecraft/profile/{memberUuid}"
        # if (guildSize > 60):
        #     time.sleep(0.5)

        res = requests.get(person)
        try:
            guildMembers = res.json()
        except:
            await interaction.response.send_message("**API is Down**")
            guildMembers = res.json()
        counter += 1
        try:
            personName = str(guildMembers["name"])
            print(counter)
            print(personName)

        except:
            print(personName)

        try:
            exp += member["expHistory"][str(day8)]
            whichday = "(" + str(day2) + " to " + str(day8) + ")"
        except:
            exp += member["expHistory"][str(day1)]
            whichday = "(" + str(day1) + " to " + str(day7) + ")"

        exp += member["expHistory"][str(day2)]
        exp += member["expHistory"][str(day3)]
        exp += member["expHistory"][str(day4)]
        exp += member["expHistory"][str(day5)]
        exp += member["expHistory"][str(day6)]
        exp += member["expHistory"][str(day7)]

        sorter.append(personName)
        sorter.append(exp)
        leaderboard.append(exp)

        leaderboard.sort(reverse=True)

    for x in leaderboard:
        lbFinal.append(str(sorter[sorter.index(x) - 1]) + " - " + str(x))
        sorter.remove(x)

    finalMsg, finalMsg2, finalMsg3, finalMsg4, finalMsg5, finalMsg6, finalMsg7 = "`", "`", "`", "`", "`", "`", "`"
    counter = 0
    counter2 = 1

    for x in lbFinal:
        if lbFinal.index(x) < 20:
            try:
                finalMsg += str(counter2) + " - " + str(lbFinal[counter] +
                                                        "\n")
                counter += 1
                counter2 += 1
            except:
                break
        elif lbFinal.index(x) < 40:
            try:
                finalMsg2 += str(counter2) + " - " + str(lbFinal[counter] +
                                                         "\n")
                counter += 1
                counter2 += 1
            except:
                break
        elif lbFinal.index(x) < 60:
            try:
                finalMsg3 += str(counter2) + " - " + str(lbFinal[counter] +
                                                         "\n")
                counter += 1
                counter2 += 1
            except:
                break
        elif lbFinal.index(x) < 80:
            try:
                finalMsg4 += str(counter2) + " - " + str(lbFinal[counter] +
                                                         "\n")
                counter += 1
                counter2 += 1
            except:
                break
        elif lbFinal.index(x) < 100:
            try:
                finalMsg5 += str(counter2) + " - " + str(lbFinal[counter] +
                                                         "\n")
                counter += 1
                counter2 += 1
            except:
                break
        elif lbFinal.index(x) < 120:
            try:
                finalMsg6 += str(counter2) + " - " + str(lbFinal[counter] +
                                                         "\n")
                counter += 1
                counter2 += 1
            except:
                break
        else:
            try:
                finalMsg7 += str(counter2) + " - " + str(lbFinal[counter] +
                                                         "\n")
                counter += 1
                counter2 += 1
            except:
                break

    finalMsg += "`"
    finalMsg2 += "`"
    finalMsg3 += "`"
    finalMsg4 += "`"
    finalMsg5 += "`"
    finalMsg6 += "`"
    finalMsg7 += "`"
    #checks if discord needs to send multiple message
    finalText = discord.Embed(title=whichday, colour=0xFF7CEF)

    finalText.set_author(name="Weekly GEXP Leaderboard - " + guildName)
    finalText.add_field(name="Top 20", value=finalMsg, inline=False)

    if finalMsg2 != "``":
        finalText.add_field(name="Top 40", value=finalMsg2, inline=False)

    if finalMsg3 != "``":
        finalText.add_field(name="Top 60", value=finalMsg3, inline=False)

    if finalMsg4 != "``":
        finalText.add_field(name="Top 80", value=finalMsg4, inline=False)

    if finalMsg5 != "``":
        finalText.add_field(name="Top 100", value=finalMsg5, inline=False)

    if finalMsg6 != "``":
        finalText.add_field(name="Top 120", value=finalMsg6, inline=False)

    if finalMsg7 != "``":
        finalText.add_field(name="Top 125", value=finalMsg7, inline=False)

    numServers = len(client.guilds)
    finalText.set_footer(text="I am in " + str(numServers) +
                         " servers. Made by monketech")

    await interaction.edit_original_response(embed=finalText)


@tree.command(name="getname")
async def getName(interaction: discord.Interaction, uuid: str):
    name = requests.get(
        f'https://api.mojang.com/user/profiles/{uuid}/names').json()
    name = name["name"]
    await interaction.response.send_message(name)


#@functools.lru_cache()
@tree.command(name="getdaily")
async def getdaily(interaction: discord.Interaction, hypixelguild: str):
    sorter = []
    leaderboard = []

    #guildName = "+".join(hypixelguild)
    guildName = hypixelguild
    print(guildName)
    today = datetime.date.today()
    day7 = today - datetime.timedelta(days=1)
    day8 = today - datetime.timedelta(days=0)

    guildInfo = functions.get_guildInfo(guildName)
    try:
        memberList = guildInfo["guild"]["members"]
        guildName = guildInfo["guild"]["name"]
        estTime = functions.get_number_of_elements(memberList)
        await interaction.response.send_message("estimated time: " + str(estTime / 6) + " seconds")
    except:
        await interaction.response.send_message("**" + guildName + "**" +
                                                " IS NOT A GUILD MONKE")

    counter = 0
    for member in memberList:
        lbFinal = []
        exp = 0
        memberUuid = member["uuid"]

        person = f"https://api.hypixel.net/player?key={API_KEY}&uuid={memberUuid}"
        #if (guildSize > 60):
        #    time.sleep(0.5)

        counter += 1

        res = requests.get(person)
        #print(person)
        try:
            guildMembers = res.json()
            #print(guildMembers)
        except:
            await interaction.response.send_message("**API is Down**")
            guildMembers = res.json()

        try:
            personName = str(guildMembers["player"]["playername"])
            print(personName)
        except:
            print(personName)

        try:
            exp += member["expHistory"][str(day7)]
            whichday = "(" + str(day7) + ")"
        except:
            exp += member["expHistory"][str(day8)]
            whichday = "(" + str(day8) + ")"

        sorter.append(personName)
        sorter.append(exp)
        leaderboard.append(exp)

        leaderboard.sort(reverse=True)

    for x in leaderboard:
        lbFinal.append(str(sorter[sorter.index(x) - 1]) + " - " + str(x))
        sorter.remove(x)

    finalMsg, finalMsg2, finalMsg3, finalMsg4, finalMsg5, finalMsg6, finalMsg7 = "`", "`", "`", "`", "`", "`", "`"
    counter = 0
    counter2 = 1

    for x in lbFinal:
        if lbFinal.index(x) < 20:
            try:
                finalMsg += str(counter2) + " - " + str(lbFinal[counter] +
                                                        "\n")
                counter += 1
                counter2 += 1
            except:
                break
        elif lbFinal.index(x) < 40:
            try:
                finalMsg2 += str(counter2) + " - " + str(lbFinal[counter] +
                                                         "\n")
                counter += 1
                counter2 += 1
            except:
                break
        elif lbFinal.index(x) < 60:
            try:
                finalMsg3 += str(counter2) + " - " + str(lbFinal[counter] +
                                                         "\n")
                counter += 1
                counter2 += 1
            except:
                break
        elif lbFinal.index(x) < 80:
            try:
                finalMsg4 += str(counter2) + " - " + str(lbFinal[counter] +
                                                         "\n")
                counter += 1
                counter2 += 1
            except:
                break
        elif lbFinal.index(x) < 100:
            try:
                finalMsg5 += str(counter2) + " - " + str(lbFinal[counter] +
                                                         "\n")
                counter += 1
                counter2 += 1
            except:
                break
        elif lbFinal.index(x) < 120:
            try:
                finalMsg6 += str(counter2) + " - " + str(lbFinal[counter] +
                                                         "\n")
                counter += 1
                counter2 += 1
            except:
                break
        else:
            try:
                finalMsg7 += str(counter2) + " - " + str(lbFinal[counter] +
                                                         "\n")
                counter += 1
                counter2 += 1
            except:
                break

    finalMsg += "`"
    finalMsg2 += "`"
    finalMsg3 += "`"
    finalMsg4 += "`"
    finalMsg5 += "`"
    finalMsg6 += "`"
    finalMsg7 += "`"
    #makes embed
    finalText = discord.Embed(title=whichday, colour=0xFF7CEF)

    finalText.set_author(name="Daily GEXP Leaderboard" + " - " + guildName)
    finalText.add_field(name="Top 20", value=finalMsg, inline=False)

    if finalMsg2 != "``":
        finalText.add_field(name="Top 40", value=finalMsg2, inline=False)

    if finalMsg3 != "``":
        finalText.add_field(name="Top 60", value=finalMsg3, inline=False)

    if finalMsg4 != "``":
        finalText.add_field(name="Top 80", value=finalMsg4, inline=False)

    if finalMsg5 != "``":
        finalText.add_field(name="Top 100", value=finalMsg5, inline=False)

    if finalMsg6 != "``":
        finalText.add_field(name="Top 120", value=finalMsg6, inline=False)

    if finalMsg7 != "``":
        finalText.add_field(name="Top 125", value=finalMsg7, inline=False)

    numServers = len(client.guilds)
    finalText.set_footer(text="I am in " + str(numServers) +
                         " servers. Made by monketech")

    await interaction.edit_original_response(embed=finalText)


keep_alive()
my_secret = os.environ['TOKEN']
client.run(my_secret)

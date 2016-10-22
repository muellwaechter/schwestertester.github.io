# -*- coding: utf-8 -*-
import discord
from discord.ext import commands
import random
import requests


id = 'channelfuerdenoutput'
discord_token = 'tokenfuerdenbotlogin'

msg4 = "**ENDE ENDE ENDE ENDE ENDE ENDE ENDE ENDE ENDE ENDE ENDE ENDE ENDE ENDE ENDE ENDE ENDE ENDE ENDE ENDE ENDE ENDE ENDE ENDE ENDE ENDE ENDE ENDE ENDE ENDE ENDE ENDE**"
payload = {
}
headers = {
}


def get_users(start):
    url = "https://api.younow.com/php/api/younow/trendingUsers/locale=ww/numberOfRecords=20/startFrom=%s" % start
    response = requests.get(url, data=payload, headers=headers)
    response.raise_for_status()
    data = response.json()['trending_users']
    return data

def get_string(start):
    url = "https://api.younow.com/php/api/younow/trendingUsers/locale=ww/numberOfRecords=20/startFrom=%s" % start
    response = requests.get(url, data=payload, headers=headers)
    response.raise_for_status()
    data = response.json()
    return data

def streams_total():
    url = "https://api.younow.com/php/api/younow/trendingUsers/locale=ww/numberOfRecords=20/startFrom=80"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()['total']
    return data

client = discord.Client()
@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!level2'):
        g = streams_total()
        for counter in range(0,g+40,20):
            f = get_users(counter)
            for i in f:
                level = float(i['userlevel'])
                if level <= float(2):
                    print ("https://www.younow.com/" + i['profile'])
                    msg1 = "https://www.younow.com/" + i['profile']
                    msg2 = "https://ynassets.younow.com/broadcastdynamic/live/" + i['broadcastId'] +"/"+ i['broadcastId']+ ".jpg"
                    await client.send_message(client.get_channel(id), msg2 + " " + msg1)
        await client.send_message(client.get_channel(id), msg4)
        print ("ENDE")

    if message.content.startswith('!level3'):
        g = streams_total()
        for counter in range(0,g+40,20):
            f = get_users(counter)
            for i in f:
                level = float(i['userlevel'])
                if level <= float(3):
                    print ("https://www.younow.com/" + i['profile'])
                    msg1 = "https://www.younow.com/" + i['profile']
                    msg2 = "https://ynassets.younow.com/broadcastdynamic/live/" + i['broadcastId'] +"/"+ i['broadcastId']+ ".jpg"
                    await client.send_message(client.get_channel(id), msg2 + " " + msg1)
        await client.send_message(client.get_channel(id), msg4)
        print ("ENDE")

    if message.content.startswith('!level4'):
        g = streams_total()
        for counter in range(0,g+40,20):
            f = get_users(counter)
            for i in f:
                level = float(i['userlevel'])
                if level <= float(4):
                    print ("https://www.younow.com/" + i['profile'])
                    msg1 = "https://www.younow.com/" + i['profile']
                    msg2 = "https://ynassets.younow.com/broadcastdynamic/live/" + i['broadcastId'] +"/"+ i['broadcastId']+ ".jpg"
                    await client.send_message(client.get_channel(id), msg2 + " " + msg1)
        await client.send_message(client.get_channel(id), msg4)
        print ("ENDE")

    if message.content.startswith('!level5'):
        g = streams_total()
        for counter in range(0,g+40,20):
            f = get_users(counter)
            for i in f:
                level = float(i['userlevel'])
                if level <= float(5):
                    print ("https://www.younow.com/" + i['profile'])
                    msg1 = "https://www.younow.com/" + i['profile']
                    msg2 = "https://ynassets.younow.com/broadcastdynamic/live/" + i['broadcastId'] +"/"+ i['broadcastId']+ ".jpg"
                    await client.send_message(client.get_channel(id), msg2 + " " + msg1)
        await client.send_message(client.get_channel(id), msg4)
        print ("ENDE")

    if message.content.startswith('!streamers'):
        g = streams_total()
        msg3 = int(g)
        await client.send_message(message.channel , "**Kaschperle online auf YouNow:**")
        await client.send_message(message.channel , msg3)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)



client.run(discord_token)

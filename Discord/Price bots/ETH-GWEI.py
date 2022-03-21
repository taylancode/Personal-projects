#Import modules
import discord
from GWEI import gwei_getter
import asyncio
import json

#Read tokens.json and get API token
t = open("tokens.json", "r")
tokens = json.load(t, parse_float=str)
TOKEN = tokens["eth-gwei"]
guild_id = int(tokens["guild"])

#Initiate discord module
client = discord.Client()

#Called via on_ready() function
async def send_update(price):

    #Change to string for nickname
    nickname = str(price)

    #Updates nickname and sleeps for 20 seconds
    await client.get_guild(guild_id).me.edit(nick=f'{nickname} GWEI')
    await asyncio.sleep(20)

#Initiates once bot connects to discord
@client.event
async def on_ready():

    print(f"{client.user} has connected to Discord!")

    #Changes activity, it's static and doesn't need to change
    await client.change_presence(activity = discord.Activity(type = discord.ActivityType.watching, name = "ETH Gas"))

    #Initiate while loop to keep bot active
    while True:

        #Calls gwei_getter class from GWEI.py
        eth = gwei_getter().eth_gwei()
        await send_update(eth)

client.run(TOKEN)
import discord
from GWEI import gwei_getter
import asyncio

TOKEN = 'OTI2MjY4MTI3Nzk5NTQxODMw.Yc5Mag.VVtcqS6FGfgyJcIkVP8IQcEs9ns'

client = discord.Client()

async def send_update(price):

    nickname = str(price)
    await client.get_guild(923971045298421790).me.edit(nick=f'{nickname} GWEI')
    await asyncio.sleep(20)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    await client.change_presence(activity = discord.Activity(type = discord.ActivityType.watching, name = "ETH Gas"))

    while True:

        eth = gwei_getter().eth_gwei()
        await send_update(eth)

client.run(TOKEN)
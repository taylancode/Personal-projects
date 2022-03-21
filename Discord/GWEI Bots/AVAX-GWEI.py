import discord
from GWEI import gwei_getter
import asyncio

TOKEN = 'OTI2MjY2ODQwMzQxMTc2MzUw.Yc5LNw.m8obMagZfe8eKOx9kSP_6SaAk_I'

client = discord.Client()

async def send_update(price):

    nickname = str(price)
    await client.get_guild(923971045298421790).me.edit(nick=f'{nickname} nAVAX')
    await asyncio.sleep(20)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    await client.change_presence(activity = discord.Activity(type = discord.ActivityType.watching, name = "AVAX Gas"))

    while True:

        avax = gwei_getter().avax_gwei()

        await send_update(avax)

client.run(TOKEN)
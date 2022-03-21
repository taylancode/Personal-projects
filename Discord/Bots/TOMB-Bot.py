#Importing modules
import discord
from CoinGecko import Price
import asyncio
import logging
import json

#Set variable due to bots being individual/unique
coin = "tomb"

#Gathering discord API token and guild ID from JSON file
t = open("tokens.json", "r")
tokens = json.load(t, parse_float=str)
TOKEN = tokens[coin]
guild_id = int(tokens["guild"])

#Logging functionality
logging.basicConfig(
    filename=f"Price-Bot.log", 
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(module)s - %(funcName)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S")

#Initiate discord class
client = discord.Client()

#Called via on_ready() function if data was gathered successfully
async def send_update(priceusd, pricegbp, price1h, price24h):

    #Setting data to string to be used in nickname
    usd = str(priceusd)
    gbp = str(pricegbp)

    try:

        #Updates nickname/activity, logs and sleeps
        await client.get_guild(guild_id).me.edit(nick=f"${usd}/£{gbp}")
        await client.change_presence(activity = discord.Activity(type = discord.ActivityType.playing, name = f"1h {price1h} 24h {price24h}"))
        logging.info("Update sent to discord")
        await asyncio.sleep(60)

    except Exception as e:
        logging.error(f"Could not send update to Discord: {e}")
        await asyncio.sleep(60)

#Initiated once bot connects to Discord
@client.event
async def on_ready():

    #Logs initial connection
    logging.info(f"{client.user} has connected to Discord!")

    #Loop to keep bot active
    while True:

        #Data gathering from coingecko.py 
        try:
            init_Price = Price(coin)

            priceusd = init_Price.get_price_usd()
            pricegbp = init_Price.get_price_gbp()
            price1h = init_Price.get_price_1h()
            price24h = init_Price.get_price_24h()

            logging.info(f"Retrieved data from coingecko: ${priceusd}-£{pricegbp}-%{price1h}-%{price24h}")

            #Sets arrows based on % change for use in nickname
            if price1h > 0:
                price1h = f"⬈({price1h}%)"
            elif price1h == 0:
                price1h = f"―({price1h}%)"
            else:
                price1h = f"⬊({price1h}%)"
            if price24h > 0:
                price24h = f"⬈({price24h}%)"
            elif price24h == 0:
                price24h = f"―({price24h}%)"
            else:
                price24h = f"⬊({price24h}%)"

            #Calling send_update function to update nickname
            await send_update(priceusd, pricegbp, price1h, price24h)

        except Exception as e:
            logging.error(f"Get price failed with error: {e}")
            await asyncio.sleep(60)

client.run(TOKEN)
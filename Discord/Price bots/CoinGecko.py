#Importing pycoingecko module
from pycoingecko import CoinGeckoAPI

#Price class to be initiated with any crypto coin (e.g Price(bitcoin))
class Price():

    #Initializes pycoingecko module and sets coin variable
    def __init__(self, coin):
        self.cg = CoinGeckoAPI()
        self.coin = coin

        #Tries API call to coingecko API
        try:
            self.get_price_data = self.cg.get_coin_by_id(id=self.coin, market_data=True)
        except:
            raise
    
    #Gets USD price from JSON data
    def get_price_usd(self):
        price = self.get_price_data["market_data"]["current_price"]["usd"]
        return price

    #Gets GBP price from JSON data
    def get_price_gbp(self):
        price = self.get_price_data["market_data"]["current_price"]["gbp"]
        return price
    
    #Gets 1h % change from JSON data
    def get_price_1h(self):
        price_change_1h = round(self.get_price_data["market_data"]["price_change_percentage_1h_in_currency"]["usd"], 1)
        return price_change_1h

    #Gets 24h % change from JSON data
    def get_price_24h(self):
        price_change_24h = round(self.get_price_data["market_data"]["price_change_percentage_24h_in_currency"]["usd"], 1)
        return price_change_24h
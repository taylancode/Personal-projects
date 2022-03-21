import requests
import json

class gwei_getter():

    #Opens and reads tokens file on initiation
    def __init__(self):
        g = open("tokens.json", "r")
        self.gwei = json.load(g, parse_float=str)

    #Makes API call to snowtrace.io to get avax gwei
    def avax_gwei(self):

        self.apikey = self.gwei["avax-api"]
        self.url = f"https://api.snowtrace.io/api?module=proxy&action=eth_gasPrice&apikey={self.apikey}"

        r = requests.get(self.url)

        if r.status_code == 200:

            r = r.json()
            result = json.dumps(r)

            #Conversion to gwei
            gwei = (int(r["result"], 0) / 1000000000)
            
            #Returns value
            return gwei

    #Makes API call to ethgasstation.info to get ethereum gwei
    def eth_gwei(self):

        self.apikey = self.gwei["eth-api"]
        self.url = f"https://ethgasstation.info/api/ethgasAPI.json?api-key={self.apikey}"

        r = requests.get(self.url)

        if r.status_code == 200:

            r = r.json()
            result = json.dumps(r)

            #Conversion to gwei
            gwei = int(r["average"]/10)
            
            #Returns value
            return gwei
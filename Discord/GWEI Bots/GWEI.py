import requests
import json

class gwei_getter():

    def avax_gwei(self):

        self.apikey = '3TRNMNVYRW6W6F413VV3HY93NKVSTJTQ9G'
        self.url = f"https://api.snowtrace.io/api?module=proxy&action=eth_gasPrice&apikey={self.apikey}"

        r = requests.get(self.url)

        if r.status_code == 200:

            r = r.json()
            result = json.dumps(r)

            gwei = (int(r['result'], 0) / 1000000000)
            
            return gwei

    def eth_gwei(self):

        self.apikey = 'e87324ab750d26743d9dd397d8e253e95bcd4477060d04da0d218a88e613'
        self.url = f'https://ethgasstation.info/api/ethgasAPI.json?api-key={self.apikey}'

        r = requests.get(self.url)

        if r.status_code == 200:

            r = r.json()
            result = json.dumps(r)

            gwei = int(r['average']/10)
            
            return gwei
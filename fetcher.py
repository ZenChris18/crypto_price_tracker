import requests

def get_price(coin_id):
    url = f"https://api.coinpaprika.com/v1/tickers/{coin_id}"
    res = requests.get(url)
    data = res.json()
    return data["quotes"]["USD"]["price"]


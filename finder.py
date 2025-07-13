import requests


# run this file to find the specific coin you want
def find_coin_id(symbol):
    url = "https://api.coinpaprika.com/v1/coins"
    response = requests.get(url)
    coins = response.json()

    for coin in coins:
        if coin["symbol"].lower() == symbol.lower():
            print(f"{symbol.upper()} ➜ {coin['id']} ({coin['name']})")

# Try it
find_coin_id("ron")

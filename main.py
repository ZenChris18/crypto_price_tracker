from fastapi import FastAPI
from watchlist import watchlist
from fetcher import get_price
from usd_php import get_usd_to_php # this returns the conversion of 1usd to php

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Crypto tracker API is running"}

@app.get("/prices")
def price(coin_id: str="axs"):
    # return {coin: get_price(coin_id) for coin, coin_id in watchlist.items()} this is for returning the whole watchlist
    if coin_id in watchlist:
        coin_name = watchlist[coin_id]
        return {coin_id: round(get_price(coin_name) * get_usd_to_php(), 2)} 
    else:
        return {"Input Valid Coin name"}


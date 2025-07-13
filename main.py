from fastapi import FastAPI
from watchlist import watchlist
from fetcher import get_price

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Crypto tracker API is running"}

@app.get("/prices")
def price():
    return {coin: get_price(coin_id) for coin, coin_id in watchlist.items()}

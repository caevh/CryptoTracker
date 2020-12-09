import requests
from pycoingecko import CoinGeckoAPI
import time

cg = CoinGeckoAPI()

def get_price():
    cg = CoinGeckoAPI()
    price = cg.get_price('cardano', 'gbp')
    return price


def price_change(coin_values):
    current_coin_value = coin_values[-1]
    if len(coin_values) == 1:
        print(f"Current Price: {current_coin_value}")
    elif coin_values[-1] == coin_values[-2]:
        print(f"Price has not changed.\nCurrent Price: {current_coin_value}")
    elif coin_values[-1] > coin_values[-2]:
        price_change = coin_values[-1] - coin_values[-2]
        print(f"Price has gone up!\nCurrent Price: {current_coin_value}\nPrice Change: +{price_change}")
    else:
        price_change = coin_values[-2] - coin_values[-1]
        print(f"Price has gone down!\nCurrent Price: {current_coin_value}\nPrice Change: -{price_change}")


coin_prices = []
while True:
    
    info = get_price()
    price = info["cardano"]["gbp"]

    coin_prices.append(price)
    
    price_change(coin_prices)


    print(coin_prices)
    print("-" * 50)
    time.sleep(10)
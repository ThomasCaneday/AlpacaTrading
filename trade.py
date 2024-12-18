import requests, json
from config import *

HEADERS = {"APCA-API-KEY-ID": API_KEY, "APCA-API-SECRET-KEY": SECRET_KEY}

def get_account():
    r = requests.get(ACCOUNT_URL, headers=HEADERS)

    return json.loads(r.content)

def create_order(symbol, qty, side, type, time_in_force):
    data = {
        "symbol": symbol,
        "qty": qty,
        "side": side,
        "type": type,
        "time_in_force": time_in_force
    }

    r = requests.post(ORDERS_URL, json=data, headers=HEADERS)

    return json.loads(r.content)

def order_prompt():
    symbol = input("ticker symbol: ")
    qty = input("quantity: ")
    side = input("buy or sell: ")
    type = input("market, limit, stop, stop_limit: ")
    time_in_force = input("day, gtc, opg, cls, ioc, fok: ")

    return symbol, qty, side, type, time_in_force

symbol, qty, side, type, time_in_force = order_prompt()
response = create_order(symbol, qty, side, type, time_in_force)
print(response)
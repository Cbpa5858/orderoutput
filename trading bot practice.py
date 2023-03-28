import time
import numpy as np
import asyncio
import aiohttp
from alpaca_trade_api import StreamConn, REST
from alpaca_trade_api.common import URL
import numpy as np
import datetime

API_KEY = '...'
API_SECRET = '...'
BASE_URL = 'https://paper-api.alpaca.markets'

symbol = 'AAPL'
timeframe = '1Min'

min_trade_size = 1  # Set the minimum trade size

rest = REST(API_KEY, API_SECRET, base_url=URL(BASE_URL))

from alpha_vantage.timeseries import TimeSeries

ALPHA_VANTAGE_API_KEY = '...'

def get_alpha_vantage_data(symbol, interval):
    ts = TimeSeries(key=ALPHA_VANTAGE_API_KEY, output_format='pandas')
    if interval == '1min':
        data, _ = ts.get_intraday(symbol=symbol, interval='1min', outputsize='compact')
    elif interval == 'daily':
        data, _ = ts.get_daily(symbol=symbol, outputsize='compact')

    data = data.rename(columns={
        '1. open': 'open',
        '2. high': 'high',
        '3. low': 'low',
        '4. close': 'close',
        '5. volume': 'volume'
    })

    data.reset_index(inplace=True)
    return data.to_dict('records')



#Trade indicator logic goes here...

async def perform_trade():


#missing some of the perform trade section
   

    account = rest.get_account()
    usd_balance = float(account.cash)

    current_price = rest.get_latest_trade(symbol).price

    # calculate trade quantity based on 80% of available USD balance
    trade_quantity = round(usd_balance * 0.8 / current_price)

    # check if the last order was a buy order and calculate the stop loss price
    if last_order == "BUY":
        stop_loss_price = current_price * 0.98  # set the stop loss price 2% below the current price
    else:
        stop_loss_price = 0  # if last order was not a buy order, set the stop loss price to 0

    if supertrend_signal != last_order:
        if supertrend_signal == "BUY":
            print("Buy signal")

           #Buy logic


        elif supertrend_signal == "SELL":
            print("Sell signal")

            
             #Sell Logic



async def trade_updates_handler():
    conn = StreamConn(API_KEY, API_SECRET, base_url=URL(BASE_URL))

    async def on_trade_update(conn, channel, data):
        print('Received trade:', data)
        await perform_trade()

    conn.register_trade_updates(on_trade_update)

    async with conn:
        await conn.subscribe_trade_updates()
        while True:
            try:
                await conn._consume_msg()
            except KeyboardInterrupt:
                break
            except Exception as e:
                print(f"Error: {e}")cdc
                break


#run section...


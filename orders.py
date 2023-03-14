import os
import json
import alpaca_trade_api as tradeapi
from flask import Flask, request

app = Flask(__name__)

ALPACA_API_KEY = os.environ.get('ALPACA_API_KEY')
ALPACA_SECRET_KEY = os.environ.get('ALPACA_SECRET_KEY')
ALPACA_API_BASE_URL = os.environ.get('ALPACA_API_BASE_URL')

api = tradeapi.REST(ALPACA_API_KEY, ALPACA_SECRET_KEY, base_url=ALPACA_API_BASE_URL)

@app.route('/buy', methods=['POST'])
def buy():
    data = request.get_json()
    symbol = data['symbol']
    qty = data['qty']
    side = data['side']
    type = data['type']
    time_in_force = data['time_in_force']
    order = api.submit_order(
        symbol=symbol,
        qty=qty,
        side=side,
        type=type,
        time_in_force=time_in_force
    )
    return json.dumps(order._raw)

if __name__ == '__main__':
    app.run()

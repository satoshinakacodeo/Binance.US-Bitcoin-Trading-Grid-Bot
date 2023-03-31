import time
import ccxt

sell_order = "null"
buy_order = "null"

exchange = ccxt.binanceus({
    'apiKey': 'API KEY HERE',
    'secret': 'API SECRET KEY HERE',
    'enableRateLimit': True,
})

pair = 'BTC/USD'
price_range = 25
num_grids = 100
quantity = 0.00066

total_trades = 0
total_buys = 0
total_sells = 0
buy_dollars = 0
sell_dollars = 0
last_profit = 0
while True:   
    try:
        orders = exchange.fetch_open_orders(symbol='BTC/USD')
    except Exception as e:
        print('Error:', e)
    # Loop through orders and cancel them
    for order in orders:
        try:
            exchange.cancel_order(order['id'],symbol='BTC/USD')
        except Exception as e:
            print('Error:', e)
    # initialize grid levels
    ticker = exchange.fetch_ticker(pair)
    current_price = loop_price = ticker['last']
    bid = ticker['bid']
    ask = ticker['ask']
    buy_price = sell_price = current_price = round(((bid + ask) / 2), 1)

    # track successful orders
    successful_orders = set()

    # place initial orders
    for i in range(num_grids):
            buy_price -= price_range
            sell_price += price_range
            try:
                buy_order = exchange.create_limit_buy_order(pair, quantity, buy_price)
            except Exception as e:
                print('Error:', e)
            try:
                sell_order = exchange.create_limit_sell_order(pair, quantity, sell_price)
            except Exception as e:
                print('Error:', e)
            successful_orders.add(buy_order['id'])
            successful_orders.add(sell_order['id'])
            print(f'NEW GRID --> BUY at {buy_price}')
            print(f'NEW GRID --> SELL at {sell_price}')
            time.sleep(.05)
    loop_time = the_time = int(time.time())        
    print('')
    print(f'price_range = {price_range}    num_grids = {num_grids}   quantity = {quantity}      Profit per Grid = ${price_range*quantity}    Grid RANGE = {current_price+(price_range*num_grids)} - {current_price-(price_range*num_grids)}')    
    print('')
    while (True):
        the_time = int(time.time())
        try:
            ticker = exchange.fetch_ticker(pair)
            loop_price = ticker['last']
            orders = exchange.fetch_closed_orders(symbol=pair)
            for order in orders:
                order_price = order['price']
                order_side = order['side']
                order_id = order['id']
                order_amount = order['amount']
                if order_id in successful_orders:
                    sell_order = buy_order = None
                    current_time = time.strftime("%H:%M:%S", time.localtime())
                    print(order_side, f' {order_price}  {current_time} ', end = '')
                    if (order_side == 'buy'):
                        sell_price = order_price + price_range
                        total_buys += 1
                        buy_dollars = buy_dollars + (order_price*quantity)
                        try:
                            sell_order = exchange.create_limit_sell_order(pair, quantity, sell_price)
                            print(f'Sell at {sell_price}  Total BUYS= {total_buys} Total SELLS= {total_sells} Total Trades= {total_buys+total_sells} lastprofit={last_profit}')
                            #print(sell_order['id'])
                            if sell_order is not None:
                                successful_orders.remove(order_id)
                        except Exception as e:
                            print('Error:', e)    
                        successful_orders.add(sell_order['id'])
                        if (total_buys == total_sells):
                                print(f'Profit = {round((sell_dollars-buy_dollars),2)}')
                                last_profit = sell_dollars-buy_dollars
                    elif (order_side == 'sell'):
                        buy_price = order_price - price_range
                        total_sells += 1
                        sell_dollars = sell_dollars + (order_price*quantity)
                        try:
                            buy_order = exchange.create_limit_buy_order(pair, quantity, buy_price)
                            print(f'Buy at {buy_price} Total BUYS= {total_buys} Total SELLS= {total_sells} Total Trades= {total_buys+total_sells} lastprofit={last_profit}')
                            #print(buy_order['id'])
                            if buy_order is not None:
                                successful_orders.remove(order_id)
                        except Exception as e:
                            print('Error:', e)    
                        successful_orders.add(buy_order['id'])
                        if (total_buys == total_sells):
                                print(f'Profit = {round((sell_dollars-buy_dollars),2)}')
                                last_profit = sell_dollars-buy_dollars
            time.sleep(2)
        except Exception as e:
            print('An error occurred:', e)

# Binance.US-Bitcoin-Trading-Grid-Bot

Trading Bitcoin involves risk.  The author of the program is not responsible for any losses you may incur.

There is a bug in the code that causes the grid to break down over time.  There should always be 200 orders open.

Over time I notice the total number of open orders drop and I am not sure what is causing it or how to prevent it.

Can stress test the code by making the grid size very small.  I don't see any exceptions being thrown.

I have no idea what the optimal settings are for profit unfortunately, but you don't want the price of Bitcoin to escape the grid range.  Grid trading isn't really optimal for Bitcoin due to the large swings.  Market tanks and the program will load you up on Bitcoin.  Market takes off and the program will take profits too soon and unload your Bitcoin.  I have found the profits to be very low and wonder if the few dollars is worth missing out on the big pumps and getting extra exposure for the crashes...

This YouTube video helped me understand how a grid bot works:
https://www.youtube.com/watch?v=oV_xQFBCM3M

Quick note about the API key pairs you will have to generate at Binance.us - by default the API key pair should not have withdrawal access.  Withdrawal access is not required for this program and I strongly recommend against ever enabling withdrawal access for any key pairs!

Please note that you want at least double the amount of BTC/USD in your account than is required to place the original 200 orders.  Imagine if the price just moves straight up or down the 100 buy orders can turn in to 100 new sell orders and vice versa.


Development work has been put on hold permenently unless Binance.US reverses course on becoming crypto only.

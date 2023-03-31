# Binance.US-Bitcoin-Trading-Grid-Bot
Trading Bitcoin involves risk.  The author of the program is not responsible for any losses you may incur.

There may be bugs in the code!  I appreciate any fixes or improvement suggestions.

I created this python program because I could not find any free options.  I had to either pay a monthly fee, or per trade!

It did take significant effort on my part mostly since I had not written a computer program in about 20 years!

I am offering it online for free because I think others may find it helpful.

If you do find it helpful I would greatly appreciate a donation of any size.

Bitcoin - 179BSmdDiqbCACmz5yDpVYynhh3g5GQ4tf

DOGE - DBvGe8trgKTCA9dHoxv6pC4s2mVNniXE4d

ETH (ERC20) - 0xbfbac763bdf69bc29e73afdff7f1680247dc52dd

LTC - LgfH9MJfu35K84CqVLjJhE5BuRwDLyLKc7

It will encourage me to continue development and enable support for other trading platforms as well.

Robinhood or TD Ameritrade for stocks, commodities, and fiat would be fun for me =)

I have no idea what the optimal settings are for profit unfortunately, but you don't want the price of Bitcoin to escape the grid range.  Grid trading isn't really optimal for Bitcoin due to the large swings.  Market tanks and the program will load you up on Bitcoin.  Market takes off and the program will take profits too soon and unload your Bitcoin.  I have found the profits to be very low and wonder if the few dollars is worth missing out on the big pumps and getting extra exposure for the crashes...

This YouTube video helped me understand how a grid bot works:
https://www.youtube.com/watch?v=oV_xQFBCM3M

Quick note about the API key pairs you will have to generate at Binance.us - by default the API key pair should not have withdrawal access.  Withdrawal access is not required for this program and I strongly recommend against ever enabling withdrawal access for any key pairs!

Please note that you want at least double the amount of BTC/USD in your account than is required to place the original 200 orders.  Imagine if the price just moves straight up or down the 100 buy orders can turn in to 100 new sell orders and vice versa.

#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# This test loads market data.
#

# AutoZone is AZO
# Apple is AAPL
# S&P500 is INDEXSP:.INX
# DOW is INDEXDJX:.DJI

import json
import googlefinance

dowTicker = 'INDEXDJX:.DJI'
spTicker = 'INDEXSP:.INX'

data = googlefinance.getQuotes({ dowTicker, spTicker})
    
ticker_d = data[0]["StockSymbol"]
print ticker_d

price_d = data[0]["LastTradePrice"]
print price_d

ticker_s = data[1]["StockSymbol"]
print ticker_s

price_s = data[1]["LastTradePrice"]
print price_s

inJSON = json.dumps({ticker_d: price_d, ticker_s: price_s}, 
    sort_keys=True, 
    indent=4, 
    separators=(',', ' : '))

fileName = 'market.json'
file = open(fileName, "w")
file.write(inJSON)
file.close()

import krakenex

from decimal import Decimal as D
import pprint
import krakenex
import decimal
import time


k = krakenex.API()
k.load_key('kraken.key')

volume = 0.006
data = {"pair":"XETHZUSD", "type":"buy", "ordertype":"market", "volume":"0.02"}
order_res = k.query_private('AddOrder', data)

print("order_res", order_res)
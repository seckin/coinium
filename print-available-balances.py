import krakenex

from decimal import Decimal as D
import pprint

k = krakenex.API()
k.load_key('kraken.key')

balance = k.query_private('Balance')
orders = k.query_private('OpenOrders')

balance = balance['result']
orders = orders['result']

print("balance", balance)
coins = ['XXBT', 'XETH', 'XXRP']
for coin in coins:
    if coin not in balance.keys():
        balance[coin] = 0.0
print("updated balance", balance)

newbalance = dict()
mid_mkt_vals = dict()
new_mid_mkt_vals = dict()
for currency in balance:
    if currency != "ZUSD":
        print("currency", currency)
        pair = currency + "ZUSD"
        print("pair", pair)
        spread = k.query_public('Spread', data = {'pair': pair, 'since': -1})
        # print("spread", spread)
        timestamp = int(spread['result'][pair][-1][0])
        bestbid = float(spread['result'][pair][-1][1])
        bestask = float(spread['result'][pair][-1][2])
        print("timestamp", timestamp)
        print("bestbid", bestbid)
        print("bestask", bestask)
        mid_mkt_vals[currency] = (bestbid + bestask) / 2.0
    # remove first symbol ('Z' or 'X'), but not for GNO or DASH
    newname = currency[1:] if len(currency) == 4 and currency != "DASH" else currency
    newbalance[newname] = D(balance[currency]) # type(balance[currency]) == str
    if currency != "ZUSD":
        new_mid_mkt_vals[newname] = float(D(mid_mkt_vals[currency]))
balance = newbalance

total_coin_val = 0.0
for k, v in balance.items():
    # convert to string for printing
    if v == D('0'):
        s = '0'
    else:
        s = str(v)
    # remove trailing zeros (remnant of being decimal)
    s = s.rstrip('0').rstrip('.') if '.' in s else s
    #
    if k != "USD":
        val = new_mid_mkt_vals[k] * float(s)
        print(k, s, "price:", new_mid_mkt_vals[k], "total $ val:", val)
        total_coin_val += val
    else:
        print(k, s)

print("total_coin_val", total_coin_val)

for k, v in balance.items():
    # convert to string for printing
    if v == D('0'):
        s = '0'
    else:
        s = str(v)
    # remove trailing zeros (remnant of being decimal)
    s = s.rstrip('0').rstrip('.') if '.' in s else s
    #
    if k != "USD":
        val = new_mid_mkt_vals[k] * float(s)
        print(k, s, "price:", new_mid_mkt_vals[k], "total $ val:", val, "% of total coin holdings:", 100.0 * (val / total_coin_val))
    else:
        print(k, s)
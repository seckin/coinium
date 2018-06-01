import krakenex

from decimal import Decimal as D
import pprint
import krakenex
import decimal
import time
import pymysql
import pymysql.cursors


kapi = krakenex.API()
kapi.load_key('kraken.key')

balance = kapi.query_private('Balance')
orders = kapi.query_private('OpenOrders')

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
        spread = kapi.query_public('Spread', data = {'pair': pair, 'since': -1})
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



connection = pymysql.connect(host='localhost',
                             user='root',
                             password='co1n23im',
                             db='coinim',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


try:
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM `Lists`"
        cursor.execute(sql, ())
        lists = cursor.fetchall()
        print("lists", lists)
        for list in lists:
            if list["id"] != 9:
                continue
            # get the latest distribution for the list
            sql = "SELECT * FROM `ListHasDistribution` WHERE `list_id`=%s order by created_at desc limit 1"
            cursor.execute(sql, (list["id"],))
            list_has_distribution = cursor.fetchall()
            print("list_has_distribution", list_has_distribution)
            if len(list_has_distribution):
                list_has_distribution = list_has_distribution[0]
            else:
                print("list_has_distribution not found. skipping list.")
                continue
            sql = "SELECT * FROM `Distributions` WHERE `id`=%s"
            cursor.execute(sql, (list_has_distribution["distribution_id"],))
            distributions = cursor.fetchall()
            if len(distributions):
                latest_distribution_of_list = distributions[0]
            else:
                print("distributions not found. skipping list.")
                continue
            
            # get all approved subscriptions of this list
            sql = "SELECT * FROM `Subscription` WHERE approved = 1 and `list_id`=%s"
            cursor.execute(sql, (list["id"],))
            subscriptions_of_list = cursor.fetchall()
            print("subscriptions_of_list", subscriptions_of_list)
            total_holding_amounts_for_list = dict()
            # TODO: right now assuming all kraken.com holdings belong to the list being processed. fix this
            total_holding_amounts_for_list["btc"] = list["kraken_btc"] + float(balance["XBT"])
            total_holding_amounts_for_list["eth"] = list["kraken_eth"] + float(balance["ETH"])
            total_holding_amounts_for_list["xrp"] = list["kraken_xrp"] + float(balance["XRP"])
            total_holding_amounts_for_list["zcash"] = 0
            for subscription in subscriptions_of_list:
                print("subscription", subscription)
                if subscription["kraken_processed"] == 0:
                    print("kraken_processed is zero. updating to 1")
                    sql = "UPDATE `Subscription` SET kraken_processed=1 WHERE `id`=%s"
                    cursor.execute(sql, (subscription["id"],))
                    connection.commit()
                    total_holding_amounts_for_list["btc"] += subscription["kraken_btc"]
                    total_holding_amounts_for_list["eth"] += subscription["kraken_eth"]
                    total_holding_amounts_for_list["xrp"] += subscription["kraken_xrp"]
                    total_holding_amounts_for_list["zcash"] += subscription["kraken_zcash"]
                else:
                    print("kraken_processed not zero")
            for key in total_holding_amounts_for_list.keys():
                print("holding ", key, " amount:", total_holding_amounts_for_list[key])
            total_coin_val_for_list = dict()
            total_coin_val_for_list["btc"] = new_mid_mkt_vals["XBT"] * total_holding_amounts_for_list["btc"]
            total_coin_val_for_list["eth"] = new_mid_mkt_vals["ETH"] * total_holding_amounts_for_list["eth"]
            total_coin_val_for_list["xrp"] = new_mid_mkt_vals["XRP"] * total_holding_amounts_for_list["xrp"]
            total_coin_val_for_list["zcash"] = new_mid_mkt_vals["ZEC"] * total_holding_amounts_for_list["zcash"]
            total_coin_val_in_usd = total_coin_val_for_list["btc"] + \
                                    total_coin_val_for_list["eth"] + \
                                    total_coin_val_for_list["xrp"] + \
                                    total_coin_val_for_list["zcash"]
            print("total_coin_val_in_usd", total_coin_val_in_usd)
            print("current percentage holdings for list#", list["id"])
            print("btc $", total_coin_val_for_list["btc"], " pct:", 100.0 * (0.0 if total_coin_val_for_list["btc"] == 0 else total_coin_val_for_list["btc"] / total_coin_val_in_usd))
            print("eth $", total_coin_val_for_list["eth"], " pct:", 100.0 * (0.0 if total_coin_val_for_list["eth"] == 0 else total_coin_val_for_list["eth"] / total_coin_val_in_usd))
            print("xrp $", total_coin_val_for_list["xrp"], " pct:", 100.0 * (0.0 if total_coin_val_for_list["xrp"] == 0 else total_coin_val_for_list["xrp"] / total_coin_val_in_usd))
            print("zcash $", total_coin_val_for_list["zcash"], " pct:", 100.0 * (0.0 if total_coin_val_for_list["zcash"] == 0 else total_coin_val_for_list["zcash"] / total_coin_val_in_usd))
            print("")
            print("final pct holding should be = latest_distribution_of_list: ", latest_distribution_of_list)
            print("final btc pct:", latest_distribution_of_list["btc"])
            print("final eth pct:", latest_distribution_of_list["eth"])
            print("final xrp pct:", latest_distribution_of_list["xrp"])

            # final coin holdings we want to ideally reach:
            final_coin_holding_to_reach = dict()
            final_coin_holding_to_reach["btc"] = ((latest_distribution_of_list["btc"] / 100.0) * total_coin_val_in_usd) / new_mid_mkt_vals["XBT"]
            final_coin_holding_to_reach["eth"] = ((latest_distribution_of_list["eth"] / 100.0) * total_coin_val_in_usd) / new_mid_mkt_vals["ETH"]
            final_coin_holding_to_reach["xrp"] = ((latest_distribution_of_list["xrp"] / 100.0) * total_coin_val_in_usd) / new_mid_mkt_vals["XRP"]
            final_coin_holding_to_reach["zcash"] = 0.0
            print('final_coin_holding_to_reach["btc"]', final_coin_holding_to_reach["btc"], 'total_holding_amounts_for_list["btc"]', total_holding_amounts_for_list["btc"])
            print('final_coin_holding_to_reach["eth"]', final_coin_holding_to_reach["eth"], 'total_holding_amounts_for_list["eth"]', total_holding_amounts_for_list["eth"])
            print('final_coin_holding_to_reach["xrp"]', final_coin_holding_to_reach["xrp"], 'total_holding_amounts_for_list["xrp"]', total_holding_amounts_for_list["xrp"])
            print('final_coin_holding_to_reach["zcash"]', final_coin_holding_to_reach["zcash"], 'total_holding_amounts_for_list["zcash"]', total_holding_amounts_for_list["zcash"])

            # try to sell extra amounts:
            if total_holding_amounts_for_list["btc"] > final_coin_holding_to_reach["btc"]:
                volume_to_sell = total_holding_amounts_for_list["btc"] - final_coin_holding_to_reach["btc"]
                print("will try to sell btc, volume_to_sell:", volume_to_sell)
                try:
                    data = {"pair":"XXBTZUSD", "type":"sell", "ordertype":"market", "volume":str(volume_to_sell)}
                    order_res = kapi.query_private('AddOrder', data)
                finally:
                    print("order_res", order_res)
            if total_holding_amounts_for_list["eth"] > final_coin_holding_to_reach["eth"]:
                volume_to_sell = total_holding_amounts_for_list["eth"] - final_coin_holding_to_reach["eth"]
                print("will try to sell eth, volume_to_sell:", volume_to_sell)
                try:
                    data = {"pair":"XETHZUSD", "type":"sell", "ordertype":"market", "volume":str(volume_to_sell)}
                    order_res = kapi.query_private('AddOrder', data)
                finally:
                    print("order_res", order_res)
            if total_holding_amounts_for_list["xrp"] > final_coin_holding_to_reach["xrp"]:
                volume_to_sell = total_holding_amounts_for_list["xrp"] - final_coin_holding_to_reach["xrp"]
                print("will try to sell xrp, volume_to_sell:", volume_to_sell)
                try:
                    data = {"pair":"XXRPZUSD", "type":"sell", "ordertype":"market", "volume":str(volume_to_sell)}
                    order_res = kapi.query_private('AddOrder', data)
                finally:
                    print("order_res", order_res)
            if total_holding_amounts_for_list["zcash"] > final_coin_holding_to_reach["zcash"]:
                volume_to_sell = total_holding_amounts_for_list["zcash"] - final_coin_holding_to_reach["zcash"]
                print("will try to sell zcash, volume_to_sell:", volume_to_sell)
                try:
                    data = {"pair":"XZECZUSD", "type":"sell", "ordertype":"market", "volume":str(volume_to_sell)}
                    order_res = kapi.query_private('AddOrder', data)
                finally:
                    print("order_res", order_res)

            # now try to buy
            if final_coin_holding_to_reach["btc"] > total_holding_amounts_for_list["btc"]:
                volume_to_buy = final_coin_holding_to_reach["btc"] - total_holding_amounts_for_list["btc"]
                print("will try to buy btc, volume_to_buy:", volume_to_buy)
                try:
                    data = {"pair":"XXBTZUSD", "type":"buy", "ordertype":"market", "volume":str(volume_to_buy)}
                    order_res = kapi.query_private('AddOrder', data)
                finally:
                    print("order_res", order_res)
            if final_coin_holding_to_reach["eth"] > total_holding_amounts_for_list["eth"]:
                volume_to_buy = final_coin_holding_to_reach["eth"] - total_holding_amounts_for_list["eth"]
                print("will try to buy eth, volume_to_buy:", volume_to_buy)
                try:
                    data = {"pair":"XETHZUSD", "type":"buy", "ordertype":"market", "volume":str(volume_to_buy)}
                    order_res = kapi.query_private('AddOrder', data)
                finally:
                    print("order_res", order_res)
            if final_coin_holding_to_reach["xrp"] > total_holding_amounts_for_list["xrp"]:
                volume_to_buy = final_coin_holding_to_reach["xrp"] - total_holding_amounts_for_list["xrp"]
                print("will try to buy xrp, volume_to_buy:", volume_to_buy)
                try:
                    data = {"pair":"XXRPZUSD", "type":"buy", "ordertype":"market", "volume":str(volume_to_buy)}
                    order_res = kapi.query_private('AddOrder', data)
                finally:
                    print("order_res", order_res)
            # if final_coin_holding_to_reach["zcash"] > total_holding_amounts_for_list["zcash"]:
            #     volume_to_buy = final_coin_holding_to_reach["zcash"] - total_holding_amounts_for_list["zcash"]
            #     print("will try to sell zcash, volume_to_buy:", volume_to_buy)
            #     try:
            #         data = {"pair":"XZECZUSD", "type":"buy", "ordertype":"market", "volume":str(volume_to_buy)}
            #         order_res = kapi.query_private('AddOrder', data)
            #     finally:
            #         print("order_res", order_res)

            print("\n\n")
            print("=============================================")
            print("\n\n")



finally:
    connection.close()